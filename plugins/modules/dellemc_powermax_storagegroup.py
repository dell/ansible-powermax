#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_storagegroup
version_added: '1.0.3'
short_description:  Manage storage groups on PowerMax/VMAX Storage System
description:
- Managing storage groups on a PowerMax storage system includes listing the
  volumes of a storage group, creating a new storage group, deleting an
  existing storage group, adding existing volumes to an existing storage
  group, removing existing volumes from an existing storage group, creating
  new volumes in an existing storage group, modifying existing storage group
  attributes, adding child storage groups inside an existing storage group
  (parent), and removing a child storage group from an existing parent storage
  group.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
author:
- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
options:
  sg_name:
    description:
    - The name of the storage group.
    required: true
    type: str
  service_level:
    description:
    - The Name of SLO.
    type: str
  srp:
    description:
    - Name of the storage resource pool.
    - This parameter is ignored if service_level is not specified.
    - Default is to use whichever is the default SRP on the array.
    type: str
  compression:
    description:
    - compression on storage group.
    - Compression parameter is ignored if service_level is not specified.
    - Default is true.
    type: bool
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
    type: list
    elements: dict
  vol_state:
    description:
    - Describes the state of volumes inside the SG.
    choices: [present-in-group , absent-in-group]
    type: str
  child_storage_groups:
    description:
    - This is a list of child storage groups
    type: list
    elements: str
  child_sg_state:
    description:
    - Describes the state of CSG inside parent SG
    choices: [present-in-group, absent-in-group]
    type: str
  new_sg_name:
    description:
     - The new name of the storage group.
    type: str
  state:
    description:
    - Define whether the storage group should exist or not.
    choices: [absent, present]
    type: str
    required: true
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
    sg_name: "ansible_sg"
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
    sg_name: "parent_sg"
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
    sg_name: "ansible_sg"
    new_sg_name: "ansible_sg_renamed"
    state: "present"
'''


RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
add_child_sg:
    description: Sets to true when a child SG is added.
    returned: When value exists.
    type: bool
add_new_vols_to_sg:
    description: Sets to true when new volumes are added to the SG.
    returned: When value exists.
    type: bool
add_vols_to_sg:
    description: Sets to true when existing volumes are added to the SG.
    returned: When value exists.
    type: bool
added_vols_details:
    description: Volume IDs of the volumes added.
    returned: When value exists.
    type: list
create_sg:
    description: Sets to true when a new SG is created.
    returned: When value exists.
    type: bool
delete_sg:
    description: Sets to true when an SG is deleted.
    returned: When value exists.
    type: bool
modify_sg:
    description: Sets to true when an SG is modified.
    returned: When value exists.
    type: bool
remove_child_sg:
    description: Sets to true when a child SG is removed.
    returned: When value exists.
    type: bool
remove_vols_from_sg:
    description: Sets to true when volumes are removed.
    returned: When value exists.
    type: bool
removed_vols_details:
    description: Volume IDs of the volumes removed.
    returned: When value exists.
    type: list
rename_sg:
    description: Sets to true when an SG is renamed.
    returned: When value exists.
    type: bool
storage_group_details:
    description: Details of the storage group.
    returned: When storage group exists.
    type: complex
    contains:
        base_slo_name:
            description: Base Service Level Objective (SLO) of a storage
                         group.
            type: str
        cap_gb:
            description: Storage group capacity in GB.
            type: int
        compression:
            description: Compression flag.
            type: bool
        device_emulation:
            description: Device emulation type.
            type: str
        num_of_child_sgs:
            description: Number of child storage groups.
            type: int
        num_of_masking_views:
            description: Number of masking views associated with the storage
                         group.
            type: int
        num_of_parent_sgs:
            description: Number of parent storage groups.
            type: int
        num_of_snapshots:
            description: Number of snapshots for the storage group.
            type: int
        num_of_vols:
            description: Number of volumes in the storage group.
            type: int
        service_level:
            description: Type of service level.
            type: str
        slo:
            description: Service level objective (SLO) type.
            type: str
        slo_compliance:
            description: Type of SLO compliance.
            type: str
        srp:
            description: Storage resource pool.
            type: str
        storageGroupId:
            description: Id for the storage group.
            type: str
        type:
            description: type of storage group.
            type: str
        unprotected:
            description: Flag for storage group protection.
            type: bool
        vp_saved_percent:
            description: Percentage saved for virtual pools.
            type: int
storage_group_volumes_details:
    description: Details of the storage group volumes.
    returned: When storage group volumes exists.
    type: complex
    contains:
        effective_wwn:
            description: Effective WWN of the volume.
            type: str
        type:
            description: Type of the volume.
            type: str
        volumeId:
            description: Unique ID of the volume.
            type: str
        volume_identifier:
            description: Name associated with the volume.
            type: str
        wwn:
            description: WWN of the volume.
            type: str
'''

import logging
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('dellemc_powermax_storagegroup', log_devel=logging.
                       INFO)
HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.2'


class PowerMaxStorageGroup(object):
    """Class with Storage Group operations"""

    protected_sg_msg = "Modifying a volume(s)/child storagegroup(s)" \
                       " for an SRDF protected storage group will " \
                       "render it unprotected and unmanageable." \
                       " Hence this operation is not allowed through" \
                       " Ansible Module."

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_powermax_storage_group_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )
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
        self.provisioning = self.u4v_conn.provisioning
        self.replication = self.u4v_conn.replication
        self.common = self.u4v_conn.common
        self.foxtail_version = '5978.444.444'
        LOG.info('Got PyU4V instance for provisioning on PowerMax ')

    def get_volume(self):
        """Get volume details"""
        vol_id = self.module.params['vol_id']
        if vol_id is None:
            vol_id = self.provisioning.find_volume_device_id(
                self.module.params['vol_name'])
        try:
            LOG.info('Getting volume %s details', vol_id)
            return self.provisioning.get_volume(vol_id)
        except Exception as e:
            LOG.error('Got error %s while getting details of volume %s',
                      str(e), vol_id)
            return None

    def get_volumes_details_storagegroup(self, sg_name):
        """Get volumes details of a storage group"""
        if sg_name is None:
            errmsg = 'StorageGroup name is required to get the candidate ' \
                     'volumes details'
            self.show_error_exit(msg=errmsg)
        try:
            LOG.info('Getting volumes details of storage group %s', sg_name)
            sg_vol_list = self.provisioning.\
                get_volumes_from_storage_group(sg_name)
            LOG.info('%s volumes present in storage group %s',
                     len(sg_vol_list), sg_name)
            sg_vol_details = []
            for vol in sg_vol_list:
                vol_details = self.provisioning.get_volume(device_id=vol)
                details = dict(
                    type='',
                    volumeId=vol,
                    volume_identifier='',
                    wwn='',
                    effective_wwn='',
                )
                if 'volume_identifier' in vol_details:
                    details['volume_identifier'] = \
                        vol_details['volume_identifier']
                details['wwn'] = vol_details['wwn']
                details['effective_wwn'] = vol_details['effective_wwn']
                details['type'] = vol_details['type']
                sg_vol_details.append(details)
            return sg_vol_details
        except Exception as e:
            errmsg = 'Failed to get the volumes details of storage group %s'\
                     ' with error %s', sg_name, str(e)
            self.show_error_exit(msg=errmsg)
            return None

    def get_storage_group(self, sg_name):
        """Get storage group details"""
        try:
            LOG.info('Getting storage group %s details', sg_name)
            return self.provisioning.get_storage_group(sg_name)
        except Exception as e:
            LOG.info('Got error %s while getting details of storage '
                     'group %s', str(e), sg_name)
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
            LOG.info('Creating empty storage group %s ', sg_name)
            resp = self.provisioning.create_empty_storage_group(
                srp, sg_name, slo, workload=None,
                disable_compression=disable_compression)
            return True, resp
        except Exception as e:
            self.show_error_exit(msg='Create storage group {0} failed.{1}'
                                 .format(sg_name, str(e)))

    def add_volume_storage_group(self, sg_name):
        """Add new volume(s) to existing storage group"""
        volumes = self.module.params['volumes']
        LOG.info('Creating new volumes for SG %s', sg_name)
        changed = False
        storage_group = self.provisioning.get_storage_group(sg_name)
        for vol in volumes:
            LOG.info('Processing vol %s', vol)
            if ('vol_id' in vol) and ('vol_name' in vol):
                LOG.warn(
                    'Both name and id are found for volume %s. No action '
                    'would be taken. Please specify either name or id',
                    sg_name)
            elif ('cap_unit' in vol) or ('vol_name' in vol) or \
                    ('size' in vol):
                if 'cap_unit' in vol:
                    unit = vol['cap_unit']
                else:
                    unit = 'GB'
                if 'vol_name' in vol:
                    name = vol['vol_name']
                else:
                    self.show_error_exit(
                        msg='No valid name was specified for the volume {0}'
                            .format(vol))
                if 'size' in vol:
                    size = vol['size']
                else:
                    self.show_error_exit(
                        msg='No valid size was specified for the volume {0}'
                            .format(vol))
                try:
                    params = {"storageGroupId": sg_name,
                              "volume_identifier": name}
                    volume_list = self.provisioning.get_volume_list(params)
                    if not volume_list or len(volume_list) == 0:
                        LOG.info(
                            'No volume found with volume identifier %s '
                            'in storage group %s', name, sg_name)
                        remote_array = None
                        remote_array_sg = None

                        # Check SRDF protected SG
                        if not storage_group['unprotected']:
                            array_id = self.module.params['serial_no']
                            array_details = self.common.get_array(
                                array_id=array_id)
                            if utils.parse_version(array_details['ucode']) \
                                < utils.parse_version(
                                    self.foxtail_version):
                                msg = ("Add new volumes on SRDF protected"
                                       " storage group is supported from"
                                       " v5978.444.444 onward. Please"
                                       " upgrade the array for this support.")
                                self.show_error_exit(msg=msg)
                            rdfg_list = self.replication. \
                                get_storage_group_srdf_group_list(
                                    storage_group_id=sg_name)

                            # Basic configuration
                            if len(rdfg_list) == 1:
                                rdfg_details = self.replication.\
                                    get_rdf_group(rdf_number=rdfg_list[0])
                                remote_array = rdfg_details['remoteSymmetrix']
                                remote_array_sg = sg_name

                                msg = ("Creating volume with parameters:"
                                       "storage_group_id= ", sg_name,
                                       ", num_vols= ", 1,
                                       ", vol_size= ", size,
                                       ", cap_unit= ", unit,
                                       ", vol_name= ", name,
                                       ", create_new_volumes= ", True,
                                       ", remote_array_1_id= ", remote_array,
                                       ", remote_array_1_sgs= ",
                                       remote_array_sg)
                                LOG.info(msg)
                                self.provisioning.add_new_volume_to_storage_group(
                                    storage_group_id=sg_name, num_vols=1,
                                    vol_size=size, cap_unit=unit,
                                    vol_name=name,
                                    create_new_volumes=True,
                                    remote_array_1_id=remote_array,
                                    remote_array_1_sgs=remote_array_sg)
                                LOG.info('Volume created!')
                                changed = True

                            # Multisite configuration
                            if len(rdfg_list) == 2:
                                remote_array_1 = None
                                remote_array_1_sg = None
                                remote_array_2 = None
                                remote_array_2_sg = None
                                LOG.info("Concurrent configuration detected "
                                         "for %s", sg_name)
                                rdfg_details = self.replication. \
                                    get_rdf_group(rdf_number=rdfg_list[0])
                                remote_array_1 = rdfg_details['remoteSymmetrix']
                                remote_array_1_sg = sg_name
                                rdfg_details = self.replication. \
                                    get_rdf_group(rdf_number=rdfg_list[1])
                                remote_array_2 = rdfg_details['remoteSymmetrix']
                                remote_array_2_sg = sg_name
                                msg = ("Creating volume with parameters:"
                                       "storage_group_id= ", sg_name,
                                       ", num_vols= ", 1,
                                       ", vol_size= ", size,
                                       ", cap_unit= ", unit,
                                       ", vol_name= ", name,
                                       ", create_new_volumes= ", True,
                                       ", remote_array_1_id= ",
                                       remote_array_1,
                                       ", remote_array_1_sgs= ",
                                       remote_array_1_sg,
                                       ", remote_array_2_id= ",
                                       remote_array_2,
                                       ", remote_array_2_sgs= ",
                                       remote_array_2_sg
                                       )
                                LOG.info(msg)
                                self.provisioning.add_new_volume_to_storage_group(
                                    storage_group_id=sg_name, num_vols=1,
                                    vol_size=size, cap_unit=unit,
                                    vol_name=name,
                                    create_new_volumes=True,
                                    remote_array_1_id=remote_array_1,
                                    remote_array_1_sgs=remote_array_1_sg,
                                    remote_array_2_id=remote_array_2,
                                    remote_array_2_sgs=remote_array_2_sg)
                                LOG.info('Volume created!')
                                changed = True
                            if len(rdfg_list) > 2:
                                err_msg = (
                                    "More than 2 rdf groups exists for the given "
                                    "storage group {0}. Create volume is not "
                                    "supported.".formate(sg_name))
                                self.show_error_exit(msg=err_msg)

                        # non SRDF protected SG
                        else:
                            LOG.info('Creating volume with name %s, '
                                     'size %s %s', name, size, unit)
                            self.provisioning.add_new_volume_to_storage_group(
                                storage_group_id=sg_name, num_vols=1,
                                vol_size=size, cap_unit=unit, vol_name=name,
                                create_new_volumes=True,
                                remote_array_1_id=remote_array,
                                remote_array_1_sgs=remote_array_sg)
                            LOG.info('Volume created!')
                            changed = True
                    elif len(volume_list) >= 1:
                        for volume in volume_list:
                            isbreak = False
                            vol_details = self.provisioning.get_volume(volume)
                            if ((unit == 'GB' and vol_details['cap_gb']
                                 == size)
                                or (unit == 'MB' and vol_details['cap_mb']
                                    == size)
                                or (unit == 'TB' and vol_details['cap_gb']
                                    == utils.get_size_in_gb(size, unit))):
                                isbreak = True

                            if not isbreak:
                                self.show_error_exit(
                                    msg='A volume with identifier {0} '
                                    'but different size {1} GB '
                                    'already exists. Please use '
                                    'a different identifier for'
                                    ' volume creation.Currently,'
                                    ' we support only unique '
                                    'identifiers for '
                                    'volume creation on '
                                    'PowerMax from Ansible'. format(
                                        name, vol_details['cap_gb']))
                except Exception as e:
                    err_msg = "Add new volume(s) on storage group %s failed" \
                        " with error %s", sg_name, str(e)
                    self.show_error_exit(msg=err_msg)
        existing_volumes_details_in_sg = self.\
            get_volumes_details_storagegroup(sg_name)
        return changed, existing_volumes_details_in_sg

    def delete_storage_group(self, sg_name):
        """Delete storage group from PowerMax"""
        try:
            self.check_for_linked_snapshots(sg_name)
            self.provisioning.delete_storage_group(sg_name)
            return True
        except Exception as e:
            err_msg = "Delete storage group %s failed with error %s ", sg_name,\
                str(e)
            self.show_error_exit(msg=err_msg)

    def add_existing_volumes_to_sg(self, vol_list, sg_name):
        """Add existing Volumes to existing Storage Group"""

        storage_group = self.provisioning.get_storage_group(sg_name)
        existing_volumes_in_sg = self.provisioning.get_volumes_from_storage_group(
            sg_name)
        vol_ids = []
        for vol in vol_list:
            if ('vol_id' in vol) and ('vol_name' in vol):
                LOG.warn(
                    'Both name and id are found for volume %s. No action'
                    'would be taken. Please specify either name or id', vol)
            elif 'vol_id' in vol:
                vol_ids.append(vol['vol_id'])

        volumes_to_add = [
            vol for vol in vol_ids if vol not in set(existing_volumes_in_sg)]

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
            self.show_error_exit(
                msg="One or more volumes to be added to SG {0} "
                    "has the same identifer.".format(sg_name))

        duplicate_names = any(elem in vol_names_to_be_added for elem in
                              existing_volume_names_in_sg)

        if duplicate_names:
            self.show_error_exit(
                msg="One or more volumes to be added are already present in"
                    " SG {0} with the same name.".
                    format(sg_name))

        if not volumes_to_add:
            LOG.info(
                'The given volumes %s are already present in storage group '
                '%s', vol_ids, sg_name)
            existing_volumes_details_in_sg = self.\
                get_volumes_details_storagegroup(sg_name)
            return False, existing_volumes_details_in_sg
        try:

            if not storage_group['unprotected']:
                self.show_error_exit(msg=self.protected_sg_msg)

            self.provisioning.add_existing_vol_to_sg(sg_name, volumes_to_add)
            existing_volumes_details_in_sg = self.\
                get_volumes_details_storagegroup(sg_name)
            return True, existing_volumes_details_in_sg
        except Exception as e:
            errorMsg = ("Add existing volume(s) to storage group %s failed "
                        "with error %s", sg_name, str(e))
            self.show_error_exit(msg=errorMsg)

    def remove_volumes_from_sg(self, vol_list, sg_name):
        """Remove volume(s) from Storage Group"""
        existing_volumes_in_sg = self.provisioning.get_volumes_from_storage_group(
            sg_name)
        vol_ids = []
        for vol in vol_list:
            if ('vol_id' in vol) and ('vol_name' in vol):
                LOG.warn('Both name and id are found for volume %s. '
                         'No action would be taken. Please specify '
                         'either name or id', vol)
            elif 'vol_id' in vol:
                vol_ids.append(vol['vol_id'].upper())
            elif 'vol_name' in vol:
                params = {"storageGroupId": sg_name,
                          "volume_identifier": vol['vol_name']}
                volume_list = self.provisioning.get_volume_list(params)
                if not volume_list or len(volume_list) == 0:
                    LOG.info(
                        'No volume found with volume identifier %s in storage'
                        ' group %s', vol['vol_name'], sg_name)
                elif len(volume_list) > 1:
                    self.show_error_exit(msg='Duplicate volumes found: '
                                         'There are {0} volume(s) with '
                                         'the same name {1} in '
                                         'the storage group {2}'.
                                         format(len(volume_list),
                                                vol['vol_name'],
                                                sg_name)
                                         )
                else:
                    vol_ids.append(volume_list[0])

        volumes_to_remove = [
            vol for vol in vol_ids if vol in set(existing_volumes_in_sg)]

        if not volumes_to_remove:
            LOG.info('The given volumes %s are not present on the storage '
                     'group %s', vol_ids, sg_name)
            existing_volumes_details_in_sg = self.\
                get_volumes_details_storagegroup(sg_name)
            return False, existing_volumes_details_in_sg
        try:
            storage_group = self.provisioning.get_storage_group(sg_name)
            remote_array = None
            remote_array_sg = None
            remote_array_1 = None
            remote_array_1_sg = None
            remote_array_2 = None
            remote_array_2_sg = None

            # check SRDF Protected SG.
            if not storage_group['unprotected']:
                rdfg_list = self.replication.\
                    get_storage_group_srdf_group_list(storage_group_id=sg_name)

                # Multisite configuration
                if len(rdfg_list) == 2:
                    msg = ("Concurrent configuration detected "
                           "for %s", sg_name)
                    LOG.info(msg)
                    rdfg_details = self.replication. \
                        get_rdf_group(rdf_number=rdfg_list[0])
                    remote_array_1 = rdfg_details['remoteSymmetrix']
                    remote_array_1_sg = sg_name
                    rdfg_details = self.replication. \
                        get_rdf_group(rdf_number=rdfg_list[1])
                    remote_array_2 = rdfg_details['remoteSymmetrix']
                    remote_array_2_sg = sg_name
                    for vol in volumes_to_remove:
                        self.provisioning.remove_volume_from_storage_group(
                            storage_group_id=sg_name, vol_id=vol,
                            remote_array_1_id=remote_array_1,
                            remote_array_1_sgs=remote_array_1_sg,
                            remote_array_2_id=remote_array_2,
                            remote_array_2_sgs=remote_array_2_sg)
                    vol_details = self.get_volumes_details_storagegroup(
                        sg_name)
                    return True, vol_details

                if len(rdfg_list) > 2:
                    err_msg = ("More than 2 rdf groups exists for the given "
                               "storage group %s. Create volume is not "
                               "supported.", sg_name)
                    self.show_error_exit(msg=err_msg)

                rdfg_details = self.replication.\
                    get_rdf_group(rdf_number=rdfg_list[0])
                remote_array = rdfg_details['remoteSymmetrix']
                remote_array_sg = sg_name

            for vol in volumes_to_remove:
                self.provisioning.remove_volume_from_storage_group(
                    storage_group_id=sg_name, vol_id=vol,
                    remote_array_1_id=remote_array,
                    remote_array_1_sgs=remote_array_sg)
            vol_details = self.get_volumes_details_storagegroup(sg_name)
            return True, vol_details

        except Exception as e:
            errorMsg = ("Remove existing volume from storage group %s "
                        "failed with error %s", sg_name, str(e))
            self.show_error_exit(msg=errorMsg)

    def modify_sg_srp(self, storage_group, new_srp):
        """Modify SRP of the Storage Group"""

        payload = {
            "editStorageGroupActionParam": {
                "editStorageGroupSRPParam": {
                    "srpId": new_srp
                },
            }
        }
        LOG.info('Modifying the SG SRP to %s ', new_srp)
        try:
            self.provisioning.modify_storage_group(storage_group, payload)
        except Exception as e:
            errorMsg = ("Modify attribute SRP of storage group %s failed "
                        "with error %s", storage_group, str(e))
            self.show_error_exit(msg=errorMsg)

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
        LOG.info('Modifying the SG SLO to %s ', new_slo)
        if ('slo' in storage_group and storage_group['slo'].lower() !=
            self.module.params['service_level'].lower()) or \
                ('slo' not in storage_group and
                 self.module.params['service_level'].lower() != "none"):
            try:
                LOG.info('The existing SG SLO is %s and the desired SG SLO '
                         'is %s ', storage_group['slo'],
                         self.module.params['service_level'])
                self.provisioning.modify_storage_group(sg_name, payload)
            except Exception as e:
                errorMsg = ("Modify attribute SLO of storage group %s "
                            "failed with error %s", sg_name, str(e))
                self.show_error_exit(msg=errorMsg)

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

        if 'compression' in storage_group and storage_group[
                'compression'] != self.module.params['compression']:
            try:
                LOG.info('The existing SG compression is %s and the desired'
                         ' SG compression is %s ',
                         storage_group['compression'],
                         self.module.params['compression'])
                self.provisioning.modify_storage_group(sg_name, payload)
            except Exception as e:
                errorMsg = ("Modify attribute compression of storage group "
                            "%s failed with error %s", sg_name, str(e))
                self.show_error_exit(msg=errorMsg)

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
            self.modify_sg_compression(
                storage_group, modified_param['modified_compression'])
            changed = True

        return changed

    def add_child_sg_to_parent_sg(self, child_sg_list, parent_sg):
        """Add a child Storage Group(s) to parent Storage Group"""
        changed = False
        for child_sg in child_sg_list:
            if not self.provisioning.is_child_sg_in_parent_sg(
                    child_sg, parent_sg):
                try:
                    storage_group = self.provisioning.get_storage_group(
                        parent_sg)
                    # SRDF protected SG are not allowed to be modified.
                    if not storage_group['unprotected']:
                        self.show_error_exit(msg=self.protected_sg_msg)
                    self.provisioning.add_child_sg_to_parent_sg(
                        child_sg, parent_sg)
                    changed = True
                except Exception as e:
                    error_message = ('Adding child SG %s to parent storage '
                                     'group %s failed with error %s',
                                     child_sg, parent_sg, str(e))
                    self.show_error_exit(msg=error_message)
        return changed

    def remove_child_sg_from_parent_sg(self, child_sg_list, parent_sg):
        """Remove a child Storage Group from parent Storage Group"""
        changed = False
        storage_group = self.provisioning.get_storage_group(parent_sg)
        for child_sg in child_sg_list:
            if self.provisioning.\
                    is_child_sg_in_parent_sg(child_sg, parent_sg):
                try:
                    # SRDF protected SG are not allowed to be modified.
                    if not storage_group['unprotected']:
                        self.show_error_exit(msg=self.protected_sg_msg)
                    self.provisioning.remove_child_sg_from_parent_sg(
                        child_sg, parent_sg)
                    changed = True
                except Exception as e:
                    error_message = ('Removing child SG %s from parent '
                                     'storage group %s failed with error %s ',
                                     child_sg, parent_sg, str(e))
                    self.show_error_exit(msg=error_message)
        return changed

    def is_storage_group_modified(self, storage_group):
        """Determine if the desired storage group state is different from
        existing SG"""
        modified = False
        modified_param = dict()

        if ('srp' in storage_group and self.module.params['srp'] is not None
            and storage_group['srp'].lower() != self.module.params['srp'].
            lower()) or ('srp' not in storage_group and self.module.
                         params['srp'] is not None and self.module.params['srp'].
                         lower() != "none"):
            modified_param['modified_srp'] = self.module.params['srp']
            modified = True

        if ('slo' in storage_group and self.module.params['service_level'] is
            not None and storage_group['slo'].lower() != self.
            module.params['service_level'].lower()) or \
                ('slo' not in storage_group and self.module.
                 params['service_level'] is not None and
                 self.module.params['service_level'].lower() != "none"):
            modified_param['modified_slo'] = \
                self.module.params['service_level']
            modified = True

        if 'compression' in storage_group and self.\
            module.params['compression'] is not None and \
                storage_group['compression'] != \
                self.module.params['compression']:
            modified_param['modified_compression'] = \
                self.module.params['compression']
            modified = True

        LOG.info('The storage group %s needs to be modified and the modified '
                 'param are %s ', modified, modified_param)

        return modified, modified_param

    def rename_storage_group(self, storage_group, new_sg_name):
        """Rename the Storage Group"""
        if storage_group is None:
            error_message = ('Rename storage group %s to new name %s '
                             'failed because SG %s does not exist ',
                             self.module.params['sg_name'], new_sg_name)
            self.show_error_exit(msg=error_message)
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
            error_message = ('Rename storage group %s to new name %s '
                             'failed with error %s ',
                             self.module.params['sg_name'], new_sg_name,
                             str(e))
            self.show_error_exit(msg=error_message)
        return changed

    def check_for_linked_snapshots(self, sg_name):
        snap_list = None
        try:
            try:
                snap_list = self.replication.get_storagegroup_snapshot_list(
                    sg_name)
            except utils.PyU4V.utils.exception.ResourceNotFoundException as e:
                LOG.info(
                    "Got exception error while deleting  storage group: %s",
                    str(e))
                return snap_list
            for snap in snap_list:
                gen_list = \
                    self.replication.get_storagegroup_snapshot_generation_list(
                        storagegroup_id=sg_name,
                        snap_name=snap)
                for gen in gen_list:
                    gen_details = \
                        self.replication.get_snapshot_generation_details(
                            sg_id=sg_name,
                            snap_name=snap,
                            gen_num=gen)
                    if gen_details['isLinked']:
                        self.show_error_exit(msg="Cannot delete SG {0} "
                                             "because it "
                                             "has snapshot(s) in linked "
                                             "state. "
                                             "Please unlink the snapshot(s) "
                                             "and retry.".format(sg_name))
        except Exception as e:
            error_msg = "Delete storage group %s failed with error %s ",\
                sg_name, str(e)
            self.show_error_exit(msg=error_msg)

    def check_task_validity(self, volumes, vol_state):
        if volumes and vol_state is None:
            self.show_error_exit(msg="Please provide a valid vol_state.")

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
        state = self.module.params['state']
        sg_name = self.module.params['sg_name']
        volumes = self.module.params['volumes']
        vol_state = self.module.params['vol_state']
        child_sgs = self.module.params['child_storage_groups']
        child_sg_state = self.module.params['child_sg_state']
        new_sg_name = self.module.params['new_sg_name']

        self.check_task_validity(volumes, vol_state)
        storage_group = self.get_storage_group(sg_name)

        vols_before_op = self.provisioning.get_volumes_from_storage_group(
            storage_group_id=sg_name)

        modified = False
        if storage_group:
            modified, modified_param = self.is_storage_group_modified(
                storage_group)

        result = dict(
            changed=False,
            create_sg='',
            modify_sg='',
            add_vols_to_sg='',
            add_new_vols_to_sg='',
            added_vols_details='',
            remove_vols_from_sg='',
            removed_vols_details='',
            add_child_sg='',
            remove_child_sg='',
            rename_sg='',
            delete_sg='',
            storage_group_volumes_details='',
            storage_group_details='',
        )
        if state == 'present' and storage_group and not new_sg_name \
                and not volumes:
            LOG.info('Get volumes details of storage group %s', sg_name)
            result['storage_group_volumes_details'] = self.\
                get_volumes_details_storagegroup(sg_name)
        elif state == 'present' and not (storage_group or new_sg_name):
            LOG.info('Creating storage group %s', sg_name)
            result['create_sg'], result['storage_group_details'] = self.\
                create_storage_group(sg_name)
            LOG.info('Get volumes details of storage group %s', sg_name)
            result['storage_group_volumes_details'] = self.\
                get_volumes_details_storagegroup(sg_name)
        elif state == 'absent' and storage_group:
            LOG.info('Delete storage group %s ', sg_name)
            result['delete_sg'] = self.delete_storage_group(sg_name)

        if state == 'present' and vol_state == 'present-in-group'\
                and storage_group and volumes:
            LOG.info('Create new volume(s) for storage group %s', sg_name)
            result['add_new_vols_to_sg'],\
                result['storage_group_volumes_details'] = self.\
                add_volume_storage_group(sg_name)
            LOG.info('Add existing volume(s) to storage group %s', sg_name)
            result['add_vols_to_sg'], result['storage_group_volumes_details']\
                = self.add_existing_volumes_to_sg(
                volumes, sg_name)
        elif state == 'present' and vol_state == 'absent-in-group'\
                and storage_group and volumes:
            LOG.info(
                'Remove existing volume(s) from storage group %s', sg_name)
            result['remove_vols_from_sg'], \
                result['storage_group_volumes_details'] = self.\
                remove_volumes_from_sg(volumes, sg_name)

        if state == 'present' and storage_group and modified:
            LOG.info('Modifying Storage group %s', sg_name)
            result['modify_sg'] = self.modify_storage_group_attributes(
                sg_name, modified_param)
            result['storage_group_volumes_details'] = self.\
                get_volumes_details_storagegroup(sg_name)

        if state == 'present' and child_sg_state == 'present-in-group'\
                and storage_group and child_sgs:
            LOG.info('Adding child SG to parent storage group %s', sg_name)
            result['add_child_sg'] = self.add_child_sg_to_parent_sg(
                child_sgs, sg_name)
            LOG.info('Get volumes details of storage group %s', sg_name)
            result['storage_group_volumes_details'] = self.\
                get_volumes_details_storagegroup(sg_name)
        elif state == 'present' and child_sg_state == 'absent-in-group'\
                and storage_group and child_sgs:
            LOG.info(
                'Removing child SG from parent storage group %s', sg_name)
            result['remove_child_sg'] = self.remove_child_sg_from_parent_sg(
                child_sgs, sg_name)
            LOG.info('Get volumes details of storage group %s', sg_name)
            result['storage_group_volumes_details'] = self.\
                get_volumes_details_storagegroup(sg_name)

        if state == 'present' and new_sg_name:
            LOG.info('Rename SG %s to new name %s', sg_name, new_sg_name)
            result['rename_sg'] = self.rename_storage_group(
                storage_group, new_sg_name)
            if result['rename_sg']:
                sg_name = new_sg_name
                LOG.info('Get volumes details of storage group %s', sg_name)
                result['storage_group_volumes_details'] = self.\
                    get_volumes_details_storagegroup(sg_name)

        if state == 'present' and storage_group:
            LOG.info('Found storage group %s', storage_group)
            updated_sg = self.get_storage_group(sg_name)
            result['storage_group_details'] = updated_sg

        if result['create_sg'] or result['modify_sg'] or \
                result['add_vols_to_sg'] or result['remove_vols_from_sg']\
                or result['add_child_sg'] or result['remove_child_sg'] or \
                result['delete_sg'] or result['add_new_vols_to_sg'] or \
                result['rename_sg']:
            result['changed'] = True

        vols_after_op = self.provisioning.get_volumes_from_storage_group(
            storage_group_id=sg_name)
        result['added_vols_details'] = \
            list(set(vols_after_op) - set(vols_before_op))
        result['removed_vols_details'] = \
            list(set(vols_before_op) - set(vols_after_op))

        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")

        # Finally update the module result.
        self.module.exit_json(**result)


def get_powermax_storage_group_parameters():
    return dict(
        sg_name=dict(
            required=True,
            type='str'),
        service_level=dict(
            required=False,
            type='str'),
        srp=dict(
            required=False,
            type='str'),
        compression=dict(
            required=False,
            type='bool'),
        volumes=dict(
            required=False,
            type='list', elements='dict'),
        vol_state=dict(
            required=False,
            choices=[
                'absent-in-group',
                'present-in-group'],
            type='str'),
        child_storage_groups=dict(
            required=False,
            type='list', elements='str'),
        child_sg_state=dict(
            required=False,
            choices=[
                'absent-in-group',
                'present-in-group'],
            type='str'),
        new_sg_name=dict(
            required=False,
            type='str'),
        state=dict(
            required=True,
            choices=[
                'present',
                'absent'],
            type='str'),
    )


def main():
    """Create PowerMax storage group object and perform action on it
        based on user input from playbook"""
    obj = PowerMaxStorageGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
