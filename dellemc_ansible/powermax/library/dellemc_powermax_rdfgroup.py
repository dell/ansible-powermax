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
module: dellemc_powermax_rdfgroup
version_added: '2.6'
short_description: Gets the detail information about RDF Groups of 
  a PowerMax/VMAX storage system
description:
- Gets details of a RDF Group from a specified PowerMax/VMAX 
  storage system.
- Lists the volumes of a RDF Group from a specified PowerMax/VMAX 
  storage System
extends_documentation_fragment:
  - dellemc.dellemc_powermax
author:
- Arindam Datta (arindam.datta@dell.com)
options:
  rdfgroup_number:
    description:
    - Identifier of a RDF Group of type string       
    required: True
    type: str  
          
'''

EXAMPLES = r'''
- name: Get the detais of rdf group and volumes
    dellemc_powermax_rdfgroup:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      rdfgroup_number: "{{rdfgroup_id}}"
'''

RETURN = r'''  
'''

LOG = utils.get_logger('dellemc_powermax_rdfgroup', log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.1'


class PowerMaxRDFGroup(object):
    """Class with RDF Group operations"""

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_powermax_rdf_group_parameters())
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False)

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
        self.replication = self.u4v_conn.replication
        LOG.info('Got PyU4V instance for replication on to PowerMax ')

    def get_rdf_group_volumes(self, rdf_number):
        """Get the list of volumes of a RDF Group from a given
           PowerMax/Vmax storage system"""

        try:
            LOG.info('Getting Volume List from RDF Group ')
            vol_list = self.replication.get_rdf_group_volume_list(rdf_number=rdf_number)
            LOG.info('Successfully listed {0} volumes from RDG Group {1}'.format(
                    len(vol_list), rdf_number))

            rdf_group_device_list = []

            for vol in vol_list:
                dev_details = self.replication.get_rdf_group_volume(
                              rdf_number, vol)
                rdf_group_device_list.append(dev_details)

            LOG.info('Successfully listed {0} RDF Volume device details '
                     'from RDF Group Number {1}'.format(
                      len(rdf_group_device_list),rdf_number))
            return rdf_group_device_list

        except Exception as e:
            msg = 'Get RDF Volumes for RDF Group {0} failed with error {1} '.format(
                   rdf_number, str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_rdf_group_details(self, rdf_number):
        """Get the details of the rdf group of a given PowerMax/Vmax storage
        system"""

        try:
            LOG.info('Getting RDF Group {0} Details'.format(rdf_number))

            rdf_group_details = self.replication.get_rdf_group(
                                rdf_number=rdf_number)
            LOG.info(
                'Successfully listed RDF Group {0} Details : {1}'.format(
                 rdf_number, rdf_group_details))

            return rdf_group_details

        except Exception as e:
            msg = ('Get RDF Group {0} Details failed with error {1}'
                   .format(rdf_number, str(e)))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):

        rdfgroup_number = self.module.params['rdfgroup_number']

        rdf_group_details = self.get_rdf_group_details(rdfgroup_number)
        rdf_vols_details = self.get_rdf_group_volumes(rdfgroup_number)

        self.module.exit_json(
            changed=False,
            RDFGroupDetails=rdf_group_details,
            RDFGroupVolumes=rdf_vols_details,
            )


def get_powermax_rdf_group_parameters():
    """This method provide the parameters required for the ansible
    modules on PowerMax"""
    return dict(
            rdfgroup_number=dict(type='str', required=True),
            )


def main():
    """ Create PowerMax RDF Group object and perform action on it
        based on user input from playbook """
    obj = PowerMaxRDFGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
