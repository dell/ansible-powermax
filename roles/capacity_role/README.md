Capacity Optimized Placement
============================

This role provides basic support for capacity optimized placement for PowerMax. The inputs are:
- size (integer) for the desired capacity
- cap_unit ('GB' or 'TB' -- default is 'GB') for the desired capacity
- service_level for the desired capacity
- Unisphere connection parameters

The role will scan all available PowerMax arrays with the given Unisphere, and find out if there 
is enough capacity of the given service level in any array. If the capacity is available in multiple 
arrays, it will prioritize the storage pool which is least used and return that pool as the
'assigned_pool'.

Requirements
------------

None

Role Variables
--------------

input variables:
- size (float)
- cap_unit ('GB' or 'TB' -- default is 'GB')
- service_level (string)
- sg_name (string)

Output variable:
- assigned_pool (string)

Dependencies
------------

None

Example Playbook
----------------
- name: Include the PowerMax role to get the Serial Number and Assigned Pool
  include_role:
    name: capacity_role

License
-------

Apache 2

Author Information
------------------

- Akash Shendge (@shenda1) <ansible.team@dell.com>
