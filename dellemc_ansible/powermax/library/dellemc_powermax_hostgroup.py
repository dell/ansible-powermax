#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

import logging
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
import copy
import re

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_hostgroup
version_added: '2.6'
short_description:  Manage host group (cascaded initiator group) on
                    PowerMax/VMAX Storage System
description:
- Managing host group on PowerMax Storage System includes create host group
  with set of hosts, add/remove hosts to/from host group, rename host group,
  modify host flags of host group and delete host group
extends_documentation_fragment:
  - dellemc_powermax.dellemc_powermax
author:
- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
options:
  hostgroup_name:
    description:
    - The name of the host group. No Special Character support except for _.
      Case sensitive for REST Calls.
    required: true
  hosts:
    description:
    - List of host names to be added to the host group or removed from host
      group.
    - Creation of empty host group is allowed.
  state:
    description:
    - Define whether the host group should be present or absent on the system.
    - present - indicates that the host group should be present on system
    - absent - indicates that the host group should be absent on system
    required: true
    choices: [absent, present]
  host_state:
    description:
    - Define whether the host should be present or absent in host group.
    - present-in-group - indicates that the hosts should exist in host group
    - absent-in-group - indicates that the hosts should not exist in host 
                        group
    choices: [present-in-group, absent-in-group]
  host_flags:
    description: 
    - input as an yaml dictionary
    - List of all host_flags -
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
    - The new name for host group for renaming function. No Special Character
      support except for _. Case sensitive for REST Calls
Notes:
  - In gather facts module, empty host groups will be listed as hosts.
  '''

EXAMPLES = r'''
- name: Create host group
    dellemc_powermax_hostgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      hostgroup_name: "{{hostgroup_name}}"
      hosts:
      - Ansible_Testing_host
      state: 'present'
      host_state: 'present-in-group'
      host_flags:
          spc2_protocol_version: true
          consistent_lun: true
          disable_q_reset_on_ua: false
          openvms: unset

  - name: Get host group details
    dellemc_powermax_hostgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      hostgroup_name: "{{hostgroup_name}}"
      state: 'present'

  - name: Adding host to host group
    dellemc_powermax_hostgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      hostgroup_name: "{{hostgroup_name}}"
      hosts:
      - Ansible_Testing_host2
      state: 'present'
      host_state: 'present-in-group'

  - name: Removing host from host group
    dellemc_powermax_hostgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      hostgroup_name: "{{hostgroup_name}}"
      hosts:
      - Ansible_Testing_host2
      state: 'present'
      host_state: 'absent-in-group'

  - name: Modify flags of host group
    dellemc_powermax_hostgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      hostgroup_name: "{{hostgroup_name}}"
      host_flags:
          spc2_protocol_version: unset
          disable_q_reset_on_ua: false
          openvms: false
          avoid_reset_broadcast: true
      state: 'present'

  - name: Rename host group
    dellemc_powermax_hostgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      hostgroup_name: "{{hostgroup_name}}"
      new_name: "Ansible_Testing_hostgroup2"
      state: 'present'

  - name: Delete host group
    dellemc_powermax_hostgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      hostgroup_name: "Ansible_Testing_hostgroup2"
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
			description: Flag for consistent LUN in host group.
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
			description: list of hosts present in the host group.
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
			description: Number of masking views, host group is associated
			             with.
            type: int
		port_flags_override:
			description: Whether any of the initiator's port flags are
			             overridden.
            type: bool
		type:
			description: Type of host group.
            type: str
'''

LOG = utils.get_logger('dellemc_powermax_hostgroup', log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.2'


class PowerMaxHostGroup(object):
    '''Class with host group (cascaded initiator group) operations'''

    u4v_conn = None
    def __init__(self):
        ''' Define all parameters required by this module'''
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(self.get_powermax_hostgroup_parameters())

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )
        # result is a dictionary that contains changed status and host details
        self.result = {"changed": False, "host_details": {}}
        self.host_flags_list = {'volume_set_addressing', 'environ_set',
                                'disable_q_reset_on_ua', 'openvms',
                                'avoid_reset_broadcast', 'scsi_3',
                                'spc2_protocol_version', 'scsi_support1'}
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
            LOG.info("universion_details: {0}".format(universion_details))

            if not universion_details['is_valid_universion']:
                self.show_error_exit(msg=universion_details['user_message'])

        try:
            self.u4v_conn = utils.get_U4V_connection(
                    self.module.params, application_type=APPLICATION_TYPE)
        except Exception as e:
            self.show_error_exit(msg=str(e))
        self.provisioning = self.u4v_conn.provisioning
        LOG.info('Got PyU4V instance for provisioning on to VMAX ')

    def get_powermax_hostgroup_parameters(self):
        return dict(
            hostgroup_name=dict(required=True, type='str'),
            hosts=dict(required=False, type='list'),
            state=dict(required=True, type='str'),
            host_state=dict(required=False, type='str'),
            host_flags=dict(required=False, type='dict'),
            new_name=dict(type='str', required=False)
        )

    def get_hostgroup(self, hostgroup_name):
        '''
        Get details of a given host group
        '''
        try:
            LOG.info('Getting host group {0} details'.format(hostgroup_name))
            hostGroupFromGet = self.provisioning.get_hostgroup(hostgroup_name)
            if hostGroupFromGet:
                return hostGroupFromGet

        except Exception as e:
            LOG.error('Got error {0} while getting details of host group {0}'
                      .format(str(e), hostgroup_name))
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

    def create_hostgroup(self, hostgroup_name):
        '''
        Create host group with given hosts and host flags
        '''
        hosts = self.module.params['hosts']
        host_state = self.module.params['host_state']
        received_host_flags = self.module.params['host_flags']
        emptyHostGroupFlag = False
        param_list = [hostgroup_name]
        new_host_flags_dict = {}

        if (hosts is None or len(hosts) == 0 or not host_state or
                host_state == 'absent-in-group'):
            emptyHostGroupFlag = True
        else:
            param_list.append(hosts)

        if received_host_flags:
            self._create_host_flags_dict(
                received_host_flags, new_host_flags_dict)
            param_list.append(new_host_flags_dict)

        try:
            if emptyHostGroupFlag:
                LOG.info('Creating empty HostGroup {0} with parameters {1}'
                         .format(hostgroup_name, param_list))
                self.provisioning.create_host(hostgroup_name,
                                              host_flags=new_host_flags_dict,
                                              initiator_list=None)
            else:
                for host in hosts:
                    try:
                        self.provisioning.get_host(host_id=host)
                    except Exception as e:
                        errorMsg = 'Create host group {0} failed as the host {1} does not exist'.format(
                                hostgroup_name, host)
                        self.show_error_exit(msg=errorMsg)
                LOG.info('Creating host group {0} with parameters {1}'
                         .format(hostgroup_name, param_list))
                self.provisioning.create_hostgroup(hostgroup_name,
                                                   host_flags=new_host_flags_dict,
                                                   host_list=hosts)
            return True

        except Exception as e:
            errorMsg = 'Create host group {0} failed with error {1}'.format(
                hostgroup_name, str(e))
            self.show_error_exit(msg=errorMsg)
        return None

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
            LOG.info('Hosts are already present in host group {0}'
                     .format(hostgroup_name))
            return False

        add_list = self._get_add_hosts(existing_hosts, hosts)
        if len(add_list) > 0:
            try:
                LOG.info('Adding hosts {0} to host group {1}'.format(
                        add_list, hostgroup_name))
                self.provisioning.modify_hostgroup(hostgroup_name,
                                                   add_host_list=add_list)
                return True
            except Exception as e:
                errorMsg = (("Adding host {0} to host group {1} failed with"
                             "error {2}").format(
                                     add_list, hostgroup_name, str(e)))
                self.show_error_exit(msg=errorMsg)
        else:
            LOG.info('No hosts to add to host group {0}'.format(
                    hostgroup_name))
            return False

    def remove_hosts_from_hostgroup(self, hostgroup_name, hosts):
        hostgroup = self.get_hostgroup(hostgroup_name)
        existing_hosts = []
        '''
        Get the existing host and validate with input hosts
        before modifying host group.
        API does not allow removoval of non-existing hosts from host group
        '''
        if hostgroup and 'host' in hostgroup:
            for host in hostgroup['host']:
                existing_hosts.append(host['hostId'])

        if existing_hosts is None or not len(existing_hosts):
            LOG.info('Hosts are not present in host group {0}'
                     .format(hostgroup_name))
            return False

        rem_list = self._get_remove_hosts(existing_hosts, hosts)
        if len(rem_list) > 0:
            try:
                LOG.info('Removing hosts {0} from host group {1}'.format(
                        rem_list, hostgroup_name))
                self.provisioning.modify_hostgroup(hostgroup_name,
                                                   remove_host_list=rem_list)
                return True
            except Exception as e:
                errorMsg = (("Removing host {0} from host group {1} failed"
                             "with error {2}").format(rem_list, hostgroup_name,
                                                      str(e)))
                self.show_error_exit(msg=errorMsg)
        else:
            LOG.info('No hosts to remove from host group {0}'.format(
                    hostgroup_name))
            return False

    def rename_hostgroup(self, hostgroup_name, new_name):
        try:
            self.provisioning.modify_hostgroup(
                hostgroup_name, new_name=new_name)
            return True
        except Exception as e:
            errorMsg = ('Renaming of host group {0} failed with error {1}'
                        .format(hostgroup_name, str(e)))
            self.show_error_exit(msg=errorMsg)
            return None

    def delete_hostgroup(self, hostgroup_name):
        '''
        Delete host group from system
        A host group cannot be deleted if it is associated with a masking view.
        '''
        try:
            self.provisioning.delete_hostgroup(hostgroup_name)
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

    def modify_host_flags(self, hostgroup_name, received_host_flags):
        current_flags = {}
        self._recreate_host_flag_dict(
            self.get_hostgroup(hostgroup_name), current_flags)
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
            return False
        else:
            try:
                LOG.info('Modifying host group flags for host {0} with {1}'
                         .format(hostgroup_name, new_flags_dict))
                self.provisioning.modify_hostgroup(
                    hostgroup_name, new_flags_dict)
                return True

            except Exception as e:
                errorMsg = ('Modify host group {0} failed with error {1}'
                            .format(hostgroup_name, str(e)))
                self.show_error_exit(msg=errorMsg)
            return None

    def _create_result_dict(self, changed):
        self.result['changed'] = changed
        if self.module.params['state'] == 'absent':
            self.result['hostgroup_details'] = {}
        else:
            self.result['hostgroup_details'] = self.get_hostgroup(
                self.module.params['hostgroup_name'])

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection {0}".format(
                    self.u4v_conn))
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = "Failed to close unisphere connection with error:" \
                          " {0}".format(str(e))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        '''
        Perform different actions on host group based on user parameter
        choosen in playbook
        '''
        state = self.module.params['state']
        host_state = self.module.params['host_state']
        hostgroup_name = self.module.params['hostgroup_name']
        hosts = self.module.params['hosts']
        new_name = self.module.params['new_name']
        host_flags = self.module.params['host_flags']

        hostgroup = self.get_hostgroup(hostgroup_name)
        changed = False

        if (state == 'present' and not hostgroup and hostgroup_name):
            LOG.info('Creating host group {0}'.format(hostgroup_name))
            changed = self.create_hostgroup(hostgroup_name)

        if (state == 'present' and host_state == 'present-in-group' and
                hostgroup and hosts and len(hosts) > 0):
            LOG.info('Add hosts to host group {0}'.format(hostgroup_name))
            changed = self.add_hosts_to_hostgroup(
                hostgroup_name, hosts) or changed

        if (state == 'present' and host_state == 'absent-in-group' and
                hostgroup and hosts and len(hosts) > 0):
            LOG.info('Remove hosts from host group {0}'.format(hostgroup_name))
            changed = self.remove_hosts_from_hostgroup(
                hostgroup_name, hosts) or changed

        if (state == 'present' and hostgroup and host_flags):
            LOG.info(
                'Modifying host group flags of hostgroup {0} to {1}'.format(
                    hostgroup_name, host_flags))
            changed = (self.modify_host_flags(hostgroup_name, host_flags) or
                       changed)

        if (state == 'present' and hostgroup and new_name):
            if hostgroup['hostGroupId'] != new_name:
                LOG.info(
                    'Renaming host group {0} to {1}'.format(
                        hostgroup_name, new_name))
                changed = self.rename_hostgroup(hostgroup_name, new_name)
                self.module.params['hostgroup_name'] = new_name

        if (state == 'absent' and hostgroup):
            LOG.info('Delete host group {0} '.format(hostgroup_name))
            changed = self.delete_hostgroup(hostgroup_name) or changed

        self._create_result_dict(changed)
        # Update the module's final state
        LOG.info('changed {0}'.format(changed))
        LOG.info("Closing unisphere connection {0}".format(self.u4v_conn))
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")
        self.module.exit_json(**self.result)


def main():
    ''' Create PowerMax host group object and perform action on it
        based on user input from playbook'''
    obj = PowerMaxHostGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
