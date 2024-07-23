#!/usr/bin/python
# Copyright: (c) 2019-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: snapshot
version_added: '1.0.0'
short_description: Manage Snapshots on PowerMax/VMAX Storage System
description:
- Managing snapshots on a PowerMax storage system includes the following operations.
- Creating a new storage group (SG) snapshot.
- Getting details of the SG snapshot.
- Renaming the SG snapshot.
- Changing the snapshot link status.
- Deleting an existing SG snapshot.
extends_documentation_fragment:
  - dellemc.powermax.powermax
  - dellemc.powermax.powermax.powermax_serial_no
author:
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
options:
  sg_name:
    description:
    - The name of the storage group.
    required: true
    type: str
  snapshot_name:
    description:
    - The name of the snapshot.
    required: true
    type: str
  ttl:
    description:
    - The Time To Live (TTL) value for the snapshot.
    - If the TTL is not specified, the storage group snap details are
      returned.
    - However, to create a SG snap - TTL must be given.
    - If the SG snap should not have any TTL - specify TTL as C(None).
    type: str
  ttl_unit:
    description:
    - The unit for the I(ttl).
    - If no I(ttl_unit) is specified, C(days) is taken as default I(ttl_unit).
    choices: [hours, days]
    default: days
    type: str
  generation:
    description:
    - The generation number of the snapshot.
    - Generation is required for link, unlink, rename and delete operations.
    - Optional for Get snapshot details.
    - Create snapshot will always create a new snapshot with a generation
      number 0.
    - Rename is supported only for generation number 0.
    type: int
  snapshot_id:
    description:
    - Unique ID of the snapshot.
    - I(snapshot_id) is required for link, unlink, rename and delete operations.
    - Optional for Get snapshot details.
    type: int
  new_snapshot_name:
    description:
    - The new name of the snapshot.
    type: str
  target_sg_name:
    description:
    - The target storage group.
    type: str
  link_status:
    description:
    - Describes the link status of the snapshot.
    choices: [linked, unlinked]
    type: str
  restore:
    description:
    - Whether to restore a storage group to its snapshot.
    type: bool
    version_added: '3.1.0'
  state:
    description:
    - Define whether the snapshot should exist or not.
    required: true
    choices: [absent, present]
    type: str
notes:
  - Paramters I(generation) and I(snapshot_id) are mutually exclusive.
  - If I(generation) or I(snapshot_id) is not provided then a list of generation
    against snapshot_id is returned.
  - Use of I(snapshot_id) over I(generation) is preferably recommended for
    PowerMax microcode version 5978.669.669 and onwards.
  - The I(check_mode) is supported.
'''

EXAMPLES = r'''
- name: Create a Snapshot for a Storage Group
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    ttl: "2"
    ttl_unit: "days"
    state: "present"

- name: Get Storage Group Snapshot details
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    state: "present"

- name: Get Storage Group Snapshot details using generation
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    generation: 1
    state: "present"

- name: Get Storage Group Snapshot details using snapshot_id
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    snapshot_id: 135023964929
    state: "present"

- name: Rename Storage Group Snapshot using generation
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    new_snapshot_name: "ansible_snap_new"
    generation: 0
    state: "present"

- name: Rename Storage Group Snapshot using snapshot_id
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    new_snapshot_name: "ansible_snap_new"
    snapshot_id: 135023964929
    state: "present"

- name: Change Snapshot Link Status to Linked using generation
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    generation: 1
    target_sg_name: "ansible_sg_target"
    link_status: "linked"
    state: "present"

- name: Change Snapshot Link Status to UnLinked using generation
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    generation: 1
    target_sg_name: "ansible_sg_target"
    link_status: "unlinked"
    state: "present"

- name: Change Snapshot Link Status to Linked using snapshot_id
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    snapshot_id: 135023964515
    target_sg_name: "ansible_sg_target"
    link_status: "linked"
    state: "present"

- name: Change Snapshot Link Status to UnLinked using snapshot_id
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    snapshot_id: 135023964515
    target_sg_name: "ansible_sg_target"
    link_status: "unlinked"
    state: "present"

- name: Restore storage group snapshot using generation
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    generation: 1
    restore: true
    state: "present"

- name: Restore Storage Group Snapshot using snapshot_id
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    snapshot_id: 135023964929
    restore: true
    state: "present"

- name: Delete Storage Group Snapshot using generation
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    generation: 1
    state: "absent"

- name: Delete Storage Group Snapshot using snapshot_id
  dellemc.powermax.snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    snapshot_id: 135023964929
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
    sample: "false"
create_sg_snap:
    description: Flag sets to true when the snapshot is created.
    returned: When snapshot is created.
    type: bool
    sample: "false"
delete_sg_snap:
    description: Flag sets to true when the snapshot is deleted.
    returned: When snapshot is deleted.
    type: bool
    sample: "false"
rename_sg_snap:
    description: Flag sets to true when the snapshot is renamed.
    returned: When snapshot is renamed.
    type: bool
    sample: "false"
restore_sg_snap:
    description: Flag sets to true when the snapshot is restored.
    returned: When snapshot is restored.
    type: bool
    sample: "false"
sg_snap_details:
    description: Details of the snapshot.
    returned: When snapshot exists.
    type: complex
    contains:
        generation/snapid:
            description: The generation/snapshot ID of the snapshot.
            type: int
        expired:
            description: Indicates whether the snapshot is expired or not.
            type: bool
        linked:
            description: Indicates whether the snapshot is linked or not.
            type: bool
        restored:
            description: Indicates whether the snapshot is restored or not.
            type: bool
        name:
            description: Name of the snapshot.
            type: str
        non_shared_tracks:
            description: Number of non-shared tracks.
            type: int
        num_source_volumes:
            description: Number of source volumes.
            type: int
        num_storage_group_volumes:
            description: Number of storage group volumes.
            type: int
        source_volume:
            description: Source volume details.
            type: list
            contains:
                capacity:
                    description: Volume capacity.
                    type: int
                capacity_gb:
                    description: Volume capacity in GB.
                    type: int
                name:
                    description: Volume ID.
                    type: str
        state:
            description: State of the snapshot.
            type: str
        time_to_live_expiry_date:
            description: Time to live expiry date.
            type: str
        timestamp:
            description: Snapshot time stamp.
            type: str
        timestamp_utc:
            description: Snapshot time stamp specified in UTC.
            type: int
        tracks:
            description: Number of tracks.
            type: int
    sample: {
        "change_snap_link_status": "",
        "changed": false,
        "create_sg_snap": "",
        "delete_sg_snap": "",
        "rename_sg_snap": "",
        "restore_sg_snap": "",
        "sg_snap_details": {
            "generation": 0,
            "isExpired": false,
            "isLinked": false,
            "isRestored": false,
            "name": "ansible_sample_snapshot",
            "nonSharedTracks": 0,
            "numSharedTracks": 0,
            "numSourceVolumes": 1,
            "numStorageGroupVolumes": 1,
            "numUniqueTracks": 0,
            "sourceVolume": [
                {
                    "capacity": 547,
                    "capacity_gb": 1.0015869,
                    "name": "00205"
                }
            ],
            "state": [
                "Established"
            ],
            "timeToLiveExpiryDate": "09:55:28 Thu, 11 Jul 2024 +0000",
            "timestamp": "09:55:28 Wed, 10 Jul 2024 +0000",
            "timestamp_utc": 1720605328000,
            "tracks": 0
        }
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils

LOG = utils.get_logger('snapshot')

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v3.1.0'


class Snapshot(object):
    """Class with Snapshot operations"""

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_snapshot_parameters())

        # initialize the Ansible module
        mutually_exclusive = [['generation', 'snapshot_id']]
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            mutually_exclusive=mutually_exclusive,
            supports_check_mode=True
        )
        self.result = {
            "changed": False,
            "create_sg_snap": '',
            "delete_sg_snap": '',
            "rename_sg_snap": '',
            "change_snap_link_status": '',
            "restore_sg_snap": '',
            "sg_snap_details": None
        }
        if HAS_PYU4V is False:
            self.show_error_exit(
                msg="Ansible modules for PowerMax require "
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
        self.replication = self.u4v_conn.replication
        self.common = self.u4v_conn.common
        LOG.info("Check Mode flag is %s", self.module.check_mode)
        LOG.info('Got PyU4V instance for provisioning on PowerMax ')

    def is_snap_id_supported(self):
        """check if the operation need to be performed by snapshot_id,
        snapshot_id will be supported for microcode 5978.669.669 & above."""

        try:
            supported_array_version = "5978.669.669"
            supported_sdk_version = "9.2.0.8"

            curr_version = utils.PyU4V.__version__
            array_details = self.common.get_array(self.module.params
                                                  ['serial_no'])
            if (utils.pkg_resources.parse_version(curr_version)
                >= utils.pkg_resources.parse_version(supported_sdk_version)) and \
                    ('ucode' not in array_details or (utils.parse_version(array_details['ucode'])
                                                      >= utils.parse_version(supported_array_version))):
                return True
            return False
        except Exception as e:
            err_msg = f"Failed to determine the platform details with error {str(e)}"
            self.show_error_exit(msg=err_msg)

    def get_snapshot(self, sg_id, snapshot_name, generation=None,
                     snap_id=None):
        """Get snapshot details"""
        try:
            if not (isinstance(generation, int) or isinstance(snap_id, int)):
                return self._get_snapshots(sg_id, snapshot_name)
            if generation is not None:
                return self.replication.get_snapshot_generation_details(
                    sg_id, snapshot_name, generation)
            if snap_id is not None:
                return self.replication.get_snapshot_snap_id_details(
                    sg_id=sg_id, snap_name=snapshot_name, snap_id=snap_id)
        except Exception as e:
            error_message = (f'Got error: {str(e)} while getting details of '
                             f'storage group {sg_id} snapshot {snapshot_name}')
            self.show_error_exit(msg=error_message)

    def _get_snapshots(self, sg_id, snapshot_name):
        snapshots = []
        generations = self.replication.get_storage_group_snapshot_generation_list(
            sg_id, snapshot_name)
        if self.is_snap_id_supported():
            snap_ids = self.replication.get_storage_group_snapshot_snap_id_list(
                storage_group_id=sg_id, snap_name=snapshot_name)
            if snap_ids and generations and (len(generations) == len(snap_ids)):
                for gen_id, snap_id in zip(generations, snap_ids):
                    snapshots.append({'generation': gen_id,
                                      'snapid': snap_id})
        else:
            for gen in generations:
                snapshots.append({'generation': gen})
        return snapshots

    def create_sg_snapshot(self, sg_id, snap_name, ttl, ttl_unit):
        """Create Storage Group Snapshot"""
        try:
            resp = {}
            if ttl_unit == 'days':
                ttl_unit = False
            else:
                ttl_unit = True
            if ttl == 'None':
                ttl = None
            if not self.module.check_mode:
                resp = \
                    self.replication.create_storage_group_snapshot(storage_group_id=sg_id,
                                                                   snap_name=snap_name,
                                                                   ttl=ttl,
                                                                   hours=ttl_unit)
            return True, resp
        except Exception as e:
            error_message = (f'Create snapshot {snap_name} for storage group {sg_id} failed '
                             f'with error {str(e)} ')
            self.show_error_exit(msg=error_message)

    def delete_sg_snapshot(self, sg_id, snap_name, generation=None,
                           snap_id=None):
        """Delete Storage Group Snapshot"""
        snapshot = None
        try:
            if generation is not None:
                snapshot = self.replication.get_snapshot_generation_details(
                    sg_id,
                    snap_name,
                    generation)
            if snap_id is not None:
                snapshot = self.replication.get_snapshot_snap_id_details(
                    sg_id=sg_id,
                    snap_name=snap_name,
                    snap_id=snap_id)
        except Exception as e:
            LOG.info("snapshot_id or generation not found,"
                     " got error: %s", str(e))
            return False
        try:
            if snapshot:
                if generation is not None and not self.module.check_mode:
                    self.replication.delete_storage_group_snapshot(sg_id,
                                                                   snap_name,
                                                                   generation)
                if snap_id is not None and not self.module.check_mode:
                    self.replication.delete_storage_group_snapshot_by_snap_id(
                        sg_id,
                        snap_name,
                        snap_id)
            return True
        except Exception as e:
            error_message = (f'Delete storage group {sg_id} snapshot {snap_name} failed with '
                             f'error {str(e)} ')
            self.show_error_exit(msg=error_message)

    def rename_sg_snapshot(self, sg_id, snap_name,
                           new_snap_name, generation=None, snap_id=None):
        """Rename Storage Group Snapshot"""
        try:
            snapshot = self.get_snapshot(sg_id, snap_name, generation,
                                         snap_id)
            if snap_name == new_snap_name:
                return False, snapshot

            resp = snapshot
            if snapshot:
                if generation is not None and not self.module.check_mode:
                    resp = self.replication. \
                        modify_storage_group_snapshot(
                            src_storage_grp_id=sg_id,
                            tgt_storage_grp_id=None,
                            snap_name=snap_name,
                            gen_num=generation,
                            new_name=new_snap_name
                        )
                if snap_id is not None and not self.module.check_mode:
                    resp = self.replication. \
                        modify_storage_group_snapshot_by_snap_id(
                            src_storage_grp_id=sg_id,
                            tgt_storage_grp_id=None,
                            snap_name=snap_name,
                            snap_id=snap_id,
                            new_name=new_snap_name)
            return True, resp
        except Exception as e:
            error_message = (f'Renaming snapshot {snap_name} for storage group {sg_id} '
                             f'failed with error {str(e)} ')
            self.show_error_exit(msg=error_message)

    def change_snapshot_link_status(self, sg_id, target_sg,
                                    snap_name, link_status, generation=None,
                                    snap_id=None):
        """Change Snapshot Link status"""
        snapshot = self.get_snapshot(sg_id, snap_name, generation,
                                     snap_id)
        if 'isLinked' in snapshot:
            modify = self.is_link_modify_needed(
                snapshot=snapshot,
                link_param='isLinked',
                linked_sg_param='linkedStorageGroup',
                target_sg=target_sg,
                link_status=link_status)

        # 'linked' key is returned in snapshot details w.r.t. snapshot_id
        if 'linked' in snapshot:
            modify = self.is_link_modify_needed(
                snapshot=snapshot,
                link_param='linked',
                linked_sg_param='linked_storage_group',
                target_sg=target_sg,
                link_status=link_status)

        if modify is False:
            return False, snapshot

        link = link_status == 'linked'
        unlink = link_status == 'unlinked'

        if not self.module.check_mode:
            return True, self.modify_snapshot(sg_id=sg_id,
                                              target_sg=target_sg,
                                              snap_name=snap_name,
                                              link=link,
                                              unlink=unlink,
                                              snap_id=snap_id,
                                              generation=generation)
        return True, snapshot

    def is_link_modify_needed(self, snapshot, link_param, linked_sg_param, target_sg, link_status):
        if snapshot[link_param] is True and link_status == 'linked':
            for linked_sg in snapshot[linked_sg_param]:
                linked = False
                if linked_sg['name'] == target_sg:
                    linked = True
                    break
            if linked is True:
                return False
        elif snapshot[link_param] is False \
                and link_status == 'unlinked':
            return False
        else:
            return True

    def modify_snapshot(self, sg_id, target_sg, snap_name, link, unlink, snap_id, generation):
        try:
            if generation is not None:
                return self.replication. \
                    modify_storage_group_snapshot(
                        src_storage_grp_id=sg_id,
                        tgt_storage_grp_id=target_sg,
                        snap_name=snap_name,
                        link=link,
                        unlink=unlink,
                        gen_num=generation)
            if snap_id is not None:
                return self.replication. \
                    modify_storage_group_snapshot_by_snap_id(
                        src_storage_grp_id=sg_id,
                        tgt_storage_grp_id=target_sg,
                        snap_name=snap_name,
                        link=link,
                        unlink=unlink,
                        snap_id=snap_id)

        except Exception as e:
            error_message = (f'Change storage group {sg_id} snapshot {snap_name} link status failed '
                             f'with error {str(e)} ')
            self.show_error_exit(msg=error_message)

    def restore_snapshot(self, sg_id, snap_name, snap_id=None, generation=None):
        """Restore Snapshot"""
        try:
            if generation is not None and not self.module.check_mode:
                self.replication. \
                    modify_storage_group_snapshot(
                        src_storage_grp_id=sg_id,
                        tgt_storage_grp_id=None,
                        snap_name=snap_name,
                        gen_num=generation,
                        restore=True
                    )
            if snap_id is not None and not self.module.check_mode:
                self.replication. \
                    modify_storage_group_snapshot_by_snap_id(
                        src_storage_grp_id=sg_id,
                        tgt_storage_grp_id=None,
                        snap_name=snap_name,
                        snap_id=snap_id,
                        restore=True
                    )
            return True
        except Exception as e:
            error_message = (f'Restore storage group {sg_id} snapshot {snap_name} failed with '
                             f'error {str(e)}')
            self.show_error_exit(msg=error_message)

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection {self.u4v_conn}")
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = f"Failed to close unisphere connection with error: {str(e)}"
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def is_valid_generation_or_id(self, generation, snap_id):
        if not (isinstance(generation, int) or isinstance(snap_id, int)):
            self.show_error_exit("Specify a valid generation or a snapshot_id.")

    def validate_params(self, snapshot_params):
        """ Validate snapshot parameters """
        if snapshot_params.get('state') == 'present' and snapshot_params.get("sg_name") and \
                snapshot_params.get('snapshot_name') and snapshot_params.get('new_snapshot_name'):
            self.is_valid_generation_or_id(
                generation=snapshot_params.get('generation'),
                snap_id=snapshot_params.get('snapshot_id'))

        if snapshot_params["state"] == 'present' and snapshot_params["snapshot_name"] \
                and snapshot_params["link_status"] and snapshot_params["target_sg_name"]:
            self.is_valid_generation_or_id(
                generation=snapshot_params.get('generation'),
                snap_id=snapshot_params.get('snapshot_id'))

        if snapshot_params["state"] == 'present' and snapshot_params["snapshot_name"] \
                and snapshot_params["restore"]:
            self.is_valid_generation_or_id(
                generation=snapshot_params.get('generation'),
                snap_id=snapshot_params.get('snapshot_id'))

        if snapshot_params["state"] == 'absent':
            self.is_valid_generation_or_id(
                generation=snapshot_params.get('generation'),
                snap_id=snapshot_params.get('snapshot_id'))


def get_snapshot_parameters():
    return dict(
        sg_name=dict(required=True, type='str'),
        snapshot_name=dict(required=True, type='str'),
        ttl=dict(required=False, type='str'),
        ttl_unit=dict(required=False, default='days',
                      choices=['hours', 'days'], type='str'),
        generation=dict(required=False, type='int'),
        snapshot_id=dict(required=False, type='int'),
        new_snapshot_name=dict(required=False, type='str'),
        target_sg_name=dict(required=False, type='str'),
        link_status=dict(required=False, choices=['linked', 'unlinked'],
                         type='str'),
        restore=dict(type='bool'),
        state=dict(required=True, choices=['present', 'absent'],
                   type='str'),
    )


class SnapshotExitHandler:
    def handle(self, snapshot_obj, snapshot_params):
        if snapshot_params["state"] == 'present' and not snapshot_params["ttl"] and not \
                snapshot_params["link_status"] and not snapshot_params["new_snapshot_name"]:
            LOG.info("Returning storage group %s snapshot %s",
                     snapshot_params["sg_name"], snapshot_params["snapshot_name"])
            snapshot_obj.result["sg_snap_details"] = snapshot_obj.get_snapshot(
                sg_id=snapshot_params['sg_name'],
                snapshot_name=snapshot_params['snapshot_name'],
                generation=snapshot_params['generation'],
                snap_id=snapshot_params['snapshot_id'])

        if snapshot_obj.result['create_sg_snap'] or snapshot_obj.result['delete_sg_snap'] or \
                snapshot_obj.result['rename_sg_snap'] or snapshot_obj.result['change_snap_link_status'] or \
                snapshot_obj.result['restore_sg_snap']:
            snapshot_obj.result['changed'] = True
        LOG.info("Closing unisphere connection {snapshot_obj.u4v_conn}")
        utils.close_connection(snapshot_obj.u4v_conn)
        LOG.info("Connection closed successfully")
        snapshot_obj.module.exit_json(**snapshot_obj.result)


class SnapshotDeleteHandler():
    def handle(self, snapshot_obj, snapshot_params):
        if snapshot_params["state"] == "absent":
            LOG.info("Delete storage group %s snapshot %s generation %s ",
                     snapshot_params["sg_name"], snapshot_params["snapshot_name"], snapshot_params["generation"])
            snapshot_obj.result['delete_sg_snap'] = snapshot_obj.delete_sg_snapshot(
                sg_id=snapshot_params["sg_name"],
                snap_name=snapshot_params["snapshot_name"],
                generation=snapshot_params["generation"],
                snap_id=snapshot_params["snapshot_id"])

        SnapshotLinkHandler().handle(snapshot_obj, snapshot_params)


class SnapshotLinkHandler:
    def handle(self, snapshot_obj, snapshot_params):
        if snapshot_params["state"] == 'present' and snapshot_params["snapshot_name"] is not None and \
                snapshot_params["link_status"] is not None and snapshot_params["target_sg_name"] is not None:
            LOG.info("Change storage group %s snapshot %s link status ",
                     snapshot_params["sg_name"], snapshot_params["snapshot_name"])
            snapshot_obj.result['change_snap_link_status'], snapshot_obj.result['sg_snap_link_details'] = \
                snapshot_obj.change_snapshot_link_status(
                    sg_id=snapshot_params["sg_name"],
                    target_sg=snapshot_params["target_sg_name"],
                    snap_name=snapshot_params["snapshot_name"],
                    link_status=snapshot_params["link_status"],
                    generation=snapshot_params["generation"],
                    snap_id=snapshot_params["snapshot_id"])

        SnapshotRenameHandler().handle(snapshot_obj, snapshot_params)


class SnapshotRestoreHandler:
    def handle(self, snapshot_obj, snapshot_params):
        if snapshot_params["state"] == 'present' and snapshot_params["restore"] is True:
            snapshot_details = snapshot_obj.get_snapshot(
                sg_id=snapshot_params['sg_name'],
                snapshot_name=snapshot_params['snapshot_name'],
                generation=snapshot_params['generation'],
                snap_id=snapshot_params['snapshot_id'])
            if snapshot_details is not None and 'Restored' not in snapshot_details['state']:
                LOG.info("Restoring storage group %s snapshot %s",
                         snapshot_params['sg_name'], snapshot_params['snapshot_name'])
                LOG.info(snapshot_details)
                snapshot_obj.result['restore_sg_snap'] = \
                    snapshot_obj.restore_snapshot(
                        sg_id=snapshot_params['sg_name'],
                        snap_name=snapshot_params['snapshot_name'],
                        snap_id=snapshot_params['snapshot_id'],
                        generation=snapshot_params['generation'])

        SnapshotExitHandler().handle(snapshot_obj, snapshot_params)


class SnapshotRenameHandler:
    def handle(self, snapshot_obj, snapshot_params):
        if snapshot_params["state"] == "present" and snapshot_params["sg_name"] is not None and \
                snapshot_params["snapshot_name"] is not None and snapshot_params["new_snapshot_name"] is not None:
            if snapshot_params["snapshot_id"] is not None or snapshot_params["generation"] == 0:
                LOG.info("Rename storage group %s snapshot %s",
                         snapshot_params["sg_name"], snapshot_params["snapshot_name"])
                snapshot_obj.result['rename_sg_snap'], snapshot_obj.result['sg_snap_rename_details'] = \
                    snapshot_obj.rename_sg_snapshot(
                        sg_id=snapshot_params['sg_name'],
                        snap_name=snapshot_params['snapshot_name'],
                        new_snap_name=snapshot_params['new_snapshot_name'],
                        generation=snapshot_params['generation'],
                        snap_id=snapshot_params['snapshot_id'])

        SnapshotRestoreHandler().handle(snapshot_obj, snapshot_params)


class SnapshotCreateHandler:
    def handle(self, snapshot_obj, snapshot_params):
        if snapshot_params["state"] == "present" and snapshot_params["ttl"] and not \
                (snapshot_params["new_snapshot_name"] or snapshot_params["link_status"]):
            LOG.info("Creating snapshot %s for storage group %s",
                     snapshot_params["snapshot_name"], snapshot_params["sg_name"])
            snapshot_obj.result["create_sg_snap"], snapshot_obj.result["sg_snap_details"] = \
                snapshot_obj.create_sg_snapshot(
                    sg_id=snapshot_params['sg_name'],
                    snap_name=snapshot_params['snapshot_name'],
                    ttl_unit=snapshot_params['ttl_unit'],
                    ttl=snapshot_params['ttl'])

        SnapshotDeleteHandler().handle(snapshot_obj, snapshot_params)


class SnapshotHandler:
    def handle(self, snapshot_obj, snapshot_params):
        snapshot_obj.validate_params(snapshot_params=snapshot_params)
        SnapshotCreateHandler().handle(
            snapshot_obj=snapshot_obj, snapshot_params=snapshot_params)


def main():
    """Create PowerMax Snapshot object and perform action on it
        based on user input from playbook"""
    obj = Snapshot()
    SnapshotHandler().handle(obj, obj.module.params)


if __name__ == '__main__':
    main()
