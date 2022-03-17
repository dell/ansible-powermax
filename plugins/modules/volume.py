#!/usr/bin/python
# Copyright: (c) 2019-2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: volume
version_added: '1.0.0'
short_description:  Manage volumes on PowerMax Storage System
description:
- Managing volumes on PowerMax storage system includes creating a volume,
  renaming a volume, expanding a volume, and deleting a volume.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
options:
  vol_name:
    description:
    - The name of the volume.
    type: str
  sg_name:
    description:
    - The name of the storage group.
    type: str
  new_sg_name:
    description:
    - The name of the target storage group.
    type: str
  vol_id:
    description:
    - The native id of the volume.
    - Required for rename and delete volume operations.
    type: str
  size:
    description:
    - The new size of existing volume.
    - Required for create and expand volume operations.
    type: float
  cap_unit:
    description:
    - volume capacity units.
    - If not specified, default value is GB.
    choices: [ MB, GB, TB ]
    type: str
  new_name:
    description:
    - The new volume identifier for the volume.
    type: str
  vol_wwn:
    description:
    - The WWN of the volume.
    type: str
  state:
    description:
    - Defines whether the volume should exist or not.
    required: true
    choices: [absent, present]
    type: str
notes:
- To expand a volume, either provide vol_id or vol_name or vol_wwn and sg_name.
- size is required to create/expand a volume.
- vol_id is required to rename/delete a volume.
- vol_name, sg_name and new_sg_name is required to move volumes between
  storage groups.
- Deletion of volume will fail if the storage group is part of a masking
  view.
'''

EXAMPLES = r'''
- name: Create volume
  dellemc.powermax.volume:
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
  dellemc.powermax.volume:
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
  dellemc.powermax.volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    new_name:  "Test_GOLD_vol_Renamed"
    vol_id: "0059B"
    state: 'present'

- name: Delete volume using volume ID
  dellemc.powermax.volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    vol_id: "0059B"
    state: 'absent'

- name: Delete volume using volume WWN
  dellemc.powermax.volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    vol_wwn: "60000970000197900237533030303246"
    state: 'absent'

- name: Move volume between storage group
  dellemc.powermax.volume:
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
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
volume_details:
    description: Details of the volume.
    returned: When volume exists.
    type: complex
    contains:
        allocated_percent:
            description: Allocated percentage the volume.
            type: int
        cap_cyl:
            description: Number of cylinders.
            type: int
        cap_gb:
            description: Volume capacity in GB.
            type: int
        cap_mb:
            description: Volume capacity in MB.
            type: int
        effective_wwn:
            description: Effective WWN of the volume.
            type: str
        emulation:
            description: Volume emulation type.
            type: str
        encapsulated:
            description: Flag for encapsulation.
            type: bool
        has_effective_wwn:
            description: Flag for effective WWN presence.
            type: str
        mobility_id_enabled:
            description: Flag for enabling mobility.
            type: bool
        num_of_front_end_paths:
            description: Number of front end paths in the volume.
            type: int
        num_of_storage_groups:
            description: Number of storage groups in which volume is present.
            type: int
        pinned:
            description: Pinned flag.
            type: bool
        rdfGroupId:
            description: RDFG number for volume.
            type: int
        reserved:
            description: Reserved flag.
            type: bool
        snapvx_source:
            description: Source SnapVX flag.
            type: bool
        snapvx_target:
            description: Target SnapVX flag.
            type: bool
        ssid:
            description: SSID of the volume.
            type: str
        status:
            description: Volume status.
            type: str
        storageGroupId:
            description: Storage group ID of the volume.
            type: str
        storage_groups:
            description: List of storage groups for the volume.
            type: list
        type:
            description: Type of the volume.
            type: str
        volumeId:
            description: Unique ID of the volume.
            type: str
        volume_identifier:
            description: Name identifier for the volume.
            type: str
        wwn:
            description: WWN of the volume.
            type: str
'''

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule
import logging

LOG = utils.get_logger('volume')
HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class Volume(object):
    """Class with volume operations"""

    volume_id = None
    u4v_conn = None

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_volume_parameters())

        mutually_exclusive = [
            ['vol_id', 'vol_name'], ['vol_id', 'vol_wwn'],
            ['vol_name', 'vol_wwn']
        ]

        required_one_of = [
            ['vol_id', 'vol_name', 'vol_wwn']
        ]

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
        )

        # result is a dictionary that contains changed status and
        # volume details
        self.result = {"changed": False, "volume_details": {}}
        if HAS_PYU4V is False:
            self.show_error_exit(msg="Ansible modules for PowerMax require "
                                 "the PyU4V python library to be "
                                 "installed. Please install the library "
                                 "before using these modules.")

        if PYU4V_VERSION_CHECK is not None:
            self.show_error_exit(msg=PYU4V_VERSION_CHECK)

        if self.module.params['universion'] is not None:
            universion_details = utils.universion_check(
                self.module.params['universion'])
            LOG.info("universion_details: %s", universion_details)

            if not universion_details['is_valid_universion']:
                self.show_error_exit(msg=universion_details['user_message'])

        try:
            self.u4v_conn = utils.get_U4V_connection(
                self.module.params, application_type=APPLICATION_TYPE)
        except Exception as e:
            self.show_error_exit(msg=str(e))
        LOG.info('Check Mode Flag %s', self.module.check_mode)
        LOG.info('Got PyU4V instance for provisioning on to VMAX ')
        self.provisioning = self.u4v_conn.provisioning
        self.replication = self.u4v_conn.replication
        self.common = self.u4v_conn.common
        self.foxtail_version = '5978.444.444'

    def get_volume(self):
        """
        Get volume details
        """
        if self.volume_id:
            return self.get_volume_by_nativeid(self.volume_id)

        sg_name = self.module.params['sg_name']

        volume_list = None
        volume_name = None
        if self.module.params['vol_name'] is not None:
            volume_name = self.module.params['vol_name']
            params = {"storageGroupId": sg_name,
                      "volume_identifier": volume_name}
            volume_list = self.provisioning.get_volume_list(params)

        if self.module.params['vol_wwn'] is not None:
            vol_wwn = self.module.params['vol_wwn']
            params = {"storageGroupId": sg_name, "wwn": vol_wwn}
            volume_list = self.provisioning.get_volume_list(params)

        vol = None
        if not volume_list or len(volume_list) == 0:
            LOG.debug('No volume found in storage group %s', sg_name)
        elif len(volume_list) > 1:
            self.show_error_exit(msg='Duplicate volumes found: '
                                 'There are {0} '
                                 'volume(s) with the same name {1} in '
                                 'the storage group {2}'.
                                 format(len(volume_list), volume_name,
                                        sg_name)
                                 )
        else:
            vol = self.get_volume_by_nativeid(volume_list[0])
            if self.module.params['vol_wwn'] is not None and "effective_wwn" \
                    in vol and vol['effective_wwn'] \
                    != self.module.params['vol_wwn']:
                msg = ('The given volume with WWN: %s also has an effective'
                       ' WWN: %s associated with it, which does not match. '
                       'It is recommended that the user retries the '
                       'operation with Volume name or ID'
                       % (self.module.params['vol_wwn'], vol['effective_wwn']))
                self.show_error_exit(msg=msg)
        return vol

    def get_volume_by_nativeid(self, native_id):
        try:
            LOG.info('Getting volume %s details using native id', native_id)
            return self.provisioning.get_volume(native_id)
        except Exception as e:
            LOG.error('Got error %s while getting details of volume %s',
                      str(e), native_id)
            return None

    def delete_volume_deallocate(self, vol_id):
        """
        Deallocate a volume first and then delete it
        """
        try:
            if not self.module.check_mode:
                self.provisioning.deallocate_volume(vol_id)
                self.provisioning.delete_volume(vol_id)
            return True
        except Exception as e:
            error_msg = 'Delete volume %s failed with error %s ' \
                        % (vol_id, str(e))
            self.show_error_exit(msg=error_msg)

    def delete_volume(self, vol_id):
        """
        Delete volume from system
        """
        try:
            if not self.module.check_mode:
                self.provisioning.delete_volume(vol_id)
            return True
        except Exception as e:
            if "A free of all allocations is required" in str(e):
                if not self.module.check_mode:
                    self.delete_volume_deallocate(vol_id)
                return True
            else:
                error_msg = 'Delete volume %s failed with error %s ' \
                            % (vol_id, str(e))
                self.show_error_exit(msg=error_msg)

    def rename_volume(self, vol_id, vol_new_name):
        """Rename the volume's identifier"""
        try:
            volume_sg_list = self.provisioning.get_storage_group_from_volume(
                vol_id)
            if volume_sg_list is not None:
                for sg in volume_sg_list:
                    params = {"storageGroupId": sg,
                              "volume_identifier": vol_new_name}
                    volume_list = self.provisioning.get_volume_list(params)

                    if volume_list:
                        self.show_error_exit(
                            msg="Volume already exists with volume"
                                " name {0} in storage group {1}".
                            format(vol_new_name, sg))

            if not self.module.check_mode:
                self.provisioning.rename_volume(vol_id, vol_new_name)
            return True
        except Exception as e:
            self.show_error_exit(msg='Rename volume {0} failed with '
                                 'error {1}'.format(vol_id, str(e)))

    def expand_volume(self, vol_id, size_in_gb, existing_vol_size,
                      rdfg_no=None):
        msg = ("Expanding volume capacity from %s GB to %s GB with rdf group "
               "no %s and vol_id %s" % (existing_vol_size, size_in_gb,
                                        rdfg_no, vol_id))
        LOG.info(msg)
        if not self.module.check_mode:
            self.provisioning.extend_volume(
                vol_id, str(size_in_gb), rdf_group_num=rdfg_no)
        return True

    def expand_concurrent_configuration(self, vol, size_in_gb,
                                        existing_vol_size):
        rdfg_list = vol['rdfGroupId']
        vol_id = vol['volumeId']

        hop1_vol_rdf_details = self.replication.get_rdf_group_volume(
            rdf_number=rdfg_list[0]['rdf_group_number'], device_id=vol_id)

        hop2_vol_rdf_details = self.replication.get_rdf_group_volume(
            rdf_number=rdfg_list[1]['rdf_group_number'], device_id=vol_id)

        self.u4v_conn.set_array_id(
            array_id=hop1_vol_rdf_details['remoteSymmetrixId'])
        hop1_volume_details = self.get_volume_by_nativeid(
            hop1_vol_rdf_details['remoteVolumeName'])

        self.u4v_conn.set_array_id(
            array_id=hop2_vol_rdf_details['remoteSymmetrixId'])
        hop2_volume_details = self.get_volume_by_nativeid(
            hop2_vol_rdf_details['remoteVolumeName'])

        '''
        Example configuration:
                R11 -- R21 -- R2
                |
                R2
        '''
        # TODO:  will revisit after PyU4V implements unique way of
        #  identifying Metro DR replication
        if (len(hop1_volume_details['rdfGroupId']) > 1 or
                len(hop2_volume_details['rdfGroupId']) > 1):
            msg = ("Expansion of volume in Cascaded / Metro DR "
                   "configurations is not supported by Ansible modules")
            self.show_error_exit(msg=msg)

        if (hop1_vol_rdf_details['rdfMode'] == 'Active' or
                hop2_vol_rdf_details['rdfMode'] == 'Active'):
            array_details = self.common.get_array(
                hop1_vol_rdf_details['localSymmetrixId'])
            if utils.parse_version(array_details['ucode']) \
                    < utils.parse_version(self.foxtail_version):
                msg = ("Expansion of SRDF/Metro protected volumes is "
                       "supported from v5978.444.444 onward. Please upgrade "
                       "the array for this support.")
                self.show_error_exit(msg=msg)

        if hop1_vol_rdf_details['rdfMode'] == 'Active' \
                or hop2_vol_rdf_details['rdfMode'] != 'Active':
            # expand hop2 device first.  Need to direct PyU4V to remote Array
            self.u4v_conn .set_array_id(
                array_id=hop2_vol_rdf_details['remoteSymmetrixId'])
            self.expand_volume(
                vol_id=hop2_vol_rdf_details['remoteVolumeName'],
                size_in_gb=size_in_gb,
                existing_vol_size=existing_vol_size)
            # expand local device
            self.u4v_conn.set_array_id(
                array_id=hop1_vol_rdf_details['localSymmetrixId'])
            return self.expand_volume(vol_id=vol_id,
                                      size_in_gb=size_in_gb,
                                      existing_vol_size=existing_vol_size,
                                      rdfg_no=hop1_vol_rdf_details[
                                          'localRdfGroupNumber'])

        # expand hop1 device first.  Need to direct PyU4V to remote Array
        self.u4v_conn.set_array_id(
            array_id=hop1_vol_rdf_details['remoteSymmetrixId'])

        self.expand_volume(vol_id=hop1_vol_rdf_details['remoteVolumeName'],
                           size_in_gb=size_in_gb,
                           existing_vol_size=existing_vol_size)
        # expand local device
        self.u4v_conn.set_array_id(
            array_id=hop2_vol_rdf_details['localSymmetrixId'])
        return self.expand_volume(vol_id=vol_id,
                                  size_in_gb=size_in_gb,
                                  existing_vol_size=existing_vol_size,
                                  rdfg_no=hop2_vol_rdf_details[
                                      'localRdfGroupNumber'])

    def srdf_volume_expansion(self, vol, size_in_gb, existing_vol_size):
        rdfg_list = vol['rdfGroupId']
        try:
            # TODO:  will revisit after PyU4V implements unique way of
            #  identifying Metro DR replication
            if len(rdfg_list) == 2 and (vol['type'] == 'RDF2+TDEV' or
                                        vol['type'] == 'RDF21+TDEV'):
                # cascaded configuration detected
                msg = ("Expansion of volume in Cascaded / Metro DR "
                       "configurations is not supported by Ansible modules")
                self.show_error_exit(msg=msg)

            elif len(rdfg_list) == 1 and (vol['type'] == 'RDF2+TDEV' or
                                          vol['type'] == 'RDF21+TDEV'):
                # find rdf1+tdev volume and call the function with that
                vol_rdf_details = self.replication.get_rdf_group_volume(
                    rdf_number=rdfg_list[0]['rdf_group_number'],
                    device_id=vol['volumeId'])
                self.u4v_conn.set_array_id(
                    array_id=vol_rdf_details['remoteSymmetrixId'])
                return self.srdf_volume_expansion(
                    self.get_volume_by_nativeid(
                        vol_rdf_details['remoteVolumeName']),
                    size_in_gb, existing_vol_size)

            if len(rdfg_list) == 1 and vol['type'] == 'RDF1+TDEV':
                # check for SRDF/Metro link
                vol_rdf_details = self.replication.get_rdf_group_volume(
                    rdf_number=rdfg_list[0]['rdf_group_number'],
                    device_id=vol['volumeId'])

                if vol_rdf_details['rdfMode'] == 'Active':
                    array_details = self.common.get_array(
                        vol_rdf_details['localSymmetrixId'])
                    if utils.parse_version(array_details['ucode']) \
                            < utils.parse_version(self.foxtail_version):
                        msg = ("Expansion of SRDF/Metro protected volumes is"
                               " supported from v5978.444.444 onward. Please "
                               "upgrade the array for this support.")
                        self.show_error_exit(msg=msg)

                # check for SRDF/cascaded configuration
                self.u4v_conn.set_array_id(
                    array_id=vol_rdf_details['remoteSymmetrixId'])
                remote_volume_details = self.get_volume_by_nativeid(
                    vol_rdf_details['remoteVolumeName'])
                # TODO:  will revisit after PyU4V implements unique way of
                #  identifying Metro DR replication
                if len(remote_volume_details['rdfGroupId']) > 1:
                    msg = ("Expansion of volume in Cascaded / Metro DR "
                           "configurations is not supported by Ansible "
                           "modules")
                    self.show_error_exit(msg=msg)

                self.u4v_conn.set_array_id(
                    array_id=vol_rdf_details['localSymmetrixId'])
                return self.expand_volume(vol['volumeId'], size_in_gb,
                                          existing_vol_size,
                                          rdfg_no=rdfg_list[0]
                                          ['rdf_group_number'])

            # case where len(rdfg_list)==2 and vol['type'] == 'RDF1+TDEV':
            return self.expand_concurrent_configuration(vol,
                                                        size_in_gb,
                                                        existing_vol_size)

        except Exception as e:
            msg = 'Expand volume {0} failed with error: {1}'.format(
                vol['volumeId'], str(e))
            self.show_error_exit(msg=msg)

    def expand_volume_helper(self, vol, size_in_gb, existing_vol_size):
        """Expand volume's size to new size"""
        vol_id = vol['volumeId']
        try:
            if size_in_gb < existing_vol_size:
                self.show_error_exit(msg='Current volume size {0} GB is '
                                     'greater than {1} GB specified.'.
                                     format(existing_vol_size, size_in_gb))
            elif size_in_gb > existing_vol_size:
                if 'rdfGroupId' in vol:
                    array_id = self.module.params['serial_no']
                    array_details = self.common.get_array(array_id=array_id)
                    if utils.parse_version(array_details['ucode'])\
                            < utils.parse_version(self.foxtail_version):
                        msg = ("Expansion of SRDF protected volume is"
                               " supported from v5978.444.444 onward. Please"
                               " upgrade the array for this support.")
                        self.show_error_exit(msg=msg)
                    return self.srdf_volume_expansion(vol, size_in_gb,
                                                      existing_vol_size)
                return self.expand_volume(vol_id, size_in_gb,
                                          existing_vol_size)

            LOG.info('Current volume size and specified volume size'
                     ' are equal')
            return False
        except Exception as e:
            error_message = 'Expand volume %s failed with error: %s' \
                            % (vol_id, str(e))
            self.show_error_exit(msg=error_message)

    def create_volume(self, vol_name, sg_name, size, cap_unit):
        """Create PowerMax volume in a storage group"""
        try:
            if self.module.params['vol_name'] is None:
                self.show_error_exit(msg='vol_name is required'
                                     ' during volume creation')
            LOG.info("SG MSG: %s ", sg_name)
            remote_array = None
            remote_array_sg = None
            remote_array_1 = None
            remote_array_1_sg = None
            remote_array_2 = None
            remote_array_2_sg = None
            vol_id = None

            # Check SRDF protected SG
            if sg_name is not None:
                storage_group = self.get_storage_group(sg_name)
                if (storage_group is not None and
                        self.if_srdf_protected(storage_group)):
                    array_id = self.module.params['serial_no']
                    array_details = self.common.get_array(array_id=array_id)
                    if utils.parse_version(array_details['ucode']) \
                            < utils.parse_version(self.foxtail_version):
                        msg = ("Creating new volumes on SRDF protected"
                               " storage groups is supported from"
                               " v5978.444.444 onward. Please upgrade the"
                               " array for this support.")
                        self.show_error_exit(msg=msg)
                    rdfg_list = self.replication.\
                        get_storage_group_srdf_group_list(
                            storage_group_id=sg_name)

                    # Multisite configuration
                    if len(rdfg_list) == 2:
                        LOG.info("Concurrent configuration detected "
                                 "for %s", sg_name)
                        rdfg_details = self.replication.\
                            get_rdf_group(rdf_number=rdfg_list[0])
                        remote_array_1 = rdfg_details['remoteSymmetrix']
                        remote_array_1_sg = sg_name
                        rdfg_details = self.replication. \
                            get_rdf_group(rdf_number=rdfg_list[1])
                        remote_array_2 = rdfg_details['remoteSymmetrix']
                        remote_array_2_sg = sg_name
                        msg = ('Creating volume with parameters:'
                               'storage_group_id= ', sg_name,
                               ', num_vols= ', 1,
                               ', vol_size= ', size,
                               ', cap_unit= ', cap_unit,
                               ', vol_name= ', vol_name,
                               ', create_new_volumes= ', True,
                               ', remote_array_1_id= ',
                               remote_array_1,
                               ', remote_array_1_sgs= ',
                               remote_array_1_sg,
                               ', remote_array_2_id= ',
                               remote_array_2,
                               ', remote_array_2_sgs= ',
                               remote_array_2_sg
                               )
                        LOG.info(msg)
                        if not self.module.check_mode:
                            self.provisioning.add_new_volume_to_storage_group(
                                storage_group_id=sg_name, num_vols=1,
                                vol_size=size,
                                cap_unit=cap_unit, vol_name=vol_name,
                                create_new_volumes=True,
                                remote_array_1_id=remote_array_1,
                                remote_array_1_sgs=remote_array_1_sg,
                                remote_array_2_id=remote_array_2,
                                remote_array_2_sgs=remote_array_2_sg)
                            vol_id = self.provisioning.find_volume_device_id(
                                volume_name=vol_name)
                        LOG.info('Created volume native ID: %s', vol_id)
                        return vol_id

                    elif len(rdfg_list) > 2:
                        err_msg = ("More than 2 rdf groups exists for the "
                                   "given storage group %s. Create volume is "
                                   "not supported.", sg_name)
                        self.show_error_exit(msg=err_msg)

                    rdfg_details = self.replication. \
                        get_rdf_group(rdf_number=rdfg_list[0])
                    remote_array = rdfg_details['remoteSymmetrix']
                    remote_array_sg = sg_name

            # Create new volume and add to storage group
            msg = ('Creating volume with parameters:'
                   'storage_group_id= ', sg_name,
                   ', num_vols= ', 1,
                   ', vol_size= ', size,
                   ', cap_unit= ', cap_unit,
                   ', vol_name= ', vol_name,
                   ', create_new_volumes= ', True,
                   ', remote_array_1_id= ',
                   remote_array_1,
                   ', remote_array_1_sgs= ',
                   remote_array_1_sg)
            LOG.info(msg)
            if not self.module.check_mode:
                self.provisioning.add_new_volume_to_storage_group(
                    storage_group_id=sg_name, num_vols=1, vol_size=size,
                    cap_unit=cap_unit, vol_name=vol_name,
                    create_new_volumes=True, remote_array_1_id=remote_array,
                    remote_array_1_sgs=remote_array_sg)
                vol_id = self.provisioning.find_volume_device_id(
                    volume_name=vol_name)
            LOG.info('Created volume native ID: %s', vol_id)
            return vol_id
        except Exception as e:
            error_message = 'Create volume %s failed with error %s' \
                            % (vol_name, str(e))
            self.show_error_exit(msg=error_message)

    def move_volume_between_storage_groups(self, vol, sg_name,
                                           new_sg_name):
        """Move volume between storage group"""
        vol_name = vol['volume_identifier']
        try:
            volume_list = None
            if vol_name is not None:
                params = {"storageGroupId": new_sg_name,
                          "volume_identifier": vol_name}
                volume_list = self.provisioning.get_volume_list(params)

            if volume_list:
                self.show_error_exit(msg="Volume already exists with volume "
                                     "name %s in storage group %s"
                                     % (vol_name, new_sg_name))
            storage_group_src = self.get_storage_group(sg_name)
            if self.if_srdf_protected(storage_group_src):
                protected_sg_msg = ("Move volume from Storage group %s "
                                    "not supported from Ansible module "
                                    "as this operation for an SRDF protected"
                                    " Storage Group will render it "
                                    "unprotected and unmanageable." % sg_name)
                self.show_error_exit(msg=protected_sg_msg)

            storage_group_dstn = self.get_storage_group(new_sg_name)
            if self.if_srdf_protected(storage_group_dstn):
                protected_sg_msg = ("Move volume to Storage group %s "
                                    "not supported from Ansible module as"
                                    " this operation for an SRDF protected"
                                    " Storage Group will render it "
                                    "unprotected and unmanageable." %
                                    new_sg_name)
                self.show_error_exit(msg=protected_sg_msg)
            if not self.module.check_mode:
                self.provisioning.move_volumes_between_storage_groups(
                    vol['volumeId'], sg_name, new_sg_name)
            return True
        except Exception as e:
            error_message = ('Move volume %s from SG %s to SG %s failed with'
                             ' error %s' % (vol_name, sg_name, new_sg_name,
                                            str(e)))
            self.show_error_exit(msg=error_message)

    def if_srdf_protected(self, sg_details):
        """Check if this storage group is protected with srdf"""
        try:
            if not sg_details['unprotected']:
                srdf_sgs = self.replication.get_replication_enabled_storage_groups(has_srdf=True)
                if sg_details['storageGroupId'] in srdf_sgs:
                    return True
            return False
        except Exception as e:
            msg = "Failed to determine if storage group %s is srdf protected, " \
                  "with error %s" % (sg_details['storageGroupId'], str(e))
            LOG.error(msg)
            self.show_error_exit(msg=msg)

    def get_storage_group(self, sg_name):
        """Get storage group details"""
        try:
            LOG.info('Getting storage group %s details', sg_name)
            return self.provisioning.get_storage_group(sg_name)
        except Exception as e:
            msg = 'Get storage group %s failed with error %s' % (
                sg_name, str(e))
            LOG.error(msg)
            self.show_error_exit(msg=msg)

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = "Failed to close unisphere connection with error:" \
                          " {0}".format(str(e))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

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

        if vol_name is not None and sg_name is None:
            self.show_error_exit(msg='Specify Storage group name along '
                                 'with volume name')

        if size and cap_unit is None:
            cap_unit = 'GB'
        elif cap_unit and size is None:
            self.show_error_exit(msg='Parameters size and cap_unit are '
                                     'required together')
        self.volume_id = vol_id

        vol = self.get_volume()

        existing_vol_size = 0
        if vol is not None:
            self.volume_id = vol['volumeId']
            vol_id = vol['volumeId']
            existing_vol_size = vol['cap_gb']

        changed = False

        # Call to create volume in storage group
        if state == 'present' and vol is None:
            if new_name:
                self.show_error_exit(msg="Invalid argument new_name "
                                         "while creating a volume")
            if size is None:
                self.show_error_exit(msg='Size is required to create volume')
            vol_id = self.create_volume(vol_name, sg_name, size, cap_unit)
            changed = True

        if state == 'present' and vol and size:
            if size is None:
                self.show_error_exit(msg='Size is required to expand volume')
            # Convert the given size to GB
            if size is not None and size > 0:
                size = utils.get_size_in_gb(size, cap_unit)
                LOG.info('Existing Size: %s GB, Specified Size: %s GB',
                         existing_vol_size, size)
            changed = self.expand_volume_helper(vol, size, existing_vol_size)

        if state == 'present' and vol and new_name is not None:
            if len(new_name.strip()) == 0:
                self.show_error_exit(msg="Please provide valid volume "
                                         "name.")

            vol_name = vol['volume_identifier']
            if new_name != vol_name:
                LOG.info('Changing the name of volume %s to %s',
                         vol_name, new_name)
                changed = self.rename_volume(vol_id, new_name) or changed

        if state == 'absent' and vol:
            LOG.info('Deleting volume %s ', vol_id)
            changed = self.delete_volume(vol_id) or changed

        if state == 'present' and vol and new_sg_name:
            vol_sg = vol['storageGroupId'][0]
            if vol_sg != new_sg_name:
                LOG.info('Moving volume from %s to %s', vol_sg, new_name)
                changed = self.move_volume_between_storage_groups(
                    vol, sg_name, new_sg_name) or changed

        '''
        Finally update the module changed state and saving updated volume
        details
        '''
        self.u4v_conn.set_array_id(
            array_id=self.module.params['serial_no'])
        self.result["changed"] = changed
        if state == 'present':
            self.result["volume_details"] = self.get_volume()
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")
        self.module.exit_json(**self.result)


def get_volume_parameters():
    """This method provide parameter required for the ansible volume
    modules on PowerMax"""
    return dict(
        vol_name=dict(required=False, type='str'),
        vol_id=dict(required=False, type='str'),
        size=dict(type='float'),
        sg_name=dict(required=False, type='str'),
        new_sg_name=dict(required=False, type='str'),
        new_name=dict(required=False, type='str'),
        cap_unit=dict(choices=['MB', 'GB', 'TB'], type='str'),
        vol_wwn=dict(required=False, type='str'),
        state=dict(required=True, type='str', choices=['absent', 'present'])
    )


def main():
    """ Create PowerMax volume object and perform action on it
        based on user input from playbook"""
    obj = Volume()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
