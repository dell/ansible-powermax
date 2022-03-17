#!/usr/bin/python
# Copyright: (c) 2019-2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: hostgroup
version_added: '1.0.0'
short_description:  Manage a host group (cascaded initiator group) on a
                    PowerMax/VMAX storage system
description:
- Managing a host group on a PowerMax storage system includes creating a host
  group with a set of hosts, adding or removing hosts to or from a host group,
  renaming a host group, modifying host flags of a host group, and deleting
  a host group.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
options:
  hostgroup_name:
    description:
    - The name of the host group. No Special Character support except for _.
      Case sensitive for REST Calls.
    required: true
    type: str
  hosts:
    description:
    - List of host names to be added to the host group or removed from the
      host group.
    - Creation of an empty host group is allowed.
    type: list
    elements: str
  state:
    description:
    - Define whether the host group should be present or absent on the system.
    - present - indicates that the host group should be present on the system.
    - absent - indicates that the host group should be absent on the system.
    required: true
    choices: [absent, present]
    type: str
  host_state:
    description:
    - Define whether the host should be present or absent in the host group.
    - present-in-group - indicates that the hosts should exist in the host
                         group.
    - absent-in-group - indicates that the hosts should not exist in the host
                        group.
    choices: [present-in-group, absent-in-group]
    type: str
  host_flags:
    description:
    - input as an yaml dictionary.
    - List of all host_flags -
    - 1. volume_set_addressing.
    - 2. disable_q_reset_on_ua.
    - 3. environ_set.
    - 4. avoid_reset_broadcast.
    - 5. openvms.
    - 6. scsi_3.
    - 7. spc2_protocol_version.
    - 8. scsi_support1.
    - 9. consistent_lun.
    - Possible values are true, false, unset(default state).
    required: false
    type: dict
  host_type:
    description:
      - Describing the OS type (default or hpux).
    required: false
    choices: [default, hpux]
    type: str
  new_name:
    description:
    - The new name for the host group for the renaming function. No Special
      Character support except for _. Case sensitive for REST Calls.
    type: str
notes:
  - In the gather facts module, empty host groups will be listed as hosts.
  - host_flags and host_type are mutually exclusive parameters.
  - Hostgroups with 'default' host_type will have 'default' hosts.
  - Hostgroups with 'hpux' host_type will have 'hpux' hosts.
'''

EXAMPLES = r'''
- name: Create host group with 'default' host_type
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    host_type: "default"
    hosts:
      - ansible_test_1
    host_state: 'present-in-group'
    state: 'present'

- name: Create host group with 'hpux' host_type
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_2"
    host_type: "hpux"
    hosts:
      - ansible_test_2
    host_state: 'present-in-group'
    state: 'present'

- name: Create host group with host_flags
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_3"
    hosts:
      - ansible_test_3
    state: 'present'
    host_state: 'present-in-group'
    host_flags:
      spc2_protocol_version: true
      consistent_lun: true
      volume_set_addressing: 'unset'
      disable_q_reset_on_ua: false
      openvms: 'unset'

- name: Get host group details
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    state: 'present'

- name: Adding host to host group
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    hosts:
      - Ansible_Testing_host2
    state: 'present'
    host_state: 'present-in-group'

- name: Removing host from host group
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    hosts:
      - Ansible_Testing_host2
    state: 'present'
    host_state: 'absent-in-group'

- name: Modify host group using host_type
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    host_type: "hpux"
    state: 'present'

- name: Modify host group using host_flags
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    host_flags:
      spc2_protocol_version: unset
      disable_q_reset_on_ua: false
      openvms: false
      avoid_reset_broadcast: true
    state: 'present'

- name: Rename host group
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    new_name: "ansible_test_hostgroup_1"
    state: 'present'

- name: Delete host group
  dellemc.powermax.hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_hostgroup_1"
    state: 'absent'
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
hostgroup_details:
    description: Details of the host group.
    returned: When host group exist.
    type: complex
    contains:
        consistent_lun:
            description: Flag for consistent LUN in the host group.
            type: bool
        enabled_flags:
            description: List of any enabled port flags overridden by the
                         initiator.
            type: list
        disabled_flags:
            description: List of any disabled port flags overridden by the
                         initiator.
            type: list
        host:
            description: List of hosts present in the host group.
            type: list
            contains:
                hostId:
                    description: Unique identifier for the host.
                    type: str
                initiator:
                    description: List of initiators present in the host.
                    type: list
        hostGroupId:
            description: Host group ID.
            type: str
        maskingview:
            description: Masking view in which host group is present.
            type: list
        num_of_hosts:
            description: Number of hosts in the host group.
            type: int
        num_of_initiators:
            description: Number of initiators in the host group.
            type: int
        num_of_masking_views:
            description: Number of masking views associated with the host
                         group.
            type: int
        port_flags_override:
            description: Whether any of the initiator's port flags are
                         overridden.
            type: bool
        type:
            description: Type of initiator of the hosts of the host group.
            type: str
'''

import re
import copy
import logging
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils

LOG = utils.get_logger('hostgroup')

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'

BASE_FLAGS = {'volume_set_addressing': {'enabled': False, 'override': False},
              'disable_q_reset_on_ua': {'enabled': False, 'override': False},
              'environ_set': {'enabled': False, 'override': False},
              'avoid_reset_broadcast': {'enabled': False, 'override': False},
              'openvms': {'enabled': False, 'override': False},
              'scsi_3': {'enabled': False, 'override': False},
              'spc2_protocol_version': {'enabled': False, 'override': False},
              'scsi_support1': {'enabled': False, 'override': False},
              'consistent_lun': False
              }


def flags_default():
    """
    Build Host Flags for the default host_type
    :return: (dict)
    """
    return BASE_FLAGS


def flags_hpux():
    """
    Build Host Flags for HPUX host_type
    :return: (dict)
    """
    flags = BASE_FLAGS.copy()
    flags['volume_set_addressing'] = {'enabled': True, 'override': True}
    flags['spc2_protocol_version'] = {'enabled': True, 'override': True}
    flags['openvms'] = {'enabled': False, 'override': True}
    return flags


HOST_FLAGS = {'default': flags_default(),
              'hpux': flags_hpux()}


class HostGroup(object):
    '''Class with host group (cascaded initiator group) operations'''

    u4v_conn = None

    def __init__(self):
        ''' Define all parameters required by this module'''
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_hostgroup_parameters())

        mutually_exclusive = [['host_flags', 'host_type']]
        required_together = [['hosts', 'host_state']]

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive,
            required_together=required_together
        )
        # result is a dictionary that contains changed status and host details
        self.result = {"changed": False, "hostgroup_details": {}}
        self.host_flags_list = ['volume_set_addressing', 'environ_set',
                                'disable_q_reset_on_ua', 'openvms',
                                'avoid_reset_broadcast', 'scsi_3',
                                'spc2_protocol_version', 'scsi_support1']
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
        LOG.info('Check Mode Flag %s', self.module.check_mode)
        LOG.info('Got PyU4V instance for provisioning on to VMAX ')

    def get_hostgroup(self, hostgroup_name):
        '''
        Get details of a given host group
        '''
        try:
            LOG.info('Getting host group %s details', hostgroup_name)
            hostGroupFromGet = self.provisioning.get_host_group(hostgroup_name)
            if hostGroupFromGet:
                return hostGroupFromGet

        except Exception as e:
            LOG.error('Got error %s while getting details of host group %s',
                      str(e), hostgroup_name)
        return None

    def _set_to_enable(self, host_flag_name, host_flag_dict):
        host_flag_dict[host_flag_name.lower()] = {
            'enabled': True,
            'override': True
        }

    def _set_to_disable(self, host_flag_name, host_flag_dict):
        host_flag_dict[host_flag_name.lower()] = {
            'enabled': False,
            'override': True
        }

    def _set_to_default(self, host_flag_name, host_flag_dict):
        host_flag_dict[host_flag_name.lower()] = {
            'enabled': False,
            'override': False
        }

    def _disable_consistent_lun(self, host_flag_dict):
        host_flag_dict['consistent_lun'] = False

    def _enable_consistent_lun(self, host_flag_dict):
        host_flag_dict['consistent_lun'] = True

    def _create_host_flags_dict(self, received_host_flags,
                                new_host_flags_dict):
        '''
        Creating the expected payload for host_flags
        '''
        for host_flag_name in self.host_flags_list:
            if (host_flag_name not in received_host_flags or
                    received_host_flags[host_flag_name]
                    in ['unset', 'Unset']):
                self._set_to_default(host_flag_name, new_host_flags_dict)

            elif (received_host_flags[host_flag_name] is False or
                  received_host_flags[host_flag_name] in ['false', 'False']):
                self._set_to_disable(host_flag_name, new_host_flags_dict)

            else:
                self._set_to_enable(host_flag_name, new_host_flags_dict)

        if ('consistent_lun' not in received_host_flags
            or received_host_flags['consistent_lun'] is False
            or received_host_flags['consistent_lun'] in ['unset', 'Unset',
                                                         'false', 'False']):
            self._disable_consistent_lun(new_host_flags_dict)

        else:
            self._enable_consistent_lun(new_host_flags_dict)

    def create_hostgroup(self, hostgroup_name):
        '''
        Create host group with given hosts and host flags
        '''
        hosts = self.module.params['hosts']
        host_state = self.module.params['host_state']
        received_host_flags = self.module.params['host_flags']
        host_type = self.module.params['host_type']
        emptyHostGroupFlag = False
        param_list = [hostgroup_name]
        new_host_flags_dict = {}

        if not hosts or host_state == 'absent-in-group':
            emptyHostGroupFlag = True
        else:
            param_list.append(hosts)

        if received_host_flags:
            self._create_host_flags_dict(
                received_host_flags, new_host_flags_dict)
            param_list.append(new_host_flags_dict)
        elif host_type:
            new_host_flags_dict = HOST_FLAGS[host_type]
        else:
            new_host_flags_dict = None

        try:
            if emptyHostGroupFlag:
                LOG.info('Creating empty HostGroup %s with parameters %s',
                         hostgroup_name, param_list)
                self.provisioning.create_host(hostgroup_name,
                                              host_flags=new_host_flags_dict,
                                              initiator_list=None)
            else:
                for host in hosts:
                    try:
                        self.provisioning.get_host(host_id=host)
                    except Exception as e:
                        errorMsg = 'Create host group {0} failed as the ' \
                                   'host {1} does not exist'\
                            .format(hostgroup_name, host)
                        self.show_error_exit(msg=errorMsg)
                LOG.info('Creating host group %s with parameters %s',
                         hostgroup_name, param_list)
                if not self.module.check_mode:
                    self.provisioning.create_host_group(
                        hostgroup_name, host_flags=new_host_flags_dict,
                        host_list=hosts)
            return True

        except Exception as e:
            errorMsg = 'Create host group {0} failed with error {1}'.format(
                hostgroup_name, str(e))
            self.show_error_exit(msg=errorMsg)

    def _get_add_hosts(self, existing, requested):
        add_hosts = list(set(existing + requested) - set(existing))
        return add_hosts

    def _get_remove_hosts(self, existing, requested):
        rem_hosts = list(set(existing).intersection(set(requested)))
        return rem_hosts

    def add_hosts_to_hostgroup(self, hostgroup_name, hosts):
        hostgroup = self.get_hostgroup(hostgroup_name)
        existing_hosts = []
        '''
        Get the existing host and validate with input hosts
        before modifying host group.
        API does not allow to add hosts already present in the host group
        '''
        if hostgroup and 'host' in hostgroup:
            for host in hostgroup['host']:
                existing_hosts.append(host['hostId'])

        if hosts and (set(hosts).issubset(set(existing_hosts))):
            LOG.info('Hosts are already present in host group %s',
                     hostgroup_name)
            return False

        add_list = self._get_add_hosts(existing_hosts, hosts)
        if len(add_list) > 0:
            try:
                LOG.info('Adding hosts %s to host group %s',
                         add_list, hostgroup_name)
                if not self.module.check_mode:
                    self.provisioning.modify_host_group(
                        hostgroup_name, add_host_list=add_list)
                return True
            except Exception as e:
                errorMsg = ("Adding host %s to host group %s failed with"
                            " error %s" % (add_list, hostgroup_name, str(e)))
                self.show_error_exit(msg=errorMsg)
        else:
            LOG.info('No hosts to add to host group %s', hostgroup_name)
            return False

    def remove_hosts_from_hostgroup(self, hostgroup_name, hosts):
        hostgroup = self.get_hostgroup(hostgroup_name)
        existing_hosts = []
        '''
        Get the existing host and validate with input hosts
        before modifying host group.
        API does not allow removal of non-existing hosts from host group
        '''
        if hostgroup and 'host' in hostgroup:
            for host in hostgroup['host']:
                existing_hosts.append(host['hostId'])

        if not existing_hosts or not len(existing_hosts):
            LOG.info('Hosts are not present in host group %s', hostgroup_name)
            return False

        rem_list = self._get_remove_hosts(existing_hosts, hosts)
        if len(rem_list) > 0:
            try:
                LOG.info('Removing hosts %s from host group %s',
                         rem_list, hostgroup_name)
                if not self.module.check_mode:
                    self.provisioning.modify_host_group(
                        hostgroup_name, remove_host_list=rem_list)
                return True
            except Exception as e:
                errorMsg = ("Removing host %s from host group %s failed with"
                            " error %s", rem_list, hostgroup_name, str(e))
                self.show_error_exit(msg=errorMsg)
        else:
            LOG.info('No hosts to remove from host group %s', hostgroup_name)
            return False

    def rename_hostgroup(self, hostgroup_name, new_name):
        try:
            if not self.module.check_mode:
                self.provisioning.modify_host_group(hostgroup_name,
                                                    new_name=new_name)
            return True
        except Exception as e:
            errorMsg = 'Renaming of host group {0} failed with ' \
                       'error {1}'.format(hostgroup_name, str(e))
            self.show_error_exit(msg=errorMsg)

    def delete_hostgroup(self, hostgroup_name):
        '''
        Delete host group from system
        A host group cannot be deleted if it is associated with a masking view.
        '''
        try:
            if not self.module.check_mode:
                self.provisioning.delete_host_group(hostgroup_name)
            return True
        except Exception as e:
            errorMsg = 'Delete host group {0} failed with error {1}'.format(
                hostgroup_name, str(e))
            self.show_error_exit(msg=errorMsg)

    def _create_default_host_flags_dict(self, current_flags):
        for flag in self.host_flags_list:
            self._set_to_default(flag, current_flags)

        self._disable_consistent_lun(current_flags)

    def _recreate_host_flag_dict(self, host, current_flags):
        '''
        Recreate current flags dictionary using output from get_host() function
        '''
        self._create_default_host_flags_dict(current_flags)

        for flag in host['enabled_flags'].split(','):
            if len(flag) > 0:
                '''
                Remove any extra text from information received from get_host()
                to match the desired input to VMAX python SDK
                '''
                self._set_to_enable(
                    re.sub(
                        r'\(.*?\)',
                        '',
                        flag),
                    current_flags)

        for flag in host['disabled_flags'].split(','):
            if len(flag) > 0:
                self._set_to_disable(
                    re.sub(
                        r'\(.*?\)',
                        '',
                        flag),
                    current_flags)

        if host['consistent_lun'] is False:
            self._disable_consistent_lun(current_flags)
        else:
            self._enable_consistent_lun(current_flags)

    def modify_host_flags(self, hostgroup_name, received_host_flags=None,
                          host_type=None):
        current_flags = {}
        self._recreate_host_flag_dict(
            self.get_hostgroup(hostgroup_name), current_flags)
        new_flags_dict = copy.deepcopy(current_flags)

        if host_type:
            new_flags_dict = HOST_FLAGS[host_type]
        elif received_host_flags:
            for flag in received_host_flags:
                if flag != 'consistent_lun':
                    if (received_host_flags[flag] is True or
                            received_host_flags[flag] in ['True', 'true']):
                        self._set_to_enable(flag, new_flags_dict)

                    elif (received_host_flags[flag] is False or
                          received_host_flags[flag] in ['false', 'False']):
                        self._set_to_disable(flag, new_flags_dict)

                    else:
                        self._set_to_default(flag, new_flags_dict)

                elif (received_host_flags['consistent_lun'] is False or
                      received_host_flags['consistent_lun'] in
                      ['False', 'false', 'unset', 'Unset']):

                    self._disable_consistent_lun(new_flags_dict)
                else:
                    self._enable_consistent_lun(new_flags_dict)

        if new_flags_dict == current_flags:
            LOG.info('No change detected')
            return False
        else:
            try:
                LOG.info('Modifying host group flags for host %s with %s',
                         hostgroup_name, new_flags_dict)
                if not self.module.check_mode:
                    self.provisioning.modify_host_group(hostgroup_name,
                                                        new_flags_dict)
                return True

            except Exception as e:
                errorMsg = ('Modify host group %s failed with error %s'
                            % (hostgroup_name, str(e)))
                self.show_error_exit(msg=errorMsg)

    def _create_result_dict(self, changed, hostgroup):
        self.result['changed'] = changed
        if self.module.params['state'] == 'absent' or \
                (not hostgroup and self.module.check_mode):
            self.result['hostgroup_details'] = {}
        else:
            if self.module.params['new_name'] and not self.module.check_mode:
                self.result['hostgroup_details'] = self.get_hostgroup(
                    self.module.params['new_name'])
            else:
                self.result['hostgroup_details'] = self.get_hostgroup(
                    self.module.params['hostgroup_name'])

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = ("Failed to close unisphere connection with error:"
                           " %s", str(e))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        '''
        Perform different actions on host group based on user parameter
        chosen in playbook
        '''
        state = self.module.params['state']
        host_state = self.module.params['host_state']
        hostgroup_name = self.module.params['hostgroup_name']
        hosts = self.module.params['hosts']
        new_name = self.module.params['new_name']
        host_flags = self.module.params['host_flags']
        host_type = self.module.params['host_type']

        if (hostgroup_name is None) or (hostgroup_name is not None and
                                        len(hostgroup_name.strip()) == 0):
            error_msg = "hostgroup_name is mandatory parameter. Please " \
                        "provide valid host group name."
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        hostgroup = self.get_hostgroup(hostgroup_name)
        changed = False

        if state == 'present' and not hostgroup and hostgroup_name:
            if new_name:
                error_msg = "Invalid argument 'new_name' while " \
                            "creating a host"
                LOG.error(error_msg)
                self.show_error_exit(msg=error_msg)

            if host_state and host_state != "present-in-group":
                error_msg = "Incorrect host_state specified for Create" \
                            " hostgroup functionality"
                LOG.error(error_msg)
                self.show_error_exit(msg=error_msg)

            LOG.info('Creating host group %s', hostgroup_name)
            changed = self.create_hostgroup(hostgroup_name)

        if (state == 'present' and host_state == 'present-in-group' and
                hostgroup and hosts and len(hosts) > 0):
            LOG.info('Add hosts to host group %s', hostgroup_name)
            changed = self.add_hosts_to_hostgroup(
                hostgroup_name, hosts) or changed

        if (state == 'present' and host_state == 'absent-in-group' and
                hostgroup and hosts and len(hosts) > 0):
            LOG.info('Remove hosts from host group %s', hostgroup_name)
            changed = self.remove_hosts_from_hostgroup(
                hostgroup_name, hosts) or changed

        if state == 'present' and hostgroup and (host_flags or host_type):
            LOG.info('Modifying host group flags of hostgroup %s',
                     hostgroup_name)
            changed = (self.modify_host_flags(hostgroup_name,
                                              received_host_flags=host_flags,
                                              host_type=host_type) or changed)

        if state == 'present' and hostgroup and new_name is not None:
            if len(new_name.strip()) == 0:
                self.show_error_exit(msg="Please provide valid hostgroup "
                                         "name.")

            if hostgroup['hostGroupId'] != new_name:
                LOG.info('Renaming host group %s to %s',
                         hostgroup_name, new_name)
                changed = self.rename_hostgroup(hostgroup_name, new_name)

        if state == 'absent' and hostgroup:
            LOG.info('Delete host group %s ', hostgroup_name)
            changed = self.delete_hostgroup(hostgroup_name) or changed

        self._create_result_dict(changed, hostgroup)
        # Update the module's final state
        LOG.info('changed %s', changed)
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")
        self.module.exit_json(**self.result)


def get_hostgroup_parameters():
    return dict(
        hostgroup_name=dict(required=True, type='str'),
        hosts=dict(required=False, type='list', elements='str'),
        state=dict(required=True, type='str', choices=['present', 'absent']),
        host_state=dict(required=False, type='str',
                        choices=['present-in-group', 'absent-in-group']),
        host_flags=dict(required=False, type='dict'),
        host_type=dict(type='str', required=False,
                       choices=['default', 'hpux']),
        new_name=dict(type='str', required=False)
    )


def main():
    ''' Create PowerMax host group object and perform action on it
        based on user input from playbook'''
    obj = HostGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
