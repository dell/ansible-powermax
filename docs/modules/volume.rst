.. _volume_module:


volume -- Manage volumes on PowerMax Storage System
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing volumes on PowerMax storage system includes creating a volume, renaming a volume, expanding a volume, and deleting a volume.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  vol_name (optional, str, None)
    The name of the volume.


  sg_name (optional, str, None)
    The name of the storage group.


  new_sg_name (optional, str, None)
    The name of the target storage group.


  vol_id (optional, str, None)
    The native id of the volume.

    Required for rename and delete volume operations.


  size (optional, float, None)
    The new size of existing volume.

    Required for create and expand volume operations.


  cap_unit (optional, str, None)
    volume capacity units.

    If not specified, default value is GB.


  new_name (optional, str, None)
    The new volume identifier for the volume.


  vol_wwn (optional, str, None)
    The WWN of the volume.


  append_vol_id (optional, bool, None)
    Appends volume id to the volume name, Applicable from V4 (Juniper).


  state (True, str, None)
    Defines whether the volume should exist or not.


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
   - To expand a volume, either provide vol\_id or vol\_name or vol\_wwn and sg\_name.
   - size is required to create/expand a volume.
   - vol\_id is required to rename/delete a volume.
   - vol\_name, sg\_name and new\_sg\_name is required to move volumes between storage groups.
   - Deletion of volume will fail if the storage group is part of a masking view.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create volume
      dellemc.powermax.volume:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        vol_name: "{{vol_name}}"
        sg_name: "{{sg_name}}"
        size: 1
        cap_unit: "{{cap_unit}}"
        append_vol_id: true
        state: 'present'

    - name: Expanding volume size
      dellemc.powermax.volume:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        size: 3
        cap_unit: "{{cap_unit}}"
        vol_id: "0059B"
        state: 'present'

    - name: Renaming volume
      dellemc.powermax.volume:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        new_name: "Test_GOLD_vol_Renamed"
        vol_id: "0059B"
        state: 'present'

    - name: Delete volume using volume ID
      dellemc.powermax.volume:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        vol_id: "0059B"
        state: 'absent'

    - name: Delete volume using volume WWN
      dellemc.powermax.volume:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        vol_wwn: "60000970000197900237533030303246"
        state: 'absent'

    - name: Move volume between storage group
      dellemc.powermax.volume:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        vol_name: "{{vol_name}}"
        sg_name: "{{sg_name}}"
        new_sg_name: "{{new_sg_name}}"
        state: 'present'

    - name: Create volume with capacity unit as cylinder
      dellemc.powermax.volume:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        vol_name: "{{vol_name}}"
        sg_name: "{{sg_name}}"
        size: 1
        cap_unit: "CYL"
        state: 'present'



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


volume_details (When volume exists., complex, )
  Details of the volume.


  allocated_percent (, int, )
    Allocated percentage the volume.


  cap_cyl (, int, )
    Number of cylinders.


  cap_gb (, int, )
    Volume capacity in GB.


  cap_mb (, int, )
    Volume capacity in MB.


  effective_wwn (, str, )
    Effective WWN of the volume.


  emulation (, str, )
    Volume emulation type.


  encapsulated (, bool, )
    Flag for encapsulation.


  has_effective_wwn (, str, )
    Flag for effective WWN presence.


  mobility_id_enabled (, bool, )
    Flag for enabling mobility.


  num_of_front_end_paths (, int, )
    Number of front end paths in the volume.


  num_of_storage_groups (, int, )
    Number of storage groups in which volume is present.


  pinned (, bool, )
    Pinned flag.


  rdfGroupId (, int, )
    RDFG number for volume.


  reserved (, bool, )
    Reserved flag.


  snapvx_source (, bool, )
    Source SnapVX flag.


  snapvx_target (, bool, )
    Target SnapVX flag.


  ssid (, str, )
    SSID of the volume.


  status (, str, )
    Volume status.


  storageGroupId (, str, )
    Storage group ID of the volume.


  storage_groups (, list, )
    List of storage groups for the volume.


  type (, str, )
    Type of the volume.


  volumeId (, str, )
    Unique ID of the volume.


  volume_identifier (, str, )
    Name identifier for the volume.


  wwn (, str, )
    WWN of the volume.






Status
------





Authors
~~~~~~~

- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>
- Pavan Mudunuri (@Pavan-Mudunuri) <ansible.team@dell.com>

