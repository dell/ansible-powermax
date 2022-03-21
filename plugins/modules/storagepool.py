#!/usr/bin/python
# Copyright: (c) 2021, Dell EMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: storagepool

version_added: '1.5.0'

short_description: Manage storage pools on PowerMax/VMAX storage system

description:
- Managing storage pools on PowerMax storage system includes getting details
  of storage pools.

extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no

author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>

options:
  pool:
    description:
    - The name of the storage pool.
    required: True
    type: str

  state:
    description:
    - State variable to determine whether storage pool will exist or not.
    required: True
    type: str
    choices: ['absent', 'present']
'''

EXAMPLES = r'''
- name: Get specific storage pool details
  dellemc.powermax.storagepool:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    pool: "SRP_1"
    state: "present"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
pool_details:
    description: Details of the storage pool.
    returned: When storage pool exist.
    type: complex
    contains:
        serial_no:
           description: The PowerMax array on which storage pool resides
           type: str
        service_levels:
            description: The service levels supported by storage pool
            type: list
        srpId:
           description: The ID of the storage pool
           type: str
        srp_capacity:
            description: SRP capacity details
            type: complex
            contains:
                effective_used_capacity_percent:
                    description: The effective used capacity, expressed as a percentage
                    type: int
                usable_total_tb:
                    description: Usable capacity of the storage pool in TB
                    type: float
                usable_used_tb:
                    description: Used capacity of the storage pool in TB
                    type: float
        srp_efficiency:
            description: SRP efficiency details
            type: complex
            contains:
                compression_state:
                    description: Indicates whether compression is enabled or
                                 disabled for this storage resource pool.
                    type: str
        total_free_tb:
           description: Free capacity of the storage pool in TB
           type: str
'''

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule
import logging

LOG = utils.get_logger('storagepool')
HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class Pool(object):
    """Class with storage pool operations"""

    def __init__(self):
        """ Define all parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_pool_parameters())

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
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
        LOG.info('Got PyU4V instance for provisioning on to VMAX ')

    def get_pool(self, pool_id):
        """
        Get the details of pool
        """
        error_message = "Failed to get details of storage pool {0} with " \
                        "error {1}"
        try:
            pool_details = self.provisioning.get_srp(srp=pool_id)

            if 'serial_no' in self.module.params:
                pool_details['serial_no'] = self.module.params['serial_no']
            if 'usable_total_tb' in pool_details['srp_capacity'] and \
                    'usable_used_tb' in pool_details['srp_capacity']:
                pool_details['total_free_tb'] = \
                    pool_details['srp_capacity']['usable_total_tb'] - \
                    pool_details['srp_capacity']['usable_used_tb']

            LOG.debug("Pool details: %s", pool_details)
            return pool_details
        except utils.ResourceNotFoundException as e:
            error_message = error_message.format(pool_id, str(e))
            LOG.error(error_message)
            return None
        except Exception as e:
            error_message = error_message.format(pool_id, str(e))
            self.show_error_exit(msg=error_message)

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
        """
        Perform different actions on storage pool based on user parameter
        chosen in playbook
        """

        pool = self.module.params['pool']
        state = self.module.params['state']

        # result is a dictionary that contains changed status and storage
        # pool details
        result = dict(
            changed=False,
            pool_details=None
        )

        if pool is None or len(pool.strip()) == 0:
            error_message = 'Please provide valid storage pool.'
            self.show_error_exit(error_message)

        pool_details = self.get_pool(pool)

        if state == 'present' and not pool_details:
            error_message = 'Storage pool {0} not found - Creation of ' \
                            'storage pool is not allowed through Ansible ' \
                            'module'.format(pool)
            LOG.error(error_message)
            self.show_error_exit(msg=error_message)

        if state == 'absent' and pool_details:
            error_message = 'Deletion of storage pool is not allowed ' \
                            'through Ansible module'
            LOG.error(error_message)
            self.show_error_exit(msg=error_message)

        result['pool_details'] = pool_details
        self.module.exit_json(**result)


def get_pool_parameters():
    """This method provide parameter required for the ansible pool
    modules on PowerMax"""
    return dict(
        pool=dict(required=True, type='str'),
        state=dict(required=True, type='str', choices=['absent', 'present'])
    )


def main():
    """ Create PowerMax storage pool object and perform action on it
        based on user input from playbook"""
    obj = Pool()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
