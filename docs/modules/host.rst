.. _host_module:


host -- Manage host (initiator group) on PowerMax/VMAX Storage System
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing hosts on a PowerMax storage system includes creating a host with a set of initiators and host flags, adding and removing initiators to or from a host, modifying host flag values, renaming a host, and deleting a host.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  host_name (True, str, None)
    The name of the host. No Special Character support except for \_. Case sensitive for REST Calls.

    Creation of an empty host is allowed.


  initiators (optional, list, None)
    List of Initiator WWN or IQN or alias to be added to or removed from the host.


  state (True, str, None)
    Define whether the host should exist or not.

    absent - indicates that the host should not exist in the system.

    present - indicates that the host should exist in the system.


  initiator_state (optional, str, None)
    Define whether the initiators should be present or absent on the host.

    absent-in-host - indicates that the initiators should not exist on the host.

    present-in-host - indicates that the initiators should exist on the host.

    Required when creating a host with initiators or adding and removing initiators to or from an existing host.


  host_flags (False, dict, None)
    Input as a yaml dictionary.

    List of all host\_flags-

    1. volume\_set\_addressing.

    2. disable\_q\_reset\_on\_ua.

    3. environ\_set.

    4. avoid\_reset\_broadcast.

    5. openvms.

    6. scsi\_3.

    7. spc2\_protocol\_version.

    8. scsi\_support1.

    9. consistent\_lun.

    Possible values are true, false, unset (default state).


  host_type (False, str, None)
    Describing the OS type.


  new_name (optional, str, None)
    The new name of the host for the renaming function. No Special Character support except for \_. Case sensitive for REST Calls.


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
   - host\_flags and host\_type are mutually exclusive parameters.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create host with host_type 'default'
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1"
        host_type: "default"
        state: 'present'

    - name: Create host with host_type 'hpux'
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_2"
        host_type: "hpux"
        state: 'present'

    - name: Create host with host_flags
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_3"
        initiators:
          - 1000000000000001
          - 'host/HBA01'
        host_flags:
          spc2_protocol_version: true
          consistent_lun: true
          volume_set_addressing: 'unset'
          disable_q_reset_on_ua: false
          openvms: 'unset'
        state: 'present'
        initiator_state: 'present-in-host'

    - name: Get host details
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1"
        state: 'present'

    - name: Adding initiator to host
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1"
        initiators:
          - 1000000000000001
          - 'host/HBA01'
        initiator_state: 'present-in-host'
        state: 'present'

    - name: Removing initiator from host
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1"
        initiators:
          - 1000000000000001
          - 'host/HBA01'
        initiator_state: 'absent-in-host'
        state: 'present'

    - name: Modify host using host_type
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1"
        host_type: "hpux"
        state: 'present'

    - name: Modify host using host_flags
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1"
        host_flags:
          spc2_protocol_version: unset
          consistent_lun: unset
          volume_set_addressing: true
          disable_q_reset_on_ua: false
          openvms: false
          avoid_reset_broadcast: true
        state: 'present'

    - name: Rename host
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1"
        new_name: "ansible_test_1_host"
        state: 'present'

    - name: Delete host
      dellemc.powermax.host:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        host_name: "ansible_test_1_host"
        state: 'absent'



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


host_details (When host exist., complex, )
  Details of the host.


  bw_limit (, int, )
    Bandwidth limit of the host.


  consistent_lun (, bool, )
    Flag for consistent LUN in host.


  enabled_flags (, list, )
    List of any enabled port flags overridden by the initiator.


  disabled_flags (, list, )
    List of any disabled port flags overridden by the initiator.


  hostId (, str, )
    Host ID.


  hostgroup (, list, )
    List of host groups that the host is associated with.


  initiator (, list, )
    List of initiators present in the host.


  maskingview (, list, )
    List of masking view in which the host group is present.


  num_of_hostgroups (, int, )
    Number of host groups associated with the host.


  num_of_initiators (, int, )
    Number of initiators present in the host.


  num_of_masking_views (, int, )
    Number of masking views associated with the host.


  num_of_powerpath_hosts (, int, )
    Number of PowerPath hosts associated with the host.


  port_flags_override (, bool, )
    Whether any of the initiator port flags are overridden.


  type (, str, )
    Type of initiator.






Status
------





Authors
~~~~~~~

- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

