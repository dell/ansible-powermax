#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: rdfgroup
version_added: '1.3.0'
short_description: Gets the detail information about RDF Groups of
  a PowerMax/VMAX storage system
description:
- Gets details of an RDF Group from a specified PowerMax/VMAX storage system.
- Lists the volumes of an RDF Group from a specified PowerMax/VMAX storage
  system.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
options:
  rdfgroup_number:
    description:
    - Identifier of an RDF Group of type string.
    required: True
    type: str
'''

EXAMPLES = r'''
- name: Get the details of rdf group and volumes
  dellemc.powermax.rdfgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    rdfgroup_number: "{{rdfgroup_id}}"
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
RDFGroupDetails:
    description: Details of the RDF group.
    returned: When the RDF group exist.
    type: list
    contains:
        async:
            description: Flag sets to true when an SRDF pair is in async mode.
            type: bool
        biasConfigured:
            description: Flag for configured bias.
            type: bool
        biasEffective:
            description: Flag for effective bias.
            type: bool
        device_polarity:
            description: Type of device polarity.
            type: str
        hardware_compression:
            description: Flag for hardware compression.
            type: bool
        label:
            description: RDF group label.
            type: str
        link_limbo:
            description: The amount of time that the array's operating
                         environment waits after the SRDF link goes down
                         before updating the link's status. The link limbo
                         value can be set from 0 to 120 seconds.
                         The default value is 10 seconds.
            type: int
        localOnlinePorts:
            description: List of local online ports.
            type: list
        localPorts:
            description: List of local ports.
            type: list
        metro:
            description: Flag for metro configuration.
            type: list
        modes:
            description: Mode of the SRDF link.
            type: str
        numDevices:
            description: Number of devices involved in the pairing.
            type: int
        offline:
            description: Offline flag.
            type: bool
        rdfa_properties:
            description: Properties associated with the RDF group.
            type: list
            contains:
                average_cycle_time:
                    description: Average cycle time (seconds) configured for
                                 this session in seconds.
                    type: int
                consistency_exempt_volumes:
                    description: Flag that indicates if consistency is exempt.
                    type: bool
                cycle_number:
                    description: Number of cycles in seconds.
                    type: int
                dse_active:
                    description: Flag for active Delta Set Extension.
                    type: bool
                dse_autostart:
                    description: Indicates DSE autostart state.
                    type: str
                dse_threshold:
                    description: Flag for DSE threshold.
                    type: int
                duration_of_last_cycle:
                    description: The cycle time (in secs) of the most recently
                                 completed cycle.
                    type: int
                duration_of_last_transmit_cycle:
                    description: Duration of last transmitted cycle in
                                 seconds.
                    type: int
                r1_to_r2_lag_time:
                    description: Time that R2 is behind R1 in seconds.
                    type: int
                session_priority:
                    description: Priority used to determine which RDFA
                                 sessions to drop if cache becomes full.
                                 Values range from 1 to 64, with 1 being the
                                 highest priority (last to be dropped).
                    type: int
                session_uncommitted_tracks:
                    description: Number of uncommitted session tracks.
                    type: int
                transmit_idle_state:
                    description: Indicates RDFA transmit idle state.
                    type: str
                transmit_idle_time:
                    description: Time the transmit cycle has been idle.
                    type: int
                transmit_queue_depth:
                    description: The transmitted queue depth of disks.
                    type: int
        rdfgNumber:
            description: RDF group number on primary device.
            type: int
        remoteOnlinePorts:
            description: List of remote online ports.
            type: list
        remotePorts:
            description: List of remote ports.
            type: list
        remoteRdfgNumber:
            description: RDF group number at remote device.
            type: int
        remoteSymmetrix:
            description: Remote device ID.
            type: int
        software_compression:
            description: Flag for software compression.
            type: bool
        totalDeviceCapacity:
            description: Total capacity of RDF group in GB.
            type: int
        type:
            description: Type of RDF group.
            type: str
        vasa_group:
            description: Flag for VASA group member.
            type: bool
        witness:
            description: Flag for witness.
            type: bool
        witnessConfigured:
            description: Flag for configured witness.
            type: bool
        witnessDegraded:
            description: Flag for degraded witness.
            type: bool
        witnessEffective:
            description: Flag for effective witness.
            type: bool
        witnessProtectedPhysical:
            description: Flag for physically protected witness.
            type: bool
        witnessProtectedVirtual:
            description: Flag for virtually protected witness.
            type: bool
        RDFGroupVolumes:
            description: List of various properties of RDF group volume(s).
            type: list
            contains:
                largerRdfSide:
                    description: Larger RDF side among the devices.
                    type: str
                localRdfGroupNumber:
                    description: RDF group number at primary device.
                    type: int
                localSymmetrixId:
                    description: Primary device ID.
                    type: int
                localVolumeName:
                    description: Volume name at primary device.
                    type: str
                localVolumeState:
                    description: Volume state at primary device
                    type: str
                local_wwn_external:
                    description: External WWN of volume at primary device.
                    type: int
                rdfMode:
                    description: SRDF mode of pairing.
                    type: str
                rdfpairState:
                    description: SRDF state of pairing.
                    type: str
                remoteRdfGroupNumber:
                    description: RDF group number at remote device.
                    type: int
                remoteSymmetrixId:
                    description: Remote device ID.
                    type: int
                remoteVolumeName:
                    description: Volume name at remote device.
                    type: str
                remoteVolumeState:
                    description: Volume state at remote device.
                    type: str
                remote_wwn_external:
                    description: External WWN of volume at remote device.
                    type: int
                volumeConfig:
                    description: Type of volume.
                    type: str
'''

import logging
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('rdfgroup')

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class RDFGroup(object):
    """Class with RDF Group operations"""

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_rdf_group_parameters())
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False)

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
        self.replication = self.u4v_conn.replication
        LOG.info('Got PyU4V instance for replication on to PowerMax ')

    def get_rdf_group_volumes(self, rdf_number):
        """Get the list of volumes of a RDF Group from a given
           PowerMax/Vmax storage system"""

        try:
            LOG.info('Getting Volume List from RDF Group ')
            vol_list = self.replication.get_rdf_group_volume_list(
                rdf_number=rdf_number)
            LOG.info('Successfully listed %s volumes from RDG Group %s',
                     len(vol_list), rdf_number)

            rdf_group_device_list = []

            for vol in vol_list:
                dev_details = self.replication.get_rdf_group_volume(
                    rdf_number, vol)
                rdf_group_device_list.append(dev_details)

            LOG.info('Successfully listed %s RDF Volume device details from '
                     'RDF Group Number %s',
                     len(rdf_group_device_list), rdf_number)
            return rdf_group_device_list

        except Exception as e:
            msg = ('Get RDF Volumes for RDF Group %s failed with error %s' %
                   (rdf_number, str(e)))
            self.show_error_exit(msg=msg)

    def get_rdf_group_details(self, rdf_number):
        """Get the details of the rdf group of a given PowerMax/Vmax storage
        system"""

        try:
            LOG.info('Getting RDF Group %s Details', rdf_number)

            rdf_group_details = self.replication.get_rdf_group(
                rdf_number=rdf_number)
            LOG.info('Successfully listed RDF Group %s details',
                     rdf_number)

            return rdf_group_details

        except Exception as e:
            msg = ('Get RDF Group %s Details failed with error %s' %
                   (rdf_number, str(e)))
            self.show_error_exit(msg=msg)

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

        rdfgroup_number = self.module.params['rdfgroup_number']

        rdf_group_details = self.get_rdf_group_details(rdfgroup_number)
        rdf_vols_details = self.get_rdf_group_volumes(rdfgroup_number)
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")

        self.module.exit_json(
            changed=False,
            RDFGroupDetails=rdf_group_details,
            RDFGroupVolumes=rdf_vols_details,
        )


def get_rdf_group_parameters():
    """This method provide the parameters required for the ansible
    modules on PowerMax"""
    return dict(
        rdfgroup_number=dict(type='str', required=True),
    )


def main():
    """ Create PowerMax RDF Group object and perform action on it
        based on user input from playbook """
    obj = RDFGroup()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
