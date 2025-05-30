.. _snapshot_module:


snapshot -- Manage Snapshots on PowerMax/VMAX Storage System
============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing snapshots on a PowerMax storage system includes the following operations.

Creating a new storage group (SG) snapshot.

Getting details of the SG snapshot.

Renaming the SG snapshot.

Changing the snapshot link status.

Deleting an existing SG snapshot.



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


  snapshot_name (True, str, None)
    The name of the snapshot.


  ttl (optional, str, None)
    The Time To Live (TTL) value for the snapshot.

    If the TTL is not specified, the storage group snap details are returned.

    However, to create a SG snap - TTL must be given.

    If the SG snap should not have any TTL - specify TTL as :literal:`None`.


  ttl_unit (optional, str, days)
    The unit for the :emphasis:`ttl`.

    If no :emphasis:`ttl\_unit` is specified, :literal:`days` is taken as default :emphasis:`ttl\_unit`.


  generation (optional, int, None)
    The generation number of the snapshot.

    Generation is required for link, unlink, rename and delete operations.

    Optional for Get snapshot details.

    Create snapshot will always create a new snapshot with a generation number 0.

    Rename is supported only for generation number 0.


  snapshot_id (optional, int, None)
    Unique ID of the snapshot.

    :emphasis:`snapshot\_id` is required for link, unlink, rename and delete operations.

    Optional for Get snapshot details.


  new_snapshot_name (optional, str, None)
    The new name of the snapshot.


  target_sg_name (optional, str, None)
    The target storage group.


  link_status (optional, str, None)
    Describes the link status of the snapshot.


  restore (optional, bool, None)
    Whether to restore a storage group to its snapshot.


  state (True, str, None)
    Define whether the snapshot should exist or not.


  unispherehost (True, str, None)
    IP or FQDN of the Unisphere host


  universion (False, int, None)
    Unisphere version. This parameter has been deprecated. It is no longer necessary to specify this parameter.


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
   - Paramters :emphasis:`generation` and :emphasis:`snapshot\_id` are mutually exclusive.
   - If :emphasis:`generation` or :emphasis:`snapshot\_id` is not provided then a list of generation against snapshot\_id is returned.
   - Use of :emphasis:`snapshot\_id` over :emphasis:`generation` is preferably recommended for PowerMax microcode version 5978.669.669 and onwards.
   - The :emphasis:`check\_mode` is supported.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a Snapshot for a Storage Group
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        ttl: "2"
        ttl_unit: "days"
        state: "present"

    - name: Get Storage Group Snapshot details
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        state: "present"

    - name: Get Storage Group Snapshot details using generation
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        generation: 1
        state: "present"

    - name: Get Storage Group Snapshot details using snapshot_id
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        snapshot_id: 135023964929
        state: "present"

    - name: Rename Storage Group Snapshot using generation
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        new_snapshot_name: "ansible_snap_new"
        generation: 0
        state: "present"

    - name: Rename Storage Group Snapshot using snapshot_id
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        new_snapshot_name: "ansible_snap_new"
        snapshot_id: 135023964929
        state: "present"

    - name: Change Snapshot Link Status to Linked using generation
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_snap_new"
        generation: 1
        target_sg_name: "ansible_sg_target"
        link_status: "linked"
        state: "present"

    - name: Change Snapshot Link Status to UnLinked using generation
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_snap_new"
        generation: 1
        target_sg_name: "ansible_sg_target"
        link_status: "unlinked"
        state: "present"

    - name: Change Snapshot Link Status to Linked using snapshot_id
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_snap_new"
        snapshot_id: 135023964515
        target_sg_name: "ansible_sg_target"
        link_status: "linked"
        state: "present"

    - name: Change Snapshot Link Status to UnLinked using snapshot_id
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_snap_new"
        snapshot_id: 135023964515
        target_sg_name: "ansible_sg_target"
        link_status: "unlinked"
        state: "present"

    - name: Restore storage group snapshot using generation
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        generation: 1
        restore: true
        state: "present"

    - name: Restore Storage Group Snapshot using snapshot_id
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        snapshot_id: 135023964929
        restore: true
        state: "present"

    - name: Delete Storage Group Snapshot using generation
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        generation: 1
        state: "absent"

    - name: Delete Storage Group Snapshot using snapshot_id
      dellemc.powermax.snapshot:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "ansible_sg"
        snapshot_name: "ansible_sg_snap"
        snapshot_id: 135023964929
        state: "absent"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


create_sg_snap (When snapshot is created., bool, false)
  Flag sets to true when the snapshot is created.


delete_sg_snap (When snapshot is deleted., bool, false)
  Flag sets to true when the snapshot is deleted.


rename_sg_snap (When snapshot is renamed., bool, false)
  Flag sets to true when the snapshot is renamed.


restore_sg_snap (When snapshot is restored., bool, false)
  Flag sets to true when the snapshot is restored.


sg_snap_details (When snapshot exists., complex, {'change_snap_link_status': '', 'changed': False, 'create_sg_snap': '', 'delete_sg_snap': '', 'rename_sg_snap': '', 'restore_sg_snap': '', 'sg_snap_details': {'generation': 0, 'isExpired': False, 'isLinked': False, 'isRestored': False, 'name': 'ansible_sample_snapshot', 'nonSharedTracks': 0, 'numSharedTracks': 0, 'numSourceVolumes': 1, 'numStorageGroupVolumes': 1, 'numUniqueTracks': 0, 'sourceVolume': [{'capacity': 547, 'capacity_gb': 1.0015869, 'name': '00205'}], 'state': ['Established'], 'timeToLiveExpiryDate': '09:55:28 Thu, 11 Jul 2024 +0000', 'timestamp': '09:55:28 Wed, 10 Jul 2024 +0000', 'timestamp_utc': 1720605328000, 'tracks': 0}})
  Details of the snapshot.


  generation/snapid (, int, )
    The generation/snapshot ID of the snapshot.


  expired (, bool, )
    Indicates whether the snapshot is expired or not.


  linked (, bool, )
    Indicates whether the snapshot is linked or not.


  restored (, bool, )
    Indicates whether the snapshot is restored or not.


  name (, str, )
    Name of the snapshot.


  non_shared_tracks (, int, )
    Number of non-shared tracks.


  num_source_volumes (, int, )
    Number of source volumes.


  num_storage_group_volumes (, int, )
    Number of storage group volumes.


  source_volume (, list, )
    Source volume details.


    capacity (, int, )
      Volume capacity.


    capacity_gb (, int, )
      Volume capacity in GB.


    name (, str, )
      Volume ID.



  state (, str, )
    State of the snapshot.


  time_to_live_expiry_date (, str, )
    Time to live expiry date.


  timestamp (, str, )
    Snapshot time stamp.


  timestamp_utc (, int, )
    Snapshot time stamp specified in UTC.


  tracks (, int, )
    Number of tracks.






Status
------





Authors
~~~~~~~

- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
- Trisha Datta (@trisha-dell) <ansible.team@dell.com>

