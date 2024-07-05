.. _srdf_module:


srdf -- Manage SRDF pair on PowerMax/VMAX Storage System
========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Managing SRDF link on a PowerMax storage system includes creating an SRDF pair for a storage group, modifying the SRDF mode, modifying the SRDF state of an existing SRDF pair, and deleting an SRDF pair. All create and modify calls are asynchronous by default.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  sg_name (False, str, None)
    Name of storage group. SRDF pairings are managed at a storage group level.

    Required to identify the SRDF link.


  serial_no (True, str, None)
    The serial number will refer to the source PowerMax/VMAX array when protecting a storage group. However srdf\_state operations may be issued from primary or remote array.


  remote_serial_no (False, str, None)
    Integer 12-digit serial number of remote PowerMax or VMAX array.

    Required while creating an SRDF link.


  rdfg_no (False, int, None)
    The RDF group number.

    Optional parameter for each call. For a create operation, if specified, the array will reuse the RDF group, otherwise an error is returned. For modify and delete operations, if the RFD group number is not specified, and the storage group is protected by multiple RDF groups, then an error is raised.


  state (True, str, None)
    Define whether the SRDF pairing should exist or not.

    present indicates that the SRDF pairing should exist in system.

    absent indicates that the SRDF pairing should not exist in system.


  srdf_mode (False, str, None)
    The replication mode of the SRDF pair.

    Required when creating an SRDF pair.

    Can be modified by providing a required value.


  srdf_state (False, str, None)
    Desired state of the SRDF pairing. While creating a new SRDF pair, allowed values are 'Establish' and 'Suspend'. If the state is not specified, the pair will be created in a 'Suspended' state. When modifying the state, only certain changes are allowed.


  new_rdf_group (False, bool, None)
    Overrides the SRDF group selection functionality and forces the creation of a new SRDF group.

    PowerMax has a limited number of RDF groups. If this flag is set to True, and the RDF groups are exhausted, then SRDF link creation will fail.

    If not specified, default value is 'false'.


  wait_for_completion (False, bool, False)
    Flag to indicate if the operation should be run synchronously or asynchronously. True signifies synchronous execution. By default, all create and update operations will be run asynchronously.


  job_id (False, str, None)
    Job ID of an asynchronous task. Can be used to get details of a job.


  witness (False, bool, None)
    Flag to specify use of Witness for a Metro configuration. Setting to True signifies to use Witness, setting it to False signifies to use Bias. It is recommended to configure a witness for SRDF Metro in a production environment, this is configured via Unisphere for PowerMax UI or REST.

    The flag can be set only for modifying srdf\_state to either Establish, Suspend, or Restore.

    While creating a Metro configuration, the witness flag must be set to True.


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

    
    - name: Create and establish storagegroup SRDF/a pairing
      register: Job_details_body
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        remote_serial_no: "{{remote_serial_no}}"
        srdf_mode: 'Asynchronous'
        srdf_state: 'Establish'
        state: 'present'

    - name: Create storagegroup SRDF/s pair in default suspended mode as an
            Synchronous task
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name2}}"
        remote_serial_no: "{{remote_serial_no}}"
        state: 'present'
        srdf_mode: 'Synchronous'
        wait_for_completion: true

    - name: Create storagegroup Metro SRDF pair with Witness for resiliency
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        remote_serial_no: "{{remote_serial_no}}"
        state: 'present'
        srdf_mode: 'Active'
        wait_for_completion: true
        srdf_state: 'Establish'

    - name: Suspend storagegroup Metro SRDF pair
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        remote_serial_no: "{{remote_serial_no}}"
        state: 'present'
        srdf_state: 'Suspend'

    - name: Establish link for storagegroup Metro SRDF pair and use Bias for
            resiliency
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        remote_serial_no: "{{remote_serial_no}}"
        state: 'present'
        wait_for_completion: false
        srdf_state: 'Establish'
        witness: false

    - name: Get SRDF details
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        state: 'present'

    - name: Modify SRDF mode
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        srdf_mode: 'Synchronous'
        state: 'present'

    - name: Failover SRDF link
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        srdf_state: 'Failover'
        state: 'present'

    - name: Get SRDF Job status
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        job_id: "{{Job_details_body.Job_details.jobId}}"
        state: 'present'

    - name: Establish SRDF link
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name2}}"
        srdf_state: 'Establish'
        state: 'present'

    - name: Suspend SRDF link
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name2}}"
        srdf_state: 'Suspend'
        state: 'present'

    - name: Delete SRDF link
      dellemc.powermax.srdf:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        sg_name: "{{sg_name}}"
        state: 'absent'



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


Job_details (When job exist., list, )
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



SRDF_link_details (When SRDF link exists., complex, )
  Details of the SRDF link.


  hop2Modes (, str, )
    SRDF hop2 mode.


  hop2Rdfgs (, str, )
    Hop2 RDF group number.


  hop2States (, str, )
    SRDF hop2 state.


  largerRdfSides (, str, )
    Larger volume side of the link.


  localR1InvalidTracksHop1 (, int, )
    Number of invalid R1 tracks on local volume.


  localR2InvalidTracksHop1 (, int, )
    Number of invalid R2 tracks on local volume.


  modes (, str, )
    Mode of the SRDF pair.


  rdfGroupNumber (, int, )
    RDF group number of the pair.


  remoteR1InvalidTracksHop1 (, int, )
    Number of invalid R1 tracks on remote volume.


  remoteR2InvalidTracksHop1 (, int, )
    Number of invalid R2 tracks on remote volume.


  remoteSymmetrix (, str, )
    Remote symmetrix ID.


  states (, str, )
    State of the SRDF pair.


  storageGroupName (, str, )
    Name of storage group that is SRDF protected.


  symmetrixId (, str, )
    Primary symmetrix ID.


  totalTracks (, int, )
    Total number of tracks in the volume.


  volumeRdfTypes (, str, )
    RDF type of volume.






Status
------





Authors
~~~~~~~

- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

