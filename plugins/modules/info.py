#!/usr/bin/python
# Copyright: (c) 2019-2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: info
version_added: '1.0.0'
short_description: Gathers information about PowerMax/VMAX Storage entities
description:
- Gathers the list of specified PowerMax/VMAX storage system entities, such as
  the list of registered arrays, storage groups, hosts, host groups, storage
  groups, storage resource pools, port groups, masking views, initiators,
  array health status, alerts and metro DR environments, so on.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
options:
  serial_no:
    description:
    - The serial number of the PowerMax/VMAX array. It is not required for
     getting the list of arrays.
    type: str
    required: False
  tdev_volumes:
     description:
     - Boolean variable to filter the volume list.
       This will have a small performance impact.
       By default it is set to true, only TDEV volumes will be returned.
     - True - Will return only the TDEV volumes.
     - False - Will return all the volumes.
     required: False
     type: bool
     choices: [True, False]
     default: True
  gather_subset:
    description:
    - List of string variables to specify the PowerMax/VMAX entities for which
      information is required.
    - Required only if the serial_no is present.
    - List of all PowerMax/VMAX entities supported by the module.
    - alert - gets alert summary information.
    - health - health status of a specific PowerMax array.
    - vol - volumes.
    - srp - storage resource pools.
    - sg - storage groups.
    - pg - port groups.
    - host - hosts.
    - hg -  host groups.
    - port - ports.
    - mv - masking views.
    - rdf - rdf groups.
    - metro_dr_env - metro DR environments.
    - snapshot_policies - snapshot policies.
    - initiators - initiators.
    required: False
    type: list
    elements: str
    choices: [alert, health, vol, srp, sg, pg , host, hg, port, mv, rdf,
              metro_dr_env, snapshot_policies, initiators]
  filters:
    description:
    - List of filters to support filtered output for storage entities.
    - Each filter is a tuple of {filter_key, filter_operator, filter_value}.
    - Supports passing of multiple filters.
    - The storage entities, 'rdf', 'health', 'snapshot_policies' and
      'metro_dr_env', does not support filters. Filters will be ignored
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
notes:
    - Filter functionality will be supported only for the following
      'filter_key' against specific 'gather_subset'.
    - vol - allocated_percent, associated, available_thin_volumes, bound_tdev,
      cap_cyl, cap_gb, cap_mb, cap_tb, cu_image_num, cu_image_ssid,
      data_volume, dld, drv, effective_wwn, emulation, encapsulated,
      encapsulated_wwn, gatekeeper, has_effective_wwn, mapped,
      mobility_id_enabled, num_of_front_end_paths, num_of_masking_views,
      num_of_storage_groups, oracle_instance_name, physical_name, pinned,
      private_volumes, rdf_group_number, reserved, split_name, status,
      storageGroupId, symmlun, tdev, thin_bcv, type, vdev, virtual_volumes,
      volume_identifier, wwn.
    - srp - compression_state, description, effective_used_capacity_percent,
      emulation, num_of_disk_groups, num_of_srp_sg_demands,
      num_of_srp_slo_demands, rdfa_dse, reserved_cap_percent,
      total_allocated_cap_gb, total_srdf_dse_allocated_cap_gb,
      total_subscribed_cap_gb, total_usable_cap_gb.
    - sg - base_slo_name, cap_gb, child, child_sg_name, ckd, compression,
      compression_ratio_to_one, fba, num_of_child_sgs, num_of_masking_views,
      num_of_parent_sgs, num_of_snapshots, num_of_vols, parent,
      parent_sg_name, slo_compliance, slo_name, srp_name, storageGroupId,
      tag, volumeId.
    - pg - dir_port, fibre, iscsi, num_of_masking_views, num_of_ports.
    - host - host_group_name, num_of_host_groups, num_of_initiators,
      num_of_masking_views, num_of_powerpath_hosts, powerPathHostId.
    - hg - host_name, num_of_hosts, num_of_masking_views.
    - port - aclx, avoid_reset_broadcast, common_serial_number, director_status,
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
    - mv - host_or_host_group_name, port_group_name,
      protocol_endpoint_masking_view, storage_group_name.
    - alert - acknowledged, array, created_date, created_date_milliseconds,
      description, object, object_type, severity, state, type.
    - initiators - alias, directorId, initiator_hba, in_a_host, iscsi,
      logged_in, num_of_host_groups, num_of_masking_views,
      num_of_powerpath_hosts, num_of_vols, on_fabric, port_flag_overrides,
      portId, powerPathHostId.
'''

EXAMPLES = r'''

- name: Get list of volumes with filter -- all TDEV volumes of size equal
        to 5GB
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

- name: Get list of storage groups with capacity between 2GB to 10GB
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
- debug:
    var: array_list

- name: Get list of tdev-volumes
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    tdev_volumes: True
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

- name: Get the list of metro DR environments for a given Unisphere host
  dellemc.powermax.info:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - metro_dr_env

- name: Get list of Storage groups
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

- name: Get list of Ports
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

- name: Get list of Hosts
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
'''

RETURN = r'''
Arrays:
    description: List of arrays in the Unisphere.
    returned: When the Unisphere exist.
    type: list
Health:
    description: Health status of the array.
    returned: When the array exist.
    type: complex
    contains:
        health_score_metric:
            description: Overall health score for the specified Symmetrix.
            type: list
            contains:
                cached_date:
                    description: Date Time stamp in epoch format when it was
                                 cached.
                    type: int
                data_date:
                    description: Date Time stamp in epoch format when it was
                                 collected.
                    type: int
                expired:
                    description: Flag to indicate the expiry of the score.
                    type: bool
                health_score:
                    description: Overall health score in numbers.
                    type: int
                instance_metrics:
                    description: Metrics about a specific instance.
                    type: list
                    contains:
                        health_score_instance_metric:
                            description: Health score of a specific instance.
                            type: int
                metric:
                    description: Information about which sub system , such as
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
            description: Array serial number.
            type: str
        created_date:
            description: Creation Date.
            type: str
        created_date_milliseconds:
            description: Creation Date in milliseconds.
            type: str
        description:
            description: Description about the alert.
            type: str
        object:
            description: Object description.
            type: str
        object_type:
            description: Resource class.
            type: str
        severity:
            description: Severity of the alert.
            type: str
        state:
            description: State of the alert.
            type: str
        type:
            description: Type of the alert.
            type: str
HostGroups:
    description: List of host groups present on the array.
    returned: When the hostgroups exist.
    type: list
Hosts:
    description: List of hosts present on the array.
    returned: When the hosts exist.
    type: list
MaskingViews:
    description: List of masking views present on the array.
    returned: When the masking views exist.
    type: list
PortGroups:
    description: List of port groups on the array.
    returned: When the port groups exist.
    type: list
Ports:
    description: List of ports on the array.
    returned: When the ports exist.
    type: complex
    contains:
        directorId:
            description: Director ID of the port.
            type: str
        portId:
            description: Port number of the port.
            type: str
RDFGroups:
    description: List of RDF groups on the array.
    returned: When the RDF groups exist.
    type: complex
    contains:
        label:
            description: Name of the RDF group.
            type: str
        rdfgNumber:
            description: Unique identifier of the RDF group.
            type: int
StorageGroups:
    description: List of storage groups on the array.
    returned: When the storage groups exist.
    type: list
StorageResourcePools:
    description: List of storage pools on the array.
    returned: When the storage pools exist.
    type: complex
    contains:
        diskGroupId:
            description: ID of the disk group.
            type: list
        emulation:
            description: Type of volume emulation.
            type: str
        num_of_disk_groups:
            description: Number of disk groups.
            type: int
        rdfa_dse:
            description: Flag for RDFA Delta Set Extension.
            type: bool
        reserved_cap_percent:
            description: Reserved capacity percentage.
            type: int
        srpId:
            description: Unique Identifier for SRP.
            type: str
        srp_capacity:
            description: Different entities to measure SRP capacity.
            type: dict
            contains:
                effective_used_capacity_percent:
                    description: Percentage of effectively used capacity.
                    type: int
                snapshot_modified_tb:
                    description: Snapshot modified in TB.
                    type: int
                snapshot_total_tb:
                    description: Total snapshot size in TB.
                    type: int
                subscribed_allocated_tb:
                    description: Subscribed allocated size in TB.
                    type: int
                subscribed_total_tb:
                    description: Subscribed total size in TB.
                    type: int
                usable_total_tb:
                    description: Usable total size in TB.
                    type: int
                usable_used_tb:
                    description: Usable used size in TB.
                    type: int
        srp_efficiency:
            description: Different entities to measure SRP efficiency.
            type: dict
            contains:
                compression_state:
                    description: Depicts the compression state of the SRP.
                    type: str
                data_reduction_enabled_percent:
                    description: Percentage of data reduction enabled in the
                                 SRP.
                    type: int
                data_reduction_ratio_to_one:
                    description: Data reduction ratio of SRP.
                    type: int
                overall_efficiency_ratio_to_one:
                    description: Overall efficiency ratio of SRP.
                    type: int
                snapshot_savings_ratio_to_one:
                    description: Snapshot savings ratio of SRP.
                    type: int
                virtual_provisioning_savings_ratio_to_one:
                    description: Virtual provisioning savings ratio of SRP.
                    type: int
        total_srdf_dse_allocated_cap_gb:
            description: Total SRDF dse allocated capacity in GB.
            type: int
Volumes:
    description: List of volumes on the array.
    returned: When the volumes exist.
    type: list
MetroDREnvironments:
    description: List of metro DR environments on the array.
    returned: When environment exists.
    type: list
SnapshotPolicies:
    description: List of snapshot policies on the array.
    returned: When snapshot policy exists.
    type: list
Initiators:
    description: List of initiators on the array.
    returned: When initiator exists.
    type: list
'''

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('info')

HAS_PYU4V = utils.has_pyu4v_sdk()
PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class Info(object):
    """Class with Gather Fact operations"""

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = get_info_parameters()
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False)
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
                         "access on Powermax")
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
        """Get the System Health information PowerMax/VMAX storage system"""
        try:
            LOG.info('Getting System Health information ')
            health_check = self.u4v_conn.system.get_system_health()
            LOG.info('Successfully listed System Health information ')
            return health_check
        except Exception as e:
            self.show_error_exit(msg=str(e))

    def get_system_alerts(self, filters_dict=None):
        """Get the alerts information PowerMax/VMAX storage system"""
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
                    error_msg = "Please provide input for filter sub-options."
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
        """Get the list of volumes of a given PowerMax/Vmax storage system"""

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
            return vol_list

        except Exception as e:
            msg = 'Get Volumes for array %s failed with error %s '\
                  % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_storage_group_list(self, filters_dict=None):
        """Get the list of storage groups of a given PowerMax/Vmax storage
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
        """Get the list of arrays of a given PowerMax/Vmax Unisphere host"""

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
        """Get the list of Storage Resource Pools of a given PowerMax/Vmax
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
        """Get the list of port groups of a given PowerMax/Vmax storage
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
        """Get the list of hosts of a given PowerMax/Vmax storage system"""

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
        """Get the list of host groups of a given PowerMax/Vmax storage
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
        """Get the list of ports of a given PowerMax/Vmax storage system"""

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
        """Get the list of masking views of a given PowerMax/Vmax storage
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

    def get_rdfgroup_list(self):
        """Get the list of rdf group of a given PowerMax/Vmax storage system
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
        """Get the list of metro DR environments of a given PowerMax/Vmax
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
            msg = 'Get metro DR environment for array %s failed with error ' \
                  '%s ' % (self.module.params['serial_no'], str(e))
            self.show_error_exit(msg=msg)

    def get_snapshot_policies_list(self):
        """Get the list of snapshot policies of a given PowerMax/Vmax
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
        """Get the list of initiators of a given PowerMax/Vmax
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
                LOG.info("Closing unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = "Failed to close unisphere connection with " \
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
            if 'mv' in str(subset):
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

            LOG.info("Closing unisphere connection %s", self.u4v_conn)
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
                Initiators=initiators)


def get_info_parameters():
    """This method provide the parameters required for the ansible
    modules on PowerMax"""

    return dict(
        unispherehost=dict(type='str', required=True, no_log=True),
        universion=dict(type='int', required=False, choices=[91, 92]),
        verifycert=dict(type='bool', required=True, choices=[True, False]),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        serial_no=dict(type='str', required=False, default=''),
        tdev_volumes=dict(type='bool', required=False,
                          default=True, choices=[True, False]),
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
                                    'initiators'
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
