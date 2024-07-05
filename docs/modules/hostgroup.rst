.. _hostgroup_module:


hostgroup -- Manage a host group (cascaded initiator group) on a PowerMax/VMAX storage system
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing a host group on a PowerMax storage system includes creating a host group with a set of hosts, adding or removing hosts to or from a host group, renaming a host group, modifying host flags of a host group, and deleting a host group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  hostgroup_name (True, str, None)
    The name of the host group. No Special Character support except for \_. Case sensitive for REST Calls.


  hosts (optional, list, None)
    List of host names to be added to the host group or removed from the host group.

    Creation of an empty host group is allowed.


  state (True, str, None)
    Define whether the host group should be present or absent on the system.

    present - indicates that the host group should be present on the system.

    absent - indicates that the host group should be absent on the system.


  host_state (optional, str, None)
    Define whether the host should be present or absent in the host group.

    present-in-group - indicates that the hosts should exist in the host group.

    absent-in-group - indicates that the hosts should not exist in the host group.


  host_flags (False, dict, None)
    input as an yaml dictionary.

    List of all host\_flags -

    1. volume\_set\_addressing.

    2. disable\_q\_reset\_on\_ua.

    3. environ\_set.

    4. avoid\_reset\_broadcast.

    5. openvms.

    6. scsi\_3.

    7. spc2\_protocol\_version.

    8. scsi\_support1.

    9. consistent\_lun.

    Possible values are true, false, unset(default state).


  host_type (False, str, None)
    Describing the OS type (default or hpux).


  new_name (optional, str, None)
    The new name for the host group for the renaming function. No Special Character support except for \_. Case sensitive for REST Calls.


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
   - In the gather facts module, empty host groups will be listed as hosts.
   - host\_flags and host\_type are mutually exclusive parameters.
   - Hostgroups with 'default' host\_type will have 'default' hosts.
   - Hostgroups with 'hpux' host\_type will have 'hpux' hosts.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create host group with 'default' host_type
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_1"
        host_type: "default"
        hosts:
          - ansible_test_1
        host_state: 'present-in-group'
        state: 'present'

    - name: Create host group with 'hpux' host_type
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_2"
        host_type: "hpux"
        hosts:
          - ansible_test_2
        host_state: 'present-in-group'
        state: 'present'

    - name: Create host group with host_flags
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_3"
        hosts:
          - ansible_test_3
        state: 'present'
        host_state: 'present-in-group'
        host_flags:
          spc2_protocol_version: true
          consistent_lun: true
          volume_set_addressing: 'unset'
          disable_q_reset_on_ua: false
          openvms: 'unset'

    - name: Get host group details
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_1"
        state: 'present'

    - name: Adding host to host group
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_1"
        hosts:
          - Ansible_Testing_host2
        state: 'present'
        host_state: 'present-in-group'

    - name: Removing host from host group
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_1"
        hosts:
          - Ansible_Testing_host2
        state: 'present'
        host_state: 'absent-in-group'

    - name: Modify host group using host_type
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_1"
        host_type: "hpux"
        state: 'present'

    - name: Modify host group using host_flags
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_1"
        host_flags:
          spc2_protocol_version: unset
          disable_q_reset_on_ua: false
          openvms: false
          avoid_reset_broadcast: true
        state: 'present'

    - name: Rename host group
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_HG_1"
        new_name: "ansible_test_hostgroup_1"
        state: 'present'

    - name: Delete host group
      dellemc.powermax.hostgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        hostgroup_name: "ansible_test_hostgroup_1"
        state: 'absent'



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


hostgroup_details (When host group exist., complex, )
  Details of the host group.


  consistent_lun (, bool, )
    Flag for consistent LUN in the host group.


  enabled_flags (, list, )
    List of any enabled port flags overridden by the initiator.


  disabled_flags (, list, )
    List of any disabled port flags overridden by the initiator.


  host (, list, )
    List of hosts present in the host group.


    hostId (, str, )
      Unique identifier for the host.


    initiator (, list, )
      List of initiators present in the host.



  hostGroupId (, str, )
    Host group ID.


  maskingview (, list, )
    Masking view in which host group is present.


  num_of_hosts (, int, )
    Number of hosts in the host group.


  num_of_initiators (, int, )
    Number of initiators in the host group.


  num_of_masking_views (, int, )
    Number of masking views associated with the host group.


  port_flags_override (, bool, )
    Whether any of the initiator's port flags are overridden.


  type (, str, )
    Type of initiator of the hosts of the host group.






Status
------





Authors
~~~~~~~

- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

