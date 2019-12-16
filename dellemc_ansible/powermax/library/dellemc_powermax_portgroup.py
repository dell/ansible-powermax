#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_portgroup
version_added: '2.6'
short_description:  Manage port groups on PowerMax/VMAX Storage System
description:
- Managing port groups on PowerMax Storage System includes create port group 
  with set of ports, add/remove single or multiple ports to/from port group, 
  rename port group and delete port group
extends_documentation_fragment:
  - dellemc.dellemc_powermax
author:
- Vasudevu Lakhinana (Vasudevu.Lakhinana@dell.com)
- Ashish Verma (Ashish.Verma1@emc.com)
- Rajshree Khare (Rajshree.Khare@emc.com)
options:
  portgroup_name:
    description:
    - The name of the port group. No Special Character support except for _.
      Case sensitive for REST Calls.
    required: true
  ports:
    description:
    - List of Directors and Ports to be added or removed to/from the Port Group
  new_name:
      description:
      - New name of the port group while renaming. No Special Character support
        except for _. Case sensitive for REST Calls.
      required: false
  state:
    description:
    - Define whether the port group should exist or not.
    - present - indicates that the port group should be present on system
    - absent - indicates that the port group should not be present on system
    required: true
    choices: [ absent, present]
  port_state:
    description:
    - Define whether the port should be present or absent in port group.
    - present-in-group - indicates that the ports should be present on port
      group object
    - absent-in-group - indicates that the ports should not be present on port
      group object
    choices: [present-in-group, absent-in-group]
  '''

EXAMPLES = r'''
  - name: Create port group without ports
    dellemc_powermax_portgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{array_id}}"
      portgroup_name: "{{portgroup_name}}"
      state: "present"

  - name: Create port group with ports
    dellemc_powermax_portgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{array_id}}"
      portgroup_name: "{{portgroup_name}}"
      state: "present"
      ports:
      - director_id: "FA-1D"
        port_id: "5"
      - director_id: "FA-2D"
        port_id: "5"
      port_state: "present-in-group"

  - name: Add ports to port group
    dellemc_powermax_portgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{array_id}}"
      portgroup_name: "{{portgroup_name}}"
      state: "present"
      ports:
      - director_id: "FA-2D"
        port_id: "8"
      - director_id: "FA-2D"
        port_id: "9"
      port_state: "present-in-group"

  - name: Remove ports from port group
    dellemc_powermax_portgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{array_id}}"
      portgroup_name: "{{portgroup_name}}"
      state: "present"
      ports:
      - director_id: "FA-2D"
        port_id: "8"
      - director_id: "FA-2D"
        port_id: "9"
      port_state: "absent-in-group"

  - name: Modify port group
    dellemc_powermax_portgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{array_id}}"
      portgroup_name: "{{portgroup_name}}"
      state: "present"
      new_name: "{{new_name}}"

  - name: Delete port group
    dellemc_powermax_portgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{array_id}}"
      portgroup_name: "{{portgroup_name}}"
      state: "absent"
'''

RETURN = r'''
'''

LOG = utils.get_logger('dellemc_powermax_portgroup', log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.1'

class PowerMaxPortGroup(object):
    """Class with port group operations"""

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_powermax_portgroup_parameters())
        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )
        # result is a dictionary that contains changed status and portgroup details
        self.result = {"changed": False, "portgroup_details": {}}

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

        # Getting PyU4V instance for provisioning on to VMAX
        self.u4v_conn = utils.get_U4V_connection(self.module.params,
                                                 application_type=
                                                 APPLICATION_TYPE
                                                 )
        self.provisioning = self.u4v_conn.provisioning
        LOG.info('Got PyU4V instance for provisioning on PowerMax')

    def get_portgroup(self, portgroup_name):
        """Get details of a given port group"""
        try:
            LOG.info('Getting port group {0} details'.format(portgroup_name))
            return self.provisioning.get_portgroup(portgroup_name)
        except Exception as e:
            LOG.error('Got error {0} while getting details of port group {0}'
                      .format(str(e), portgroup_name))
            return None

    def create_portgroup(self, portgroup_name):
        """Create port group with given ports"""

        ports = self.module.params['ports']
        port_state = self.module.params['port_state']
        try:
            if port_state and port_state != 'present-in-group':
                self.module.fail_json(msg="Invalid port_state: Ports can only "
                                      "be added while creating portgroup")
            if ports:
                for port in ports:
                    port['directorId'] = port.pop('director_id')
                    port['portId'] = port.pop('port_id')
            LOG.info('Creating port group {0} with ports {1}'.format(
                    portgroup_name, ports))
            self.provisioning.create_multiport_portgroup(portgroup_name, ports)
            return True
        except Exception as e:
            LOG.error('Failed to create port group {0} with error {1}'
                      .format(portgroup_name, str(e)))
            self.module.fail_json(msg='Create port group {0} failed; error {1}'
                                  .format(portgroup_name, str(e)))

    def _get_add_ports(self, existing, ports):
        add_ports = []
        if ports is not None:
            add_ports = {key: ports[key] for key in ports
                         if key in existing and ports[key] != existing[key]}
            LOG.debug(' {0} Ports to be added to port group '
                      .format(add_ports))
        return add_ports

    def _get_rem_ports(self, existing, ports):
        rem_ports = []
        if ports is not None:
            rem_ports = {key: ports[key] for key in ports
                         if key in existing and ports[key] == existing[key]}
            LOG.debug(' {0} Ports to be removed from port group'
                      .format(rem_ports))
        return rem_ports

    def add_ports_to_portgroup(self, portgroup_name):
        """Add ports to existing port group"""

        existing_ports = self.provisioning.get_ports_from_pg(portgroup_name)
        add_ports = self.module.params['ports']
        if add_ports is None or len(add_ports) == 0:
            LOG.info(' No Ports to be added to port group  {0}'.format(
                    portgroup_name))
            self.module.fail_json(msg="List of ports to be added is empty for"
                                  "portgroup {0}".format(portgroup_name))
        try:
            '''
            Need to iterate through all the input port parameters
            as there is no update method in SDK to change them at once.
            '''
            # changed is true if state is changed and false otherwise
            changed = False
            for port in add_ports:
                add_port = (port["director_id"], port["port_id"])
                add_port_present = False
                for existing_port in existing_ports:
                    if str(str(port["director_id"]) + ':' + str(port["port_id"])) == str(existing_port):
                        add_port_present = True
                if not add_port_present:
                    # if port is not already present, then port is added
                    self.provisioning.modify_portgroup(portgroup_name,
                                                       add_port=add_port)
                    changed = True
            return changed
        except Exception as e:
            LOG.error('Add port {0} to port group {1} failed with error {2}'
                      .format(port, portgroup_name, str(e)))
            self.module.fail_json(msg='Add port {0} to port group {1} failed with error {2}.'
                                  .format(port, portgroup_name, str(e)))

    def remove_ports_from_portgroup(self, portgroup_name):
        """Remove ports from portgroup"""

        existing_ports = self.provisioning.get_ports_from_pg(portgroup_name)
        rem_ports = self.module.params['ports']
        if rem_ports is None or len(rem_ports) == 0:
            LOG.info('No ports to remove from port group {0}'.format(portgroup_name))
            self.module.fail_json(msg='List of ports to be removed is empty for portgroup {0}'.format(portgroup_name))
        try:
            '''
            Need to iterate through all the input port parameters
            as there is no update method in SDK to change them at once.
            '''
            # changed is true if state is changed and false otherwise
            changed = False
            for port in rem_ports:
                rem_port = (port["director_id"], port["port_id"])
                # Need to check whether the port to be removed is present in port-group
                rem_port_present = False
                for existing_port in existing_ports:
                    if str(str(port["director_id"]) + ':' + str(port["port_id"])) == str(existing_port):
                        rem_port_present = True
                if rem_port_present:
                    self.provisioning.modify_portgroup(portgroup_name,
                                                       remove_port=rem_port)
                    changed = True
            return changed
        except Exception as e:
            LOG.error('Remove port {0} from port group {1} failed with error {2}'
                      .format(port, portgroup_name, str(e)))
            self.module.fail_json(msg='Remove port {0} from port group {1} failed with error {2}.'
                                  .format(port, portgroup_name, str(e)))

    def delete_portgroup(self, portgroup_name):
        """
        Delete port group from system
        A port group cannot be deleted if it is associated with a masking view.
        """
        try:
            self.provisioning.delete_portgroup(portgroup_name)
            return True
        except Exception as e:
            LOG.error('Delete port group {0} failed with error {1} '
                      .format(portgroup_name, str(e)))
            self.module.fail_json(msg='Delete port group {0} failed.'
                                  .format(portgroup_name))

    def modify_portgroup(self, portgroup_name):
        """
        Modify an existing port group
        """
        new_name = self.module.params['new_name']

        if len(new_name) == 0:
            LOG.info(' No new name for port group {0}'
                     .format(portgroup_name))
            error_msg = 'Please provide new name for the port group {0}' \
                .format(portgroup_name)
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        '''
        Check if current port group name and new port group name
        are same
        '''
        if new_name == portgroup_name:
            LOG.info(' New name is same as current port group {0}'
                     .format(portgroup_name))
            return False
        try:
            LOG.info('Renaming port group {0} with new name {1}'
                     .format(portgroup_name, new_name))
            self.provisioning.modify_portgroup(portgroup_name,
                                               rename_portgroup=new_name)
            return True
        except Exception as e:
            LOG.error('Modifying port group {0} failed with error {1}'
                      .format(portgroup_name, str(e)))
            self.module.fail_json(msg='Modify port group {0} failed with error {1}.'
                                  .format(portgroup_name, str(e)))

    def perform_module_operation(self):
        """
        Perform different actions on port group based on user parameter
        chosen in playbook
        """
        state = self.module.params['state']
        port_state = self.module.params['port_state']
        portgroup_name = self.module.params['portgroup_name']
        new_name = self.module.params['new_name']

        portgroup = self.get_portgroup(portgroup_name)
        changed = False
        if state == 'present' and not portgroup and \
                portgroup_name and not new_name:
            LOG.info('Creating port group {0}'.format(portgroup_name))
            changed = self.create_portgroup(portgroup_name)
        elif state == 'present' and portgroup and new_name:
            LOG.info('Modifying port group {0}'.format(portgroup_name))
            changed_name = self.modify_portgroup(portgroup_name)
            if changed_name:
                portgroup_name = new_name
            changed = changed or changed_name
        if state == 'present' and port_state == 'present-in-group' and \
                portgroup:
            LOG.info('Adding ports to port group {0}'.format(portgroup_name))
            changed = self.add_ports_to_portgroup(portgroup_name) or changed
        elif state == 'present' and port_state == 'absent-in-group' and \
                portgroup:
            LOG.info('Removing ports from port group {0}'.format(portgroup_name))
            changed = self.remove_ports_from_portgroup(portgroup_name) or changed
        elif state == 'absent' and portgroup:
            LOG.info('Delete post group {0} '.format(portgroup_name))
            changed = self.delete_portgroup(portgroup_name) or changed

        '''
        Finally update the module changed state and saving updated portgroup
        details
        '''
        self.result["changed"] = changed
        if state == 'absent':
            del self.result["portgroup_details"]
        else:
            self.result["portgroup_details"] = self.get_portgroup(portgroup_name)
        self.module.exit_json(**self.result)


def get_powermax_portgroup_parameters():
    """This method provide parameter required for the ansible port group modules on PowerMax"""
    return dict(
        portgroup_name=dict(required=True, type='str'),
        ports=dict(required=False, type='list'),
        state=dict(required=True, type='str'),
        port_state=dict(required=False, type='str'),
        new_name=dict(required=False, type='str')
        )


def main():
    """Create PowerMax port group object and perform action on it
        based on user input from playbook"""
    obj = PowerMaxPortGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
