#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_gatherfacts
version_added: '2.6'
short_description: Gathers information about PowerMax/VMAX Storage entities
description:
- Gathers the list of specified PowerMax/VMAX Storage System entities, like the
  list of registered arrays, storage groups, hosts, host groups, storage groups,
  storage resource pools, port groups, masking views, etc.
author:
- Arindam Datta (arindam.datta@dell.com)
options:
  serial_no:
    description:
    - the serial number of  PowerMax/VMAX array. It is a required parameter
      when getting information about specific entities. In absence of this
      parameter, the script will list all the registered array's serial numbers
      on the specified Unisphere.
    - required only if gather_subset is present
    required: False
  unispherehost:
    description:
    - IP or FQDN of the Unisphere host
    required: True
  universion:
    description:
    - Unisphere version
    required: True
  verifycert:
    description:
    - boolean variable to specify whether to validate SSL certificate or not.
    - True - indicates that the SSL certificate should be verified.
    - False - indicates that the SSL certificate should not be verified.
    required: True
    choices: [ True, False]
  user:
    description:
    - username of the Unisphere host.
    required: True
  password:
    description:
    - the password of the Unisphere host.
    required: True
  gather_subset:
    description:
    - List of string variables to specify the PowerMax/VMAX entities for which
      information is required.
    - Required only if serial_no is present
    - List of all PowerMax/VMAX entities supported by the module - 
    - vol - volumes
    - srp - storage resource pools
    - sg - storage groups
    - pg - port groups
    - host - hosts
    - hg -  host groups
    - port - ports
    - mv - masking views
    required: False 
    choices: [vol, srp, sg, pg , host, hg, port, mv]
'''

EXAMPLES = r'''

- name: Get list of volumes
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - vol

- name: Get array list
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"

- name: Get list of Storage groups
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - sg

- name: Get list of Storage Resource Pools
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - srp

- name: Get list of Port Groups
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - pg

- name: Get list of Hosts
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - host

- name: Get list of Host Groups
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - hg

- name: Get list of Ports
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - port

- name: Get list of Maskng Views
    dellemc_powermax_gatherfacts:
      unispherehost: "{{unispherehost}}"
      universion: "{{universion}}"
      verifycert: "{{verifycert}}"
      user: "{{user}}"
      password: "{{password}}"
      serial_no: "{{serial_no}}"
      gather_subset:
         - mv

'''

RETURN = r'''  '''


LOG = utils.get_logger('dellemc_powermax_gatherfacts', log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()


class PowerMaxGatherFacts(object):
    """Class with Gather Fact operations"""

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = get_powermax_gatherfacts_parameters()
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True)
        serial_no = self.module.params['serial_no']
        if HAS_PYU4V is False:
            self.module.fail_json(msg="Ansible modules for PowerMax require "
                                      "the PyU4V python library to be "
                                      "installed. Please install the library "
                                      "before using these modules.")
        if PYU4V_VERSION_CHECK is not None:
            self.module.fail_json(msg=PYU4V_VERSION_CHECK)
            LOG.error(PYU4V_VERSION_CHECK)

        if serial_no is '':
            self.u4v_unisphere_con = utils.get_u4v_unisphere_connection(
                self.module.params)
            self.common = self.u4v_unisphere_con.common
            LOG.info(
                    "Got PyU4V Unisphere instance for common lib method "
                     "access on VMAX")
        else:
            self.module_params.update(
                utils.get_powermax_management_host_parameters())
            self.u4v_conn = utils.get_U4V_connection(self.module.params)
            self.provisioning = self.u4v_conn.provisioning
            self.u4v_conn.set_array_id(serial_no)
            LOG.info('Got PyU4V instance for provisioning on to VMAX ')

    def get_volume_list(self):
        """Get the list of volumes of a given PowerMax/Vmax storage system"""

        try:
            LOG.info('Getting Volume List ')
            array_serial_no = self.module.params['serial_no']
            vol_list = self.provisioning.get_volume_list()
            LOG.info('Successfully listed {0} volumes from array {1}' .format(
                len(vol_list), array_serial_no))
            return vol_list

        except Exception as e:
            msg = 'Get Volumes for array {0} failed with error {1} '.format(
                 self.module.params['serial_no'], str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_storage_group_list(self):
        """Get the list of storage groups of a given PowerMax/Vmax storage
        system"""

        try:
            LOG.info('Getting Storage Group List ')
            array_serial_no = self.module.params['serial_no']
            sg_list = self.provisioning.get_storage_group_list()
            LOG.info(
                'Successfully listed {0} Storage Group from array {1}'.format(
                    len(sg_list), array_serial_no))
            return sg_list

        except Exception as e:
            msg = ('Get Storage Group for array {0} failed with error {1}'
                   .format(self.module.params['serial_no'], str(e)))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_array_list(self):
        """Get the list of arrays of a given PowerMax/Vmax Unisphere host"""

        try:
            LOG.info('Getting Array List ')
            array_list = self.common.get_array_list()
            LOG.info('Got {0} Arrays from Unisphere Host  {1}' .format(
                len(array_list), self.module_params['unispherehost']))
            return array_list

        except Exception as e:
            msg = ('Get Array List for Unisphere host {0} failed with error \
                   {1}'
                   .format(self.module_params['unispherehost'], str(e)))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_srp_list(self):
        """Get the list of Storage Resource Pools of a given PowerMax/Vmax
        storage system"""

        try:
            LOG.info('Getting Storage Resource Pool List')
            array_serial_no = self.module.params['serial_no']
            srp_list = self.provisioning.get_srp_list()
            LOG.info('Got {0} Storage Resource Pool from array {1}'.format(
                len(srp_list), array_serial_no))
            return srp_list

        except Exception as e:
            msg = ('Get Storage Resource Pool for array {0} failed with error \
                   {1} '.format(self.module.params['serial_no'], str(e)))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_portgroup_list(self):
        """Get the list of port groups of a given PowerMax/Vmax storage
        system"""

        try:
            LOG.info('Getting Port Group List ')
            array_serial_no = self.module.params['serial_no']
            pg_list = self.provisioning.get_portgroup_list()
            LOG.info('Got {0} PortGroup from array {1}'.format(
                len(pg_list), array_serial_no))
            return pg_list

        except Exception as e:
            msg = 'Get Port Group for array {0} failed with error {1} '.format(
                self.module.params['serial_no'], str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_host_list(self):
        """Get the list of hosts of a given PowerMax/Vmax storage system"""

        try:
            LOG.info('Getting Host List ')
            array_serial_no = self.module.params['serial_no']
            host_list = self.provisioning.get_host_list()
            LOG.info('Got {0} Host from array {1}'.format(
                len(host_list), array_serial_no))
            return host_list

        except Exception as e:
            msg = 'Get Host for array {0} failed with error {1} '.format(
                self.module.params['serial_no'], str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_hostgroup_list(self):
        """Get the list of host groups of a given PowerMax/Vmax storage
        system"""

        try:
            LOG.info('Getting Host Group List ')
            array_serial_no = self.module.params['serial_no']
            hostgroup_list = self.provisioning.get_hostgroup_list()
            LOG.info('Got {0} Host Group from array {1}'.format(
                len(hostgroup_list), array_serial_no))
            return hostgroup_list

        except Exception as e:
            msg = 'Get Host Group for array {0} failed with error {1} '.format(
                self.module.params['serial_no'], str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_port_list(self):
        """Get the list of ports of a given PowerMax/Vmax storage system"""

        try:
            LOG.info('Getting Port List ')
            array_serial_no = self.module.params['serial_no']
            port_list = self.provisioning.get_port_list()
            LOG.info('Got {0} Port from array {1}'.format(
                len(port_list), array_serial_no))
            return port_list

        except Exception as e:
            msg = 'Get Port Group for array {0} failed with error {1} '.format(
                self.module.params['serial_no'], str(e))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def get_masking_view_list(self):
        """Get the list of masking views of a given PowerMax/Vmax storage
        system"""

        try:
            LOG.info('Getting Masking View List')
            array_serial_no = self.module.params['serial_no']
            mv_list = self.provisioning.get_masking_view_list()
            LOG.info('Got {0} Getting Masking View from array {1}'.format(
                len(mv_list), array_serial_no))
            return mv_list

        except Exception as e:
            msg = ('Get Masking View for array {0} failed with error {1}'
                   .format(self.module.params['serial_no'], str(e)))
            LOG.error(msg)
            self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        serial_no = self.module.params['serial_no']
        if serial_no is '':
            array_list = self.get_array_list()
            self.module.exit_json(Arrays=array_list)
        else:
            subset = self.module.params['gather_subset']
            vol = []
            srp = []
            sg = []
            pg = []
            host = []
            hg = []
            port = []
            mv = []
            if 'vol' in str(subset):
                vol = self.get_volume_list()
            if 'sg' in str(subset):
                sg = self.get_storage_group_list()
            if 'srp' in str(subset):
                srp = self.get_srp_list()
            if 'pg' in str(subset):
                pg = self.get_portgroup_list()
            if 'host' in str(subset):
                host = self.get_host_list()
            if 'hg' in str(subset):
                hg = self.get_hostgroup_list()
            if 'port' in str(subset):
                port = self.get_port_list()
            if 'mv' in str(subset):
                mv = self.get_masking_view_list()
            self.module.exit_json(
                Volumes=vol,
                StorageGroups=sg,
                StorageResourcePools=srp,
                PortGroups=pg,
                Hosts=host,
                HostGroups=hg,
                Ports=port,
                MaskingViews=mv)


def get_powermax_gatherfacts_parameters():
    """This method provide the parameters required for the ansible modules on PowerMax"""
    return dict(
            unispherehost=dict(type='str', required=True),
            universion=dict(type='int', required=True),
            verifycert=dict(type='bool', required=True),
            user=dict(type='str', required=True),
            password=dict(type='str', required=True, no_log=True),
            serial_no=dict(type='str', required=False, default=''),
            gather_subset=dict(type='list', required=False, default=[])
    )


def main():
    """ Create PowerMaxGatherFacts object and perform action on it
        based on user input from playbook """
    obj = PowerMaxGatherFacts()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
