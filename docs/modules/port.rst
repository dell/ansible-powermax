.. _port_module:


port -- Manage ports on PowerMax/VMAX Storage System
====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing ports on PowerMax storage system includes getting details of a port.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  ports (True, list, None)
    List of port director and port id


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

    
    - name: Get details of single/multiple ports
      dellemc.powermax.port:
        unispherehost: "{{unispherehost}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{array_id}}"
        ports:
          - director_id: "FA-1D"
            port_id: "5"
          - director_id: "SE-1F"
            port_id: "29"



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


port_details (When the port exist., list, )
  Details of the port.


  symmetrixPort (, list, )
    Type of volume.


    aclx (, bool, )
      Indicates whether access control logic is enabled or disabled.


    avoid_reset_broadcast (, bool, )
      Indicates whether the Avoid Reset Broadcasting feature is enabled or disabled.


    common_serial_number (, bool, )
      Indicates whether the Common Serial Number feature is enabled or disabled.


    director_status (, str, )
      Director status.


    disable_q_reset_on_ua (, bool, )
      Indicates whether the Disable Q Reset on UA (Unit Attention) is enabled or disabled.


    enable_auto_negotiate (, bool, )
      Indicates whether the Enable Auto Negotiate feature is enabled or disabled.


    environ_set (, bool, )
      Indicates whether the environmental error reporting feature is enabled or disabled.


    hp_3000_mode (, bool, )
      Indicates whether HP 3000 Mode is enabled or disabled.


    identifier (, str, )
      Unique identifier for port.


    init_point_to_point (, bool, )
      Indicates whether Init Point to Point is enabled or disabled.


    iscsi_target (, bool, )
      Indicates whether ISCSI target is enabled or disabled.


    maskingview (, list, )
      List of Masking views that the port is a part of.


    max_speed (, str, )
      Maximum port speed in GB/Second.


    negotiate_reset (, bool, )
      Indicates whether the Negotiate Reset feature is enabled or disabled.


    negotiated_speed (, str, )
      Negotiated speed in GB/Second.


    no_participating (, bool, )
      Indicates whether the No Participate feature is enabled or disabled.


    num_of_cores (, int, )
      Number of cores for the director.


    num_of_mapped_vols (, int, )
      Number of volumes mapped with the port.


    num_of_masking_views (, int, )
      Number of masking views associated with the port.


    num_of_port_groups (, int, )
      Number of port groups associated with the port.


    port_status (, str, )
      Port status, ON/OFF.


    portgroup (, list, )
      List of masking views associated with the port.


    scsi_3 (, bool, )
      Indicates whether the SCSI-3 protocol is enabled or disabled.


    scsi_support1 (, bool, )
      Indicates whether the SCSI Support1 is enabled or disabled.


    siemens (, bool, )
      Indicates whether the Siemens feature is enabled or disabled.


    soft_reset (, bool, )
      Indicates whether the Soft Reset feature is enabled or disabled.


    spc2_protocol_version (, bool, )
      Indicates whether the SPC2 Protocol Version feature is enabled or disabled.


    sunapee (, bool, )
      Indicates whether the Sunapee feature is enabled or disabled.


    symmetrixPortKey (, list, )
      Symmetrix system director and port in the port group.


      drectorId (, str, )
        Director ID of the port.


      portId (, str, )
        Port number of the port.



    type (, str, )
      Type of port.


    unique_wwn (, bool, )
      Indicates whether the Unique WWN feature is enabled or disabled.


    vnx_attached (, bool, )
      Indicates whether the VNX attached feature is enabled or disabled.


    volume_set_addressing (, bool, )
      Indicates whether Volume Vet Addressing is enabled or disabled.


    wwn_node (, str, )
      WWN node of port.







Status
------





Authors
~~~~~~~

- Ashish Verma (@vermaa31) <ansible.team@dell.com>

