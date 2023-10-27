.. _info_module:


info -- Gathers information about PowerMax or VMAX storage entities
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gathers the list of specified PowerMax or VMAX storage system entities, such as the list of registered arrays, storage groups, hosts, host groups, storage groups, storage resource pools, port groups, masking views, initiators, array health status, alerts and metro DR environments, so on.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible 2.13, 2.14 or 2.15.



Parameters
----------

  serial_no (False, str, None)
    The serial number of the PowerMax or VMAX array. It is not required for getting the list of arrays.


  tdev_volumes (False, bool, True)
    Boolean variable to filter the volume list. This has a small performance impact. The default setting is True and; only TDEV volumes will be returned.

    True - Returns only the TDEV volumes.

    False - Rreturns all the volumes.


  gather_subset (False, list, None)
    List of string variables to specify the PowerMax or VMAX entities for which information is required.

    Required only if the serial_no is present.

    List of all PowerMax or VMAX entities supported by the module.

    To get alert summary information - alert.

    To get health status of a specific PowerMax array - health.

    To get volumes - vol.

    To get storage resource pools - srp.

    To get storage groups - sg.

    To get port groups - pg.

    To get hosts - host.

    To get host groups - hg.

    To get ports - port.

    To get masking views - mv.

    To get RDF groups - rdf.

    To get Metro DR environments - metro_dr_env.

    To get snapshot policies - snapshot_policies.

    To get initiators - initiators.

    To get masking view connections - mv_connections.


  filters (False, list, None)
    List of filters to support filtered output for storage entities.

    Each filter is a tuple of {filter_key, filter_operator, filter_value}.

    Supports passing of multiple filters.

    The storage entities, 'rdf', 'health', 'snapshot_policies' and 'metro_dr_env', does not support filters. Filters are ignored if passed.


    filter_key (True, str, None)
      Name identifier of the filter.


    filter_operator (True, str, None)
      Operation to be performed on filter key.


    filter_value (True, str, None)
      Value of the filter key.

  masking_view_name(False, str, None)
    The name of the masking view to fetch the masking view connections.


  unispherehost (True, str, None)
    IP or FQDN of the Unisphere host


  universion (False, int, None)
    Unisphere version, currently '91', '92' and '100' versions are supported.


  verifycert (True, str, None)
    Specifies system whether to validate SSL certificate or not, Values can be True or False or a custom file path for SSL certificate with .pem extension or .cer with base 64 encoding.


  user (True, str, None)
    The username of the Unisphere host.


  password (True, str, None)
    The password of the Unisphere host.





Notes
-----

.. note::
   - Filter functionality is supported only for the following 'filter_key' against specific 'gather_subset'.
   - For vol - allocated_percent, associated, available_thin_volumes, bound_tdev, cap_cyl, cap_gb, cap_mb, cap_tb, cu_image_num, cu_image_ssid, data_volume, dld, drv, effective_wwn, emulation, encapsulated, encapsulated_wwn, gatekeeper, has_effective_wwn, mapped, mobility_id_enabled, num_of_front_end_paths, num_of_masking_views, num_of_storage_groups, oracle_instance_name, physical_name, pinned, private_volumes, rdf_group_number, reserved, split_name, status, storageGroupId, symmlun, tdev, thin_bcv, type, vdev, virtual_volumes, volume_identifier, wwn.
   - For srp - compression_state, description, effective_used_capacity_percent, emulation, num_of_disk_groups, num_of_srp_sg_demands, num_of_srp_slo_demands, rdfa_dse, reserved_cap_percent, total_allocated_cap_gb, total_srdf_dse_allocated_cap_gb, total_subscribed_cap_gb, total_usable_cap_gb.
   - For sg - base_slo_name, cap_gb, child, child_sg_name, ckd, compression, compression_ratio_to_one, fba, num_of_child_sgs, num_of_masking_views, num_of_parent_sgs, num_of_snapshots, num_of_vols, parent, parent_sg_name, slo_compliance, slo_name, srp_name, storageGroupId, tag, volumeId.
   - For pg - dir_port, fibre, iscsi, num_of_masking_views, num_of_ports.
   - For host - host_group_name, num_of_host_groups, num_of_initiators, num_of_masking_views, num_of_powerpath_hosts, powerPathHostId.
   - For hg - host_name, num_of_hosts, num_of_masking_views.
   - For port - aclx, avoid_reset_broadcast, common_serial_number, director_status, disable_q_reset_on_ua, enable_auto_negotive, environ_set, hp_3000_mode, identifier, init_point_to_point, ip_list, ipv4_address, ipv6_address, iscsi_target, max_speed, negotiated_speed, neqotiate_reset, no_participating, node_wwn, num_of_cores, num_of_hypers, num_of_mapped_vols, num_of_masking_views, num_of_port_groups, port_interface, port_status, rdf_hardware_compression, rdf_hardware_compression_supported, rdf_software_compression, rdf_software_compression_supported, scsi_3, scsi_support1, siemens, soft_reset, spc2_protocol_version, sunapee, type, unique_wwn, vcm_state, vnx_attached, volume_set_addressing, wwn_node.
   - For mv - host_or_host_group_name, port_group_name, protocol_endpoint_masking_view, storage_group_name.
   - For alert - acknowledged, array, created_date, created_date_milliseconds, description, object, object_type, severity, state, type.
   - For initiators - alias, directorId, initiator_hba, in_a_host, iscsi, logged_in, num_of_host_groups, num_of_masking_views, num_of_powerpath_hosts, num_of_vols, on_fabric, port_flag_overrides, portId, powerPathHostId.
   - For mv_connections - volume_id, host_lun_address, cap_gb, initiator_id, alias, dir_port, logged_in, on_fabric.
   - The check_mode is supported.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    

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



Return Values
-------------

Arrays (When the arrays in Unisphere exist., list, )
  Aviliable list of arrays in Unisphere.


Health (When the array exist., complex, )
  The health status of the array.


  health_score_metric (, list, )
    An overall health score for the specified storage system.


    cached_date (, int, )
      A timestamp in epoch format from the date when it was cached.


    data_date (, int, )
      A timestamp in epoch format from the date it was collected.


    expired (, bool, )
      A flag to indicate the expiry of the score.


    health_score (, int, )
      An overall health score in numbers.


    instance_metrics (, list, )
      Metrics about a specific instance.


      health_score_instance_metric (, int, )
        The health score of a specific instance.



    metric (, str, )
      Information about the sub-system , such as SYSTEM_UTILIZATION, CONFIGURATION,CAPACITY, and so on.



  num_failed_disks (, int, )
    Numbers of the disk failure in this system.



Alerts (When the alert exists., list, )
  Alert summary of the array.


  acknowledged (, str, )
    Whether or not this alert is acknowledged.


  alertId (, str, )
    Unique ID of alert.


  array (, str, )
    The serial number of the array.


  created_date (, str, )
    The creation date.


  created_date_milliseconds (, str, )
    The creation date presented in milliseconds.


  description (, str, )
    The description of the alert.


  object (, str, )
    An object description.


  object_type (, str, )
    Resource class.


  severity (, str, )
    The severity of the alert.


  state (, str, )
    The state of the alert.


  type (, str, )
    The type of the alert.



HostGroups (When the hostgroups exist., list, )
  A list of Host Groups present on the array.


Hosts (When the hosts exist., list, )
  A list of hosts present on the array.


MaskingViews (When the masking views exist., list, )
  A list of masking views present on the array.


PortGroups (When the Port Groups exist., list, )
  A list of Port Groups on the array.


Ports (When the ports exist., complex, )
  A list of ports on the array.


  directorId (, str, )
    The director ID of the port.


  portId (, str, )
    The number of the port.



RDFGroups (When the RDF groups exist., complex, )
  A list of RDF groups on the array.


  label (, str, )
    Name of the RDF group.


  rdfgNumber (, int, )
    An unique identifier of the RDF group.



StorageGroups (When the storage groups exist., list, )
  A list of storage groups on the array.


StorageResourcePools (When the storage pools exist., complex, )
  A list of storage pools on the array.


  diskGroupId (, list, )
    The ID of the disk group.


  emulation (, str, )
    The type of volume emulation.


  num_of_disk_groups (, int, )
    The number of disk groups.


  rdfa_dse (, bool, )
    A flag for RDFA Delta Set Extension.


  reserved_cap_percent (, int, )
    The reserved capacity percentage.


  srpId (, str, )
    An unique Identifier for SRP.


  srp_capacity (, dict, )
    The different entities to measure SRP capacity.


    effective_used_capacity_percent (, int, )
      The percentage of effectively used capacity.


    snapshot_modified_tb (, int, )
      The snapshot modified in TB.


    snapshot_total_tb (, int, )
      The total snapshot size in TB.


    subscribed_allocated_tb (, int, )
      Subscribed allocated size in TB.


    subscribed_total_tb (, int, )
      Subscribed total size in TB.


    usable_total_tb (, int, )
      The usable total size in TB.


    usable_used_tb (, int, )
      The usable used size in TB.



  srp_efficiency (, dict, )
    The different entities to measure SRP efficiency.


    compression_state (, str, )
      Depicts the compression state of the SRP.


    data_reduction_enabled_percent (, int, )
      The percentage of data reduction enabled in the SRP.


    data_reduction_ratio_to_one (, int, )
      The data reduction ratio of SRP.


    overall_efficiency_ratio_to_one (, int, )
      The overall efficiency ratio of SRP.


    snapshot_savings_ratio_to_one (, int, )
      The snapshot savings ratio of SRP.


    virtual_provisioning_savings_ratio_to_one (, int, )
      The virtual provisioning savings ratio of SRP.



  total_srdf_dse_allocated_cap_gb (, int, )
    The total SRDF DSE allocated capacity in GB.



Volumes (When the volumes exist., list, )
  A list of volumes on the array.


MetroDREnvironments (When an environment exists., list, )
  A list of Metro DR environments on the array.


SnapshotPolicies (When a snapshot policy exists., list, )
  A list of the snapshot policies on the array.


Initiators (When an initiator exists., list, )
  A list of initiators on the array.


MVConnections (When the masking view connections exists., complex, {'masking_view_connections': [{'alias': '100000xxxx/100000xxxxxxxxx', 'cap_gb': '10.0', 'dir_port': 'XX-XX:11', 'host_lun_address': '0001', 'initiatorId': '100000aaaaaaa', 'logged_in': True, 'on_fabric': True, 'volumeId': '000XX'}], 'masking_view_id': 'mv-id-1'})
  A list of the masking view connections on the array.


  masking_view_id (, str, )
    The ID of the masking view.


  connections (, list, )
    A list of the masking view connections.






Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
- Pavan Mudunuri (@Pavan-Mudunuri) <ansible.team@dell.com>

