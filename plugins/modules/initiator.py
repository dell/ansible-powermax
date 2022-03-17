#!/usr/bin/python
# Copyright: (c) 2022, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: initiator
version_added: '1.7.0'
short_description:  Manage initiators on PowerMax/VMAX Storage System
description:
- Managing initiators on a PowerMax storage system includes retrieving details
  and renaming alias of an initiator.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Jennifer John (@johnj9) <ansible.team@dell.com>

options:
  initiator_id:
    description:
    - The initiator WWN or IQN.
    type: str
  alias:
    description:
    - Alias of initiator.
    type: str
  new_alias:
    description: Rename alias for specified initiator.
    type: dict
    suboptions:
        new_node_name:
            description: The new node name to rename the initiator alias.
            type: str
        new_port_name:
            description: The new port name to rename the initiator alias.
            type: str
  state:
    description:
    - The state of the initiator after the task is performed.
    - absent - indicates that the initiator should not exist in the system.
    - present - indicates that the initiator should exist in the system.
    required: true
    choices: [absent, present]
    type: str
notes:
  - initiator_id and alias are mutually exclusive parameters.
'''

EXAMPLES = r'''
- name: Get initiator details using initiator id
  dellemc.powermax.initiator:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    initiator_id: 1000000000000001
    state: 'present'

- name: Get initiator details using alias
  dellemc.powermax.initiator:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    alias: 'test/host_initiator'
    state: 'present'

- name: Rename initiator alias using initiator id
  dellemc.powermax.initiator:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    initiator_id: 1000000000000001
    new_alias:
      new_node_name: 'test_rename'
      new_port_name: 'host_initiator_rename'
    state: 'present'

- name: Rename initiator alias using alias
  dellemc.powermax.initiator:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    alias: 'test/host_initiator'
    new_alias:
      new_node_name: 'test_rename'
      new_port_name: 'host_initiator_rename'
    state: 'present'
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
initiator_details:
    description: Details of the initiator.
    returned: When initiator exists.
    type: complex
    contains:
        initiatorId:
            description: ID of the initiator.
            type: str
        alias:
            description: Initiator alias.
            type: str
        fabric_name:
            description: Fabric associated with the initiator.
            type: str
        fcid:
            description: FCID associated with the initiator.
            type: str
        host:
            description: Host associated with the initiator.
            type: str
        hostGroup:
            description: Host groups associated with the initiator.
            type: list
        logged_in:
            description: States whether the initiator is logged in.
            type: bool
'''

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('initiator')

HAS_PYU4V = utils.has_pyu4v_sdk()
PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class Initiator(object):
    '''Class with initiator operations'''
    u4v_conn = None

    def __init__(self):
        ''' Define all parameters required by this module'''
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_initiator_parameters())
        mutually_exclusive = [['initiator_id', 'alias']]
        required_one_of = [
            ['initiator_id', 'alias']
        ]
        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            mutually_exclusive=mutually_exclusive,
            required_one_of=required_one_of
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
        LOG.info('Got PyU4V instance for provisioning on PowerMax ')

    def get_initiator_details(self, initiator_id, alias):
        """
        Retrieve initiator details based on initiator id or alias
        """
        params = None
        initiator_details = None
        if initiator_id is not None:
            self.validate_initiator(initiator_id, 'initiator_id')
            params = {"initiator_hba": initiator_id}
        if alias is not None:
            self.validate_initiator(alias, 'alias')
            params = {"alias": alias}
        try:
            initiator_ids = self.provisioning.get_initiator_list(params)
            if not initiator_ids:
                error_msg = ('Initiator %s is not found' % (initiator_id or alias))
                self.show_error_exit(msg=error_msg)
            initiator_id = initiator_ids[0]

            if initiator_id:
                initiator_details = \
                    self.provisioning.get_initiator(initiator_id)
            return initiator_id, initiator_details
        except Exception as e:
            err_msg = ("Retrieving initiator details failed with error:"
                       " %s" % str(e))
            LOG.error(err_msg)
            self.show_error_exit(msg=err_msg)

    def rename_initiator_alias(self, initiator_id, initiator_details,
                               new_alias):
        """
        Rename initiator alias
        """
        alias = None
        alias_params = None
        new_alias, error_msg = validate_alias(new_alias, initiator_details)
        if error_msg:
            self.show_error_exit(msg=error_msg)
        if 'alias' in initiator_details:
            alias = initiator_details['alias'].split('/')
            alias = (alias[0], alias[1])
            alias_params = ((new_alias['new_node_name'] or alias[0]),
                            (new_alias['new_port_name'] or alias[1]))
        else:
            if new_alias['new_node_name'] and new_alias['new_port_name']:
                alias_params = (new_alias['new_node_name'],
                                new_alias['new_port_name'])
        if (alias and alias != alias_params) or \
                (not alias and alias_params):
            try:
                self.provisioning.modify_initiator(initiator_id,
                                                   rename_alias=alias_params)
                return True, "/".join(alias_params)
            except Exception as e:
                err_msg = ("Modifying initiator alias failed with error:"
                           " %s" % str(e))
                LOG.error(err_msg)
                self.show_error_exit(msg=err_msg)

        return False, None

    def validate_initiator(self, id_or_alias, key):
        if len(id_or_alias.strip()) == 0:
            self.show_error_exit(msg=('Please enter a valid %s' % key))

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s",
                         self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = ("Failed to close unisphere connection with error:"
                           " %s" % str(e))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        '''
        Perform different actions on host based on user parameter
        chosen in playbook
        '''
        initiator_id = self.module.params['initiator_id']
        alias = self.module.params['alias']
        new_alias = self.module.params['new_alias']
        state = self.module.params['state']
        result = dict(
            changed=False,
            initiator_details=[]
        )

        if state == 'absent':
            error_message = 'Deletion of initiators is not allowed through' \
                            ' Ansible module'
            self.show_error_exit(msg=error_message)

        initiator_id, initiator_details = \
            self.get_initiator_details(initiator_id, alias)

        if initiator_details and new_alias:
            # perform rename
            result['changed'], alias = \
                self.rename_initiator_alias(initiator_id, initiator_details,
                                            new_alias)

        if result['changed']:
            initiator_id, initiator_details = \
                self.get_initiator_details(initiator_id, alias)

        result['initiator_details'] = initiator_details
        self.module.exit_json(**result)


def get_initiator_parameters():
    return dict(
        initiator_id=dict(required=False, type='str'),
        alias=dict(required=False, type='str'),
        new_alias=dict(required=False, type='dict', options=dict(
            new_node_name=dict(type='str', required=False),
            new_port_name=dict(type='str', required=False)
        )),
        state=dict(required=True, type='str', choices=['present',
                                                       'absent']),
    )


def validate_alias(new_alias, initiator_details):
    """Validates initiator alias"""
    error_msg = None
    keys = ['new_node_name', 'new_port_name']
    for key in keys:
        if new_alias[key] is not None:
            if utils.is_empty(new_alias[key]):
                return new_alias, 'Please specify %s' % key
            if new_alias[key].strip() == 'None':
                new_alias[key] = None

    if 'alias' not in initiator_details:
        if new_alias['new_port_name'] and not new_alias['new_node_name']:
            error_msg = 'Please specify new_node_name'
        elif new_alias['new_node_name'] and not new_alias['new_port_name']:
            error_msg = 'Please specify new_port_name'

    return new_alias, error_msg


def main():
    ''' Create PowerMax initiator object and perform action on it
        based on user input from playbook'''
    obj = Initiator()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
