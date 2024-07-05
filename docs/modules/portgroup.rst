.. _portgroup_module:


portgroup -- Manage port groups on PowerMax/VMAX Storage System
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing port groups on a PowerMax storage system includes creating a port group with a set of ports, adding or removing single or multiple ports to or from the port group, renaming the port group and deleting the port group.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  portgroup_name (True, str, None)
    The name of the port group. No Special Character support except for \_. Case sensitive for REST Calls.


  ports (False, list, None)
    List of directors and ports to be added or removed to or from the port group.


  port_group_protocol (False, str, None)
    Port Group protocol.

    Required only for V4(Juniper).


  new_name (False, str, None)
    New name of the port group while renaming. No Special Character support except for \_. Case sensitive for REST Calls.


  state (True, str, None)
    Define whether the port group should exist or not.

    present - indicates that the port group should be present on the system.

    absent - indicates that the port group should not be present on the system.


  port_state (False, str, None)
    Define whether the port should be present or absent in the port group.

    present-in-group - indicates that the ports should be present on a port group object.

    absent-in-group - indicates that the ports should not be present on a port group object.


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

    
    - name: Create port group without ports
      dellemc.powermax.portgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        portgroup_name: "{{portgroup_name}}"
        state: "present"

    - name: Create port group in V4 without ports
      dellemc.powermax.portgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        portgroup_name: "new_PG"
        port_group_protocol: "SCSI_FC"
        state: "present"

    - name: Create port group with ports
      dellemc.powermax.portgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        portgroup_name: "{{portgroup_name}}"
        state: "present"
        ports:
          - director_id: "FA-1D"
            port_id: "5"
          - director_id: "FA-2D"
            port_id: "5"
        port_state: "present-in-group"

    - name: Add ports to port group
      dellemc.powermax.portgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        portgroup_name: "{{portgroup_name}}"
        state: "present"
        ports:
          - director_id: "FA-2D"
            port_id: "8"
          - director_id: "FA-2D"
            port_id: "9"
        port_state: "present-in-group"

    - name: Remove ports from port group
      dellemc.powermax.portgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        portgroup_name: "{{portgroup_name}}"
        state: "present"
        ports:
          - director_id: "FA-2D"
            port_id: "8"
          - director_id: "FA-2D"
            port_id: "9"
        port_state: "absent-in-group"

    - name: Modify port group
      dellemc.powermax.portgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        portgroup_name: "{{portgroup_name}}"
        state: "present"
        new_name: "{{new_name}}"

    - name: Delete port group
      dellemc.powermax.portgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        portgroup_name: "{{portgroup_name}}"
        state: "absent"



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


portgroup_details (When the port group exist., list, )
  Details of the port group.


  num_of_masking_views (, int, )
    Number of masking views in where port group is associated.


  num_of_ports (, int, )
    Number of ports in the port group.


  portGroupId (, str, )
    Port group ID.


  symmetrixPortKey (, list, )
    Symmetrix system director and port in the port group.


    directorId (, str, )
      Director ID of the port.


    portId (, str, )
      Port number of the port.



  type (, str, )
    Type of ports in port group.






Status
------





Authors
~~~~~~~

- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Ashish Verma (@vermaa31) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

