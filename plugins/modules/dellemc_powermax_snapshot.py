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
module: dellemc_powermax_snapshot
version_added: '1.0.0'
short_description: Manage Snapshots on PowerMax/VMAX Storage System
description:
- Managing snapshots on a PowerMax storage system includes creating a new
  storage group (SG) snapshot, getting details of the SG snapshot, renaming
  the SG snapshot, changing the snapshot link status, and deleting an
  existing storage group snapshot.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
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
    - If the ttl is not specified, the storage group snap details would be
      returned.
    - However, to create a SG snap - TTL must be given.
    - If the SG snap should not have any TTL - specify TTL as "None"
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
    - The generation number of the Snapshot.
    - Generation is mandatory for link, unlink, rename and delete operations.
    - Optional for Get snapshot details.
    - Create snapshot will always create a new snapshot with generation
      number 0.
    - Rename is supported only for generation number 0.
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
  '''

EXAMPLES = r'''
  - name: Create a Snapshot for a Storage Group
    dellemc_powermax_snapshot:
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
    dellemc_powermax_snapshot:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      sg_name: "ansible_sg"
      snapshot_name: "ansible_sg_snap"
      state: "present"

  - name: Delete Storage Group Snapshot
    dellemc_powermax_snapshot:
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

  - name: Rename Storage Group Snapshot
    dellemc_powermax_snapshot:
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

  - name: Change Snapshot Link Status to Linked
    dellemc_powermax_snapshot:
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

  - name: Change Snapshot Link Status to UnLinked
    dellemc_powermax_snapshot:
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
        generation:
            description: The generation number of the snapshot.
            type: int
        isExpired:
            description: Indicates whether the snapshot is expired or not.
            type: bool
        isLinked:
            description: Indicates whether the snapshot is linked or not.
            type: bool
        isRestored:
            description: Indicates whether the snapshot is restored or not.
            type: bool
        name:
            description: Name of the snapshot.
            type: str
        nonSharedTracks:
            description: Number of non-shared tracks.
            type: int
        numSharedTracks:
            description: Number of shared tracks.
            type: int
        numSourceVolumes:
            description: Number of source volumes.
            type: int
        numStorageGroupVolumes:
            description: Number of storage group volumes.
            type: int
        numUniqueTracks:
            description: Number of unique tracks.
            type: int
        sourceVolume:
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
        timeToLiveExpiryDate:
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

import logging
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils

LOG = utils.get_logger('dellemc_powermax_snapshot',
                       log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.4'


class PowerMaxSnapshot(object):
    """Class with Snapshot operations"""

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(
            get_powermax_snapshot_parameters())

        # initialize the Ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
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
        LOG.info('Got PyU4V instance for provisioning on PowerMax ')

    def get_snapshot(self, sg_id, snapshot_name, generation):
        """Get snapshot details"""
        try:
            LOG.info('Getting storage group %s snapshot %s details',
                     sg_id, snapshot_name)
            if generation is None:
                return self.replication.\
                    get_storage_group_snapshot_generation_list(sg_id,
                                                               snapshot_name)
            return self.replication.\
                get_snapshot_generation_details(sg_id,
                                                snapshot_name,
                                                generation)
        except Exception as e:
            error_message = 'Got error: {0} while getting details of ' \
                            'storage group {1} snapshot {2}'
            self.show_error_exit(msg=error_message.format(str(e), sg_id,
                                                          snapshot_name))

    def create_sg_snapshot(self, sg_id, snap_name, ttl, ttl_unit):
        """Create Storage Group Snapshot"""
        try:
            if ttl_unit == 'days':
                ttl_unit = False
            else:
                ttl_unit = True
            if ttl == 'None':
                ttl = None
            resp = self.replication.create_storage_group_snapshot(sg_id,
                                                                  snap_name,
                                                                  ttl,
                                                                  ttl_unit)
            return True, resp
        except Exception as e:
            error_message = 'Create Snapshot {0} for SG {1} failed ' \
                            'with error {2} '
            self.show_error_exit(msg=error_message.format(snap_name, sg_id,
                                                          str(e)))

    def delete_sg_snapshot(self, sg_id, snap_name, generation):
        """Delete Storage Group Snapshot"""
        if generation is None:
            self.show_error_exit(msg="Please specify a valid generation "
                                 "to delete a snapshot.")
        try:
            snapshot = self.replication.get_snapshot_generation_details(
                sg_id,
                snap_name,
                generation)
        except Exception as e:
            return False
        try:

            if snapshot:
                self.replication.delete_storage_group_snapshot(sg_id,
                                                               snap_name,
                                                               generation)
            return True
        except Exception as e:
            error_message = 'Delete SG {0} Snapshot {1} failed with ' \
                            'error {2} '
            self.show_error_exit(msg=error_message.format(sg_id, snap_name,
                                                          str(e)))

    def rename_sg_snapshot(self, sg_id, snap_name,
                           new_snap_name, generation):
        """Rename Storage Group Snapshot"""
        try:
            snapshot = self.get_snapshot(sg_id, snap_name, generation)
            if snap_name == new_snap_name:
                return False, snapshot
            resp = self.replication. \
                modify_storage_group_snapshot(sg_id,
                                              "None",
                                              snap_name,
                                              generation,
                                              new_name=new_snap_name
                                              )
            return True, resp
        except Exception as e:
            error_message = 'Renaming Snapshot {0} for Storage Group {1} ' \
                            'failed with error {2} '
            self.show_error_exit(msg=error_message.format(snap_name, str(e)))

    def change_snapshot_link_status(self, sg_id, target_sg,
                                    snap_name, link_status, generation):
        """Change Snapshot Link status"""
        if generation is None:
            error_message = 'Change SG {0} Snapshot {1} link status failed.' \
                            ' Please provide a valid generation '
            self.show_error_exit(msg=error_message.format(sg_id,
                                                          snap_name))
        try:
            snapshot = self.get_snapshot(sg_id, snap_name, generation)

            if snapshot['isLinked'] is True and link_status == 'linked':
                for linked_sg in snapshot['linkedStorageGroup']:
                    linked = False
                    if linked_sg['name'] == target_sg:
                        linked = True
                        break
                if linked:
                    return False, snapshot
            elif snapshot['isLinked'] is False and link_status == 'unlinked':
                return False, snapshot
            if link_status == 'linked':
                link = True
                unlink = False
            else:
                link = False
                unlink = True
            resp = self.replication. \
                modify_storage_group_snapshot(sg_id,
                                              target_sg,
                                              snap_name,
                                              link=link,
                                              unlink=unlink,
                                              gen_num=generation)
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
            LOG.info('Delete storage group %s snapshot %s generation %s ',
                     sg_name, snapshot_name, generation)
            result['delete_sg_snap'] = self.delete_sg_snapshot(sg_name,
                                                               snapshot_name,
                                                               generation)

        if state == 'present' and snapshot_name \
                and link and target_sg_name:
            LOG.info('Change storage group %s snapshot %s link status ',
                     sg_name, snapshot_name)
            result['change_snap_link_status'], \
                result['sg_snap_link_details'] = \
                self.change_snapshot_link_status(sg_name,
                                                 target_sg_name,
                                                 snapshot_name,
                                                 link,
                                                 generation)

        if state == 'present' and sg_name and snapshot_name and \
                new_snapshot_name and generation == 0:
            LOG.info('Rename storage group %s snapshot %s ',
                     sg_name, snapshot_name)
            result['rename_sg_snap'], result['sg_snap_rename_details'] = \
                self.rename_sg_snapshot(sg_name,
                                        snapshot_name,
                                        new_snapshot_name,
                                        generation)

        if state == 'present' and not ttl and not link and \
                not new_snapshot_name:
            LOG.info('Returning storage group %s snapshot %s details ',
                     sg_name, snapshot_name)
            result['sg_snap_details'] = self.get_snapshot(sg_name,
                                                          snapshot_name,
                                                          generation)

        if result['create_sg_snap'] or result['delete_sg_snap'] or result[
                'rename_sg_snap'] or result['change_snap_link_status']:
            result['changed'] = True
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")

        # Finally update the module result!
        self.module.exit_json(**result)


def get_powermax_snapshot_parameters():
    return dict(
        sg_name=dict(required=True, type='str'),
        snapshot_name=dict(required=True, type='str'),
        ttl=dict(required=False, type='str'),
        ttl_unit=dict(required=False, default='days',
                      choices=['hours', 'days'], type='str'),
        generation=dict(required=False, type='int'),
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
    obj = PowerMaxSnapshot()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
