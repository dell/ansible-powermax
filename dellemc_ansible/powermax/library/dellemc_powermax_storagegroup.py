#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_storagegroup
version_added: '2.6'
short_description:  Manage storage groups on PowerMax/VMAX Storage System
description:
- Managing storage group on PowerMax Storage System includes
  List the volumes of a Storage Group,
  Create a new Storage Group,
  Delete an existing Storage Group,
  Add existing volumes to an existing Storage Group,
  Remove existing volumes from existing Storage Group,
  Create new Volumes in an existing Storage Group,
  Modify existing Storage Group attributes,
  Add child Storage Groups inside existing Storage Group(parent),
  Remove Child Storage Groups from existing parent Storage Group  
author:
- Vasudevu Lakhinana (Vasudevu.Lakhinana@dell.com)
- Prashant Rakheja (Prashant.Rakheja@dell.com)
options:
  sg_name:
    description:
    - The name of the storage group.
    required: true
  service_level:
    description:
    - The Name of SLO.
  srp:
    description:
    - Name of the storage resource pool. 
    - This parameter is ignored if service_level is not specified. 
    - Default is to use whichever is the default SRP on the array.
  compression:
    description:
    - compression on storage group.
    - Compression parameter is ignored if service_level is not specified. 
    - Default is true.
  volumes:
    description:
    - This is a list of volumes. 
    - Each volume has four attributes-
    - vol_name
    - size
    - cap_unit
    - vol_id.
    - Either the volume ID must be provided for existing volumes,
      or the name and size must be provided to add new volumes to SG.
      The unit is optional.
    - vol_name - Represents the name of the volume
    - size - Represents the volume size
    - cap_unit - The unit in which size is represented. Default unit is GB.
                 Choices are MB, GB, TB.
    - vol_id - This is the volume ID
  vol_state:
    description:
    - Describes the state of volumes inside SG
    choices: [present-in-group , absent-in-group]
  child_storage_groups:
    description:
    - This is a list of child storage groups 
  child_sg_state:
    description:
    - Describes the state of CSG inside parent SG    
    choices: [present-in-group, absent-in-group] 
  new_sg_name:
    description:
     - The new name of the Storage Group  
  state:
    description:
    - Define whether the storage group should exist or not.
    choices: [absent, present]
  '''

EXAMPLES = r'''
- name: Get storage group details including volumes
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "ansible_sg":      
      state: "present"         
- name: Create empty storage group 
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "foo"
      service_level:  "Diamond"
      srp: "SRP_1"
      compression: True
      state: "present"
            
- name: Delete the storage Group
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "foo"
      state: "absent"
            
- name: Adding existing volume(s) to existing SG
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "foo"
      state: "present"
      volumes:
        - vol_id: "00028"
        - vol_id: "00018"
        - vol_id: "00025"
      vol_state: "present-in-group" 
            
- name: Create new volumes for existing SG
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "foo"
      state: "present"
      volumes:
        - vol_name: "foo"
          size: 1
          cap_unit: "GB"
        - vol_name: "bar"
          size: 1
          cap_unit: "GB"
      vol_state: "present-in-group" 
            
- name: Remove volume(s) from existing SG
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "foo"
      state: "present"
      volumes:
        - vol_id: "00028"
        - vol_id: "00018"
        - vol_name: "ansible-vol"
      vol_state: "absent-in-group" 
            
- name: Adding child SG to parent SG
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "parent_sg"
      state: "present"
      child_storage_groups:
        - "pie"
        - "bar"
      child_sg_state: "present-in-group" 
            
- name: Removing child SG from parent SG
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "parent_sg":
      state: "present"
      child_storage_groups:
        - "pie"
        - "bar"
      child_sg_state: "absent-in-group"
      
- name: Rename Storage Group
    dellemc_powermax_storagegroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "ansible_sg":
      new_sg_name: "ansible_sg_renamed"
      state: "present"                                                
'''


RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

LOG = utils.get_logger('dellemc_powermax_storagegroup', log_devel=logging.INFO)
HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

class PowerMaxStorageGroup(object):
    """Class with Storage Group operations"""

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_powermax_storage_group_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )
        if HAS_PYU4V is False:
            self.module.fail_json(msg="Ansible modules for PowerMax require "
                                      "the PyU4V python library to be "
                                      "installed. Please install the library "
                                      "before using these modules.")
        if PYU4V_VERSION_CHECK is not None :
            self.module.fail_json(msg=PYU4V_VERSION_CHECK)
            LOG.error(PYU4V_VERSION_CHECK)

        self.u4v_conn = utils.get_U4V_connection(self.module.params)
        self.provisioning = self.u4v_conn.provisioning
        LOG.info('Got PyU4V instance for provisioning on PowerMax ')

    def get_volume(self):
        """Get volume details"""
        vol_id = self.module.params['vol_id']
        if vol_id is None:
            vol_id = self.provisioning.find_volume_device_id(
                self.module.params['vol_name'])
        try:
            LOG.info('Getting volume {0} details'.format(vol_id))
            return self.provisioning.get_volume(vol_id)
        except Exception as e:
            LOG.error('Got error {0} while getting details of volume {0}'
                      .format(str(e), vol_id))
            return None

    def get_volumes_storagegroup(self,sg_name):
        """Get the list of volumes from a storage group"""
        if sg_name is None:
            errmsg = 'StorageGroup name is required to get the candidate volumes'
            LOG.error(errmsg)
            self.module.fail_json(msg=errmsg)
        try:
            LOG.info('Getting the list of volumes from storage group {0}'.format(sg_name))
            sg_vol_list = self.provisioning.get_vols_from_storagegroup(sg_name)
            LOG.info('{0} volumes present in storage group {1}'.format(
                len(sg_vol_list), sg_name))
            return sg_vol_list
        except Exception as e:
            errmsg = 'Failed to list the volume from storage group {0} with error {1}'' \
                     '.format(sg_name, str(e))
            LOG.error(errmsg)
            self.module.fail_json(msg=errmsg)
            return None

    def get_storage_group(self, sg_name):
        """Get storage group details"""
        try:
            LOG.info('Getting storage group {0} details'.format(sg_name))
            return self.provisioning.get_storage_group(sg_name)
        except Exception as e:
            LOG.info('Got error {0} while getting details of storage group {1}'
                      .format(str(e), sg_name))
            return None

    def create_storage_group(self, sg_name):
        """Create a storage group"""

        slo = self.module.params['service_level']
        srp = self.module.params['srp']
        compression = self.module.params['compression']

        if compression is None:
            compression = True
        if slo and srp is None:
            srp = 'SRP_1'

        disable_compression = not compression
        try:
            LOG.info('Creating empty storage group {0} '.format(sg_name))
            resp = self.provisioning.create_empty_sg(srp, sg_name, slo,
                                                     workload=None,
                                                     disable_compression=disable_compression)
            return True, resp
        except Exception as e:
            LOG.error('Failed to create storage group {0} with error {1}'
                      .format(sg_name, str(e)))
            self.module.fail_json(msg='Create storage group {0} failed.{1}'
                                  .format(sg_name, str(e)))

    def add_volume_storage_group(self, sg_name):
        """Add new volume(s) to existing storage group"""
        volumes = self.module.params['volumes']
        LOG.info('Creating new volumes for SG {0}'.format(sg_name))
        changed = False
        for vol in volumes:
            LOG.info('Processing vol {0}'.format(vol))
            if ('vol_id' in vol) and ('vol_name' in vol):
                LOG.warn('Both name and id are found for volume {0}. No action would be taken. Please specify '
                         'either name or id'.format(sg_name))
                continue
            elif ('cap_unit' in vol) or ('vol_name' in vol) or ('size' in vol):
                if 'cap_unit' in vol:
                    unit = vol['cap_unit']
                else:
                    unit = 'GB'
                if 'vol_name' in vol:
                    name = vol['vol_name']
                else:
                    LOG.error('No valid name was specified for the volume {0}'
                              .format(vol))
                    self.module.fail_json(msg='No valid name was specified for the volume {0}'
                                          .format(vol))
                if 'size' in vol:
                    size = vol['size']
                else:
                    LOG.error('No valid size was specified for the volume {0}'
                              .format(vol))
                    self.module.fail_json(msg='No valid size was specified for the volume {0}'
                                          .format(vol))
                try:
                    params = {"storageGroupId": sg_name,
                              "volume_identifier": name}
                    volume_list = self.provisioning.get_volume_list(params)
                    if not volume_list or len(volume_list) == 0:
                        LOG.info(
                            'No volume found with volume identifier {0} '
                            'in storage group {1}'.format(name,
                                                          sg_name))
                        LOG.info('Creating volume with name {0}, size {1} {2}'
                                 .format(name, size, unit))
                        self.provisioning.create_volume_from_sg_return_dev_id(
                            name, sg_name, size, unit)
                        changed = True
                    elif len(volume_list) >= 1:
                        for volume in volume_list:
                            vol_details = self.provisioning.get_volume(volume)
                            if unit == 'GB' and vol_details['cap_gb'] == size:
                                break
                            elif unit == 'MB' and vol_details['cap_mb'] == size:
                                break
                            elif unit == 'TB' and vol_details['cap_gb'] == \
                                    utils.get_size_in_gb(size, unit):
                                break
                            else:
                                self.module.fail_json(msg='A volume with identifier {0} '
                                                          'but different size {1} GB '
                                                          'already exists. Please use '
                                                          'a different identifier for volume creation. '
                                                          'Currently, we support only unique identifiers '
                                                          'for volume creation on PowerMax from Ansible'.
                                                          format(name,
                                                                 vol_details['cap_gb'])
                                                      )
                except Exception as e:
                    LOG.error('Create volume for storage group {0} failed with error {1}'
                              .format(sg_name, str(e)))
                    self.module.fail_json(msg='Create volume for storage group {0} failed.'
                                          .format(sg_name))
        existing_volumes_in_sg = self.provisioning.get_vols_from_storagegroup(sg_name)
        return changed, existing_volumes_in_sg

    def delete_storage_group(self, sg_name):
        """Delete storage group from PowerMax"""
        try:
            self.provisioning.delete_storagegroup(sg_name)
            return True
        except Exception as e:
            LOG.error('Delete storage group {0} failed with error {1} '
                      .format(sg_name, str(e)))
            self.module.fail_json(msg='Delete storage group {0} failed.'
                                  .format(sg_name))

    def add_existing_volumes_to_sg(self, vol_list, sg_name):
        """Add existing Volumes to existing Storage Group"""

        existing_volumes_in_sg = self.provisioning.get_vols_from_storagegroup(sg_name)
        vol_ids = []
        for vol in vol_list:
            if ('vol_id' in vol) and ('vol_name' in vol):
                LOG.warn('Both name and id are found for volume {0}. No action would be taken. Please specify '
                         'either name or id'.format(vol))
                continue
            elif 'vol_id' in vol:
                vol_ids.append(vol['vol_id'])

        volumes_to_add = [vol for vol in vol_ids if vol not in set(existing_volumes_in_sg)]

        existing_volume_names_in_sg = []
        for vol in existing_volumes_in_sg:
            vol_details = self.provisioning.get_volume(vol)
            if 'volume_identifier' in vol_details:
                existing_volume_names_in_sg.append(
                    vol_details['volume_identifier'])

        vol_names_to_be_added = []
        for vol in volumes_to_add:
            vol_details = self.provisioning.get_volume(vol)
            if 'volume_identifier' in vol_details:
                vol_names_to_be_added.append(
                    vol_details['volume_identifier'])

        if len(vol_names_to_be_added) > len(set(vol_names_to_be_added)):
            self.module.fail_json(
                msg="One or more volumes to be added to SG {0} "
                    "has the same identifer.".format(sg_name))

        duplicate_names = any(elem in vol_names_to_be_added for elem in
                              existing_volume_names_in_sg)

        if duplicate_names:
            self.module.fail_json(
                msg="One or more volumes to be added are already present in"
                    " SG {0} with the same name.".
                    format(sg_name))

        if not volumes_to_add:
            LOG.info('The given volumes {0} are already present in storage group {1} '
                     .format(vol_ids, sg_name))
            return False, existing_volumes_in_sg
        try:
            self.provisioning.add_existing_vol_to_sg(sg_name, volumes_to_add)
            existing_volumes_in_sg = self.provisioning.get_vols_from_storagegroup(sg_name)
            return True, existing_volumes_in_sg
        except Exception as e:
            LOG.error('Add existing volume(s) to storage group {0} failed with error {1} '
                      .format(sg_name, str(e)))
            self.module.fail_json(msg='Add existing volumes to storage group {0} failed.'
                                  .format(sg_name))

    def remove_volumes_from_sg(self, vol_list, sg_name):
        """Remove volume(s) from Storage Group"""
        existing_volumes_in_sg = self.provisioning.get_vols_from_storagegroup(sg_name)
        vol_ids = []
        for vol in vol_list:
            if ('vol_id' in vol) and ('vol_name' in vol):
                LOG.warn('Both name and id are found for volume {0}. '
                         'No action would be taken. Please specify '
                         'either name or id'.format(vol))
                continue
            elif 'vol_id' in vol:
                vol_ids.append(vol['vol_id'].upper())
            elif 'vol_name' in vol:
                params = {"storageGroupId": sg_name,
                          "volume_identifier": vol['vol_name']}
                volume_list = self.provisioning.get_volume_list(params)
                if not volume_list or len(volume_list) == 0:
                    LOG.info(
                        'No volume found with volume identifier {0} '
                        'in storage group {1}'.format(vol['vol_name'], sg_name))
                elif len(volume_list) > 1:
                    self.module.fail_json(msg='Duplicate volumes found: '
                                              'There are {0} volume(s) with '
                                              'the same name {1} in '
                                              'the storage group {2}'.
                                          format(len(volume_list),
                                                 vol['vol_name'],
                                                 sg_name)
                                          )
                else:
                    vol_ids.append(volume_list[0])

        volumes_to_remove = [vol for vol in vol_ids if vol in set(existing_volumes_in_sg)]

        if not volumes_to_remove:
            LOG.info('The given volumes {0} are not present on the storage group {1} '
                     .format(vol_ids, sg_name))
            return False, existing_volumes_in_sg
        try:
            for vol in volumes_to_remove:
                self.provisioning.remove_vol_from_storagegroup(sg_name, vol)
            vol_list = self.provisioning.get_vols_from_storagegroup(sg_name)
            return True, vol_list
        except Exception as e:
            LOG.error('Remove existing volume from storage group {0} failed with error {1} '
                      .format(sg_name, str(e)))
            self.module.fail_json(msg='Remove existing volume from storage group {0} failed.'
                                  .format(sg_name))

    def modify_sg_srp(self, storage_group, new_srp):
        """Modify SRP of the Storage Group"""

        payload = {
            "editStorageGroupActionParam": {
                "editStorageGroupSRPParam": {
                    "srpId": new_srp
                },
            }
        }
        LOG.info('Modifying the SG SRP to {0} '.format(new_srp))
        try:
            self.provisioning.modify_storage_group(storage_group, payload)
        except Exception as e:
            LOG.error('Modify attribute SRP of storage group {0} failed with error {1} '
                      .format(storage_group, str(e)))
            self.module.fail_json(msg='Modify attribute SRP of storage group {0} failed.'
                                  .format(storage_group))

    def modify_sg_slo(self, sg_name, new_slo):
        """Modify service level of the Storage Group"""

        payload = {
            "editStorageGroupActionParam": {
                "editStorageGroupSLOParam": {
                    "sloId": new_slo
                }
            }
        }

        storage_group = self.get_storage_group(sg_name)
        LOG.info('Modifying the SG SLO to {0} '.format(new_slo))
        if ('slo' in storage_group and storage_group['slo'].lower() != self.module.params['service_level'].lower()) \
                or ('slo' not in storage_group and self.module.params['service_level'].lower() != "none"):
            try:
                LOG.info('The existing SG SLO is {0} and the desired SG SLO is {1} '
                         .format(storage_group['slo'], self.module.params['service_level']))
                self.provisioning.modify_storage_group(sg_name, payload)
            except Exception as e:
                LOG.error('Modify attribute SLO of storage group {0} failed with error {1} '
                          .format(sg_name, str(e)))
                self.module.fail_json(msg='Modify attribute SLO of storage group {0} failed.'
                                      .format(sg_name))

    def modify_sg_compression(self, sg_name, new_compression):
        """Modify compression of the Storage Group"""

        payload = {
            "editStorageGroupActionParam": {
                "editCompressionParam": {
                    "compression": new_compression
                }
            }
        }

        storage_group = self.get_storage_group(sg_name)

        if 'compression' in storage_group and storage_group['compression'] != self.module.params['compression']:
            try:
                LOG.info('The existing SG compression is {0} and the desired SG compression is {1} '
                         .format(storage_group['compression'], self.module.params['compression']))
                self.provisioning.modify_storage_group(sg_name, payload)
            except Exception as e:
                LOG.error('Modify attribute compression of storage group {0} failed with error {1} '
                          .format(sg_name, str(e)))
                self.module.fail_json(msg='Modify attribute SRP of storage group {0} failed.'
                                      .format(sg_name))

    def modify_storage_group_attributes(self, storage_group, modified_param):
        """Modify the Storage group attributes"""

        changed = False
        if 'modified_srp' in modified_param:
            self.modify_sg_srp(storage_group, modified_param['modified_srp'])
            changed = True

        if 'modified_slo' in modified_param:
            self.modify_sg_slo(storage_group, modified_param['modified_slo'])
            changed = True

        if 'modified_compression' in modified_param:
            self.modify_sg_compression(storage_group, modified_param['modified_compression'])
            changed = True

        return changed

    def add_child_sg_to_parent_sg(self, child_sg_list, parent_sg):
        """Add a child Storage Group(s) to parent Storage Group"""
        changed = False
        for child_sg in child_sg_list:
            if not self.provisioning.is_child_sg_in_parent_sg(child_sg, parent_sg):
                try:
                    self.provisioning.add_child_sg_to_parent_sg(child_sg, parent_sg)
                    changed = True
                except Exception as e:
                    error_message = 'Adding child SG {0} to parent storage ' \
                                    'group {1} failed with error {2} '
                    LOG.error(error_message
                              .format(child_sg, parent_sg, str(e)))
                    self.module.fail_json(msg=error_message
                                          .format(child_sg, parent_sg,
                                                  str(e)))
        return changed

    def remove_child_sg_from_parent_sg(self, child_sg_list, parent_sg):
        """Remove a child Storage Group from parent Storage Group"""
        changed = False
        for child_sg in child_sg_list:
            if self.provisioning.is_child_sg_in_parent_sg(child_sg, parent_sg):
                try:
                    self.provisioning.remove_child_sg_from_parent_sg(child_sg, parent_sg)
                    changed = True
                except Exception as e:
                    error_message = 'Removing child SG {0} from parent storage group {1} failed with error {2} '
                    LOG.error(error_message
                              .format(child_sg, parent_sg, str(e)))
                    self.module.fail_json(msg=error_message
                                          .format(child_sg, parent_sg, str(e)))
        return changed

    def is_storage_group_modified(self, storage_group):
        """Determine if the desired storage group state is different from existing SG"""
        modified = False
        modified_param = dict()

        if ('srp' in storage_group and self.module.params['srp'] is not None and
            storage_group['srp'].lower() != self.module.params['srp'].lower()) \
                or ('srp' not in storage_group and self.module.params['srp'] is not None and
                    self.module.params['srp'].lower() != "none"):
            modified_param['modified_srp'] = self.module.params['srp']
            modified = True

        if ('slo' in storage_group and self.module.params['service_level'] is not None and
            storage_group['slo'].lower() != self.module.params['service_level'].lower()) \
                or ('slo' not in storage_group and self.module.params['service_level'] is not None
                    and self.module.params['service_level'].lower() != "none"):
            modified_param['modified_slo'] = self.module.params['service_level']
            modified = True

        if 'compression' in storage_group and self.module.params['compression'] is not None and \
                storage_group['compression'] != self.module.params['compression']:
            modified_param['modified_compression'] = self.module.params['compression']
            modified = True

        LOG.info('The storage group {0} needs to be modified and the modified param are {1} '
                 .format(modified, modified_param))

        return modified, modified_param

    def rename_storage_group(self, storage_group, new_sg_name):
        """Rename the Storage Group"""
        if storage_group is None:
            error_message = 'Rename storage group {0} to new name {1} ' \
                            'failed because SG {0} does not exist '
            LOG.error(error_message.format(self.module.params['sg_name'],
                                           new_sg_name))
            self.module.fail_json(msg=error_message.
                                  format(self.module.params['sg_name'],
                                         new_sg_name))
        changed = False
        if storage_group['storageGroupId'] == new_sg_name:
            return changed
        payload = {
            "editStorageGroupActionParam": {
                "renameStorageGroupParam": {
                    "new_storage_Group_name": new_sg_name
                },
            }
        }
        try:
            self.provisioning.\
                modify_storage_group(storage_group['storageGroupId'], payload)
            changed = True
        except Exception as e:
            error_message = 'Rename storage group {0} to new name {1} ' \
                            'failed with error {2} '
            LOG.error(error_message.format(self.module.params['sg_name'],
                                           new_sg_name, str(e)))
            self.module.fail_json(msg=error_message.
                                  format(self.module.params['sg_name'],
                                         new_sg_name,
                                         str(e)))
        return changed

    def check_task_validity(self, volumes, vol_state):
        if volumes and vol_state is None:
            self.module.fail_json(msg="Please provide a valid vol_state.")

    def perform_module_operation(self):
        """
        Perform different actions on volume based on user parameter
        chosen in playbook
        """
        state = self.module.params['state']
        sg_name = self.module.params['sg_name']
        volumes = self.module.params['volumes']
        vol_state = self.module.params['vol_state']
        child_sgs = self.module.params['child_storage_groups']
        child_sg_state = self.module.params['child_sg_state']
        new_sg_name = self.module.params['new_sg_name']

        self.check_task_validity(volumes, vol_state)
        storage_group = self.get_storage_group(sg_name)

        modified = False
        if storage_group:
            modified, modified_param = self.is_storage_group_modified(storage_group)

        result = dict(
            changed=False,
            create_sg='',
            modify_sg='',
            add_vols_to_sg='',
            add_new_vols_to_sg='',
            remove_vols_from_sg='',
            add_child_sg='',
            remove_child_sg='',
            rename_sg='',
            delete_sg='',
            storage_group_volumes='',
        )
        if state == 'present' and storage_group and not new_sg_name and not volumes:
            LOG.info('Get volumes for storage group {0}'.format(sg_name))
            result['storage_group_volumes'] = self.get_volumes_storagegroup(sg_name)
        elif state == 'present' and not (storage_group or new_sg_name):
            LOG.info('Creating storage group {0}'.format(sg_name))
            result['create_sg'], result['storage_group_details'] = self.create_storage_group(sg_name)
            LOG.info('Get volumes for storage group {0}'.format(sg_name))
            result['storage_group_volumes'] = self.get_volumes_storagegroup(sg_name)
        elif state == 'absent' and storage_group:
            LOG.info('Delete storage group {0} '.format(sg_name))
            result['delete_sg'] = self.delete_storage_group(sg_name)

        if state == 'present' and vol_state == 'present-in-group' and storage_group and volumes:
            LOG.info('Create new volume(s) for storage group {0}'.format(sg_name))
            result['add_new_vols_to_sg'], result['storage_group_volumes'] = self.add_volume_storage_group(sg_name)
            LOG.info('Add existing volume(s) to storage group {0}'.format(sg_name))
            result['add_vols_to_sg'], result['storage_group_volumes'] = self.add_existing_volumes_to_sg(volumes,
                                                                                                        sg_name)
        elif state == 'present' and vol_state == 'absent-in-group' and storage_group and volumes:
            LOG.info('Remove existing volume(s) from storage group {0}'.format(sg_name))
            result['remove_vols_from_sg'], result['storage_group_volumes'] = self.remove_volumes_from_sg(volumes,
                                                                                                         sg_name)

        if state == 'present' and storage_group and modified:
            LOG.info('Modifying Storage group {0}'.format(sg_name))
            result['modify_sg'] = self.modify_storage_group_attributes(sg_name, modified_param)
            result['storage_group_volumes'] = self.get_volumes_storagegroup(sg_name)

        if state == 'present' and child_sg_state == 'present-in-group' and storage_group and child_sgs:
            LOG.info('Adding child SG to parent storage group {0}'.format(sg_name))
            result['add_child_sg'] = self.add_child_sg_to_parent_sg(child_sgs, sg_name)
            LOG.info('Get volumes for storage group {0}'.format(sg_name))
            result['storage_group_volumes'] = self.get_volumes_storagegroup(sg_name)
        elif state == 'present' and child_sg_state == 'absent-in-group' and storage_group and child_sgs:
            LOG.info('Removing child SG from parent storage group {0}'.format(sg_name))
            result['remove_child_sg'] = self.remove_child_sg_from_parent_sg(child_sgs, sg_name)
            LOG.info('Get volumes for storage group {0}'.format(sg_name))
            result['storage_group_volumes'] = self.get_volumes_storagegroup(sg_name)

        if state == 'present' and new_sg_name:
            LOG.info('Rename SG {0} to new name {1}'.format(sg_name, new_sg_name))
            result['rename_sg'] = self.rename_storage_group(storage_group, new_sg_name)
            if result['rename_sg']:
                sg_name = new_sg_name
                LOG.info('Get volumes for storage group {0}'.format(sg_name))
                result['storage_group_volumes'] = self.get_volumes_storagegroup(sg_name)

        if state == 'present' and storage_group:
            LOG.info('Found storage group {0}'.format(storage_group))
            updated_sg = self.get_storage_group(sg_name)
            result['storage_group_details'] = updated_sg

        if result['create_sg'] or result['modify_sg'] or result['add_vols_to_sg'] or result['remove_vols_from_sg']\
                or result['add_child_sg'] or result['remove_child_sg'] or result['delete_sg'] \
                or result['add_new_vols_to_sg'] or result['rename_sg']:
            result['changed'] = True

        # Finally update the module result.
        self.module.exit_json(**result)


def get_powermax_storage_group_parameters():
    return dict(
        sg_name=dict(required=True, type='str'),
        service_level=dict(required=False, type='str'),
        srp=dict(required=False, type='str'),
        compression=dict(required=False, type='bool'),
        volumes=dict(required=False, type='list'),
        vol_state=dict(required=False, choices=['absent-in-group', 'present-in-group'], type='str'),
        child_storage_groups=dict(required=False, type='list'),
        child_sg_state=dict(required=False, choices=['absent-in-group', 'present-in-group'], type='str'),
        new_sg_name=dict(required=False, type='str'),
        state=dict(required=True, choices=['present', 'absent'], type='str'),
        )


def main():
    """Create PowerMax storage group object and perform action on it
        based on user input from playbook"""
    obj = PowerMaxStorageGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
