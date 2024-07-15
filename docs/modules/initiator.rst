.. _initiator_module:


initiator -- Manage initiators on PowerMax/VMAX Storage System
==============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing initiators on a PowerMax storage system includes retrieving details and renaming alias of an initiator.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  initiator_id (optional, str, None)
    The initiator WWN or IQN.


  alias (optional, str, None)
    Alias of initiator.


  new_alias (optional, dict, None)
    Rename alias for specified initiator.


    new_node_name (optional, str, None)
      The new node name to rename the initiator alias.


    new_port_name (optional, str, None)
      The new port name to rename the initiator alias.



  state (True, str, None)
    The state of the initiator after the task is performed.

    absent - indicates that the initiator should not exist in the system.

    present - indicates that the initiator should exist in the system.


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
   - initiator\_id and alias are mutually exclusive parameters.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get initiator details using initiator id
      dellemc.powermax.initiator:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        initiator_id: 1000000000000001
        state: 'present'

    - name: Get initiator details using alias
      dellemc.powermax.initiator:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        alias: 'test/host_initiator'
        state: 'present'

    - name: Rename initiator alias using initiator id
      dellemc.powermax.initiator:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        initiator_id: 1000000000000001
        new_alias:
          new_node_name: 'test_rename'
          new_port_name: 'host_initiator_rename'
        state: 'present'

    - name: Rename initiator alias using alias
      dellemc.powermax.initiator:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        alias: 'test/host_initiator'
        new_alias:
          new_node_name: 'test_rename'
          new_port_name: 'host_initiator_rename'
        state: 'present'



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


initiator_details (When initiator exists., complex, )
  Details of the initiator.


  initiatorId (, str, )
    ID of the initiator.


  alias (, str, )
    Initiator alias.


  fabric_name (, str, )
    Fabric associated with the initiator.


  fcid (, str, )
    FCID associated with the initiator.


  host (, str, )
    Host associated with the initiator.


  hostGroup (, list, )
    Host groups associated with the initiator.


  logged_in (, bool, )
    States whether the initiator is logged in.






Status
------





Authors
~~~~~~~

- Jennifer John (@johnj9) <ansible.team@dell.com>

