.. _process_storage_pool_dict_module:


process_storage_pool_dict -- Process storage pools on PowerMax/VMAX Storage System
==================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Process storage pools on PowerMax/VMAX storage system to find out the storage pool with maximum free storage.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  pool_data (True, list, None)
    Storage pool details including service levels, usable total space, usable free space, total free space.


  size (True, float, None)
    Size of the storage group in GB.


  sg_name (optional, str, None)
    Name of the storage group.


  service_level (optional, str, None)
    Service level of the storage group.


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
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get best suitable Pool using our python sorting module
      register: assigned_pool
      dellemc.powermax.process_storage_pool_dict:
        unispherehost: "{{unispherehost}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        pool_data: "{{ pools_list }}"
        size: 40
        service_level: "Diamond"
        sg_name: "intellgent_provisioning"



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


serial_no (when array satisfies the given criteria, str, )
  The PowerMax array on which storage pool resides


storage_pool (when storage pool exists satisfying the given criteria, str, )
  The ID of the storage pool


storage_group (when storage group exists satisfying the given criteria, str, )
  Name of the storage group


all_pools (when pool exists, list, )
  List of all pools on unisphere


  serial_no (when array satisfies the given criteria, str, )
    The PowerMax array on which storage pool resides


  storage_pool (when storage pool exists satisfying the given criteria, str, )
    The ID of the storage pool






Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- Akash Shendge (@shenda1) <ansible.team@dell.com>

