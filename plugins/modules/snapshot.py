#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: snapshot
version_added: '1.0.0'
short_description: Manage Snapshots on PowerMax/VMAX Storage System
description:
- Managing snapshots on a PowerMax storage system includes creating a new
  storage group (SG) snapshot, getting details of the SG snapshot, renaming
  the SG snapshot, changing the snapshot link status, and deleting an
  existing SG snapshot.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
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
    - If the SG snap should not have any TTL - specify TTL as "None".
    type: str
  ttl_unit:
    description:
    - The unit for the ttl.
    - If no ttl_unit is specified, 'days' is taken as default ttl_unit.
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
    - snapshot_id is required for link, unlink, rename and delete operations.
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
  state:
    description:
    - Define whether the snapshot should exist or not.
    required: true
    choices: [absent, present]
    type: str
notes:
  - Paramters 'generation' and 'snapshot_id' are mutually exclusive.
  - If 'generation' or 'snapshot_id' is not provided then a list of generation
    versus snapshot_id is returned.
  - Use of 'snapshot_id' over 'generation' is preferably recommended for
    PowerMax microcode version 5978.669.669 and onwards.
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
create_sg_snap:
    description: Flag sets to true when the snapshot is created.
    returned: When snapshot is created.
    type: bool
delete_sg_snap:
    description: Flag sets to true when the snapshot is deleted.
    returned: When snapshot is deleted.
    type: bool
rename_sg_snap:
    description: Flag sets to true when the snapshot is renamed.
    returned: When snapshot is renamed.
    type: bool
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
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils

LOG = utils.get_logger('snapshot')

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


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
        LOG.info('Check Mode flag is %s', self.module.check_mode)
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
            if ((utils.pkg_resources.parse_version(
                curr_version) >= utils.pkg_resources.parse_version(
                supported_sdk_version))
                    and
                    (utils.parse_version(
                        array_details['ucode']) >= utils.parse_version(
                        supported_array_version))):
                return True
            return False
        except Exception as e:
            err_msg = "Failed to determine the platform details with error" \
                      " %s" % str(e)
            self.show_error_exit(msg=err_msg)

    def get_snapshot(self, sg_id, snapshot_name, generation=None,
                     snap_id=None):
        """Get snapshot details"""
        try:
            LOG.info('Getting storage group %s snapshot %s details',
                     sg_id, snapshot_name)
            if not (isinstance(generation, int) or isinstance(snap_id, int)):
                snapshots = []
                generations = self.replication.\
                    get_storage_group_snapshot_generation_list(sg_id,
                                                               snapshot_name)
                for gen in generations:
                    snapshots.append({'generation': gen})

                if self.is_snap_id_supported():
                    snap_ids = self.replication.\
                        get_storage_group_snapshot_snap_id_list(
                            storage_group_id=sg_id,
                            snap_name=snapshot_name)
                    if snap_ids and generations \
                            and (len(generations) == len(snap_ids)):
                        snapshots = []
                        for gen_id, snap_id in zip(generations,
                                                   snap_ids):
                            snapshots.append({'generation': gen_id,
                                              'snapid': snap_id})
                return snapshots
            if generation is not None:
                return self.replication.get_snapshot_generation_details(
                    sg_id,
                    snapshot_name,
                    generation)
            if snap_id is not None:
                return self.replication.get_snapshot_snap_id_details(
                    sg_id=sg_id,
                    snap_name=snapshot_name,
                    snap_id=snap_id)
        except Exception as e:
            error_message = 'Got error: {0} while getting details of ' \
                            'storage group {1} snapshot {2}'
            self.show_error_exit(msg=error_message.format(str(e), sg_id,
                                                          snapshot_name))

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
                    self.replication.create_storage_group_snapshot(sg_id,
                                                                   snap_name,
                                                                   ttl,
                                                                   ttl_unit)
            return True, resp
        except Exception as e:
            error_message = 'Create Snapshot {0} for SG {1} failed ' \
                            'with error {2} '
            self.show_error_exit(msg=error_message.format(snap_name, sg_id,
                                                          str(e)))

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
            if snapshot and (generation is not None):
                if not self.module.check_mode:
                    self.replication.delete_storage_group_snapshot(sg_id,
                                                                   snap_name,
                                                                   generation)
            if snapshot and (snap_id is not None):
                if not self.module.check_mode:
                    self.replication.delete_storage_group_snapshot_by_snap_id(
                        sg_id,
                        snap_name,
                        snap_id)
            return True
        except Exception as e:
            error_message = 'Delete SG {0} Snapshot {1} failed with ' \
                            'error {2} '
            self.show_error_exit(msg=error_message.format(sg_id, snap_name,
                                                          str(e)))

    def rename_sg_snapshot(self, sg_id, snap_name,
                           new_snap_name, generation=None, snap_id=None):
        """Rename Storage Group Snapshot"""
        try:
            snapshot = self.get_snapshot(sg_id, snap_name, generation,
                                         snap_id)
            if snap_name == new_snap_name:
                return False, snapshot

            resp = snapshot
            if snapshot and (generation is not None):
                if not self.module.check_mode:
                    resp = self.replication.\
                        modify_storage_group_snapshot(sg_id,
                                                      None,
                                                      snap_name,
                                                      generation,
                                                      new_name=new_snap_name
                                                      )
            if snapshot and (snap_id is not None):
                if not self.module.check_mode:
                    resp = self.replication.\
                        modify_storage_group_snapshot_by_snap_id(
                            src_storage_grp_id=sg_id,
                            tgt_storage_grp_id=None,
                            snap_name=snap_name,
                            snap_id=snap_id,
                            new_name=new_snap_name)
            return True, resp
        except Exception as e:
            error_message = 'Renaming Snapshot {0} for Storage Group {1} ' \
                            'failed with error {2} '
            self.show_error_exit(msg=error_message.format(snap_name, sg_id,
                                                          str(e)))

    def change_snapshot_link_status(self, sg_id, target_sg,
                                    snap_name, link_status, generation=None,
                                    snap_id=None):
        """Change Snapshot Link status"""
        try:
            snapshot = self.get_snapshot(sg_id, snap_name, generation,
                                         snap_id)

            # 'isLinked' key is returned in snapshot details w.r.t. generation
            if 'isLinked' in snapshot:
                if snapshot['isLinked'] is True and link_status == 'linked':
                    for linked_sg in snapshot['linkedStorageGroup']:
                        linked = False
                        if linked_sg['name'] == target_sg:
                            linked = True
                            break
                    if linked:
                        return False, snapshot
                elif snapshot['isLinked'] is False \
                        and link_status == 'unlinked':
                    return False, snapshot

            # 'linked' key is returned in snapshot details w.r.t. snapshot_id
            if 'linked' in snapshot:
                if snapshot['linked'] is True and link_status == 'linked':
                    for linked_sg in snapshot['linked_storage_group']:
                        linked = False
                        if linked_sg['name'] == target_sg:
                            linked = True
                            break
                    if linked:
                        return False, snapshot
                elif snapshot['linked'] is False \
                        and link_status == 'unlinked':
                    return False, snapshot

            if link_status == 'linked':
                link = True
                unlink = False
            else:
                link = False
                unlink = True

            resp = snapshot
            if snapshot and (generation is not None):
                if not self.module.check_mode:
                    resp = self.replication. \
                        modify_storage_group_snapshot(sg_id,
                                                      target_sg,
                                                      snap_name,
                                                      link=link,
                                                      unlink=unlink,
                                                      gen_num=generation)
                return True, resp
            if snapshot and (snap_id is not None):
                if not self.module.check_mode:
                    resp = self.replication.\
                        modify_storage_group_snapshot_by_snap_id(
                            src_storage_grp_id=sg_id,
                            tgt_storage_grp_id=target_sg,
                            snap_name=snap_name,
                            link=link,
                            unlink=unlink,
                            snap_id=snap_id)
                return True, resp
        except Exception as e:
            error_message = 'Change SG {0} Snapshot {1} link status failed ' \
                            'with error {2} '
            self.show_error_exit(msg=error_message.format(sg_id,
                                                          snap_name, str(e)))

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
        Perform different actions on Snapshot based on user parameter
        chosen in playbook
        """

        sg_name = self.module.params['sg_name']
        snapshot_name = self.module.params['snapshot_name']
        ttl = self.module.params['ttl']
        ttl_unit = self.module.params['ttl_unit']
        generation = self.module.params['generation']
        snap_id = self.module.params['snapshot_id']
        new_snapshot_name = self.module.params['new_snapshot_name']
        target_sg_name = self.module.params['target_sg_name']
        link = self.module.params['link_status']
        state = self.module.params['state']

        result = dict(
            changed=False,
            create_sg_snap='',
            delete_sg_snap='',
            rename_sg_snap='',
            change_snap_link_status='',
        )

        if snap_id is not None and not self.is_snap_id_supported():
            self.show_error_exit("snapshot_id is not supported by this"
                                 " platform")

        if state == 'present' and ttl and not \
                (new_snapshot_name or link):
            LOG.info('Creating snapshot %s for storage group %s ',
                     snapshot_name, sg_name)
            result['create_sg_snap'], result['sg_snap_details'] = \
                self.create_sg_snapshot(sg_name,
                                        snapshot_name,
                                        ttl,
                                        ttl_unit)
        elif state == 'absent':
            if not (isinstance(generation, int) or isinstance(snap_id, int)):
                self.show_error_exit(msg="Please specify a valid generation "
                                         "or a snapshot_id to delete a "
                                         "snapshot.")
            else:
                LOG.info('Delete storage group %s snapshot %s generation %s ',
                         sg_name, snapshot_name, generation)
                result['delete_sg_snap'] = self.delete_sg_snapshot(
                    sg_name,
                    snapshot_name,
                    generation,
                    snap_id)

        if state == 'present' and snapshot_name \
                and link and target_sg_name:
            if not (isinstance(generation, int) or isinstance(snap_id, int)):
                self.show_error_exit(msg="Please specify a valid generation "
                                         "or a snapshot_id to change the "
                                         "link status of a snapshot.")
            else:
                LOG.info('Change storage group %s snapshot %s link status ',
                         sg_name, snapshot_name)
                result['change_snap_link_status'], \
                    result['sg_snap_link_details'] = \
                    self.change_snapshot_link_status(sg_name,
                                                     target_sg_name,
                                                     snapshot_name,
                                                     link,
                                                     generation,
                                                     snap_id)

        if state == 'present' and sg_name and snapshot_name and \
                new_snapshot_name:
            if not (isinstance(generation, int) or isinstance(snap_id, int)):
                self.show_error_exit("Please specify a valid generation or "
                                     "a snapshot_id to rename a snapshot.")
            elif snap_id is not None or generation == 0:
                LOG.info('Rename storage group %s snapshot %s ',
                         sg_name, snapshot_name)
                result['rename_sg_snap'], result['sg_snap_rename_details'] = \
                    self.rename_sg_snapshot(sg_name,
                                            snapshot_name,
                                            new_snapshot_name,
                                            generation,
                                            snap_id)

        if state == 'present' and not ttl and not link and \
                not new_snapshot_name:
            LOG.info('Returning storage group %s snapshot %s details ',
                     sg_name, snapshot_name)
            result['sg_snap_details'] = self.get_snapshot(sg_name,
                                                          snapshot_name,
                                                          generation,
                                                          snap_id)

        if result['create_sg_snap'] or result['delete_sg_snap'] or result[
                'rename_sg_snap'] or result['change_snap_link_status']:
            result['changed'] = True
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")

        # Finally update the module result!
        self.module.exit_json(**result)


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
        state=dict(required=True, choices=['present', 'absent'],
                   type='str'),
    )


def main():
    """Create PowerMax Snapshot object and perform action on it
        based on user input from playbook"""
    obj = Snapshot()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
