#!/usr/bin/python
# Copyright: (c) 2019-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: portgroup
version_added: '1.0.0'
short_description:  Manage port groups on PowerMax/VMAX Storage System
description:
- Managing port groups on a PowerMax storage system includes creating a port
  group with a set of ports, adding or removing single or multiple ports to or
  from the port group, renaming the port group and deleting the port group.
extends_documentation_fragment:
  - dellemc.powermax.powermax
  - dellemc.powermax.powermax.powermax_serial_no
author:
- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Ashish Verma (@vermaa31) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
options:
  portgroup_name:
    description:
    - The name of the port group. No Special Character support except for _.
      Case sensitive for REST Calls.
    required: true
    type: str
  ports:
    description:
    - List of directors and ports to be added or removed to or from the port
      group.
    required: false
    type: list
    elements: dict
  port_group_protocol:
    description:
    - Port Group protocol.
    - Required only for V4(Juniper).
    required: false
    choices: [SCSI_FC, iSCSI, NVMe_TCP, NVMe_FC]
    type: str
  new_name:
    description:
    - New name of the port group while renaming. No Special Character support
      except for _. Case sensitive for REST Calls.
    required: false
    type: str
  state:
    description:
    - Define whether the port group should exist or not.
    - present - indicates that the port group should be present on the system.
    - absent - indicates that the port group should not be present on the
               system.
    required: true
    choices: [ absent, present]
    type: str
  port_state:
    description:
    - Define whether the port should be present or absent in the port group.
    - present-in-group - indicates that the ports should be present on a port
      group object.
    - absent-in-group - indicates that the ports should not be present on a
      port group object.
    required: false
    choices: [present-in-group, absent-in-group]
    type: str
'''

EXAMPLES = r'''
- name: Create port group without ports
  dellemc.powermax.portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "{{portgroup_name}}"
    state: "present"

- name: Create port group in V4 without ports
  dellemc.powermax.portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "new_PG"
    port_group_protocol: "SCSI_FC"
    state: "present"

- name: Create port group with ports
  dellemc.powermax.portgroup:
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
  dellemc.powermax.portgroup:
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
  dellemc.powermax.portgroup:
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
  dellemc.powermax.portgroup:
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
  dellemc.powermax.portgroup:
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
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
portgroup_details:
    description: Details of the port group.
    returned: When the port group exist.
    type: list
    contains:
        num_of_masking_views:
            description: Number of masking views in where port group is
                         associated.
            type: int
        num_of_ports:
            description: Number of ports in the port group.
            type: int
        portGroupId:
            description: Port group ID.
            type: str
        symmetrixPortKey:
            description: Symmetrix system director and port in the port group.
            type: list
            contains:
                directorId:
                    description: Director ID of the port.
                    type: str
                portId:
                    description: Port number of the port.
                    type: str
        type:
            description: Type of ports in port group.
            type: str
'''

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('portgroup')

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v3.0.0'


class PortGroup(object):
    """Class with port group operations"""

    u4v_conn = None

    def __init__(self):
        """Define all parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_portgroup_parameters())
        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )
        # result is a dictionary that contains changed status and portgroup
        # details
        self.result = {"changed": False, "portgroup_details": {}}

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

        # Getting PyU4V instance for provisioning on to VMAX
        try:
            self.u4v_conn = utils.get_U4V_connection(
                self.module.params, application_type=APPLICATION_TYPE)
        except Exception as e:
            self.show_error_exit(msg=str(e))
        self.provisioning = self.u4v_conn.provisioning
        self.common = self.u4v_conn.common
        LOG.info('Check Mode flag is %s', self.module.check_mode)
        LOG.info('Got PyU4V instance for provisioning on PowerMax')

    def get_portgroup(self, portgroup_name):
        """Get details of a given port group"""
        try:
            LOG.info('Getting port group %s details', portgroup_name)
            return self.provisioning.get_port_group(portgroup_name)
        except Exception as e:
            LOG.error('Got error %s while getting details of port group %s',
                      str(e), portgroup_name)
            return None

    def create_portgroup(self, portgroup_name):
        """Create port group with given ports"""
        ports = self.module.params['ports']
        port_state = self.module.params['port_state']
        port_group_protocol = self.module.params['port_group_protocol']
        try:
            if port_state and port_state != 'present-in-group':
                self.show_error_exit(msg="Invalid port_state: Ports can only "
                                     "be added while creating portgroup")
            if ports:
                for port in ports:
                    port['directorId'] = port.pop('director_id')
                    port['portId'] = port.pop('port_id')
            LOG.info('Creating port group %s with ports %s',
                     portgroup_name, ports)
            if not self.module.check_mode:
                if utils.is_array_v4():
                    if ports:
                        self.provisioning.\
                            create_new_port_group(portgroup_name, ports, port_group_protocol)
                    else:
                        self.provisioning.\
                            create_empty_port_group(portgroup_name, port_group_protocol)
                else:
                    self.provisioning.\
                        create_multiport_port_group(portgroup_name, ports)
            return True
        except Exception as e:
            self.show_error_exit(msg="Create port group %s failed; error %s"
                                     % (portgroup_name, str(e)))

    def add_ports_to_portgroup(self, portgroup_name):
        """Add ports to existing port group"""

        try:
            existing_ports = ""
            port_group = self.provisioning.get_port_group(portgroup_name)
            if 'symmetrixPortKey' in port_group:
                existing_ports = port_group["symmetrixPortKey"]
            add_ports = self.module.params['ports']
            if add_ports is None or len(add_ports) == 0:
                self.show_error_exit(
                    msg=("List of ports to be added is empty for portgroup "
                         "%s", portgroup_name))
            '''
            Need to iterate through all the input port parameters
            as there is no update method in SDK to change them at once.
            '''
            # changed is true if state is changed and false otherwise
            changed = False
            for port in add_ports:
                add_port_present = check_port_exists(existing_ports, port)
                if not add_port_present:
                    # if port is not already present, then port is added
                    add_port = (port["director_id"], port["port_id"])
                    if not self.module.check_mode:
                        self.provisioning.modify_port_group(portgroup_name,
                                                            add_port=add_port)
                    changed = True
            return changed
        except Exception as e:
            self.show_error_exit(
                msg=('Add port %s to port group %s failed with error %s.' %
                     (port, portgroup_name, str(e))))

    def remove_ports_from_portgroup(self, portgroup_name):
        """Remove ports from portgroup"""

        try:
            port_group = self.provisioning.get_port_group(portgroup_name)
            if 'symmetrixPortKey' not in port_group:
                LOG.info("No ports in portgroup : %s", portgroup_name)
                return False
            existing_ports = port_group["symmetrixPortKey"]
            rem_ports = self.module.params['ports']
            if rem_ports is None or len(rem_ports) == 0:
                self.show_error_exit(msg='List of ports to be removed is '
                                         'empty for portgroup %s'
                                         % portgroup_name)
            '''
            Need to iterate through all the input port parameters
            as there is no update method in SDK to change them at once.
            '''
            # changed is true if state is changed and false otherwise
            changed = False
            for port in rem_ports:
                # Need to check whether the port to be removed is present in
                # port-group
                rem_port_present = check_port_exists(existing_ports, port)
                if rem_port_present:
                    rem_port = (port["director_id"], port["port_id"])
                    if not self.module.check_mode:
                        self.provisioning.modify_port_group(portgroup_name,
                                                            remove_port=rem_port)
                    changed = True
            return changed
        except Exception as e:
            self.show_error_exit(
                msg=('Remove port %s from port group %s failed with error '
                     '%s.' % (port, portgroup_name, str(e))))

    def delete_portgroup(self, portgroup_name):
        """
        Delete port group from system
        A port group cannot be deleted if it is associated with a masking view.
        """
        try:
            if not self.module.check_mode:
                self.provisioning.delete_port_group(portgroup_name)
            return True
        except Exception as e:
            self.show_error_exit(msg='Delete port group %s failed.' %
                                 portgroup_name)

    def modify_portgroup(self, portgroup_name):
        """
        Modify an existing port group
        """
        new_name = self.module.params['new_name']

        if len(new_name) == 0:
            LOG.info(' No new name for port group %s', portgroup_name)
            error_msg = ('Please provide new name for the port group %s',
                         portgroup_name)
            self.show_error_exit(msg=error_msg)
        '''
        Check if current port group name and new port group name
        are same
        '''
        if new_name == portgroup_name:
            LOG.info(' New name is same as current port group %s',
                     portgroup_name)
            return False
        try:
            LOG.info('Renaming port group %s with new name %s',
                     portgroup_name, new_name)
            if not self.module.check_mode:
                self.provisioning.modify_port_group(portgroup_name,
                                                    rename_port_group=new_name)
            return True
        except Exception as e:
            self.show_error_exit(
                msg=('Modify port group %s failed with error %s.' %
                     (portgroup_name, str(e))))

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = ("Failed to close unisphere connection with "
                           "error: %s", str(e))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

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
            LOG.info('Creating port group %s', portgroup_name)
            changed = self.create_portgroup(portgroup_name)
        elif state == 'present' and portgroup and new_name:
            LOG.info('Modifying port group %s', portgroup_name)
            changed_name = self.modify_portgroup(portgroup_name)
            if changed_name:
                if not self.module.check_mode:
                    portgroup_name = new_name
            changed = changed or changed_name
        if state == 'present' and port_state == 'present-in-group' and \
                portgroup:
            LOG.info('Adding ports to port group %s', portgroup_name)
            changed = self.add_ports_to_portgroup(portgroup_name) or changed
        elif state == 'present' and port_state == 'absent-in-group' and \
                portgroup:
            LOG.info(
                'Removing ports from port group %s', portgroup_name)
            changed = self.remove_ports_from_portgroup(
                portgroup_name) or changed
        elif state == 'absent' and portgroup:
            LOG.info('Delete post group %s', portgroup_name)
            changed = self.delete_portgroup(portgroup_name) or changed

        '''
        Finally update the module changed state and saving updated portgroup
        details
        '''
        self.result["changed"] = changed
        if state == 'absent':
            self.result["portgroup_details"] = {}
        else:
            self.result["portgroup_details"] = self.get_portgroup(
                portgroup_name)
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")
        self.module.exit_json(**self.result)


def check_port_exists(existing_ports, port):
    for existing_port in existing_ports:
        if str(str(port["director_id"]) + ':' +
                str(port["port_id"])) == \
                str(str(existing_port["directorId"]) + ':' +
                    str(existing_port["portId"])):
            return True

    return False


def get_portgroup_parameters():
    """This method provide parameter required for the ansible port group modules on PowerMax"""
    return dict(
        portgroup_name=dict(required=True, type='str'),
        ports=dict(required=False, type='list', elements='dict'),
        state=dict(required=True, type='str', choices=['present', 'absent']),
        port_state=dict(required=False, type='str',
                        choices=['present-in-group', 'absent-in-group']),
        port_group_protocol=dict(required=False, type='str',
                                 choices=['SCSI_FC', 'iSCSI', 'NVMe_TCP', 'NVMe_FC']),
        new_name=dict(required=False, type='str')
    )


def main():
    """Create PowerMax port group object and perform action on it
        based on user input from playbook"""
    obj = PortGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
