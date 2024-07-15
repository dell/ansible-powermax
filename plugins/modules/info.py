#!/usr/bin/python
# Copyright: (c) 2019-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: info
version_added: '1.0.0'
short_description: Gathers information about PowerMax or VMAX storage entities
description:
- Gathers the list of specified PowerMax or VMAX storage system entities, such as
  the list of registered arrays, storage groups, hosts, host groups, storage
  groups, storage resource pools, port groups, masking views, initiators,
  array health status, alerts and metro DR environments, so on.
extends_documentation_fragment:
  - dellemc.powermax.powermax
  - dellemc.powermax.powermax.powermax_serial_no
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
- Pavan Mudunuri (@Pavan-Mudunuri) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>
options:
  serial_no:
    description:
    - The serial number of the PowerMax or VMAX array. It is not required for
     getting the list of arrays.
    type: str
    required: False
    default: ""
  tdev_volumes:
     description:
     - Boolean variable to filter the volume list.
       This has a small performance impact.
       The default setting is True and; only TDEV volumes will be returned.
     - True - Returns only the TDEV volumes.
     - False - Rreturns all the volumes.
     required: False
     type: bool
     choices: [True, False]
     default: True
  gather_subset:
    description:
    - List of string variables to specify the PowerMax or VMAX entities for which
      information is required.
    - Required only if the serial_no is present.
    - List of all PowerMax or VMAX entities supported by the module.
    - To get alert summary information - alert.
    - To get health status of a specific PowerMax array - health.
    - To get volumes - vol.
    - To get storage resource pools - srp.
    - To get storage groups - sg.
    - To get port groups - pg.
    - To get hosts - host.
    - To get host groups - hg.
    - To get ports - port.
    - To get masking views - mv.
    - To get RDF groups - rdf.
    - To get Metro DR environments - metro_dr_env.
    - To get snapshot policies - snapshot_policies.
    - To get initiators - initiators.
    - To get masking view connections - mv_connections.
    required: False
    type: list
    elements: str
    choices: [alert, health, vol, srp, sg, pg , host, hg, port, mv, rdf,
              metro_dr_env, snapshot_policies, initiators, mv_connections]
  filters:
    description:
    - List of filters to support filtered output for storage entities.
    - Each filter is a tuple of {filter_key, filter_operator, filter_value}.
    - Supports passing of multiple filters.
    - The storage entities, 'rdf', 'health', 'snapshot_policies' and
      'metro_dr_env', does not support filters. Filters are ignored
      if passed.
    required: False
    type: list
    elements: dict
    suboptions:
      filter_key:
        description:
        - Name identifier of the filter.
        type: str
        required: True
      filter_operator:
        description:
        - Operation to be performed on filter key.
        type: str
        choices: [equal, greater, lesser, like]
        required: True
      filter_value:
        description:
        - Value of the filter key.
        type: str
        required: True
  masking_view_name:
    description:
    - The name of the masking view to fetch the masking view connections.
    type: str
notes:
    - Filter functionality is supported only for the following
      'filter_key' against specific 'gather_subset'.
    - For vol - allocated_percent, associated, available_thin_volumes, bound_tdev,
      cap_cyl, cap_gb, cap_mb, cap_tb, cu_image_num, cu_image_ssid,
      data_volume, dld, drv, effective_wwn, emulation, encapsulated,
      encapsulated_wwn, gatekeeper, has_effective_wwn, mapped,
      mobility_id_enabled, num_of_front_end_paths, num_of_masking_views,
      num_of_storage_groups, oracle_instance_name, physical_name, pinned,
      private_volumes, rdf_group_number, reserved, split_name, status,
      storageGroupId, symmlun, tdev, thin_bcv, type, vdev, virtual_volumes,
      volume_identifier, wwn.
    - For srp - compression_state, description, effective_used_capacity_percent,
      emulation, num_of_disk_groups, num_of_srp_sg_demands,
      num_of_srp_slo_demands, rdfa_dse, reserved_cap_percent,
      total_allocated_cap_gb, total_srdf_dse_allocated_cap_gb,
      total_subscribed_cap_gb, total_usable_cap_gb.
    - For sg - base_slo_name, cap_gb, child, child_sg_name, ckd, compression,
      compression_ratio_to_one, fba, num_of_child_sgs, num_of_masking_views,
      num_of_parent_sgs, num_of_snapshots, num_of_vols, parent,
      parent_sg_name, slo_compliance, slo_name, srp_name, storageGroupId,
      tag, volumeId.
    - For pg - dir_port, fibre, iscsi, num_of_masking_views, num_of_ports.
    - For host - host_group_name, num_of_host_groups, num_of_initiators,
      num_of_masking_views, num_of_powerpath_hosts, powerPathHostId.
    - For hg - host_name, num_of_hosts, num_of_masking_views.
    - For port - aclx, avoid_reset_broadcast, common_serial_number, director_status,
      disable_q_reset_on_ua, enable_auto_negotive, environ_set, hp_3000_mode,
      identifier, init_point_to_point, ip_list, ipv4_address, ipv6_address,
      iscsi_target, max_speed, negotiated_speed, neqotiate_reset,
      no_participating, node_wwn, num_of_cores, num_of_hypers,
      num_of_mapped_vols, num_of_masking_views, num_of_port_groups,
      port_interface, port_status, rdf_hardware_compression,
      rdf_hardware_compression_supported, rdf_software_compression,
      rdf_software_compression_supported, scsi_3, scsi_support1, siemens,
      soft_reset, spc2_protocol_version, sunapee, type, unique_wwn, vcm_state,
      vnx_attached, volume_set_addressing, wwn_node.
    - For mv - host_or_host_group_name, port_group_name,
      protocol_endpoint_masking_view, storage_group_name.
    - For alert - acknowledged, array, created_date, created_date_milliseconds,
      description, object, object_type, severity, state, type.
    - For initiators - alias, directorId, initiator_hba, in_a_host, iscsi,
      logged_in, num_of_host_groups, num_of_masking_views,
      num_of_powerpath_hosts, num_of_vols, on_fabric, port_flag_overrides,
      portId, powerPathHostId.
    - For mv_connections - volume_id, host_lun_address, cap_gb, initiator_id,
      alias, dir_port, logged_in, on_fabric.
    - The check_mode is supported.
'''

EXAMPLES = r'''

- name: Get list of volumes with filter -- all TDEV volumes of size equal to 5 GB
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - vol
    filters:
      - filter_key: "tdev"
        filter_operator: "equal"
        filter_value: "True"
      - filter_key: "cap_gb"
        filter_operator: "equal"
        filter_value: "5"

- name: Get list of volumes and storage groups with filter
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - vol
      - sg
    filters:
      - filter_key: "tdev"
        filter_operator: "equal"
        filter_value: "True"
      - filter_key: "cap_gb"
        filter_operator: "equal"
        filter_value: "5"

- name: Get list of storage groups with capacity between 2 GB to 10 GB
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - sg
    filters:
      - filter_key: "cap_gb"
        filter_operator: "greater"
        filter_value: "2"
      - filter_key: "cap_gb"
        filter_operator: "lesser"
        filter_value: "10"

- name: Get the list of arrays for a given Unisphere host
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
  register: array_list

- name: Get list of TDEV-volumes
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    tdev_volumes: true
    gather_subset:
      - vol

- name: Get the list of arrays for a given Unisphere host
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"

- name: Get array health status
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - health

- name: Get array alerts summary
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - alert

- name: Get the list of Metro DR environments for a given Unisphere host
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - metro_dr_env

- name: Get list of storage groups
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - sg

- name: Get list of Storage Resource Pools
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - srp

- name: Get list of ports
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - port

- name: Get list of Port Groups
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - pg

- name: Get list of hosts
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - host

- name: Get list of Host Groups
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - hg

- name: Get list of Masking Views
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - mv

- name: Get list of RDF Groups
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - rdf

- name: Get list of snapshot policies
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - snapshot_policies

- name: Get list of initiators
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - initiators

- name: Get list of masking view connections with filter
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - mv_connections
    filters:
      - filter_key: "logged_in"
        filter_operator: "equal"
        filter_value: "True"
      - filter_key: "cap_gb"
        filter_operator: "equal"
        filter_value: "10"
'''

RETURN = r'''
Arrays:
    description: Aviliable list of arrays in Unisphere.
    returned: When the arrays in Unisphere exist.
    type: list
Health:
    description: The health status of the array.
    returned: When the array exist.
    type: complex
    contains:
        health_score_metric:
            description: An overall health score for the specified storage system.
            type: list
            contains:
                cached_date:
                    description: A timestamp in epoch format from the date when it was
                                 cached.
                    type: int
                data_date:
                    description: A timestamp in epoch format from the date it was collected.
                    type: int
                expired:
                    description: A flag to indicate the expiry of the score.
                    type: bool
                health_score:
                    description: An overall health score in numbers.
                    type: int
                instance_metrics:
                    description: Metrics about a specific instance.
                    type: list
                    contains:
                        health_score_instance_metric:
                            description: The health score of a specific instance.
                            type: int
                metric:
                    description: Information about the sub-system , such as
                                 SYSTEM_UTILIZATION, CONFIGURATION,CAPACITY,
                                 and so on.
                    type: str
        num_failed_disks:
            description: Numbers of the disk failure in this system.
            type: int
Alerts:
    description: Alert summary of the array.
    returned: When the alert exists.
    type: list
    contains:
        acknowledged:
            description: Whether or not this alert is acknowledged.
            type: str
        alertId:
            description: Unique ID of alert.
            type: str
        array:
            description: The serial number of the array.
            type: str
        created_date:
            description: The creation date.
            type: str
        created_date_milliseconds:
            description: The creation date presented in milliseconds.
            type: str
        description:
            description: The description of the alert.
            type: str
        object:
            description: An object description.
            type: str
        object_type:
            description: Resource class.
            type: str
        severity:
            description: The severity of the alert.
            type: str
        state:
            description: The state of the alert.
            type: str
        type:
            description: The type of the alert.
            type: str
HostGroups:
    description: A list of Host Groups present on the array.
    returned: When the hostgroups exist.
    type: list
Hosts:
    description: A list of hosts present on the array.
    returned: When the hosts exist.
    type: list
MaskingViews:
    description: A list of masking views present on the array.
    returned: When the masking views exist.
    type: list
PortGroups:
    description: A list of Port Groups on the array.
    returned: When the Port Groups exist.
    type: list
Ports:
    description: A list of ports on the array.
    returned: When the ports exist.
    type: complex
    contains:
        directorId:
            description: The director ID of the port.
            type: str
        portId:
            description: The number of the port.
            type: str
RDFGroups:
    description: A list of RDF groups on the array.
    returned: When the RDF groups exist.
    type: complex
    contains:
        label:
            description: Name of the RDF group.
            type: str
        rdfgNumber:
            description: An unique identifier of the RDF group.
            type: int
StorageGroups:
    description: A list of storage groups on the array.
    returned: When the storage groups exist.
    type: list
StorageResourcePools:
    description: A list of storage pools on the array.
    returned: When the storage pools exist.
    type: complex
    contains:
        diskGroupId:
            description: The ID of the disk group.
            type: list
        emulation:
            description: The type of volume emulation.
            type: str
        num_of_disk_groups:
            description: The number of disk groups.
            type: int
        rdfa_dse:
            description: A flag for RDFA Delta Set Extension.
            type: bool
        reserved_cap_percent:
            description: The reserved capacity percentage.
            type: int
        srpId:
            description: An unique Identifier for SRP.
            type: str
        srp_capacity:
            description: The different entities to measure SRP capacity.
            type: dict
            contains:
                effective_used_capacity_percent:
                    description: The percentage of effectively used capacity.
                    type: int
                snapshot_modified_tb:
                    description: The snapshot modified in TB.
                    type: int
                snapshot_total_tb:
                    description: The total snapshot size in TB.
                    type: int
                subscribed_allocated_tb:
                    description: Subscribed allocated size in TB.
                    type: int
                subscribed_total_tb:
                    description: Subscribed total size in TB.
                    type: int
                usable_total_tb:
                    description: The usable total size in TB.
                    type: int
                usable_used_tb:
                    description: The usable used size in TB.
                    type: int
        srp_efficiency:
            description: The different entities to measure SRP efficiency.
            type: dict
            contains:
                compression_state:
                    description: Depicts the compression state of the SRP.
                    type: str
                data_reduction_enabled_percent:
                    description: The percentage of data reduction enabled in the
                                 SRP.
                    type: int
                data_reduction_ratio_to_one:
                    description: The data reduction ratio of SRP.
                    type: int
                overall_efficiency_ratio_to_one:
                    description: The overall efficiency ratio of SRP.
                    type: int
                snapshot_savings_ratio_to_one:
                    description: The snapshot savings ratio of SRP.
                    type: int
                virtual_provisioning_savings_ratio_to_one:
                    description: The virtual provisioning savings ratio of SRP.
                    type: int
        total_srdf_dse_allocated_cap_gb:
            description: The total SRDF DSE allocated capacity in GB.
            type: int
Volumes:
    description: A list of volumes on the array.
    returned: When the volumes exist.
    type: list
MetroDREnvironments:
    description: A list of Metro DR environments on the array.
    returned: When an environment exists.
    type: list
SnapshotPolicies:
    description: A list of the snapshot policies on the array.
    returned: When a snapshot policy exists.
    type: list
Initiators:
    description: A list of initiators on the array.
    returned: When an initiator exists.
    type: list
MVConnections:
    description: A list of the masking view connections on the array.
    returned: When the masking view connections exists.
    type: complex
    contains:
        masking_view_id:
            description: The ID of the masking view.
            type: str
        connections:
            description: A list of the masking view connections.
            type: list
    sample:
        {
            "masking_view_connections": [
                {
                    "alias": "100000xxxx/100000xxxxxxxxx",
                    "cap_gb": "10.0",
                    "dir_port": "XX-XX:11",
                    "host_lun_address": "0001",
                    "initiatorId": "100000aaaaaaa",
                    "logged_in": True,
                    "on_fabric": True,
                    "volumeId": "000XX"
                }
            ],
            "masking_view_id": "mv-id-1"
        }
'''

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('info')

HAS_PYU4V = utils.has_pyu4v_sdk()
PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v3.0.0'


class Info(object):
    """Class with Gather Fact operations"""

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = get_info_parameters()
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True)
        serial_no = self.module.params['serial_no']
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
            if serial_no == '':
                self.u4v_unisphere_con = utils.get_u4v_unisphere_connection(
                    self.module.params, APPLICATION_TYPE)
                self.common = self.u4v_unisphere_con.common
                LOG.info("Got PyU4V Unisphere instance for common lib method "
                         "access on PowerMax")
            else:
                self.module_params.update(
                    utils.get_powermax_management_host_parameters())
                self.u4v_conn = utils.get_U4V_connection(
                    self.module.params, application_type=APPLICATION_TYPE)
                self.provisioning = self.u4v_conn.provisioning
                self.u4v_conn.set_array_id(serial_no)
                LOG.info('Got PyU4V instance for provisioning on to PowerMax')
                self.replication = self.u4v_conn.replication
                LOG.info('Got PyU4V instance for replication on to PowerMax')
        except Exception as e:
            self.show_error_exit(msg=str(e))

    def pre_check_for_PyU4V_version(self):
        """ Performs pre-check for PyU4V version"""
        curr_version = utils.PyU4V.__version__
        supp_version = "9.2"
        is_supported_version = utils.pkg_resources.parse_version(
            curr_version) >= utils.pkg_resources.parse_version(supp_version)

        if not is_supported_version:
            msg = "Listing of 'MetroDR Environments' and 'Alerts' are " \
                  "not supported currently by PyU4V version " \
                  "{0}".format(curr_version)
            self.show_error_exit(msg)

    def get_system_health(self):
        """Get the System Health information of the PowerMax or VMAX storage system"""
        try:
            LOG.info('Getting System Health information ')
            health_check = self.u4v_conn.system.get_system_health()
            LOG.info('Successfully listed System Health information ')
            return health_check
        except Exception as e:
            self.show_error_exit(msg=str(e))

    def get_system_alerts(self, filters_dict=None):
        """Get the alerts information of the PowerMax or VMAX storage system"""
        try:
            self.pre_check_for_PyU4V_version()
            alerts = []
            supported_filters = ['type', 'severity', 'state',
                                 'created_date', 'object',
                                 'object_type', 'acknowledged',
                                 'description']

            LOG.info('Getting System alerts summary')
            filter_to_apply = {}
            if filters_dict:
                for key, value in filters_dict.items():
                    if key in supported_filters:
                        if key == "object":
                            filter_to_apply.update({"_object": value})
                        elif key == "type":
                            filter_to_apply.update({"_type": value})
                        else:
                            filter_to_apply.update({key: value})

            alerts_ids = self.u4v_conn.system.get_alert_ids(**filter_to_apply)
            for alert_id in alerts_ids:
                alerts.append(
                    self.u4v_conn.system.get_alert_details(
                        alert_id=alert_id))
            LOG.info('Successfully listed %d alerts', len(alerts))
            return alerts
        except Exception as e:
            msg = "Failed to get the alerts with error %s" % str(e)
            LOG.error(msg)
            self.show_error_exit(msg=msg)

    def get_filters(self, filters=None):
        """Get the filters to be applied"""

        filters_dict = {}
        for item in filters:
            if 'filter_key' in item and 'filter_operator' in item\
                    and 'filter_value' in item:
                if item["filter_key"] is None \
                        or item["filter_operator"] is None \
                        or item["filter_value"] is None:
                    error_msg = "Provide input for filter sub-options."
                    self.show_error_exit(msg=error_msg)
                else:
                    f_key = item["filter_key"]
                    if item["filter_operator"] == "equal":
                        f_operator = ""
                    elif item["filter_operator"] == "greater":
                        f_operator = ">"
                    elif item["filter_operator"] == "lesser":
                        f_operator = "<"
                    elif item["filter_operator"] == "like":
                        f_operator = "<like>"
                    else:
                        msg = "The filter operator is not supported -- only" \
                              " 'equal', 'greater', 'lesser' and 'like' " \
                              "are supported."
                        self.show_error_exit(msg=msg)

                    val = item["filter_value"]
                    if val == "True" or val == "False":
                        f_value = val
                    else:
                        f_value = f_operator + val
                    if f_key in filters_dict:
                        # multiple filters on same key
                        if isinstance(filters_dict[f_key], list):
                            # prev_val is list, so append new f_val
                            filters_dict[f_key].append(f_value)
                        else:
                            # prev_val is not list,
                            # so create list with prev_val & f_val
                            filters_dict[f_key] = [filters_dict[f_key],
                                                   f_value]
                    else:
                        filters_dict[f_key] = f_value
            else:
                msg = 'filter_key and filter_operator and filter_value is ' \
                      'expected, "%s" given.' % list(item.keys())
                self.show_error_exit(msg=msg)
        return filters_dict

    def get_volume_list(self, tdev_volumes=False, filters_dict=None):
        """Get the list of volumes of a given PowerMax or VMAX storage system"""

        try:
            LOG.info('Getting Volume List ')
            array_serial_no = self.module.params['serial_no']
            if tdev_volumes:
                if filters_dict:
                    if "tdev" not in filters_dict.keys():
                        filters_dict["tdev"] = True
                    vol_list = self.provisioning.get_volume_list(
                        filters=filters_dict)
                else:
                    vol_list = self.provisioning.get_volume_list(
                        filters={"tdev": True})
            elif filters_dict:
                vol_list = self.provisioning.get_volume_list(
                    filters=filters_dict)
            else:
                vol_list = self.provisioning.get_volume_list()
            LOG.info('Successfully listed %d volumes from array %s',
                     len(vol_list), array_serial_no)
            vol_details_list = self.get_volume_details(vol_list)
            return vol_details_list

        except Exception as e:
            msg = 'Get Volumes for array %s failed with error %s '\
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_volume_details(self, vol_list):
        """Get volume details"""
        try:
            vol_details_list = []
            for vol in vol_list:
                vol_details = self.provisioning.get_volume(vol)
                vol_details_list.append(vol_details)
            return vol_details_list
        except Exception as e:
            msg = 'Get Volumes for array %s failed with error %s '\
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_storage_group_list(self, filters_dict=None):
        """Get the list of storage groups of a given PowerMax or VMAX storage
        system"""

        try:
            LOG.info('Getting Storage Group List ')
            array_serial_no = self.module.params['serial_no']
            if filters_dict:
                sg_list = self.provisioning.get_storage_group_list(
                    filters=filters_dict)
            else:
                sg_list = self.provisioning.get_storage_group_list()
            LOG.info('Successfully listed %d Storage Group from array %s',
                     len(sg_list), array_serial_no)
            return sg_list

        except Exception as e:
            msg = 'Get Storage Group for array %s failed with error %s' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_array_list(self):
        """Get the list of arrays of a given PowerMax or VMAX Unisphere host"""

        try:
            LOG.info('Getting Array List ')
            array_list = self.common.get_array_list()
            LOG.info('Got %s Arrays from Unisphere Host %s',
                     len(array_list), self.module_params['unispherehost'])
            return array_list

        except Exception as e:
            msg = 'Get Array List for Unisphere host %s failed with error ' \
                  '%s' % (self.module_params['unispherehost'], str(e))
            self.show_error_exit(msg=msg)

    def get_srp_list(self, filters_dict=None):
        """Get the list of Storage Resource Pools of a given PowerMax or VMAX
        storage system"""

        try:
            LOG.info('Getting Storage Resource Pool List')
            array_serial_no = self.module.params['serial_no']
            if filters_dict:
                srp_list \
                    = self.provisioning.get_srp_list(filters=filters_dict)
            else:
                srp_list = self.provisioning.get_srp_list()
            LOG.info('Got %d Storage Resource Pool from array %s',
                     len(srp_list), array_serial_no)

            srp_detail_list = []
            for srp in srp_list:
                srp_details = self.provisioning.get_srp(srp)
                srp_detail_list.append(srp_details)

            LOG.info('Successfully listed %d Storage Resource Pool details '
                     'from array %s', len(srp_detail_list), array_serial_no)
            return srp_detail_list

        except Exception as e:
            msg = 'Get Storage Resource Pool details for array %s failed ' \
                  'with error %s' % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_portgroup_list(self, filters_dict=None):
        """Get the list of port groups of a given PowerMax or VMAX storage
        system"""

        try:
            LOG.info('Getting Port Group List ')
            array_serial_no = self.module.params['serial_no']
            if filters_dict:
                pg_list = self.provisioning.get_port_group_list(
                    filters=filters_dict)
            else:
                pg_list = self.provisioning.get_port_group_list()
            LOG.info('Got %d Port Groups from array %s',
                     len(pg_list), array_serial_no)
            return pg_list

        except Exception as e:
            msg = 'Get Port Group for array %s failed with error %s' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_host_list(self, filters_dict=None):
        """Get the list of hosts of a given PowerMax or VMAX storage system"""

        try:
            LOG.info('Getting Host List ')
            array_serial_no = self.module.params['serial_no']
            if filters_dict:
                host_list = self.provisioning.get_host_list(
                    filters=filters_dict)
            else:
                host_list = self.provisioning.get_host_list()
            LOG.info('Got %d Hosts from array %s',
                     len(host_list), array_serial_no)
            return host_list

        except Exception as e:
            msg = 'Get Host for array %s failed with error %s' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_hostgroup_list(self, filters_dict=None):
        """Get the list of host groups of a given PowerMax or VMAX storage
        system"""

        try:
            LOG.info('Getting Host Group List ')
            array_serial_no = self.module.params['serial_no']
            if filters_dict:
                hostgroup_list = self.provisioning.get_host_group_list(
                    filters=filters_dict)
            else:
                hostgroup_list = self.provisioning.get_host_group_list()
            LOG.info('Got %d Host Groups from array %s',
                     len(hostgroup_list), array_serial_no)
            return hostgroup_list

        except Exception as e:
            msg = 'Get Host Group for array %s failed with error %s ' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_port_list(self, filters_dict=None):
        """Get the list of ports of a given PowerMax or VMAX storage system"""

        try:
            LOG.info('Getting Port List ')
            array_serial_no = self.module.params['serial_no']
            if filters_dict:
                port_list = self.provisioning.get_port_list(
                    filters=filters_dict)
            else:
                port_list = self.provisioning.get_port_list()
            LOG.info('Got %d Ports from array %s',
                     len(port_list), array_serial_no)
            return port_list

        except Exception as e:
            msg = 'Get Port for array %s failed with error %s ' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_masking_view_list(self, filters_dict=None):
        """Get the list of masking views of a given PowerMax or VMAX storage
        system"""

        try:
            LOG.info('Getting Masking View List')
            array_serial_no = self.module.params['serial_no']
            if filters_dict:
                mv_list = self.provisioning.\
                    get_masking_view_list(filters=filters_dict)
            else:
                mv_list = self.provisioning.get_masking_view_list()
            LOG.info('Got %d Getting Masking Views from array %s',
                     len(mv_list), array_serial_no)
            return mv_list

        except Exception as e:
            msg = 'Get Masking View for array %s failed with error %s' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def prepare_mv_connections_list(self, mv_connections_list, masking_view_id, filters_dict=None):
        connections = self.provisioning.get_masking_view_connections(masking_view_id=masking_view_id, filters=filters_dict)
        if connections:
            mv_connections_list.append(
                {
                    'masking_view_id': masking_view_id,
                    'masking_view_connections': connections
                }
            )
        return mv_connections_list

    def get_mv_connections_list(self, masking_view_name=None, filters_dict=None):
        """Get the list of masking view connections of a given PowerMax or VMAX storage
        system"""

        try:
            LOG.info('Getting Masking View Connections List')
            array_serial_no = self.module.params['serial_no']
            masking_view_list = self.get_masking_view_list()
            mv_connections_list = []

            if masking_view_name is None:
                for masking_view_id in masking_view_list:
                    mv_connections_list = self.prepare_mv_connections_list(mv_connections_list=mv_connections_list,
                                                                           masking_view_id=masking_view_id,
                                                                           filters_dict=filters_dict)
            else:
                mv_list = self.provisioning.get_masking_view_list()
                if masking_view_name not in mv_list:
                    LOG.info('Masking view %s is not present in system',
                             masking_view_name)
                    return None
                LOG.info('Getting masking view %s details', masking_view_name)
                masking_view_id = self.provisioning.get_masking_view(masking_view_name)["maskingViewId"]
                mv_connections_list = self.prepare_mv_connections_list(mv_connections_list=mv_connections_list,
                                                                       masking_view_id=masking_view_id,
                                                                       filters_dict=filters_dict)

            LOG.info('Got %d Getting Masking Views Connections from array %s',
                     len(mv_connections_list), array_serial_no)
            return mv_connections_list

        except Exception as e:
            msg = 'Get Masking View Connections for array %s failed with error %s' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_rdfgroup_list(self):
        """Get the list of rdf group of a given PowerMax or VMAX storage system
        """

        try:
            LOG.info('Getting rdf group List ')
            array_serial_no = self.module.params['serial_no']
            rdf_list = self.replication.get_rdf_group_list()
            LOG.info('Successfully listed %d rdf groups from array %s',
                     len(rdf_list), array_serial_no)
            return rdf_list

        except Exception as e:
            msg = 'Get rdf group for array %s failed with error %s ' \
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_metro_dr_env_list(self):
        """Get the list of metro DR environments of a given PowerMax or VMAX
        storage system"""

        try:

            self.pre_check_for_PyU4V_version()
            self.metro = self.u4v_conn.metro_dr
            LOG.info("Got PyU4V instance for metro DR on to PowerMax")

            LOG.info('Getting metro DR environment list ')
            array_serial_no = self.module.params['serial_no']
            metro_dr_env_list = self.metro.get_metrodr_environment_list()
            LOG.info('Successfully listed %d metro DR environments from array'
                     ' %s', len(metro_dr_env_list), array_serial_no)
            return metro_dr_env_list

        except Exception as e:
            msg = 'Get Metro DR environment for array %s failed with error ' \
                  '%s ' % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_snapshot_policies_list(self):
        """Get the list of snapshot policies of a given PowerMax or VMAX
                storage system"""

        try:
            self.pre_check_for_PyU4V_version()
            self.snapshot_policy = self.u4v_conn.snapshot_policy
            LOG.info("Got PyU4V instance for snapshot policy on to PowerMax")

            LOG.info('Getting snapshot policies list ')
            array_serial_no = self.module.params['serial_no']
            snapshot_policy_list \
                = self.snapshot_policy.get_snapshot_policy_list()
            LOG.info('Successfully listed %d snapshot policies from array'
                     ' %s', len(snapshot_policy_list), array_serial_no)
            return snapshot_policy_list

        except Exception as e:
            msg = 'Get snapshot policies for array %s failed with error ' \
                  '%s ' % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_initiators_list(self, filters_dict=None):
        """Get the list of initiators of a given PowerMax or VMAX
            storage system"""
        try:
            LOG.info('Getting Initiators List ')
            if filters_dict:
                initiators_list = self.provisioning.get_initiator_list(
                    params=filters_dict)
            else:
                initiators_list = self.provisioning.get_initiator_list()
            LOG.info('Got %d Initiators from array', len(initiators_list))
            return initiators_list
        except Exception as e:
            msg = 'Get initiator details failed with error: %s' % str(e)
            self.show_error_exit(msg=msg)

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing Unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = "Failed to close Unisphere connection with " \
                          "error: %s", str(e)
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        """ Perform different actions on Gatherfacts based on user parameters
            chosen in playbook """

        serial_no = self.module.params['serial_no']
        if serial_no == '':
            array_list = self.get_array_list()
            self.module.exit_json(Arrays=array_list)
        else:
            subset = self.module.params['gather_subset']
            tdev_volumes = self.module.params['tdev_volumes']
            masking_view_name = self.module.params['masking_view_name']
            filters = []
            filters = self.module.params['filters']
            if len(subset) == 0:
                self.show_error_exit(msg="Please specify gather_subset")

            filters_dict = {}
            if filters:
                filters_dict = self.get_filters(filters=filters)

            health_check = []
            vol = []
            srp = []
            sg = []
            pg = []
            host = []
            hg = []
            port = []
            mv = []
            rdf = []
            alert = []
            metro_dr_env = []
            snapshot_policies = []
            initiators = []
            mv_connections = []
            if 'alert' in str(subset):
                alert = self.get_system_alerts(filters_dict=filters_dict)
            if 'health' in str(subset):
                health_check = self.get_system_health()
            if 'vol' in str(subset):
                vol = self.get_volume_list(
                    tdev_volumes=tdev_volumes, filters_dict=filters_dict)
            if 'sg' in str(subset):
                sg = self.get_storage_group_list(filters_dict=filters_dict)
            if 'srp' in str(subset):
                srp = self.get_srp_list(filters_dict=filters_dict)
            if 'pg' in str(subset):
                pg = self.get_portgroup_list(filters_dict=filters_dict)
            if 'host' in str(subset):
                host = self.get_host_list(filters_dict=filters_dict)
            if 'hg' in str(subset):
                hg = self.get_hostgroup_list(filters_dict=filters_dict)
            if 'port' in str(subset):
                port = self.get_port_list(filters_dict=filters_dict)
            if 'mv' in subset:
                mv = self.get_masking_view_list(filters_dict=filters_dict)
            if 'rdf' in str(subset):
                rdf = self.get_rdfgroup_list()
            if 'metro_dr_env' in str(subset):
                metro_dr_env = \
                    self.get_metro_dr_env_list()
            if 'snapshot_policies' in str(subset):
                snapshot_policies = \
                    self.get_snapshot_policies_list()
            if 'initiators' in str(subset):
                initiators = \
                    self.get_initiators_list(filters_dict=filters_dict)
            if 'mv_connections' in subset:
                mv_connections = \
                    self.get_mv_connections_list(masking_view_name=masking_view_name,
                                                 filters_dict=filters_dict)

            LOG.info("Closing Unisphere connection %s", self.u4v_conn)
            utils.close_connection(self.u4v_conn)
            LOG.info("Connection closed successfully")

            self.module.exit_json(
                Alerts=alert,
                Health=health_check,
                Volumes=vol,
                StorageGroups=sg,
                StorageResourcePools=srp,
                PortGroups=pg,
                Hosts=host,
                HostGroups=hg,
                Ports=port,
                MaskingViews=mv,
                RDFGroups=rdf,
                MetroDREnvironments=metro_dr_env,
                SnapshotPolicies=snapshot_policies,
                Initiators=initiators,
                MVConnections=mv_connections)


def get_info_parameters():
    """This method provide the parameters required for the Ansible
    modules on PowerMax"""

    return dict(
        unispherehost=dict(type='str', required=True, no_log=True),
        universion=dict(type='int', required=False, choices=[91, 92, 100, 101]),
        verifycert=dict(type='str', required=True),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        serial_no=dict(type='str', required=False, default=''),
        timeout=dict(type='int', required=False, default=120),
        port=dict(type='int', required=False, default=8443),
        tdev_volumes=dict(type='bool', required=False,
                          default=True, choices=[True, False]),
        masking_view_name=dict(type='str'),
        gather_subset=dict(type='list', required=False, elements='str',
                           choices=['alert',
                                    'health',
                                    'vol',
                                    'sg',
                                    'srp',
                                    'pg',
                                    'host',
                                    'hg',
                                    'port',
                                    'mv',
                                    'rdf',
                                    'metro_dr_env',
                                    'snapshot_policies',
                                    'initiators',
                                    'mv_connections'
                                    ]),
        filters=dict(type='list', required=False, elements='dict',
                     options=dict(
                         filter_key=dict(type='str', required=True,
                                         no_log=False),
                         filter_operator=dict(type='str', required=True,
                                              choices=['equal', 'greater',
                                                       'lesser', 'like']),
                         filter_value=dict(type='str', required=True))
                     ),
    )


def main():
    """ Create PowerMaxGatherFacts object and perform action on it
        based on user input from playbook """

    obj = Info()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
