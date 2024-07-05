.. _storagegroup_module:


storagegroup -- Manage storage groups on PowerMax or VMAX Storage System
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing storage groups on a PowerMax storage system includes the following.

Listing the volumes of a storage group.

Creating a new storage group.

Deleting an existing storage group.

Adding existing volumes to an existing storage group.

Removing existing volumes from an existing storage group.

Creating new volumes in an existing storage group.

Modifying existing storage group attributes.

Adding child storage groups inside an existing storage group (parent).

Moving volumes between storage groups.

Removing a child storage group from an existing parent storage group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  sg_name (True, str, None)
    The name of the storage group.


  service_level (optional, str, None)
    The name of SLO.


  srp (optional, str, None)
    The name of the storage resource pool.

    This parameter is ignored if service\_level is not specified.

    Default is to use whichever is the default SRP on the array.


  compression (optional, bool, None)
    Compression on storage group.

    Compression parameter is ignored if service\_level is not specified.

    Default is true.


  volumes (optional, list, None)
    This is a list of volumes.

    Each volume has four attributes; vol\_name, size, cap\_unit, vol\_id.

    Volume ID must be provided for existing volumes.

    The size must be provided to add new volumes to SG.

    The cap\_unit is optional.

    Default value of cap\_unit is GB, choices are MB, GB, TB.


  vol_state (optional, str, None)
    Describes the state of volumes inside the SG.


  child_storage_groups (optional, list, None)
    This is a list of child storage groups.


  child_sg_state (optional, str, None)
    Describes the state of CSG inside parent SG.


  new_sg_name (optional, str, None)
    The new name of the storage group.


  target_sg_name (optional, str, None)
    The destination SG name to move the volumes to.


  force (optional, bool, None)
    This flag is to be set to True while moving volumes to target SG if volume is in a masking view.


  snapshot_policies (optional, list, None)
    List of snapshot policies.


  snapshot_policy_state (optional, str, None)
    Describes the state of snapshot policy for an SG.


  host_io_limit (optional, dict, None)
    Host I/O limit of the storage group.


    host_io_limit_iops (optional, int, None)
      The I/Os per second host I/O limit for the storage group.


    dynamic_distribution (optional, str, Never)
      The dynamic distribution of host I/O limit for the storage group.


    host_io_limit_mbps (optional, int, None)
      The MBs per second host I/O limit for the storage group.



  state (True, str, None)
    Define whether the storage group should exist or not.


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


  serial_no (True, str, None)
    The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module.





Notes
-----

.. note::
   - To set host\_io\_limit\_mbps to NOLIMIT, value can be provided as 0.
   - Idempotency is not supported when creating a new volume in the storage group without providing volume name.
   - The check\_mode is not supported.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get storage group details including volumes
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        state: "present"

    - name: Create empty storage group
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "foo"
        service_level: "Diamond"
        srp: "SRP_1"
        compression: true
        state: "present"

    - name: Delete the storage group
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "foo"
        state: "absent"

    - name: Adding existing volumes to existing SG
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "foo"
        state: "present"
        volumes:
          - vol_id: "00028"
          - vol_id: "00018"
          - vol_id: "00025"
        vol_state: "present-in-group"

    - name: Create new volumes for existing SG
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "foo"
        state: "present"
        volumes:
          - vol_name: "foo"
            size: 1
            cap_unit: "GB"
          - vol_name: "bar"
            size: 1
            cap_unit: "GB"
        vol_state: "present-in-group"

    - name: Remove volumes from existing SG
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "foo"
        state: "present"
        volumes:
          - vol_id: "00028"
          - vol_id: "00018"
          - vol_name: "ansible-vol"
        vol_state: "absent-in-group"

    - name: Move volumes to target SG
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "foo"
        target_sg_name: "foo_sg"
        force: true
        state: "present"
        volumes:
          - vol_id: "00028"
          - vol_id: "00018"
          - vol_name: "ansible-vol"
        vol_state: "absent-in-group"

    - name: Adding child SG to parent SG
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "parent_sg"
        state: "present"
        child_storage_groups:
          - "pie"
          - "bar"
        child_sg_state: "present-in-group"

    - name: Removing child SG from parent SG
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "parent_sg"
        state: "present"
        child_storage_groups:
          - "pie"
          - "bar"
        child_sg_state: "absent-in-group"

    - name: Rename storage group
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        new_sg_name: "ansible_sg_renamed"
        state: "present"

    - name: Create a storage group with snapshot policies
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_test_sg"
        service_level: "Diamond"
        srp: "SRP_1"
        compression: true
        snapshot_policies:
          - "10min_policy"
          - "30min_policy"
        snapshot_policy_state: "present-in-group"
        state: "present"

    - name: Add snapshot policy to a storage group
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_test_sg"
        snapshot_policies:
          - "15min_policy"
        snapshot_policy_state: "present-in-group"
        state: "present"

    - name: Remove snapshot policy from a storage group
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_test_sg"
        snapshot_policies:
          - "15min_policy"
        snapshot_policy_state: "absent-in-group"
        state: "present"

    - name: Set host I/O limits on an existing storage group
      dellemc.powermax.storagegroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "Test"
        host_io_limit:
          dynamic_distribution: "Always"
          host_io_limit_iops: 100
          host_io_limit_mbps: 100
        state: "present"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


add_child_sg (When value exists., bool, true)
  Sets to True when a child SG is added.


add_new_vols_to_sg (When value exists., bool, true)
  Sets to True when new volumes are added to the SG.


add_vols_to_sg (When value exists., bool, false)
  Sets to True when existing volumes are added to the SG.


added_vols_details (When value exists., list, ['0081A'])
  Volume IDs of the volumes added.


create_sg (When value exists., bool, true)
  Sets to True when a new SG is created.


delete_sg (When value exists., bool, true)
  Sets to True when an SG is deleted.


modify_sg (When value exists., bool, true)
  Sets to True when an SG is modified.


remove_child_sg (When value exists., bool, true)
  Sets to True when a child SG is removed.


remove_vols_from_sg (When value exists., bool, true)
  Sets to True when volumes are removed.


removed_vols_details (When value exists., list, ['0081A'])
  Volume IDs of the volumes removed.


rename_sg (When value exists., bool, true)
  Sets to True when an SG is renamed.


add_snapshot_policy_to_sg (When value exists., bool, true)
  Sets to True when snapshot policy is added to SG.


remove_snapshot_policy_to_sg (When value exists., bool, true)
  Sets to false when snapshot policy is removed from SG.


storage_group_details (When a storage group exists., complex, {'cap_gb': 6.01, 'compression': False, 'compression_ratio_to_one': 0.0, 'device_emulation': 'FBA', 'num_of_child_sgs': 0, 'num_of_masking_views': 0, 'num_of_parent_sgs': 0, 'num_of_snapshots': 0, 'num_of_vols': 6, 'slo': 'NONE', 'slo_compliance': 'NONE', 'srp': 'SRP_1', 'storageGroupId': 'sample_sg_name', 'type': 'Standalone', 'unprotected': True, 'unreducible_data_gb': 0.0, 'vp_saved_percent': 100.0})
  Details of the storage group.


  base_slo_name (, str, )
    Base Service Level Objective (SLO) of a storage group.


  cap_gb (, int, )
    Storage group capacity in GB.


  compression (, bool, )
    Compression flag.


  device_emulation (, str, )
    Device emulation type.


  num_of_child_sgs (, int, )
    Number of child storage groups.


  num_of_masking_views (, int, )
    Number of masking views associated with the storage group.


  num_of_parent_sgs (, int, )
    Number of parent storage groups.


  num_of_snapshots (, int, )
    Number of snapshots for the storage group.


  num_of_vols (, int, )
    Number of volumes in the storage group.


  service_level (, str, )
    Type of service level.


  slo (, str, )
    Service Level Objective type.


  slo_compliance (, str, )
    Type of SLO compliance.


  srp (, str, )
    Storage Resource Pool.


  storageGroupId (, str, )
    ID for the storage group.


  type (, str, )
    Type of storage group.


  unprotected (, bool, )
    Flag for storage group protection.


  vp_saved_percent (, int, )
    Percentage saved for virtual pools.


  hostIOLimit (, complex, )
    Host I/O limit of the storage group.


    iops (, int, )
      The I/Os per second host I/O limit for the storage group.


    dynamic_distribution (, str, )
      The dynamic distribution of host I/O limit for the storage group.


    mbps (, int, )
      The MBs per second host I/O limit for the storage group.




storage_group_volumes (When value exists., list, ['00773', '0081A'])
  Volume IDs of storage group volumes.


storage_group_volumes_details (When storage group volumes exist., complex, [{'effective_wwn': '60000970000197902573533030373733', 'type': 'TDEV', 'volumeId': '00773', 'volume_identifier': 'sample_sg_name', 'wwn': '60000970000197902573533030373733'}])
  Details of the storage group volumes.


  effective_wwn (, str, )
    Effective WWN of the volume.


  type (, str, )
    Type of the volume.


  volumeId (, str, )
    Unique ID of the volume.


  volume_identifier (, str, )
    Name associated with the volume.


  wwn (, str, )
    WWN of the volume.



snapshot_policy_compliance_details (When a snapshot policy is associated., complex, {'compliance': 'NONE', 'sl_compliance': [{'calculation_time': '2022-10-25T12:05', 'compliance': 'NONE', 'sl_name': 'ansible_SP4'}], 'sl_count': 1, 'storage_group_name': 'sample_sg_name'})
  The compliance status of this storage group.


  compliance (, str, )
    Compliance status.


  sl_compliance (, complex, )
    Compliance details.


    sl_name (, str, )
      Name of the snapshot policy.


    compliance (, str, )
      Compliance status.



  sl_count (, int, )
    Number of snapshot policies associated with storage group.


  storage_group_name (, str, )
    Name of the storage group.






Status
------





Authors
~~~~~~~

- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
- Pavan Mudunuri (@Pavan-Mudunuri) <ansible.team@dell.com>
- Trisha Datta (@Trisha-Datta) <ansible.team@dell.com>

