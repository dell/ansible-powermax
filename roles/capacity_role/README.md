Capacity Optimized Placement
============================

This role provides basic support for capacity optimized placement for PowerMax. The inputs are:
- capacity_role_size (integer) for the desired capacity
- capacity_role_cap_unit ('GB' or 'TB' -- default is 'GB') for the desired capacity
- service_level for the desired capacity
- Unisphere connection parameters

The role will scan all available PowerMax arrays with the given Unisphere, and find out if there 
is enough capacity of the given service level in any array. If the capacity is available in multiple 
arrays, it will prioritize the storage pool which is least used and return that pool as the
'capacity_role_assigned_pool'.

Requirements
------------

None

Role Variables
--------------

input variables:
- capacity_role_size (float)
- capacity_role_cap_unit ('GB' or 'TB' -- default is 'GB')
- service_level (string)
- sg_name (string)

Output variable:
- capacity_role_assigned_pool (string)

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

 GPL-3.0-or-later

Author Information
------------------

- Akash Shendge (@shenda1) <ansible.team@dell.com>
- Pavan Mudunuri (@Pavan-Mudunuri) <ansible.team@dell.com>
