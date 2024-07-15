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
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  serial_no (False, str, )
    The serial number of the PowerMax or VMAX array. It is not required for getting the list of arrays.


  tdev_volumes (False, bool, True)
    Boolean variable to filter the volume list. This has a small performance impact. The default setting is True and; only TDEV volumes will be returned.

    True - Returns only the TDEV volumes.

    False - Rreturns all the volumes.


  gather_subset (False, list, None)
    List of string variables to specify the PowerMax or VMAX entities for which information is required.

    Required only if the serial\_no is present.

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

    To get Metro DR environments - metro\_dr\_env.

    To get snapshot policies - snapshot\_policies.

    To get initiators - initiators.

    To get masking view connections - mv\_connections.


  filters (False, list, None)
    List of filters to support filtered output for storage entities.

    Each filter is a tuple of {filter\_key, filter\_operator, filter\_value}.

    Supports passing of multiple filters.

    The storage entities, 'rdf', 'health', 'snapshot\_policies' and 'metro\_dr\_env', does not support filters. Filters are ignored if passed.


    filter_key (True, str, None)
      Name identifier of the filter.


    filter_operator (True, str, None)
      Operation to be performed on filter key.


    filter_value (True, str, None)
      Value of the filter key.



  masking_view_name (optional, str, None)
    The name of the masking view to fetch the masking view connections.


  unispherehost (True, str, None)
    IP or FQDN of the Unisphere host


  universion (False, int, None)
    Unisphere version, currently '91', '92', '100' and '101' versions are supported.


  verifycert (True, str, None)
    Specifies system whether to validate SSL certificate or not, Values can be True or False or a custom file path for SSL certificate with .pem extension or .cer with base 64 encoding.


  user (True, str, None)
    The username of the Unisphere host.


  password (True, str, None)
    The password of the Unisphere host.


  timeout (optional, int, 120)
    Time after which the connection will get terminated.

    It is to be mentioned in seconds.


  port (optional, int, 8443)
    The port of the Unisphere host.





Notes
-----

.. note::
   - Filter functionality is supported only for the following 'filter\_key' against specific 'gather\_subset'.
   - For vol - allocated\_percent, associated, available\_thin\_volumes, bound\_tdev, cap\_cyl, cap\_gb, cap\_mb, cap\_tb, cu\_image\_num, cu\_image\_ssid, data\_volume, dld, drv, effective\_wwn, emulation, encapsulated, encapsulated\_wwn, gatekeeper, has\_effective\_wwn, mapped, mobility\_id\_enabled, num\_of\_front\_end\_paths, num\_of\_masking\_views, num\_of\_storage\_groups, oracle\_instance\_name, physical\_name, pinned, private\_volumes, rdf\_group\_number, reserved, split\_name, status, storageGroupId, symmlun, tdev, thin\_bcv, type, vdev, virtual\_volumes, volume\_identifier, wwn.
   - For srp - compression\_state, description, effective\_used\_capacity\_percent, emulation, num\_of\_disk\_groups, num\_of\_srp\_sg\_demands, num\_of\_srp\_slo\_demands, rdfa\_dse, reserved\_cap\_percent, total\_allocated\_cap\_gb, total\_srdf\_dse\_allocated\_cap\_gb, total\_subscribed\_cap\_gb, total\_usable\_cap\_gb.
   - For sg - base\_slo\_name, cap\_gb, child, child\_sg\_name, ckd, compression, compression\_ratio\_to\_one, fba, num\_of\_child\_sgs, num\_of\_masking\_views, num\_of\_parent\_sgs, num\_of\_snapshots, num\_of\_vols, parent, parent\_sg\_name, slo\_compliance, slo\_name, srp\_name, storageGroupId, tag, volumeId.
   - For pg - dir\_port, fibre, iscsi, num\_of\_masking\_views, num\_of\_ports.
   - For host - host\_group\_name, num\_of\_host\_groups, num\_of\_initiators, num\_of\_masking\_views, num\_of\_powerpath\_hosts, powerPathHostId.
   - For hg - host\_name, num\_of\_hosts, num\_of\_masking\_views.
   - For port - aclx, avoid\_reset\_broadcast, common\_serial\_number, director\_status, disable\_q\_reset\_on\_ua, enable\_auto\_negotive, environ\_set, hp\_3000\_mode, identifier, init\_point\_to\_point, ip\_list, ipv4\_address, ipv6\_address, iscsi\_target, max\_speed, negotiated\_speed, neqotiate\_reset, no\_participating, node\_wwn, num\_of\_cores, num\_of\_hypers, num\_of\_mapped\_vols, num\_of\_masking\_views, num\_of\_port\_groups, port\_interface, port\_status, rdf\_hardware\_compression, rdf\_hardware\_compression\_supported, rdf\_software\_compression, rdf\_software\_compression\_supported, scsi\_3, scsi\_support1, siemens, soft\_reset, spc2\_protocol\_version, sunapee, type, unique\_wwn, vcm\_state, vnx\_attached, volume\_set\_addressing, wwn\_node.
   - For mv - host\_or\_host\_group\_name, port\_group\_name, protocol\_endpoint\_masking\_view, storage\_group\_name.
   - For alert - acknowledged, array, created\_date, created\_date\_milliseconds, description, object, object\_type, severity, state, type.
   - For initiators - alias, directorId, initiator\_hba, in\_a\_host, iscsi, logged\_in, num\_of\_host\_groups, num\_of\_masking\_views, num\_of\_powerpath\_hosts, num\_of\_vols, on\_fabric, port\_flag\_overrides, portId, powerPathHostId.
   - For mv\_connections - volume\_id, host\_lun\_address, cap\_gb, initiator\_id, alias, dir\_port, logged\_in, on\_fabric.
   - The check\_mode is supported.
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
      Information about the sub-system , such as SYSTEM\_UTILIZATION, CONFIGURATION,CAPACITY, and so on.



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
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

