.. _metrodr_module:


metrodr -- Manage metro DR environment on PowerMax/VMAX Storage System
======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing a metro DR environment on a PowerMax storage system includes getting details of any specific metro DR environment, creating a metro DR environment, converting an existing SG into a metro DR environment, modifying metro DR environment attributes and deleting a metro DR environment.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  env_name (True, str, None)
    Name of the metro DR environment.

    Metro DR environment name will be unique across PowerMax.


  sg_name (False, str, None)
    Name of the storage group.

    Storage group will be present on the primary metro array and a storage group with the same name will be created on remote and DR arrays in a create operation.

    Storage group name is required in 'create metro DR environment' and 'convert SG into metro DR environment' operations.


  metro_r1_array_id (True, str, None)
    Serial number of the primary metro array.


  metro_r2_array_id (False, str, None)
    Serial number of the remote metro array.

    It is required only in create and convert operations.


  dr_array_id (False, str, None)
    Serial number of the DR array.

    It is required in create and convert operations.


  replication_mode (False, str, None)
    Replication mode whose value will indicate how the data will be replicated.

    It is required in create and modify operations.

    It is a mandatory parameter in a create operation but optional in a modify operation.


  wait_for_completion (False, bool, False)
    The flag indicates if the operation should be run synchronously or asynchronously.

    True signifies synchronous execution.

    By default, create and convert are asynchronous operations, whereas modify is a synchronous operation.


  new_rdf_group_r1 (False, bool, True)
    The flag indicates whether or not to create a new RDFG for a Metro R1 array to a DR array, or to autoselect from an existing one.

    Used in only create operation.


  new_rdf_group_r2 (False, bool, True)
    The flag indicates whether or not to create a new RDFG for a Metro R2 array to a DR array, or to autoselect from an existing one.

    It is used only in create operation.


  remove_r1_dr_rdfg (False, bool, False)
    The flag indicates whether or not to override default behavior and delete R11-R2 RDFG from the metro R1 side.

    It is used only in delete operations.


  srdf_param (False, dict, None)
    It contains parameters related to SRDF links.

    It is used only in modify operations.


    srdf_state (True, str, None)
      State of the SRDF link.

      It is a mandatory parameter for modify operations.


    metro (False, bool, False)
      The flag indicates whether or not to direct srdf\_state change towards the R1--R2 Metro Device leg of the metro DR environment.


    dr (False, bool, False)
      The flag indicates whether or not to direct srdf\_state change towards device pairs on the disaster recovery leg of the metro DR environment.


    keep_r2 (False, bool, False)
      The flag indicates whether or not in the case of srdf state suspend to make R2 data on metro available to the host.



  state (True, str, None)
    State variable to determine whether metro DR environment will exist or not.


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

    
    - name: Get metro environment details
      dellemc.powermax.metrodr:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        metro_r1_array_id: "{{metro_r1_array_id}}"
        env_name: "ansible_metrodr_env"
        state: "present"

    - name: Convert SG to metro DR environment
      dellemc.powermax.metrodr:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        sg_name: "ansible_sg"
        env_name: "ansible_metrodr_env"
        metro_r1_array_id: "{{metro_r1_array_id}}"
        metro_r2_array_id: "{{metro_r2_array_id}}"
        dr_array_id: "{{dr_array_id}}"
        replication_mode: "Asynchronous"
        wait_for_completion: false
        state: "present"

    - name: Create metro DR environment
      dellemc.powermax.metrodr:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        sg_name: "ansible_sg"
        env_name: "ansible_metrodr_env"
        metro_r1_array_id: "{{metro_r1_array_id}}"
        metro_r2_array_id: "{{metro_r2_array_id}}"
        dr_array_id: "{{dr_array_id}}"
        replication_mode: "Asynchronous"
        new_rdf_group_r1: true
        new_rdf_group_r2: true
        wait_for_completion: false
        state: "present"

    - name: Modify metro DR environment
      dellemc.powermax.metrodr:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        metro_r1_array_id: "{{metro_r1_array_id}}"
        env_name: "ansible_metrodr_env"
        srdf_param:
          srdf_state: "Suspend"
          metro: true
          dr: true
          keep_r2: true
        wait_for_completion: true
        state: "present"

    - name: Delete metro DR environment
      dellemc.powermax.metrodr:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        metro_r1_array_id: "{{metro_r1_array_id}}"
        env_name: "ansible_metrodr_env"
        remove_r1_dr_rdfg: true
        state: 'absent'



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


Job_details (When job exist., dict, )
  Details of the job.


  completed_date_milliseconds (, int, )
    Date of job completion in milliseconds.


  jobId (, str, )
    Unique identifier of the job.


  last_modified_date (, str, )
    Last modified date of job.


  last_modified_date_milliseconds (, int, )
    Last modified date of job in milliseconds.


  name (, str, )
    Name of the job.


  resourceLink (, str, )
    Resource link w.r.t Unisphere.


  result (, str, )
    Job description


  status (, str, )
    Status of the job.


  task (, list, )
    Details about the job.


  username (, str, )
    Unisphere username.



metrodr_env_details (When environment exists., dict, )
  Details of the metro DR environment link.


  capacity_gb (, float, )
    Size of volume in GB.


  dr_exempt (, bool, )
    Flag to indication that if there are exempt devices (volumes) in the DR site or not.


  dr_link_state (, str, )
    Status of DR site.


  dr_percent_complete (, int, )
    Percentage synchronized in DR session.


  dr_rdf_mode (, str, )
    Replication mode with DR site.


  dr_remain_capacity_to_copy_mb (, int, )
    Remaining capacity to copy at DR site.


  dr_service_state (, str, )
    The HA state of the DR session.


  dr_state (, str, )
    The pair states of the DR session.


  environment_exempt (, bool, )
    Flag to indication that if there are exempt devices (volumes) in the environment or not.


  environment_state (, str, )
    The state of the smart DR environment.


  metro_exempt (, bool, )
    Flag to indication that if there are exempt devices (volumes) in the DR site or not.


  metro_link_state (, str, )
    Status of metro site.


  metro_r1_array_health (, str, )
    Health status of metro R1 array.


  metro_r2_array_health (, str, )
    Health status of metro R1 array.


  metro_service_state (, str, )
    The HA state of the metro session.


  metro_state (, str, )
    The pair states of the metro session.


  metro_witness_state (, str, )
    The witness state of the metro session.


  name (, str, )
    The smart DR environment name.


  valid (, bool, )
    Flag to indicate whether valid environment or not.






Status
------





Authors
~~~~~~~

- Vivek Soni (@v-soni11) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

