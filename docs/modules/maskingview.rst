.. _maskingview_module:


maskingview -- Managing masking views on PowerMax/VMAX Storage System.
======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing masking views on PowerMax storage system includes, creating masking view with port group, storage group and host or host group, renaming masking view and deleting masking view.

For creating a masking view -

(i) portgroup\_name,

(ii) sg\_name and

(iii) any one of host\_name or hostgroup\_name is required.

All three entities must be present on the array.

For renaming a masking view, the 'new\_mv\_name' is required. After a masking view is created, only its name can be changed. No underlying entity (portgroup, storagegroup, host or hostgroup) can be changed on the masking view.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  mv_name (True, str, None)
    The name of the masking view. No Special Character support except for \_. Case sensitive for REST Calls.


  portgroup_name (optional, str, None)
    The name of the existing port group.


  host_name (optional, str, None)
    The name of the existing host. This parameter is to create an exclusive or host export.


  hostgroup_name (optional, str, None)
    The name of the existing host group. This parameter is used to create cluster export.


  sg_name (optional, str, None)
    The name of the existing storage group.


  new_mv_name (optional, str, None)
    The new name for the renaming function. No Special Character support except for \_. Case sensitive for REST Calls.


  state (True, str, None)
    Defines whether the masking view should exist or not.


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

    
    - name: Create MV with hostgroup
      dellemc.powermax.maskingview:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        mv_name: "{{mv_name}}"
        portgroup_name: "Ansible_Testing_portgroup"
        hostgroup_name: "Ansible_Testing_hostgroup"
        sg_name: "Ansible_Testing_SG"
        state: "present"

    - name: Create MV with host
      dellemc.powermax.maskingview:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        mv_name: "{{mv_name}}"
        portgroup_name: "Ansible_Testing_portgroup"
        host_name: "Ansible_Testing_host"
        sg_name: "Ansible_Testing_SG"
        state: "present"

    - name: Rename host masking view
      dellemc.powermax.maskingview:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        mv_name: "{{mv_name}}"
        new_mv_name: "Ansible_Testing_mv_renamed"
        state: "present"

    - name: Delete host masking view
      dellemc.powermax.maskingview:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        mv_name: "Ansible_Testing_mv_renamed"
        state: "absent"



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


create_mv (When masking view is created., bool, )
  Flag sets to true when a new masking view is created.


delete_mv (When masking view is deleted., bool, )
  Flag sets to true when a masking view is deleted.


modify_mv (When masking view is modified., bool, )
  Flag sets to true when a masking view is modified.


mv_details (When masking view exist., list, )
  Details of masking view.


  hostId (, str, )
    Host group present in the masking view.


  maskingViewId (, str, )
    Masking view ID.


  portGroupId (, str, )
    Port group present in the masking view.


  storageGroupId (, str, )
    Storage group present in the masking view.






Status
------





Authors
~~~~~~~

- Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
- Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>

