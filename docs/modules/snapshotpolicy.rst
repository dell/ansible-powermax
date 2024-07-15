.. _snapshotpolicy_module:


snapshotpolicy -- Manage snapshot policy on PowerMax/VMAX Storage System
========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing a snapshot policy on a PowerMax storage system includes getting details of any specific snapshot policy, creating a snapshot policy, modifying snapshot policy attributes, modifying snapshot policy state, associating or disassociating storage groups to or from snapshot policy and deleting a snapshot policy.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  universion (False, int, None)
    Unisphere version, currently '92', '100' and '101' version is supported.


  snapshot_policy_name (True, str, None)
    Name of the snapshot policy.


  interval (False, str, None)
    The value of the interval counter for snapshot policy execution.


  secure (False, bool, None)
    Secure snapshots may only be terminated after they expire or by Dell Technologies support.

    If not specified, default value is False.


  snapshot_count (False, int, None)
    The max snapshot count of the policy.

    Max value is 1024.


  offset_mins (False, int, None)
    Defines when, within the interval the snapshots will be taken for a specified snapshot policy.

    The offset must be less than the interval of the snapshot policy.

    The format must be in minutes.

    If not specified, default value is 0.


  compliance_count_warning (False, int, None)
    If the number of valid snapshots falls below this number, the compliance changes to warning (yellow).


  compliance_count_critical (False, int, None)
    If the number of valid snapshots falls below this number, the compliance changes to critical (red).


  storage_groups (False, list, None)
    List of storage groups.


  storage_group_state (False, str, None)
    The state of the storage group with regard to the snapshot policy.

    present-in-policy indicates associate SG to SP.

    absent-in-policy indicates disassociate SG from SP.


  suspend (False, bool, None)
    Suspend the snapshot policy.

    True indicates snapshot policy is in suspend state.

    False indicates snapshot policy is in resume state.


  new_snapshot_policy_name (False, str, None)
    New name of the snapshot policy.


  state (True, str, None)
    Shows if the snapshot policy should be present or absent.


  unispherehost (True, str, None)
    IP or FQDN of the Unisphere host


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
   - The max number of snapshot policies on an array is limited to 20.
   - At most four snapshot policies can be associated with a storage group.
   - compliance\_count\_critical \<= compliance\_count\_warning \< total snapshot\_count for the policy.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a snapshot policy
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_1"
        interval: "10 Minutes"
        secure: false
        snapshot_count: 10
        offset_mins: 2
        compliance_count_warning: 6
        compliance_count_critical: 4
        state: "present"

    - name: Create a snapshot policy and associate storage groups to it
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_2"
        interval: "10 Minutes"
        secure: false
        snapshot_count: 12
        offset_mins: 5
        compliance_count_warning: 8
        compliance_count_critical: 4
        storage_groups:
          - "11_ansible_test_1"
          - "11_ansible_test_2"
        storage_group_state: "present-in-policy"
        state: "present"

    - name: Get snapshot policy details
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_2"
        state: "present"

    - name: Modify snapshot policy attributes
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_2"
        new_snapshot_policy_name: "10min_policy_2_new"
        interval: "10 Minutes"
        snapshot_count: 16
        offset_mins: 8
        compliance_count_warning: 9
        compliance_count_critical: 7
        state: "present"

    - name: Modify snapshot policy, associate to storage groups
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_1"
        storage_groups:
          - "11_ansible_test_1"
          - "11_ansible_test_2"
        storage_group_state: "present-in-policy"
        state: "present"

    - name: Modify snapshot policy, disassociate from storage groups
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_1"
        storage_groups:
          - "11_ansible_test_1"
          - "11_ansible_test_2"
        storage_group_state: "absent-in-policy"
        state: "present"

    - name: Modify snapshot policy state to suspend
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_1"
        suspend: true
        state: "present"

    - name: Modify snapshot policy state to resume
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_1"
        suspend: false
        state: "present"

    - name: Delete a snapshot policy
      dellemc.powermax.snapshotpolicy:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        snapshot_policy_name: "10min_policy_1"
        state: "absent"



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


snapshot_policy_details (When snapshot policy exists., complex, )
  Details of the snapshot policy.


  compliance_count_critical (, int, )
    The number of valid snapshots that have critical compliance.


  compliance_count_warning (, int, )
    The number of valid snapshots that have warning compliance.


  interval_minutes (, int, )
    The interval minutes for snapshot policy execution.


  last_time_used (, str, )
    The timestamp indicating the last time snapshot policy was used.


  offset_minutes (, int, )
    It is the time in minutes within the interval when the snapshots will be taken for a specified Snapshot Policy.


  secure (, bool, )
    True value indicates that the secure snapshots may only be terminated after they expire or by Dell Technologies support.


  snapshot_count (, int, )
    It is the max snapshot count of the policy.


  snapshot_policy_name (, str, )
    Name of the snapshot policy.


  storage_group_count (, int, )
    The number of storage groups associated with the snapshot policy.


  storage_group (, list, )
    The list of storage groups associated with the snapshot policy.


  storage_group_snapshotID (, list, )
    Pair of storage group and list of snapshot IDs associated with the snapshot policy.


  suspended (, bool, )
    The state of the snapshot policy, true indicates policy is in suspend state.


  symmetrixID (, str, )
    The symmetrix on which snapshot policy exists.






Status
------





Authors
~~~~~~~

- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

