#!/usr/bin/python
# Copyright: (c) 2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r"""
---
module: snapshotpolicy
version_added: '1.5.0'
short_description: Manage snapshot policy on PowerMax/VMAX Storage
                   System
description:
- Managing a snapshot policy on a PowerMax storage system includes
  getting details of any specific snapshot policy, creating a snapshot policy,
  modifying snapshot policy attributes, modifying snapshot policy state,
  associating or disassociating storage groups to or from snapshot policy and
  deleting a snapshot policy.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
options:
  universion:
    description:
    - Unisphere version, currently '92' version is supported.
    type: int
    required: False
    choices: [92]
  snapshot_policy_name:
    description:
    - Name of the snapshot policy.
    required: True
    type: str
  interval:
    description:
    - The value of the interval counter for snapshot policy execution.
    required: False
    type: str
    choices: ["10 Minutes", "12 Minutes", "15 Minutes", "20 Minutes",
              "30 Minutes", "1 Hour", "2 Hours", "3 Hours", "4 Hours",
              "6 Hours", "8 Hours", "12 Hours", "1 Day", "7 Days"]
  secure:
    description:
    - Secure snapshots may only be terminated after they expire or by Dell EMC
      support.
    - If not specified, default value is False.
    required: False
    type: bool
    choices: [True, False]
  snapshot_count:
    description:
    - The max snapshot count of the policy.
    - Max value is 1024.
    required: False
    type: int
  offset_mins:
    description:
    - Defines when, within the interval the snapshots will be taken for a
      specified snapshot policy.
    - The offset must be less than the interval of the snapshot policy.
    - The format must be in minutes.
    - If not specified, default value is 0.
    required: False
    type: int
  compliance_count_warning:
    description:
    - If the number of valid snapshots falls below this number, the compliance
      changes to warning (yellow).
    required: False
    type: int
  compliance_count_critical:
    description:
    - If the number of valid snapshots falls below this number, the compliance
      changes to critical (red).
    required: False
    type: int
  storage_groups:
    description:
    - List of storage groups.
    required: False
    type: list
    elements: str
  storage_group_state:
    description:
    - The state of the storage group with regard to the snapshot policy.
    - present-in-policy indicates associate SG to SP.
    - absent-in-policy indicates disassociate SG from SP.
    required: False
    type: str
    choices: ['present-in-policy', 'absent-in-policy']
  suspend:
    description:
    - Suspend the snapshot policy.
    - True indicates snapshot policy is in suspend state.
    - False indicates snapshot policy is in resume state.
    required: False
    type: bool
    choices: [True, False]
  new_snapshot_policy_name:
    description:
    - New name of the snapshot policy.
    required: False
    type: str
  state:
    description:
    - Shows if the snapshot policy should be present or absent.
    required: True
    type: str
    choices: ['present', 'absent']
notes:
  - The max number of snapshot policies on an array is limited to 20.
  - At most four snapshot policies can be associated with a storage group.
  - compliance_count_critical <= compliance_count_warning
    < total snapshot_count for the policy.
"""

EXAMPLES = r"""
- name: Create a snapshot policy
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    interval: "10 Minutes"
    secure: false
    snapshot_count: 10
    offset_mins: 2
    compliance_count_warning: 6
    compliance_count_critical: 4
    state: "present"

- name: Create a snapshot policy and associate storage groups to it
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_2"
    interval: "10 Minutes"
    secure: false
    snapshot_count: 12
    offset_mins: 5
    compliance_count_warning: 8
    compliance_count_critical: 4
    storage_groups:
      - "11_ansible_test_1"
      - "11_ansible_test_2"
    storage_group_state: "present-in-policy"
    state: "present"

- name: Get snapshot policy details
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_2"
    state: "present"

- name: Modify snapshot policy attributes
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_2"
    new_snapshot_policy_name: "10min_policy_2_new"
    interval: "10 Minutes"
    snapshot_count: 16
    offset_mins: 8
    compliance_count_warning: 9
    compliance_count_critical: 7
    state: "present"

- name: Modify snapshot policy, associate to storage groups
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    storage_groups:
      - "11_ansible_test_1"
      - "11_ansible_test_2"
    storage_group_state: "present-in-policy"
    state: "present"

- name: Modify snapshot policy, disassociate from storage groups
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    storage_groups:
      - "11_ansible_test_1"
      - "11_ansible_test_2"
    storage_group_state: "absent-in-policy"
    state: "present"

- name: Modify snapshot policy state to suspend
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    suspend: true
    state: "present"

- name: Modify snapshot policy state to resume
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    suspend: false
    state: "present"

- name: Delete a snapshot policy
  dellemc.powermax.snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    state: "absent"
"""

RETURN = r"""
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
snapshot_policy_details:
    description: Details of the snapshot policy.
    returned: When snapshot policy exists.
    type: complex
    contains:
        compliance_count_critical:
            description: The number of valid snapshots that have critical
                         compliance.
            type: int
        compliance_count_warning:
            description: The number of valid snapshots that have warning
                         compliance.
            type: int
        interval_minutes:
            description: The interval minutes for snapshot policy execution.
            type: int
        last_time_used:
            description: The timestamp indicating the last time snapshot
                         policy was used.
            type: str
        offset_minutes:
            description: It is the time in minutes within the interval when
                         the snapshots will be taken for a specified
                         Snapshot Policy.
            type: int
        secure:
            description: True value indicates that the secure snapshots may
                         only be terminated after they expire or by Dell EMC
                         support.
            type: bool
        snapshot_count:
            description: It is the max snapshot count of the policy.
            type: int
        snapshot_policy_name:
            description: Name of the snapshot policy.
            type: str
        storage_group_count:
            description: The number of storage groups associated with the
                         snapshot policy.
            type: int
        storage_group:
            description: The list of storage groups associated with the
                         snapshot policy.
            type: list
        storage_group_snapshotID:
            description: Pair of storage group and list of snapshot IDs
                         associated with the snapshot policy.
            type: list
        suspended:
            description: The state of the snapshot policy, true indicates
                         policy is in suspend state.
            type: bool
        symmetrixID:
            description: The symmetrix on which snapshot policy exists.
            type: str
"""

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger("snapshotpolicy")

HAS_PYU4V = utils.has_pyu4v_sdk()
PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'

INTERVAL = ['10 Minutes', '12 Minutes', '15 Minutes', '20 Minutes',
            '30 Minutes', '1 Hour', '2 Hours', '3 Hours', '4 Hours',
            '6 Hours', '8 Hours', '12 Hours', '1 Day', '7 Days']


class SnapshotPolicy(object):

    def __init__(self):
        """ Initialises attributes required for snapshot policy operations
        """

        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_snapshotpolicy_parameters())

        required_together = [['storage_groups', 'storage_group_state']]

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            required_together=required_together,
            supports_check_mode=True)

        if HAS_PYU4V is False:
            msg = "Ansible modules for PowerMax require the PyU4V python " \
                  "library to be installed. Please install the library " \
                  "before using these modules"
            self.show_error_exit(msg, close_conn=False)

        if PYU4V_VERSION_CHECK is not None:
            self.show_error_exit(PYU4V_VERSION_CHECK, close_conn=False)

        self.pre_check_for_PyU4V_version()

        if self.module.params["universion"] is not None:
            universion_details = utils.universion_check(
                self.module.params["universion"])
            LOG.info("universion_details: %s", universion_details)

            if not universion_details["is_valid_universion"]:
                self.show_error_exit(
                    universion_details["user_message"], close_conn=False)

        try:
            self.conn = utils.get_U4V_connection(
                self.module.params, application_type=APPLICATION_TYPE)
            self.snapshot_policy = self.conn.snapshot_policy
            self.provisioning = self.conn.provisioning
            self.replication = self.conn.replication
        except Exception as e:
            self.show_error_exit(str(e))
        LOG.info("Got PyU4V instance for snapshot policy on PowerMax")
        LOG.info('Check Mode flag is %s', self.module.check_mode)

    def pre_check_for_PyU4V_version(self):
        """ Performs pre-check for PyU4V version"""
        curr_version = utils.PyU4V.__version__
        supp_version = "9.2.1.3"
        is_supported_version = utils.pkg_resources.parse_version(
            curr_version) >= utils.pkg_resources.parse_version(supp_version)

        if not is_supported_version:
            msg = "This functionality is not supported by PyU4V version " \
                  "{0}".format(curr_version)
            self.show_error_exit(msg)

    def close_connection(self):
        try:
            LOG.info("Closing unisphere connection %s", self.conn)
            utils.close_connection(self.conn)
            LOG.info("Connection closed successfully")
        except Exception as e:
            err_msg = ("Failed to close unisphere connection with error:"
                       " %s", str(e))
            LOG.error(err_msg)

    def show_error_exit(self, msg, close_conn=True):
        """ Log error message, closes the connection object and exit program

        :param msg: Error message to be displayed
        :type msg: str
        :param close_conn: Indicated whether to close connection or not
        :type close_conn: bool
        """
        if close_conn:
            self.close_connection()
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def get_storage_group(self, storage_group):
        """Get storage group details"""
        try:
            LOG.info('Getting storage group %s details', storage_group)
            sg = self.provisioning.get_storage_group(storage_group)
            if sg:
                return True
        except Exception as e:
            error_msg = ("Failed to get the storage group %s with error %s"
                         % (storage_group, str(e)))
            self.show_error_exit(error_msg)

    def get_snapshotpolicy_details(self, snapshot_policy=None):
        """ Get the details of snapshot policy

        :return: Snapshot policy details if exists or None
        :rtype: dict or None
        """
        try:
            if snapshot_policy:
                snapshot_policy_details = self.snapshot_policy. \
                    get_snapshot_policy(snapshot_policy)
            else:
                sp_name = self.module.params['snapshot_policy_name']
                LOG.info("Getting snapshot policy details for: %s", sp_name)
                snapshot_policy_details = self.snapshot_policy.\
                    get_snapshot_policy(sp_name)
                LOG.info("Successfully got details of snapshot policy: %s",
                         sp_name)
            return snapshot_policy_details
        except utils.ResourceNotFoundException as e:
            error_message = "Failed to get details of snapshot policy " \
                            "{0} with error {1}" \
                .format(self.module.params['snapshot_policy_name'], str(e))
            LOG.error(error_message)
            return None
        except Exception as e:
            self.show_error_exit(
                "Failed to get snapshot policy details, error: %s" % str(e))

    def create_snapshotpolicy(self):
        """ Create a snapshot policy

        :return: Snapshot policy details
        :rtype: dict
        """
        try:
            resp = {}
            sp_name = self.module.params['snapshot_policy_name']
            interval = self.module.params['interval']
            offset_mins = self.module.params['offset_mins']
            secure = self.module.params['secure']
            snapshot_count = self.module.params['snapshot_count']
            compliance_count_warning = self.module.params[
                'compliance_count_warning']
            compliance_count_critical = self.module.params[
                'compliance_count_critical']

            if interval is not None and offset_mins is not None:
                # extract integer value out of given string
                interval_mins = convert_interval_minute(interval)
                if offset_mins < 0 or offset_mins >= interval_mins:
                    err_msg = ("The offset_mins value cannot be greater "
                               "than or equal to interval %s, found %s" %
                               (interval_mins, str(offset_mins)))
                    self.show_error_exit(err_msg)

            param = {
                "snapshot_policy_name": sp_name,
                "interval": interval,
                "local_snapshot_policy_secure": secure,
                "local_snapshot_policy_snapshot_count": snapshot_count,
                "offset_mins": offset_mins,
                "compliance_count_warning": compliance_count_warning,
                "compliance_count_critical": compliance_count_critical
            }
            LOG.info("Creating snapshot policy: %s param: %s",
                     sp_name, param)
            if not self.module.check_mode:
                self.snapshot_policy.create_snapshot_policy(**param)
                LOG.info("Successfully created snapshot policy")
                resp = self.snapshot_policy.\
                    get_snapshot_policy(sp_name)
            return True, resp
        except Exception as e:
            self.show_error_exit(
                "Failed to create snapshot policy error: %s" % str(e))

    def is_snapshot_policy_modified(self):
        """ Determines whether the snapshot_policy attributes are to be
            updated or not """
        LOG.info("Checking snapshot policy attributes")
        snapshot_policy_details = self.snapshot_policy.\
            get_snapshot_policy(self.module.params['snapshot_policy_name'])
        LOG.debug("Snapshot Policy Details: %s", snapshot_policy_details)
        to_update = {}

        interval = self.module.params['interval']
        new_snapshot_policy_name = self.module.params[
            'new_snapshot_policy_name']
        secure = self.module.params['secure']
        snapshot_count = self.module.params['snapshot_count']
        offset_mins = self.module.params['offset_mins']
        compliance_count_warning = self.module.params[
            'compliance_count_warning']
        compliance_count_critical = self.module.params[
            'compliance_count_critical']
        suspend = self.module.params['suspend']

        if interval is not None:
            # extract integer value out of given string
            interval_mins = convert_interval_minute(interval)
            if snapshot_policy_details['interval_minutes'] \
                    != interval_mins:
                # check if interval_minutes > offset_mins
                if snapshot_policy_details['offset_minutes'] \
                        >= interval_mins:
                    err_msg = ("Interval value cannot be less than or "
                               "equal to offset %s, found %s"
                               % (str(snapshot_policy_details['offset_minutes']),
                                  interval_mins))
                    self.show_error_exit(err_msg)
                else:
                    to_update.update({'interval': interval})

        if (new_snapshot_policy_name is not None
                and new_snapshot_policy_name
                != snapshot_policy_details['snapshot_policy_name']):
            to_update.update({'new_snapshot_policy_name':
                              new_snapshot_policy_name})

        if (secure is not None
                and secure != snapshot_policy_details['secure']):
            err_msg = ("The secure snap option cannot be enabled or "
                       "disabled on an existing policy. Secure "
                       "snapshots may only be terminated after "
                       "they expire or by customer-authorized "
                       "Dell EMC support.")
            self.show_error_exit(err_msg)

        if (snapshot_count is not None
                and snapshot_count
                != snapshot_policy_details['snapshot_count']):
            to_update.update({'snapshot_count': snapshot_count})

        if (offset_mins is not None
                and offset_mins != snapshot_policy_details['offset_minutes']):
            # check if offset_minutes is in range of (0, interval_minutes)
            if interval is not None:
                interval_mins = convert_interval_minute(interval)
            else:
                interval_mins = snapshot_policy_details['interval_minutes']
            if 0 < offset_mins < interval_mins:
                to_update.update({'offset_mins': offset_mins})
            # check if offset_minutes = 0
            elif offset_mins == 0:
                err_msg = ("The offset_mins value must be after 00:00, "
                           "found: %s" % offset_mins)
                self.show_error_exit(err_msg)
            else:
                err_msg = ("The offset_mins value cannot be greater than "
                           "or equal to interval %s, found: %s" %
                           (interval_mins, offset_mins))
                self.show_error_exit(err_msg)

        if (compliance_count_warning is not None
                and compliance_count_warning
                != snapshot_policy_details['compliance_count_warning']):
            to_update.update({'compliance_count_warning':
                              compliance_count_warning})

        if (compliance_count_critical is not None
                and compliance_count_critical
                != snapshot_policy_details['compliance_count_critical']):
            to_update.update({'compliance_count_critical':
                              compliance_count_critical})

        if (suspend is not None
                and suspend != snapshot_policy_details['suspended']):
            to_update.update({'suspend': suspend})

        if len(to_update) > 0:
            LOG.info("Modification required")
            return to_update
        else:
            LOG.info("Modification not required")
            return None

    def modify_snapshotpolicy(self, to_modify_dict):
        """ Modify given snapshot policy attributes """

        try:
            sp_name = self.module.params['snapshot_policy_name']
            LOG.info("Modifying snapshot policy: %s", sp_name)
            # Suspend/Resume actions
            if 'suspend' in to_modify_dict:
                if to_modify_dict['suspend'] is True:
                    if not self.module.check_mode:
                        self.snapshot_policy.suspend_snapshot_policy(sp_name)
                    resp = self.display_result(sp_name)
                else:
                    if not self.module.check_mode:
                        self.snapshot_policy.resume_snapshot_policy(sp_name)
                    resp = self.display_result(sp_name)
                to_modify_dict.pop('suspend')

            if len(to_modify_dict) > 0:
                to_modify_dict.update({'snapshot_policy_name': sp_name})
                to_modify_dict.update({'action': 'Modify'})
                LOG.info("Parameters to be updated: %s", to_modify_dict)
                if 'new_snapshot_policy_name' in to_modify_dict and \
                        to_modify_dict['new_snapshot_policy_name']:
                    if not self.module.check_mode:
                        self.snapshot_policy.\
                            modify_snapshot_policy(**to_modify_dict)
                        sp_name = to_modify_dict['new_snapshot_policy_name']
                    resp = self.display_result(sp_name)
                else:
                    if not self.module.check_mode:
                        self.snapshot_policy.\
                            modify_snapshot_policy(**to_modify_dict)
                    resp = self.display_result(sp_name)
                LOG.info("Successfully modified snapshot policy")
            return True, resp
        except Exception as e:
            self.show_error_exit(
                "Failed to modify snapshot policy error: %s" % str(e))

    def associate_SG_to_SP(self):
        """ Associate storage group to snapshot policy """
        try:
            sg_list = self.module.params["storage_groups"]
            sp_name = self.module.params['snapshot_policy_name']
            LOG.info("Associating storage group(s) %s to snapshot policy: %s",
                     sg_list, sp_name)
            changed = False

            if sg_list:
                existing_sgs = self.snapshot_policy.\
                    get_snapshot_policy_storage_group_list(
                        snapshot_policy_name=sp_name)
                sgs_to_add = set(sg_list) - set(existing_sgs)

                if len(sgs_to_add) > 0:
                    if not self.module.check_mode:
                        self.snapshot_policy.associate_to_storage_groups(
                            sp_name, storage_group_names=list(sgs_to_add))
                        LOG.info("Successfully added sgs %s to snapshot "
                                 "policy %s", sgs_to_add, sp_name)
                    changed = True
                # Check if the given SGs are already associated with SP or not
                else:
                    LOG.info("Storage group(s) already associated with"
                             " snapshot policy")
                resp = self.snapshot_policy.get_snapshot_policy(sp_name)
                return changed, resp
            return False, None
        except Exception as e:
            self.show_error_exit(
                "Failed to add SG to snapshot policy with error: %s" % str(e))

    def disassociate_SG_from_SP(self):
        """ Disassociate storage group to snapshot policy """
        try:
            sg_list = self.module.params["storage_groups"]
            sp_name = self.module.params['snapshot_policy_name']
            LOG.info("Disassociating storage group(s) %s from "
                     "snapshot policy: %s",
                     sg_list, sp_name)
            changed = False

            if sg_list:
                existing_sgs = self.\
                    snapshot_policy.\
                    get_snapshot_policy_storage_group_list(
                        snapshot_policy_name=sp_name)
                sgs_to_remove = set(sg_list) & set(existing_sgs)
                if len(sgs_to_remove) > 0:
                    if not self.module.check_mode:
                        self.snapshot_policy.disassociate_from_storage_groups(
                            sp_name, list(sgs_to_remove))
                        LOG.info("Successfully removed %s SGs from snapshot "
                                 "policy %s", sgs_to_remove, sp_name)
                    changed = True
                # Check if the given SGs are already disassociated with SP or
                # not
                elif len(sgs_to_remove) == 0:
                    LOG.info("Storage group(s) already disassociated with"
                             " snapshot policy")
                resp = self.snapshot_policy.get_snapshot_policy(sp_name)
                return changed, resp
            return False, None
        except Exception as e:
            self.show_error_exit(
                "Failed to remove SGs from snapshot policy with error: %s"
                % str(e))

    def delete_snapshotpolicy(self):
        """ Delete given snapshot policy """
        try:
            sp_name = self.module.params['snapshot_policy_name']
            LOG.info("Deleting snapshot policy: %s", sp_name)
            if not self.module.check_mode:
                self.snapshot_policy.delete_snapshot_policy(sp_name)
                LOG.info("Successfully deleted snapshot policy")
            return True
        except Exception as e:
            self.show_error_exit(
                "Failed to delete snapshot policy error: %s" % str(e))

    def get_SP_SG_snapshotID(self, snap_pol_name):
        """ Get the list of snapshot IDs """

        sg_snap_id_list = []
        sp_sg_list = self.snapshot_policy.\
            get_snapshot_policy_storage_group_list(
                snapshot_policy_name=snap_pol_name)
        for sg in sp_sg_list:
            # for each SG, get the list of snapshots
            snapshot_list = self.replication.get_storage_group_snapshot_list(
                storage_group_id=sg)
            # check if that snapshot is of the desired snapshot policy
            if snap_pol_name in snapshot_list:
                snapshot_id_list = self.replication.\
                    get_storage_group_snapshot_snap_id_list(
                        storage_group_id=sg, snap_name=snap_pol_name)
                sg_snap_id_list.append({sg: snapshot_id_list})
        return sg_snap_id_list

    def display_result(self, snap_pol_name):
        """ Display snapshot policy details """
        try:
            result = dict()
            LOG.info("Display snapshot policy: %s", snap_pol_name)
            result['snapshot_policy_details'] = \
                self.get_snapshotpolicy_details(snap_pol_name)
            result['snapshot_policy_details']['storage_group'] = \
                self.snapshot_policy.get_snapshot_policy_storage_group_list(
                    snapshot_policy_name=snap_pol_name)
            result['snapshot_policy_details']['storage_group_snapshotID'] = \
                self.get_SP_SG_snapshotID(snap_pol_name)
            LOG.info("Successfully Got Display attributes of snapshot "
                     "policy %s", snap_pol_name)
            return result['snapshot_policy_details']
        except Exception as e:
            self.show_error_exit(
                "Failed to display snapshot policy details with "
                "error: %s" % str(e))

    def perform_module_operation(self):
        """ Perform snapshot policy operation based on playbook task """

        sp_name = self.module.params['snapshot_policy_name']
        state = self.module.params['state']
        sg_state = self.module.params["storage_group_state"]
        storage_groups = self.module.params['storage_groups']
        new_sp_name = self.module.params['new_snapshot_policy_name']

        # Get snapshot policy details
        if sp_name and len(sp_name.strip()):
            result = {'changed': False,
                      'snapshot_policy_details':
                          self.get_snapshotpolicy_details()}
        else:
            errmsg = 'snapshot_policy_name is required.'
            LOG.error(errmsg)
            self.show_error_exit(msg=errmsg)

        if state == "present":
            if not result['snapshot_policy_details']:
                # Create snapshot policy
                if sg_state == "absent-in-policy":
                    self.show_error_exit("storage_group_state can not be "
                                         "absent-in-policy ")
                result['changed'], result['snapshot_policy_details'] \
                    = self.create_snapshotpolicy()
            if result['snapshot_policy_details']:
                # Associate storage group to snapshot policy
                if storage_groups and sg_state == "present-in-policy":
                    result['changed'], result['snapshot_policy_details'] = \
                        self.associate_SG_to_SP()
                # Disassociate storage group from snapshot policy
                if storage_groups and sg_state == "absent-in-policy":
                    result['changed'], result['snapshot_policy_details'] \
                        = self.disassociate_SG_from_SP()
                # Modify snapshot policy attributes
                to_modify_dict = self.is_snapshot_policy_modified()
                if to_modify_dict:
                    result['changed'], result['snapshot_policy_details'] \
                        = self.modify_snapshotpolicy(to_modify_dict)
        else:
            if result['snapshot_policy_details']:
                # Delete snapshot policy
                result['changed'], result['snapshot_policy_details'] \
                    = self.delete_snapshotpolicy(), None
        if state == "present":
            if not self.module.check_mode and new_sp_name:
                snap_pol_name = new_sp_name
            else:
                snap_pol_name = sp_name
            if result['snapshot_policy_details']:
                result['snapshot_policy_details'] = self.display_result(snap_pol_name)

        self.close_connection()
        self.module.exit_json(**result)


def convert_interval_minute(interval):
    """Convert the interval to minute"""

    interval_minute = 0
    raw_interval = interval.split(' ')
    if len(raw_interval) == 2:
        interval_value = int(raw_interval[0])
        interval_unit = raw_interval[1]
        if interval_unit == 'Minutes':
            interval_minute = interval_value
        if interval_unit == 'Hour' or interval_unit == 'Hours':
            interval_minute = interval_value * 60
        if interval_unit == 'Day' or interval_unit == 'Days':
            interval_minute = interval_value * 24 * 60
    return interval_minute


def get_snapshotpolicy_parameters():
    return dict(
        universion=dict(type='int', required=False, choices=[92]),
        snapshot_policy_name=dict(required=True, type='str'),
        interval=dict(required=False, type='str', choices=INTERVAL),
        secure=dict(required=False, type='bool', choices=[True, False]),
        snapshot_count=dict(required=False, type='int'),
        offset_mins=dict(required=False, type='int'),
        compliance_count_warning=dict(required=False, type='int'),
        compliance_count_critical=dict(required=False, type='int'),
        storage_groups=dict(required=False, type='list', elements='str'),
        storage_group_state=dict(required=False, type='str',
                                 choices=['present-in-policy',
                                          'absent-in-policy']),
        suspend=dict(required=False, type='bool', choices=[True, False]),
        new_snapshot_policy_name=dict(required=False, type='str'),
        state=dict(required=True, type='str', choices=['present', 'absent']))


def main():
    """ Create PowerMaxSnapshotPolicy object and perform action on it
        based on user input from playbook """
    obj = SnapshotPolicy()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
