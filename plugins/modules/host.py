#!/usr/bin/python
# Copyright: (c) 2019-2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: host
version_added: '1.0.0'
short_description:  Manage host (initiator group) on PowerMax/VMAX Storage
                    System
description:
- Managing hosts on a PowerMax storage system includes creating a host with a
  set of initiators and host flags, adding and removing initiators to or from
  a host, modifying host flag values, renaming a host, and deleting a host.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

options:
  host_name:
    description:
    - The name of the host. No Special Character support except for _.
      Case sensitive for REST Calls.
    - Creation of an empty host is allowed.
    required: true
    type: str
  initiators:
    description:
    - List of Initiator WWN or IQN or alias to be added to or removed
      from the host.
    type: list
    elements: str
  state:
    description:
    - Define whether the host should exist or not.
    - absent - indicates that the host should not exist in the system.
    - present - indicates that the host should exist in the system.
    required: true
    choices: [absent, present]
    type: str
  initiator_state:
    description:
    - Define whether the initiators should be present or absent on the host.
    - absent-in-host - indicates that the initiators should not exist on the
      host.
    - present-in-host - indicates that the initiators should exist on the host.
    - Required when creating a host with initiators or adding and removing
      initiators to or from an existing host.
    choices: [absent-in-host, present-in-host]
    type: str
  host_flags:
    description:
    - Input as a yaml dictionary.
    - List of all host_flags-
    - 1. volume_set_addressing.
    - 2. disable_q_reset_on_ua.
    - 3. environ_set.
    - 4. avoid_reset_broadcast.
    - 5. openvms.
    - 6. scsi_3.
    - 7. spc2_protocol_version.
    - 8. scsi_support1.
    - 9. consistent_lun.
    - Possible values are true, false, unset (default state).
    required: false
    type: dict
  host_type:
    description:
      - Describing the OS type.
    required: false
    choices: [default, hpux]
    type: str
  new_name:
    description:
    - The new name of the host for the renaming function. No Special Character
      support except for _. Case sensitive for REST Calls.
    type: str
notes:
  - host_flags and host_type are mutually exclusive parameters.
'''

EXAMPLES = r'''
- name: Create host with host_type 'default'
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    host_type: "default"
    state: 'present'

- name: Create host with host_type 'hpux'
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_2"
    host_type: "hpux"
    state: 'present'

- name: Create host with host_flags
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_3"
    initiators:
      - 1000000000000001
      - 'host/HBA01'
    host_flags:
      spc2_protocol_version: true
      consistent_lun: true
      volume_set_addressing: 'unset'
      disable_q_reset_on_ua: false
      openvms: 'unset'
    state: 'present'
    initiator_state: 'present-in-host'

- name: Get host details
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    state: 'present'

- name: Adding initiator to host
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    initiators:
      - 1000000000000001
      - 'host/HBA01'
    initiator_state: 'present-in-host'
    state: 'present'

- name: Removing initiator from host
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    initiators:
      - 1000000000000001
      - 'host/HBA01'
    initiator_state: 'absent-in-host'
    state: 'present'

- name: Modify host using host_type
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    host_type: "hpux"
    state: 'present'

- name: Modify host using host_flags
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    host_flags:
      spc2_protocol_version: unset
      consistent_lun: unset
      volume_set_addressing: true
      disable_q_reset_on_ua: false
      openvms: false
      avoid_reset_broadcast: true
    state: 'present'

- name: Rename host
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    new_name: "ansible_test_1_host"
    state: 'present'

- name: Delete host
  dellemc.powermax.host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1_host"
    state: 'absent'
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
host_details:
    description: Details of the host.
    returned: When host exist.
    type: complex
    contains:
        bw_limit:
            description: Bandwidth limit of the host.
            type: int
        consistent_lun:
            description: Flag for consistent LUN in host.
            type: bool
        enabled_flags:
            description: List of any enabled port flags overridden by the
                         initiator.
            type: list
        disabled_flags:
            description: List of any disabled port flags overridden by the
                         initiator.
            type: list
        hostId:
            description: Host ID.
            type: str
        hostgroup:
            description: List of host groups that the host is associated with.
            type: list
        initiator:
            description: List of initiators present in the host.
            type: list
        maskingview:
            description: List of masking view in which the host group is
                         present.
            type: list
        num_of_hostgroups:
            description: Number of host groups associated with the host.
            type: int
        num_of_initiators:
            description: Number of initiators present in the host.
            type: int
        num_of_masking_views:
            description: Number of masking views associated with the host.
            type: int
        num_of_powerpath_hosts:
            description: Number of PowerPath hosts associated with the host.
            type: int
        port_flags_override:
            description: Whether any of the initiator port flags are
                         overridden.
            type: bool
        type:
            description: Type of initiator.
            type: str
'''

import re
import copy
import logging
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('host')

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


class Host(object):

    '''Class with host(initiator group) operations'''

    u4v_conn = None

    def __init__(self):
        ''' Define all parameters required by this module'''
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_host_parameters())

        mutually_exclusive = [['host_flags', 'host_type']]
        required_together = [['initiators', 'initiator_state']]

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive,
            required_together=required_together
        )
        # result is a dictionary that contains changed status and host details
        self.result = {"changed": False, "host_details": {}}
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
        self.host_flags_list = ['volume_set_addressing', 'environ_set',
                                'disable_q_reset_on_ua', 'openvms',
                                'avoid_reset_broadcast', 'scsi_3',
                                'spc2_protocol_version', 'scsi_support1']
        LOG.info('Check Mode Flag %s', self.module.check_mode)
        LOG.info('Got PyU4V instance for provisioning on PowerMax ')

    def get_host(self, host_name):
        '''
        Get details of a given host
        '''
        try:
            LOG.info('Getting host %s details', host_name)
            hostFromGet = self.provisioning.get_host(host_name)
            if hostFromGet:
                return hostFromGet
        except Exception as e:
            LOG.error('Got error %s while getting details of host %s',
                      str(e), host_name)
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
                    received_host_flags[host_flag_name] in ['unset', 'Unset']):
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

    def create_host(self, host_name, initiators):
        '''
        Create host with given initiators and host_flags
        '''
        received_host_flags = self.module.params['host_flags']
        host_type = self.module.params['host_type']

        new_host_flags_dict = {}
        if host_type:
            new_host_flags_dict = HOST_FLAGS[host_type]
        elif received_host_flags:
            self._create_host_flags_dict(received_host_flags,
                                         new_host_flags_dict)
        else:
            new_host_flags_dict = None

        try:
            if not self.module.check_mode:
                msg = "Creating host %s with parameters:initiators=%s, " \
                      "host_flags=%s" % (host_name, initiators,
                                         new_host_flags_dict)
                LOG.info(msg)
                self.provisioning.create_host(
                    host_name, initiator_list=initiators,
                    host_flags=new_host_flags_dict)
            return True

        except Exception as e:
            errorMsg = ('Create host %s failed with error %s'
                        % (host_name, str(e)))
            self.show_error_exit(msg=errorMsg)
        return None

    def _get_add_initiators(self, existing, requested):
        all_inits = existing + requested
        add_inits = list(set(all_inits) - set(existing))
        return add_inits

    def _get_remove_initiators(self, existing, requested):
        rem_inits = list(set(existing).intersection(set(requested)))
        return rem_inits

    def add_host_initiators(self, host_name, initiators):
        host = self.get_host(host_name)
        existing_inits = []
        if host and 'initiator' in host:
            existing_inits = host['initiator']

        if initiators and (set(initiators).issubset(set(existing_inits))):
            LOG.info('Initiators are already present in host %s', host_name)
            return False

        add_list = self._get_add_initiators(existing_inits, initiators)
        if len(add_list) > 0:
            try:
                if not self.module.check_mode:
                    LOG.info('Adding initiators %s to host %s',
                             add_list, host_name)
                    self.provisioning.modify_host(host_name,
                                                  add_init_list=add_list)
                return True
            except Exception as e:
                errorMsg = "Adding initiators {0} to host {1} failed with " \
                           "error {2}".format(add_list, host_name, str(e))
                self.show_error_exit(msg=errorMsg)
        else:
            LOG.info('No initiators to add to host %s', host_name)
            return False

    def remove_host_initiators(self, host_name, initiators):
        host = self.get_host(host_name)
        existing_inits = []
        if host and 'initiator' in host:
            existing_inits = host['initiator']

        if existing_inits is None or not len(existing_inits):
            LOG.info('No initiators are present in host %s', host_name)
            return False

        remove_list = self._get_remove_initiators(existing_inits, initiators)

        if len(remove_list) > 0:
            try:
                if not self.module.check_mode:
                    LOG.info('Removing initiators %s from host %s',
                             remove_list, host_name)
                    self.provisioning.modify_host(host_name,
                                                  remove_init_list=remove_list
                                                  )
                return True
            except Exception as e:
                errorMsg = ("Removing initiators %s from host %s failed"
                            " with error %s", remove_list, host_name, str(e))
                self.show_error_exit(msg=errorMsg)
        else:
            LOG.info('No initiators to remove from host %s', host_name)
            return False

    def rename_host(self, host_name, new_name):
        try:
            if not self.module.check_mode:
                self.provisioning.modify_host(host_name, new_name=new_name)
            return True
        except Exception as e:
            errorMsg = 'Renaming of host {0} failed with error ' \
                       '{1}'.format(host_name, str(e))
            self.show_error_exit(msg=errorMsg)

    def _create_default_host_flags_dict(self, current_flags):
        for flag in self.host_flags_list:
            self._set_to_default(flag, current_flags)

        self._disable_consistent_lun(current_flags)

    def _recreate_host_flag_dict(self, host, current_flags):
        '''
        Recreate current flags dictionary using output from get_host()
        function
        '''
        self._create_default_host_flags_dict(current_flags)

        for flag in host['enabled_flags'].split(','):
            if len(flag) > 0:
                '''
                Remove any extra text from information received from
                get_host() to match the desired input to VMAX python SDK
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

    def modify_host_flags(self, host_name, received_host_flags=None,
                          host_type=None):
        current_flags = {}
        self._recreate_host_flag_dict(self.get_host(host_name), current_flags)
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
                if not self.module.check_mode:
                    LOG.info('Modifying host flags for host %s with %s',
                             host_name, new_flags_dict)
                    self.provisioning.modify_host(
                        host_name, host_flag_dict=new_flags_dict)
                return True

            except Exception as e:
                errorMsg = ('Modify host %s failed with error %s'
                            % (host_name, str(e)))
                self.show_error_exit(msg=errorMsg)
            return None

    def delete_host(self, host_name):
        '''
        Delete host from system
        A host cannot be deleted if it is associated with a masking view.
        '''
        try:
            if not self.module.check_mode:
                self.provisioning.delete_host(host_name)
            return True
        except Exception as e:
            errorMsg = ('Delete host %s failed with error %s',
                        host_name, str(e))
            self.show_error_exit(msg=errorMsg)

    def _create_result_dict(self, changed, host=None):
        self.result['changed'] = changed
        if self.module.params['state'] == 'absent' or \
                (not host and self.module.check_mode):
            self.result['host_details'] = {}
        else:
            if self.module.params['new_name'] and not self.module.check_mode:
                self.result['host_details'] = self.get_host(
                    self.module.params['new_name'])
            else:
                self.result['host_details'] = self.get_host(
                    self.module.params['host_name'])

    def get_initiator_id(self, alias):
        '''
        Get initiator id for the specified alias.
        '''
        try:
            LOG.info("Getting details of initiator with alias %s", alias)
            params = {"alias": alias}
            initiator_ids = self.provisioning.get_initiator_list(params)
            if not initiator_ids:
                error_msg = ('Initiator alias %s is invalid' % alias)
                self.show_error_exit(msg=error_msg)
            return initiator_ids[0].split(':')[2]
        except Exception as e:
            errorMsg = ('Retrieving initiator details based on alias %s '
                        'failed with error %s' % (alias, str(e)))
            self.show_error_exit(msg=errorMsg)

    def get_initator_ids(self, initiators):
        '''
        Get list of initiator ids to be added to or removed from host.
        '''
        initiator_ids = []
        for initiator in initiators:
            if "/" in initiator:
                initiator_ids.append(self.get_initiator_id(initiator))
            else:
                if not utils.is_valid_initiator(initiator):
                    error_msg = ('Initiator %s is invalid' % initiator)
                    self.show_error_exit(msg=error_msg)
                initiator_ids.append(initiator)
        initiator_ids = list(dict.fromkeys(initiator_ids))
        return initiator_ids

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s",
                         self.u4v_conn)
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
        Perform different actions on host based on user parameter
        chosen in playbook
        '''
        state = self.module.params['state']
        initiator_state = self.module.params['initiator_state']
        host_name = self.module.params['host_name']
        initiators = self.module.params['initiators']
        new_name = self.module.params['new_name']
        host_flags = self.module.params['host_flags']
        host_type = self.module.params['host_type']

        if (host_name is None) or (host_name is not None and
                                   len(host_name.strip()) == 0):
            error_msg = "host_name is mandatory parameter. Please provide " \
                        "valid host name."
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)

        host = self.get_host(host_name)
        changed = False

        if initiators:
            initiators = self.get_initator_ids(initiators)

        if state == 'present' and not host:
            if new_name:
                error_msg = "Invalid argument 'new_name' while " \
                            "creating a host"
                LOG.error(error_msg)
                self.show_error_exit(msg=error_msg)

            if initiator_state and initiator_state != "present-in-host":
                error_msg = "Incorrect initiator_state specified for Create" \
                            " host functionality"
                LOG.error(error_msg)
                self.show_error_exit(msg=error_msg)
            LOG.info('Creating host %s', host_name)
            changed = self.create_host(host_name, initiators)

        if (state == 'present' and host and initiator_state ==
                'present-in-host' and initiators and len(initiators) > 0):
            LOG.info('Adding initiators to host %s', host_name)
            changed = (self.add_host_initiators(host_name, initiators) or
                       changed)

        if (state == 'present' and host and
                initiator_state == 'absent-in-host' and initiators and
                len(initiators) > 0):
            LOG.info('Remove initiators from host %s', host_name)
            changed = (self.remove_host_initiators(host_name, initiators)
                       or changed)

        if state == 'present' and host and (host_flags or host_type):
            LOG.info('Modifying host flags of host %s ',
                     host_name)
            changed = self.modify_host_flags(host_name,
                                             received_host_flags=host_flags,
                                             host_type=host_type) or changed

        if state == 'present' and host and new_name is not None:
            if len(new_name.strip()) == 0:
                self.show_error_exit(msg="Please provide valid host name.")

            if host['hostId'] != new_name:
                LOG.info('Renaming host %s to %s', host_name, new_name)
                changed = self.rename_host(host_name, new_name)

        if state == 'absent' and host:
            LOG.info('Delete host %s ', host_name)
            changed = self.delete_host(host_name) or changed

        self._create_result_dict(changed, host)
        # Update the module's final state
        LOG.info('changed %s', changed)
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")
        self.module.exit_json(**self.result)


def get_host_parameters():
    return dict(
        host_name=dict(required=True, type='str'),
        initiators=dict(required=False, type='list', elements='str'),
        state=dict(required=True, type='str', choices=['present',
                                                       'absent']),
        initiator_state=dict(required=False, type='str',
                             choices=['present-in-host', 'absent-in-host']),
        host_flags=dict(required=False, type='dict'),
        host_type=dict(type='str', required=False, choices=['default',
                                                            'hpux']),
        new_name=dict(type='str', required=False)
    )


def main():
    ''' Create PowerMax host object and perform action on it
        based on user input from playbook'''
    obj = Host()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
