#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging
import copy
import re

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_host
version_added: '2.6'
short_description:  Manage host (initiator group) on PowerMax/VMAX Storage
                    System
description:
- Managing host on PowerMax Storage System includes create host with a set of
  initiators and host flags, add/remove initiators to/from host, modify host
  flag values, rename host and delete host
extends_documentation_fragment:
  - dellemc.dellemc_powermax
author:
- Vasudevu Lakhinana (vasudevu.lakhinana@dell.com)
- Manisha Agrawal (manisha.agrawal@dell.com)

options:
  host_name:
    description:
    - The name of the host. No  Special Character support except for _.
      Case sensitive for REST Calls.
    - Creation of empty host is allowed
    required: true
  initiators:
    description:
    - List of Initiator WWN or IQN to be added to host or removed from the
      host.
  state:
    description:
    - Define whether the host should exist or not.
    - present - indicates that the host should exist in system
    - absent - indicates that the host should not not exist in system
    required: true
    choices: [absent, present]
  initiator_state:
    description:
    - Define whether the initiators should be present or absent in host.
    - present-in-host - indicates that the initiators should exist on host
    - absent-in-host - indicates that the initiators should not exist on host
    - Required when creating a host with initiators or adding/removing 
      initiators to/from existing host
    choices: [present-in-host, absent-in-host]
  host_flags:
    description: 
    - input as an yaml dictionary
    - List of all host_flags-
    - 1. volume_set_addressing
    - 2. disable_q_reset_on_ua
    - 3. environ_set
    - 4. avoid_reset_broadcast
    - 5. openvms
    - 6. scsi_3
    - 7. spc2_protocol_version
    - 8. scsi_support1
    - 9. consistent_lun
    required: false
    choices: [true, false, unset(default state)]
  new_name:
    description:
    - The new name host for renaming function. No Special Character support
      except for _. Case sensitive for REST Calls
  '''

EXAMPLES = r'''
- name: Create host
    dellemc_powermax_host:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      host_name: "{{host_name}}"
      initiators:
      - 10000090fa7b4e85
      host_flags:
          spc2_protocol_version: true
          consistent_lun: true
          volume_set_addressing: 'unset'
          disable_q_reset_on_ua: false
          openvms: 'unset'
      state: 'present'
      initiator_state: 'present-in-host'

name: Get host details
    dellemc_powermax_host:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      host_name: "{{host_name}}"
      state: 'present'

  - name: Adding initiator to host
    dellemc_powermax_host:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      host_name: "{{host_name}}"
      initiators:
      - 10000090fa3d303e
      initiator_state: 'present-in-host'
      state: 'present'

  - name: Removing initiator from host
    dellemc_powermax_host:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      host_name: "{{host_name}}"
      initiators:
      - 10000090fa3d303e
      initiator_state: 'absent-in-host'
      state: 'present'

  - name: Modify flags of host
    dellemc_powermax_host:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      host_name: "{{host_name}}"
      host_flags:
          spc2_protocol_version: unset
          consistent_lun: unset
          volume_set_addressing: true
          disable_q_reset_on_ua: false
          openvms: false
          avoid_reset_broadcast: true
      state: 'present'

  - name: Rename host
    dellemc_powermax_host:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      host_name: "{{host_name}}"
      new_name: "{{new_host_name}}"
      state: 'present'

  - name: Delete host
    dellemc_powermax_host:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      host_name: "{{new_host_name}}"
      state: 'absent'
'''

RETURN = r'''
'''
LOG = utils.get_logger('dellemc_powermax_host', log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.1'


class PowerMaxHost(object):

    '''Class with host(initiator group) operations'''

    def __init__(self):
        ''' Define all parameters required by this module'''
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(self.get_powermax_host_parameters())
        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )
        # result is a dictionary that contains changed status and host details
        self.result = {"changed": False, "host_details": {}}
        if HAS_PYU4V is False:
            self.module.fail_json(msg="Ansible modules for PowerMax require "
                                      "the PyU4V python library to be "
                                      "installed. Please install the library "
                                      "before using these modules.")

        if PYU4V_VERSION_CHECK is not None:
            self.module.fail_json(msg=PYU4V_VERSION_CHECK)
            LOG.error(PYU4V_VERSION_CHECK)

        universion_details = utils.universion_check(
                             self.module.params['universion'])
        LOG.info("universion_details: {0}".format(universion_details))

        if not universion_details['is_valid_universion']:
            self.module.fail_json(msg=universion_details['user_message'])

        self.u4v_conn = utils.get_U4V_connection(self.module.params,
                                                 application_type=
                                                 APPLICATION_TYPE
                                                 )
        self.provisioning = self.u4v_conn.provisioning
        self.host_flags_list = {'volume_set_addressing', 'environ_set',
                                'disable_q_reset_on_ua', 'openvms',
                                'avoid_reset_broadcast', 'scsi_3',
                                'spc2_protocol_version', 'scsi_support1'}
        LOG.info('Got PyU4V instance for provisioning on PowerMax ')

    def get_powermax_host_parameters(self):
        return dict(
                host_name=dict(required=True, type='str'),
                initiators=dict(required=False, type='list'),
                state=dict(required=True, type='str'),
                initiator_state=dict(required=False, type='str'),
                host_flags=dict(required=False, type='dict'),
                new_name=dict(type='str', required=False)
                )

    def get_host(self, host_name):
        '''
        Get details of a given host
        '''
        try:
            LOG.info('Getting host {0} details'.format(host_name))
            hostFromGet = self.provisioning.get_host(host_name)
            if hostFromGet:
                return hostFromGet
        except Exception as e:
            LOG.error('Got error {0} while getting details of host {0}'
                      .format(str(e), host_name))
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

    def create_host(self, host_name):
        '''
        Create host with given initiators and host_flags
        '''
        initiator_state = self.module.params['initiator_state']
        initiators = self.module.params['initiators']
        received_host_flags = self.module.params['host_flags']

        if (initiator_state == 'absent-in-host' or initiator_state is None):
            initiators = None

        if received_host_flags:
            new_host_flags_dict = {}
            self._create_host_flags_dict(received_host_flags,
                                         new_host_flags_dict)
        else:
            new_host_flags_dict = None

        try:
            msg = ("Creating host {0} with parameters:initiators={1},"
                   "host_flags={2}")
            LOG.info(msg.format(host_name, initiators, new_host_flags_dict))
            self.provisioning.create_host(host_name, initiator_list=initiators,
                                          host_flags=new_host_flags_dict)
            return True

        except Exception as e:
            errorMsg = 'Create host {0} failed with error {1}'.format(
                    host_name, str(e))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)
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
            LOG.info('Initiators are already present in host {0}'
                     .format(host_name))
            return False

        add_list = self._get_add_initiators(existing_inits, initiators)
        if len(add_list) > 0:
            try:
                LOG.info('Adding initiators {0} to host {1}'.format(
                        add_list, host_name))
                self.provisioning.modify_host(host_name,
                                              add_init_list=add_list)
                return True
            except Exception as e:
                errorMsg = (("Adding initiators {0} to host {1} failed with"
                             "error {2}").format(
                                     add_list, host_name, str(e)))
                LOG.error(errorMsg)
                self.module.fail_json(msg=errorMsg)
        else:
            LOG.info('No initiators to add to host {0}'.format(
                    host_name))
            return False

    def remove_host_initiators(self, host_name, initiators):
        host = self.get_host(host_name)
        existing_inits = []
        if host and 'initiator' in host:
            existing_inits = host['initiator']

        if existing_inits is None or not len(existing_inits):
            LOG.info('No initiators are present in host {0}'
                     .format(host_name))
            return False

        remove_list = self._get_remove_initiators(existing_inits, initiators)

        if len(remove_list) > 0:
            try:
                LOG.info('Removing initiators {0} from host {1}'.format(
                        remove_list, host_name))
                self.provisioning.modify_host(host_name,
                                              remove_init_list=remove_list)
                return True
            except Exception as e:
                errorMsg = (("Removing initiators {0} from host {1} failed"
                             "with error {2}").format(remove_list, host_name,
                                                      str(e)))
                LOG.error(errorMsg)
                self.module.fail_json(msg=errorMsg)
        else:
            LOG.info('No initiators to remove from host {0}'.format(
                    host_name))
            return False

    def rename_host(self, host_name, new_name):
        try:
            self.provisioning.modify_host(host_name, new_name=new_name)
            return True
        except Exception as e:
            errorMsg = 'Renaming of host {0} failed with error {1}'.format(
                host_name, str(e))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)
            return None

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

    def modify_host_flags(self, host_name, received_host_flags):
        current_flags = {}
        self._recreate_host_flag_dict(self.get_host(host_name), current_flags)
        new_flags_dict = copy.deepcopy(current_flags)

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
            self.module.exit_json(changed=False)
        else:
            try:
                LOG.info('Modifying host flags for host {0} with {1}'
                         .format(host_name, new_flags_dict))
                self.provisioning.modify_host(host_name,
                                              host_flag_dict=new_flags_dict)
                return True

            except Exception as e:
                errorMsg = 'Modify host {0} failed with error {1}'.format(
                    host_name, str(e))
                LOG.error(errorMsg)
                self.module.fail_json(msg=errorMsg)
            return None

    def delete_host(self, host_name):
        '''
        Delete host from system
        A host cannot be deleted if it is associated with a masking view.
        '''
        try:
            self.provisioning.delete_host(host_name)
            return True
        except Exception as e:
            errorMsg = ('Delete host {0} failed with error {1}'.format(
                    host_name, str(e)))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

    def _create_result_dict(self, changed):
        self.result['changed'] = changed
        if self.module.params['state'] == 'absent':
            self.result['host_details'] = {}
        else:
            self.result['host_details'] = self.get_host(
                self.module.params['host_name'])

    def perform_module_operation(self):
        '''
        Perform different actions on host based on user parameter
        chosen in playbook
        '''
        state = self.module.params['state']
        intiator_state = self.module.params['initiator_state']
        host_name = self.module.params['host_name']
        initiators = self.module.params['initiators']
        new_name = self.module.params['new_name']
        host_flags = self.module.params['host_flags']

        host = self.get_host(host_name)
        changed = False

        if state == 'present' and not host and host_name:
            LOG.info('Creating host {0}'.format(host_name))
            changed = self.create_host(host_name)

        if (state == 'present' and host and intiator_state ==
                'present-in-host' and initiators and len(initiators) > 0):
            LOG.info('Adding initiators to host {0}'.format(host_name))
            changed = (self.add_host_initiators(host_name, initiators) or
                       changed)

        if (state == 'present' and host and intiator_state == 'absent-in-host'
                and initiators and len(initiators) > 0):
            LOG.info('Remove initiators from host {0}'.format(host_name))
            changed = (self.remove_host_initiators(host_name, initiators)
                       or changed)

        if state == 'present' and host and host_flags:
            LOG.info('Modifying host flags of host {0} to {1}'.format(
                    host_name, host_flags))
            changed = self.modify_host_flags(host_name, host_flags) or changed

        if state == 'present' and host and new_name:
            if host['hostId'] != new_name:
                LOG.info('Renaming host {0} to {1}'.format(host_name,
                         new_name))
                changed = self.rename_host(host_name, new_name)
                if changed is True:
                    self.module.params['host_name'] = new_name

        if state == 'absent' and host:
            LOG.info('Delete host {0} '.format(host_name))
            changed = self.delete_host(host_name) or changed

        self._create_result_dict(changed)
        # Update the module's final state
        LOG.info('changed {0}'.format(changed))
        self.module.exit_json(**self.result)


def main():
    ''' Create PowerMax host object and perform action on it
        based on user input from playbook'''
    obj = PowerMaxHost()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
