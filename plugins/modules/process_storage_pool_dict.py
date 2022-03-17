#!/usr/bin/python
# Copyright: (c) 2021, Dell EMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: process_storage_pool_dict

version_added: '1.5.0'

short_description: Process storage pools on PowerMax/VMAX Storage System

description:
- Process storage pools on PowerMax/VMAX storage system to find out the
  storage pool with maximum free storage.

extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax

author:
- Akash Shendge (@shenda1) <ansible.team@dell.com>

options:
  pool_data:
    description:
    - Storage pool details including service levels, usable total space,
      usable free space, total free space.
    elements: dict
    required: True
    type: list

  size:
    description:
    - Size of the storage group in GB.
    required: True
    type: float

  sg_name:
    description:
    - Name of the storage group.
    type: str

  service_level:
    description:
    - Service level of the storage group.
    type: str
'''

EXAMPLES = r'''
- name: Get best suitable Pool using our python sorting module
  register: assigned_pool
  dellemc.powermax.process_storage_pool_dict:
    unispherehost: "{{unispherehost}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    pool_data: "{{ pools_list }}"
    size: 40
    service_level: "Diamond"
    sg_name: "intellgent_provisioning"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool

serial_no:
    description: The PowerMax array on which storage pool resides
    returned: when array satisfies the given criteria
    type: str

storage_pool:
    description: The ID of the storage pool
    returned: when storage pool exists satisfying the given criteria
    type: str

storage_group:
    description: Name of the storage group
    returned: when storage group exists satisfying the given criteria
    type: str

all_pools:
    description: List of all pools on unisphere
    returned: when pool exists
    type: list
    contains:
        serial_no:
            description: The PowerMax array on which storage pool resides
            returned: when array satisfies the given criteria
            type: str
        storage_pool:
            description: The ID of the storage pool
            returned: when storage pool exists satisfying the given criteria
            type: str
'''

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('process_storage_pool_dict')

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class ProcessPoolDict(object):
    """Class for performing various search or sort operations on list of
       storage pool dictionary  """

    def __init__(self):
        """ Define all parameters required by this module"""

        self.module_params = utils.get_u4v_unisphere_connection_parameters()
        self.module_params.update(get_process_dict_parameters())

        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )

        # result is a dictionary that contains changed status, storage pool,
        # storage group and serial number
        self.result = dict(
            changed=False,
            storage_pool=None,
            storage_group=None,
            serial_no=None
        )

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

    def get_connection(self, serial_no):
        """ Get the PowerMax connection object """

        try:
            self.u4v_conn = utils.get_u4v_unisphere_connection(
                self.module.params)
            self.provisioning = self.u4v_conn.provisioning
            self.u4v_conn.set_array_id(serial_no)
        except Exception as e:
            self.show_error_exit(msg=str(e))

    def get_sg_details(self, sg_name):
        """ Get the storage group details """

        try:
            return self.u4v_conn.provisioning.get_storage_group(sg_name)
        except Exception as e:
            error_msg = "Failed to get storage group {0} details".format(
                sg_name)
            LOG.error(error_msg)
            return None

    def get_srp_list(self):
        """ Get the list of storage resource pools """

        try:
            return self.u4v_conn.provisioning.get_srp_list()
        except Exception as e:
            error_msg = "Failed to get storage pool"
            LOG.error(error_msg)
            self.show_error_exit(error_msg)

    def check_sg_multiple_occurrence(self, storage_pool_list, sg_name):
        """ Check if storage group exist on multiple PowerMax arrays """

        count = 0
        for pool in storage_pool_list:
            self.get_connection(pool['serial_no'])
            srp_list = self.get_srp_list()
            for srp in srp_list:
                params = {"storageGroupId": sg_name, "srp": srp}
                sg_list = self.u4v_conn.provisioning.get_storage_group_list(
                    params)
                if len(sg_list) >= 1:
                    count += len(sg_list)
                if count > 1:
                    msg = "Storage group {0} exists on multiple " \
                          "arrays".format(sg_name)
                    self.show_error_exit(msg)

    def verify_idempotency(self, storage_pool_list, sg_name, size, service_level=None):
        """ Check for the idempotency of storage group along with size """

        # Iterate through existing serial numbers on Unisphere
        for pool in storage_pool_list:
            self.get_connection(pool['serial_no'])
            srp_list = self.u4v_conn.provisioning.get_srp_list()
            LOG.info("serial_no: %s srp: %s", pool['serial_no'], srp_list)
            # Iterate through existing SRPs on particular serial number
            for srp in srp_list:
                srp_data = self.u4v_conn.provisioning.get_srp(srp)
                # Check if storage pool supports given service level
                if service_level and service_level != "" and service_level \
                        not in srp_data['service_levels']:
                    continue
                sg_dict = self.get_sg_details(sg_name)

                # Check if existing storage group size is >= given size
                if sg_dict and sg_dict['cap_gb'] >= size:
                    self.result['serial_no'] = pool['serial_no']
                    self.result['storage_pool'] = srp
                    self.result['storage_group'] = sg_name
                # Check if existing storage group size is < given size
                elif sg_dict and sg_dict['cap_gb'] < size:
                    if "usable_total_tb" in srp_data['srp_capacity'] \
                            and "usable_used_tb" in srp_data['srp_capacity']:
                        total_free_tb = srp_data['srp_capacity']['usable_total_tb'] - srp_data['srp_capacity']['usable_used_tb']
                        total_free_gb = total_free_tb * 1024
                        required_size = size - sg_dict['cap_gb']
                        LOG.info("Free Size: %s, Required Size: %s",
                                 total_free_gb, required_size)
                        if total_free_gb >= required_size:
                            self.result['serial_no'] = pool['serial_no']
                            self.result['storage_pool'] = srp
                            self.result['storage_group'] = sg_name
                        else:
                            error_msg = "The requested size is not " \
                                        "available on the array."
                            LOG.error(error_msg)
                            self.show_error_exit(msg=error_msg)

        if not self.result['serial_no']:
            self.result['serial_no'] = "NOT_FOUND"

    def perform_module_operation(self):
        """
        Perform different actions on ansible list of dict based on user
        parameter chosen in playbook
        """
        pool_data = self.module.params['pool_data']
        size = self.module.params['size']
        service_level = self.module.params['service_level']
        sg_name = self.module.params['sg_name']
        sg_details = None

        if size is not None and size == 0:
            self.module.fail_json(msg="Size can not be 0 (Zero)")

        if sg_name is not None:
            if len(sg_name.strip()) == 0:
                self.show_error_exit(msg="Please provide valid storage "
                                         "group name.")

            for pool in pool_data:
                self.get_connection(pool['serial_no'])
                sg_details = self.get_sg_details(sg_name)
                if sg_details:
                    break

        if sg_details:
            self.check_sg_multiple_occurrence(pool_data, sg_name)
            self.verify_idempotency(pool_data, sg_name, size, service_level)
        else:
            pool_details, all_pools = process_data(pool_data, size,
                                                   service_level)
            if pool_details == "NOT_FOUND":
                self.result['serial_no'] = "NOT_FOUND"
            else:
                self.result['serial_no'] = pool_details['serial_no']
                self.result['storage_pool'] = pool_details['srpId']
            self.result['all_pools'] = all_pools
        self.module.exit_json(**self.result)


def process_data(storage_pool_list, size, service_level=None):

    best_fit_pool = {}
    all_pools = []

    LOG.info("Before Sorting: %s", storage_pool_list)
    if storage_pool_list:
        # sorting a list of storage pool dict based on pool used
        # capacity percent
        storage_pool_list.sort(key=sort_capacity)
    LOG.info("After Sorting: %s", storage_pool_list)

    for pool in storage_pool_list:
        all_pools.append(pool)
    LOG.info("All pools on unisphere: %s", all_pools)

    for pool in storage_pool_list:
        # this module always gets the size in GB & pool size is in TB
        # so convert it to GB before compare
        if (pool['total_free_tb'] * 1024) >= size:
            if service_level and service_level != "" and service_level \
                    not in pool['service_levels']:
                continue
            best_fit_pool['serial_no'] = pool['serial_no']
            best_fit_pool['srpId'] = pool['srpId']
            break

    LOG.info("Best suitable pool: %s", best_fit_pool)

    if not best_fit_pool:
        best_fit_pool = "NOT_FOUND"
    LOG.info("final output: %s", best_fit_pool)
    return best_fit_pool, all_pools


def get_process_dict_parameters():
    """This method provide parameter required by this modules"""
    return dict(
        pool_data=dict(type='list', elements='dict', required=True),
        size=dict(type='float', required=True),
        service_level=dict(),
        sg_name=dict()
    )


def sort_capacity(e):
    return e['srp_capacity']['effective_used_capacity_percent']


def main():
    """ Create PowerMax storage pool object and perform action on it
        based on user input from playbook"""
    obj = ProcessPoolDict()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
