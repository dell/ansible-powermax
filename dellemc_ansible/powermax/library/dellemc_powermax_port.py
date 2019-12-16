#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {"metadata_version": "1.1",
                    "status": ["preview"],
                    "supported_by": "community"
                    }

DOCUMENTATION = r"""
---
module: dellemc_powermax_port
version_added: '2.6'
short_description:  Manage ports on PowerMax/VMAX Storage System
description:
- Managing ports on PowerMax Storage System includes getting details of a port
extends_documentation_fragment:
  - dellemc.dellemc_powermax
author:
- Ashish Verma (Ashish.Verma1@emc.com)
options:
  ports:
    description:
    - List of port's director and port id
    required: true
"""

EXAMPLES = r"""
  - name: Get details of single/multiple ports
    dellemc_powermax_port:
      unispherehost: "{{unispherehost}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{array_id}}"
      ports:
      - director_id: "FA-1D"
        port_id: "5"
      - director_id: "SE-1F"
        port_id: "29"
"""

RETURN = r"""
"""

LOG = utils.get_logger("dellemc_powermax_port", log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.1'


class PowerMaxPort(object):
    """ Class with port operations"""

    def __init__(self):
        """ Define all the parameters required by this module"""
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_powermax_port_parameters())
        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )
        # result is a dictionary that contains changed status and port details
        self.result = {"changed": False, "port_details": {}}
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
        LOG.info("Got PyU4V instance for provisioning on to VMAX")

    def get_port_details(self):
        """
        Getting details of a port
        """
        LOG.info("Getting the details of port")
        ports = self.module.params['ports']
        try:
            details = {}
            message = "Director ID and Port ID is mandatory for listing " \
                      "port information"
            for port in ports:
                if len(port) < 2 or port["director_id"] is None or \
                        port["port_id"] is None or \
                        len(port["director_id"]) == 0 or \
                        len(port["port_id"]) == 0:
                    LOG.error(msg=message)
                    self.module.fail_json(msg=message)

                director_id = port["director_id"]
                port_id = port["port_id"]

                details[director_id + ":" + port_id] = \
                    self.provisioning.get_director_port(director_id, port_id)
                self.result["port_details"] = details
            return
        except Exception as e:
            error_message = "Failed to get details of port {0}:{1} with " \
                            "error {2}"
            LOG.error(error_message.format(director_id, port_id, str(e)))
            self.module.fail_json(msg=error_message.format(director_id,
                                                           port_id, str(e)),
                                  **self.result)

    def perform_module_operation(self):
        """
        Perform different actions on port based on user parameter
        chosen in playbook
        """

        changed = False
        self.get_port_details()
        # Finally update the module changed state
        self.result["changed"] = changed
        self.module.exit_json(**self.result)


def get_powermax_port_parameters():
    """This method provide parameter required for the ansible port modules on PowerMax"""
    return dict(
        ports=dict(required=True, type='list')
    )


def main():
    """
    Create PowerMax port object and perform action on it
    based on user input from playbook
    """
    obj = PowerMaxPort()
    obj.perform_module_operation()


if __name__ == "__main__":
    main()
