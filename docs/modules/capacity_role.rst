.. _capacity_role_module:


capacity_role -- This role provides basic support for Intelligent volume placement for PowerMax.
================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The role is intended for selecting the best suitable array and storage pool intelligently based on certain criteria accepted as user input. It scans through all available PowerMax arrays of the given Unisphere, to find available capacity, current load, service level etc. If the capacity is available in multiple arrays, it will prioritize the storage pool which is least used and returns the pool as 'assigned_pool'.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  capacity_role_size (True, float, None)
    The size of the storage group.


  capacity_role_cap_unit (True, str, GB)
    The capacity unit.


  service_level (optional, str, None)
    The service level supported by storage pool.


  sg_name (optional, str, None)
    The name of the storage group.


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

  port (optional, int, 8443)
    The port of the Unisphere host.



Notes
-----

.. note::
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
        - name: Include the PowerMax role to get the Serial Number and Assigned Pool
          include_role:
            name: capacity_role

        - name: Create storage group on the assigned serial number and SRP
          register: storage_group_details
          dellemc.powermax.storagegroup:
            unispherehost: "{{unispherehost}}"
            universion: "{{universion}}"
            verifycert: "{{verifycert}}"
            user: "{{user}}"
            password: "{{password}}"
            serial_no: "{{capacity_role_assigned_pool.serial_no}}"
            sg_name: "test_sg"
            service_level: "Diamond"
            srp: "{{capacity_role_assigned_pool.storage_pool}}"
            compression: True
            state: "present"

        - name: Create volume on the storage group
          dellemc.powermax.volume:
            unispherehost: "{{unispherehost}}"
            universion: "{{universion}}"
            verifycert: "{{verifycert}}"
            user: "{{user}}"
            password: "{{password}}"
            serial_no: "{{capacity_role_assigned_pool.serial_no}}"
            vol_name: "test_vol"
            sg_name: "test_sg"
            size: 10
            cap_unit: "GB"
            state: 'present'



Return Values
-------------

assigned_pool (When exists else returns "NOT_FOUND"., complex, )
  The role returns storage system (serial number) and pool (SRP name) with the lowest capacity utilization if the capacity provided by user is satisfied.


  changed (, bool, )
    Whether or not the resource has changed.


  serial_no (, str, )
    The serial number of the PowerMax/VMAX array.


  storage_group (, str, )
    Storage group of the volume.


  storage_pool (, str, )
    The ID of the storage pool.






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Pavan Mudunuri (@Pavan-Mudunuri) <ansible.team@dell.com>
