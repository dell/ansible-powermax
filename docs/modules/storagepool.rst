.. _storagepool_module:


storagepool -- Manage storage pools on PowerMax/VMAX storage system
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing storage pools on PowerMax storage system includes getting details of storage pools.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  pool (True, str, None)
    The name of the storage pool.


  state (True, str, None)
    State variable to determine whether storage pool will exist or not.


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
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get specific storage pool details
      dellemc.powermax.storagepool:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        pool: "SRP_1"
        state: "present"



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


pool_details (When storage pool exist., complex, )
  Details of the storage pool.


  serial_no (, str, )
    The PowerMax array on which storage pool resides


  service_levels (, list, )
    The service levels supported by storage pool


  srpId (, str, )
    The ID of the storage pool


  srp_capacity (, complex, )
    SRP capacity details


    effective_used_capacity_percent (, int, )
      The effective used capacity, expressed as a percentage


    usable_total_tb (, float, )
      Usable capacity of the storage pool in TB


    usable_used_tb (, float, )
      Used capacity of the storage pool in TB



  srp_efficiency (, complex, )
    SRP efficiency details


    compression_state (, str, )
      Indicates whether compression is enabled or disabled for this storage resource pool.



  total_free_tb (, str, )
    Free capacity of the storage pool in TB






Status
------





Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

