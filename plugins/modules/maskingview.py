#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: maskingview
version_added: '1.0.0'
short_description:  Managing masking views on PowerMax/VMAX Storage System.
description:
- Managing masking views on PowerMax storage system includes, creating masking
  view with port group, storage group and host or host group, renaming
  masking view and deleting masking view.
- For creating a masking view -
- (i) portgroup_name,
- (ii) sg_name and
- (iii) any one of host_name or hostgroup_name is required.
- All three entities must be present on the array.
- For renaming a masking view, the 'new_mv_name' is required.
  After a masking view is created, only its name can be changed.
  No underlying entity (portgroup, storagegroup, host or hostgroup)
  can be changed on the masking view.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
options:
  mv_name:
    description:
    - The name of the masking view. No Special Character support except for _.
      Case sensitive for REST Calls.
    required: true
    type: str
  portgroup_name:
    description:
    - The name of the existing port group.
    type:  str
  host_name:
    description:
    - The name of the existing host.
      This parameter is to create an exclusive or host export.
    type:  str
  hostgroup_name:
    description:
    - The name of the existing host group. This parameter is used to create
      cluster export.
    type: str
  sg_name:
    description:
    - The name of the existing storage group.
    type: str
  new_mv_name:
    description:
    - The new name for the renaming function. No Special Character support
      except for _. Case sensitive for REST Calls.
    type: str
  state:
    description:
    - Defines whether the masking view should exist or not.
    choices: [ absent, present ]
    required: true
    type: str
'''

EXAMPLES = r'''
- name: Create MV with hostgroup
  dellemc.powermax.maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "{{mv_name}}"
    portgroup_name: "Ansible_Testing_portgroup"
    hostgroup_name: "Ansible_Testing_hostgroup"
    sg_name: "Ansible_Testing_SG"
    state: "present"

- name: Create MV with host
  dellemc.powermax.maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "{{mv_name}}"
    portgroup_name: "Ansible_Testing_portgroup"
    host_name: "Ansible_Testing_host"
    sg_name: "Ansible_Testing_SG"
    state: "present"

- name: Rename host masking view
  dellemc.powermax.maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "{{mv_name}}"
    new_mv_name: "Ansible_Testing_mv_renamed"
    state: "present"

- name: Delete host masking view
  dellemc.powermax.maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "Ansible_Testing_mv_renamed"
    state: "absent"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
create_mv:
    description: Flag sets to true when a new masking view is created.
    returned: When masking view is created.
    type: bool
delete_mv:
    description: Flag sets to true when a masking view is deleted.
    returned: When masking view is deleted.
    type: bool
modify_mv:
    description: Flag sets to true when a masking view is modified.
    returned: When masking view is modified.
    type: bool
mv_details:
    description: Details of masking view.
    returned: When masking view exist.
    type: list
    contains:
        hostId:
            description: Host group present in the masking view.
            type: str
        maskingViewId:
            description: Masking view ID.
            type: str
        portGroupId:
            description: Port group present in the masking view.
            type: str
        storageGroupId:
            description: Storage group present in the masking view.
            type: str
'''

import logging
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('maskingview')
HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class MaskingView(object):
    """Class with masking view operations"""

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_masking_view_parameters())

        mutually_exclusive = [
            ['host_name', 'hostgroup_name']
        ]

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True,
            mutually_exclusive=mutually_exclusive
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
        LOG.info('Check Mode flag is %s', self.module.check_mode)
        LOG.info('Got PyU4V instance for provisioning on PowerMax')

    def get_masking_view(self, mv_name):
        """Get details of a given masking view"""
        try:
            mv_list = self.provisioning.get_masking_view_list()
            if mv_name not in mv_list:
                LOG.info('Masking view %s is not present in system',
                         mv_name)
                return None
            LOG.info('Getting masking view %s details', mv_name)
            return self.provisioning.get_masking_view(mv_name)
        except Exception as e:
            LOG.error('Got error %s while getting details of masking '
                      'view %s', str(e), mv_name)
            return None

    def is_mv_changed(self, mv):

        is_mv_changed = False
        if 'portGroupId' in mv and self.module.params['portgroup_name'] is \
                not None and mv['portGroupId'] != \
                self.module.params['portgroup_name']:
            is_mv_changed = True
        elif 'storageGroupId' in mv and self.module.params['sg_name'] \
                is not None and mv['storageGroupId'] \
                != self.module.params['sg_name']:
            is_mv_changed = True
        elif 'hostId' in mv and self.module.params['host_name'] is not None \
                and mv['hostId'] != self.module.params['host_name']:
            is_mv_changed = True
        elif 'hostGroupId' in mv and self.module.params['hostgroup_name'] \
                is not \
                None and mv['hostGroupId'] != \
                self.module.params['hostgroup_name']:
            is_mv_changed = True
        elif 'hostId' in mv and self.module.params['hostgroup_name'] \
                is not None:
            is_mv_changed = True
        elif 'hostGroupId' in mv and self.module.params['host_name'] \
                is not None:
            is_mv_changed = True
        if is_mv_changed:
            error_message = ('One or more of parameters (PG, SG, '
                             'Host/Host Group) provided for the MV '
                             '%s differ from the state of the MV on the '
                             'array.' % (mv['maskingViewId']))
            self.show_error_exit(msg=error_message)

    def create_masking_view(self, mv_name):
        """Create masking view with given SG, PG and Host(s)"""

        pg_name = self.module.params['portgroup_name']
        sg_name = self.module.params['sg_name']
        host_name = self.module.params['host_name']
        hostgroup_name = self.module.params['hostgroup_name']

        if host_name and hostgroup_name:
            error_message = ('Failed to create masking view %s,'
                             'Please provide either host or '
                             'hostgroup' % mv_name)
            self.show_error_exit(msg=error_message)
            return False
        elif (pg_name is None) or (sg_name is None) or \
                (host_name is None and hostgroup_name is None):
            error_message = ('Failed to create masking view %s, Please '
                             'provide SG, PG and host / host group name to '
                             'create masking view', mv_name)
            self.show_error_exit(msg=error_message)
            return False

        try:
            resp = {}
            LOG.info('Creating masking view %s... ', mv_name)
            if not self.module.check_mode:
                resp = self.provisioning.create_masking_view_existing_components(
                    port_group_name=pg_name, masking_view_name=mv_name,
                    storage_group_name=sg_name, host_name=host_name,
                    host_group_name=hostgroup_name)
            return True, resp
        except Exception as e:
            self.show_error_exit(msg='Create masking view %s failed; error '
                                     '%s' % (mv_name, str(e)))

    def delete_masking_view(self, mv_name):
        """Delete masking view from system"""
        try:
            if not self.module.check_mode:
                self.provisioning.delete_masking_view(mv_name)
            return True
        except Exception as e:
            self.show_error_exit(msg='Delete masking view %s failed with '
                                     'error %s.' % (mv_name, str(e)))

    def rename_masking_view(self, mv_name, new_mv_name):
        """Rename existing masking view with given name"""
        changed = False
        if mv_name == new_mv_name:
            return changed
        try:
            if not self.module.check_mode:
                self.provisioning.rename_masking_view(mv_name, new_mv_name)
            changed = True
        except Exception as e:
            self.show_error_exit(msg='Rename masking view %s failed '
                                 'with error %s.' % (mv_name, str(e)))
        return changed

    def validate_host(self, host_name):
        try:
            hosts = self.provisioning.get_host_list()
            return True if hosts and host_name in hosts else False
        except Exception as e:
            self.show_error_exit(msg='Getting list of hosts failed '
                                 'with error %s' % str(e))

    def validate_hostgroup(self, hostgroup_name):
        try:
            hostGroups = self.provisioning.get_host_group_list()
            return True if hostGroups and hostgroup_name in hostGroups \
                else False
        except Exception as e:
            self.show_error_exit(msg='Getting list of host groups '
                                 'failed with error %s' % str(e))

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = ("Failed to close unisphere connection with error:"
                           " %s" % (str(e)))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def validate_host_params(self):
        host_name = self.module.params['host_name']
        hostgroup_name = self.module.params['hostgroup_name']
        if host_name and not self.validate_host(host_name):
            self.show_error_exit('Host %s does not exist' % host_name)
        if hostgroup_name and not self.validate_hostgroup(hostgroup_name):
            self.show_error_exit('Host Group %s does not exist'
                                 % hostgroup_name)

    def perform_module_operation(self):
        """
        Perform different actions on masking view based on user parameter
        chosen in playbook
        """
        state = self.module.params['state']
        mv_name = self.module.params['mv_name']
        new_mv_name = self.module.params['new_mv_name']

        self.validate_host_params()
        masking_view = self.get_masking_view(mv_name)
        if masking_view is not None:
            self.is_mv_changed(masking_view)

        result = dict(
            changed=False,
            create_mv='',
            modify_mv='',
            delete_mv='',
        )

        if state == 'present' and not masking_view and not new_mv_name \
                and mv_name:
            LOG.info('Creating masking view %s', mv_name)
            result['create_mv'], result['mv_details'] = \
                self.create_masking_view(mv_name)

        if state == 'present' and masking_view and new_mv_name:
            LOG.info('Renaming masking view %s', mv_name)
            result['modify_mv'] = self.rename_masking_view(mv_name,
                                                           new_mv_name)
            if not self.module.check_mode:
                mv_name = new_mv_name

        if state == 'absent' and masking_view:
            LOG.info('Delete masking view %s', mv_name)
            result['delete_mv'] = self.delete_masking_view(mv_name)

        if state == 'present' and masking_view:
            updated_mv = self.get_masking_view(mv_name)
            result['mv_details'] = updated_mv

        if result['create_mv'] or result['modify_mv'] or \
                result['delete_mv']:
            result['changed'] = True

        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")

        # Finally update the module changed state!!!
        self.module.exit_json(**result)


def get_masking_view_parameters():
    """This method provides the parameters required for ansible
    masking view module"""
    return dict(
        mv_name=dict(required=True, type='str'),
        portgroup_name=dict(required=False, type='str'),
        host_name=dict(required=False, type='str'),
        hostgroup_name=dict(required=False, type='str'),
        sg_name=dict(required=False, type='str'),
        new_mv_name=dict(required=False, type='str'),
        state=dict(required=True, choices=['present', 'absent'], type='str')
    )


def main():
    """Create PowerMax masking view object and perform action on it
        based on user input from playbook"""
    obj = MaskingView()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
