#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_volume
version_added: '2.6'
short_description:  Manage volumes on PowerMax Storage System
description:
- Managing volume on PowerMax Storage System includes
  create volume, rename volume, expand volume and delete volume
author:
- Vasudevu Lakhinana (vasudevu.lakhinana@dell.com)
- Akash Shendge (Akash.Shendge@emc.com)
- Ambuj Dubey (Ambuj.Dubey@emc.com)
options:
  vol_name:
    description:
    - The name of the volume.
  sg_name:
    description:
    - The name of the storage group
  new_sg_name:
    description:
    - The name of the target storage group
  vol_id:
    description:
    - The native id of the volume.
    - Required in case of rename and delete volume.
    required: true 
  size:
    description:
    - The new size of existing volume.
    - Required in case of create and expand volume.
    required: true
  cap_unit:
    description:
    - volume capacity units
    default: GB
    choices: [ MB, GB, TB ]
  new_name:
    description:
    - The new volume identifier for the volume.
  state:
    description:
    - Define whether the volume should exist or not.
    required: true
    choices: [absent, present]  
Notes:
- To expand volume, either provide vol_id or vol_name and sg_name
- size is required to create/expand volume
- vol_id is required to rename/delete volume
- vol_name, sg_name and new_sg_name is required to move volume between
  storage group
- Deletion of volume will fail if storage group is part of masking view

  '''

EXAMPLES = r'''
- name: Create volume
    dellemc_powermax_volume:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      vol_name: "{{vol_name}}"
      sg_name: "{{sg_name}}"
      size: 1
      cap_unit: "{{cap_unit}}"
      state: 'present'

- name: Expanding volume size
    dellemc_powermax_volume:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      size:  3
      cap_unit: "{{cap_unit}}"
      vol_id: "0059B"
      state: 'present'

- name: Renaming volume
    dellemc_powermax_volume:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      new_name:  "Test_GOLD_vol_Renamed"
      vol_id: "0059B"
      state: 'present'

- name: Delete volume
    dellemc_powermax_volume:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      vol_id: "0059B"
      state: 'absent'

- name: Move volume between storage group
    dellemc_powermax_volume:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      vol_name: "{{vol_name}}"
      sg_name: "{{sg_name}}"
      new_sg_name: "{{new_sg_name}}"      
      state: 'present'
'''

RETURN = r'''
'''

LOG = utils.get_logger('dellemc_powermax_volume', log_devel=logging.INFO)
HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()


class PowerMaxVolume(object):
    """Class with volume operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_powermax_volume_parameters())

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )

        # result is a dictionary that contains changed status and
        # volume details
        self.result = {"changed": False, "volume_details": {}}
        if HAS_PYU4V is False:
            self.module.fail_json(msg="Ansible modules for PowerMax require "
                                      "the PyU4V python library to be "
                                      "installed. Please install the library "
                                      "before using these modules.")

        if PYU4V_VERSION_CHECK is not None:
            self.module.fail_json(msg=PYU4V_VERSION_CHECK)
            LOG.error(PYU4V_VERSION_CHECK)

        self.u4v_conn = utils.get_U4V_connection(self.module.params)
        self.provisioning = self.u4v_conn.provisioning
        LOG.info('Got PyU4V instance for provisioning on to VMAX ')

    def get_volume(self):
        """
        Get volume details
        """
        vol_id = self.module.params['vol_id']
        if vol_id is not None:
            return self.get_volume_by_nativeid(vol_id)

        volume_name = self.module.params['vol_name']
        sg_name = self.module.params['sg_name']
        params = {"storageGroupId": sg_name, "volume_identifier": volume_name}
        volume_list = self.provisioning.get_volume_list(params)

        vol = None
        if not volume_list or len(volume_list) == 0:
            LOG.debug('No volume found with volume identifier {0} in storage '
                      'group {1}'.format(volume_name, sg_name))
        elif len(volume_list) > 1:
            self.module.fail_json(msg='Duplicate volumes found: '
                                      'There are {0} '
                                      'volume(s) with the same name {1} in '
                                      'the storage group {2}'.
                                      format(len(volume_list), volume_name,
                                             sg_name)
                                  )
        else:
            vol = self.get_volume_by_nativeid(volume_list[0])
        return vol

    def get_volume_by_nativeid(self, native_id):
        try:
            LOG.info('Getting volume {0} details using native id'.
                     format(native_id))
            return self.provisioning.get_volume(native_id)
        except Exception as e:
            LOG.error('Got error {0} while getting details of volume {0}'.
                      format(str(e), native_id))
            return None

    def delete_volume_deallocate(self, vol_id):
        """
        Deallocate a volume first and then delete it
        """
        try:
            self.provisioning.deallocate_volume(vol_id)
            self.provisioning.delete_volume(vol_id)
            return True
        except Exception as e:
            error_msg = 'Delete volume {0} failed with error {1} '
            LOG.error(error_msg.format(vol_id, str(e)))
            self.module.fail_json(msg=error_msg.format(vol_id, str(e)))

    def delete_volume(self, vol_id):
        """
        Delete volume from system
        """
        try:
            self.provisioning.delete_volume(vol_id)
            return True
        except Exception as e:
            if "A free of all allocations is required" in str(e):
                self.delete_volume_deallocate(vol_id)
                return True
            else:
                error_msg = 'Delete volume {0} failed with error {1} '
                LOG.error(error_msg.format(vol_id, str(e)))
                self.module.fail_json(msg=error_msg.format(vol_id, str(e)))

    def rename_volume(self, vol_id, vol_new_name):
        """Rename the volume's identifier"""
        try:
            volume_sg_list = self.provisioning.get_storagegroup_from_vol(
                vol_id)
            if volume_sg_list is not None:
                for sg in volume_sg_list:
                    params = {"storageGroupId": sg,
                              "volume_identifier": vol_new_name}
                    volume_list = self.provisioning.get_volume_list(params)

                    if volume_list and len(volume_list) > 0:
                        self.module.fail_json(
                            msg="Volume already exists with volume"
                                " name {0} in storage group {1}".
                            format(vol_new_name, sg))

            self.provisioning.rename_volume(vol_id, vol_new_name)
            return True
        except Exception as e:
            LOG.error('Rename volume {0} failed with error {1} '.format(
                vol_id, str(e)))
            self.module.fail_json(msg='Rename volume {0} failed.'.format(
                vol_id))

    def expand_volume(self, vol_id, size_in_gb, existing_vol_size):
        """Expand volumes's size to new size"""
        try:
            if size_in_gb < existing_vol_size:
                self.module.fail_json(msg='Current volume size {0} GB is '
                                          'greater than {1} GB specified.'.
                                      format(existing_vol_size, size_in_gb))
            elif size_in_gb > existing_vol_size:
                LOG.info('Expanding volume capacity from {0} GB to {1} GB.'.
                         format(existing_vol_size, size_in_gb))
                self.provisioning.extend_volume(vol_id, size_in_gb)
                return True
            else:
                LOG.info('Current volume size and specified volume size'
                         ' are equal')
                return False
        except Exception as e:
            LOG.error('Expand volume {0} failed with error {1}'.
                      format(vol_id, str(e)))
            self.module.fail_json(msg='Expand volume {0} failed with error '.
                                  format(vol_id, str(e)))

    def create_volume(self, vol_name, sg_name, size, cap_unit):
        """Create PowerMax volume in a storage group"""
        try:
            vol_id = self.provisioning.create_volume_from_sg_return_dev_id(
                vol_name, sg_name, size, cap_unit)
            LOG.info('Created volume native ID: '.format(vol_id))
            return vol_id
        except Exception as e:
            LOG.error('Create volume {0} failed with error {1}'.
                      format(vol_name, str(e)))
            self.module.fail_json(msg='Create volume {0} failed with error '.
                                  format(vol_name, str(e)))

    def move_volume_between_storage_groups(self, vol_id, vol_name, sg_name,
                                           new_sg_name):
        """Move volume between storage group"""
        try:
            params = {"storageGroupId": new_sg_name,
                      "volume_identifier": vol_name}
            volume_list = self.provisioning.get_volume_list(params)

            if volume_list and len(volume_list) > 0:
                self.module.fail_json(msg="Volume already exists with volume"
                                          " name {0} in storage group {1}".
                                      format(vol_name, new_sg_name))
            return self.provisioning.move_volumes_between_storage_groups(
                vol_id, sg_name, new_sg_name)
        except Exception as e:
            error_message = 'Move volume {0} from SG {1} to SG {2} ' \
                            'failed with error {3} '
            LOG.error(error_message.
                      format(vol_name, sg_name, new_sg_name, str(e)))
            self.module.fail_json(msg=error_message.
                                  format(vol_name, sg_name, new_sg_name,
                                         str(e)))

    def perform_module_operation(self):
        """
        Perform different actions on volume based on user parameter
        chosen in playbook
        """
        size = self.module.params['size']
        state = self.module.params['state']
        new_name = self.module.params['new_name']
        vol_id = self.module.params['vol_id']
        vol_name = self.module.params['vol_name']
        sg_name = self.module.params['sg_name']
        cap_unit = self.module.params['cap_unit']
        new_sg_name = self.module.params['new_sg_name']

        if vol_id is None and vol_name is None:
            self.module.fail_json(msg='Specify Volume ID or Volume name')
        elif vol_id is not None and vol_name is not None:
            self.module.fail_json(msg='Specify Volume ID or Volume name,'
                                      ' not both')
        elif vol_name is not None and sg_name is None:
            self.module.fail_json(msg='Specify Storage group name along '
                                      'with volume name')

        vol = self.get_volume()

        existing_vol_size = 0
        if vol is not None:
            vol_id = vol['volumeId']
            existing_vol_size = vol['cap_gb']

        changed = False

        # Call to create volume in storage group
        if state == 'present' and vol is None:
            if size is None:
                self.module.fail_json(msg='Size is required to create volume')
            vol_id = self.create_volume(vol_name, sg_name, size, cap_unit)
            changed = True

        if state == 'present' and vol and size:
            if size is None:
                self.module.fail_json(msg='Size is required to expand volume')
            # Convert the given size to GB
            if size is not None and size > 0:
                size = utils.get_size_in_gb(size, self.module.params[
                    'cap_unit'])
                LOG.info('Existing Size: {0} GB, Specified Size: {1} GB'.
                         format(existing_vol_size, size))
            changed = self.expand_volume(vol_id, size, existing_vol_size)

        if state == 'present' and vol and new_name:
            vol_name = vol['volume_identifier']
            if new_name != vol_name:
                LOG.info('Changing the name of volume {0} to {1}'.
                         format(vol_name, new_name))
                changed = self.rename_volume(vol_id, new_name) or changed

        if state == 'absent' and vol:
            LOG.info('Deleting volume {0} '.format(vol_id))
            changed = self.delete_volume(vol_id) or changed

        if state == 'present' and vol and new_sg_name:
            changed = self.move_volume_between_storage_groups(
                vol_id, vol_name, sg_name, new_sg_name) or changed

        '''
        Finally update the module changed state and saving updated volume
        details
        '''
        self.result["changed"] = changed
        self.result["volume_details"] = self.get_volume()
        self.module.exit_json(**self.result)


def get_powermax_volume_parameters():
    """This method provide parameter required for the ansible volume
    modules on PowerMax"""
    return dict(
        vol_name=dict(required=False, type='str'),
        vol_id=dict(required=False, type='str'),
        size=dict(type='float', default=None),
        sg_name=dict(required=False, type='str'),
        new_sg_name=dict(required=False, type='str'),
        new_name=dict(required=False, type='str'),
        cap_unit=dict(default='GB', choices=['MB', 'GB', 'TB'], type='str'),
        state=dict(required=True, type='str')
        )


def main():
    """ Create PowerMax volume object and perform action on it
        based on user input from playbook"""
    obj = PowerMaxVolume()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
