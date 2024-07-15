.. _rdfgroup_module:


rdfgroup -- Gets the detail information about RDF Groups of a PowerMax or VMAX storage system
=============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gets details of an RDF Group from a specified PowerMax or VMAX storage system.

Lists the volumes of an RDF Group from a specified PowerMax or VMAX storage system.

Get specific volume details of an RDF Group from a specified PowerMax or VMAX storage system.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  rdfgroup_number (True, str, None)
    Identifier of an RDF Group of type string.


  vol_name (False, str, None)
    Name of the volume.


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
   - The check\_mode is not supported.
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get the details of an RDF group and volumes
      dellemc.powermax.rdfgroup:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        serial_no: "{{serial_no}}"
        rdfgroup_number: "{{rdfgroup_id}}"

    - name: Get specific volume details of an RDF Group
      dellemc.powermax.rdfgroup:
        unispherehost: "{{unispherehost}}"
        serial_no: "{{serial_no}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        rdfgroup_number: "1"
        vol_name: "0001"



Return Values
-------------

changed (always, bool, false)
  Whether or not the resource has changed.


RDFGroupDetails (When the RDF group exists., list, {'RDFGroupVolumes': [{'largerRdfSide': 'Equal', 'localRdfGroupNumber': 1, 'localSymmetrixId': '0001XXX', 'localVolumeName': 'test_vol', 'localVolumeState': 'Ready', 'local_wwn_external': '00000001111', 'rdfMode': 'Active', 'rdfpairState': 'ActiveBias', 'remoteRdfGroupNumber': 63, 'remoteSymmetrixId': '0002XXX', 'remoteVolumeName': 'test_vol_1', 'remoteVolumeState': 'Ready', 'remote_wwn_external': '11111111', 'volumeConfig': 'RDFXXXXX'}], 'async': False, 'biasConfigured': True, 'biasEffective': True, 'device_polarity': 'RDF2', 'hardware_compression': False, 'label': 'ansible_test', 'link_limbo': 10, 'localOnlinePorts': [], 'localPorts': [], 'metro': True, 'modes': ['Active'], 'numDevices': 2, 'offline': False, 'rdfgNumber': 63, 'remoteOnlinePorts': [], 'remotePorts': [], 'remoteRdfgNumber': 63, 'remoteSymmetrix': '0001XXXXX', 'software_compression': False, 'totalDeviceCapacity': 20.0, 'type': 'Metro', 'vasa_group': False, 'witness': False, 'witnessConfigured': False, 'witnessDegraded': False, 'witnessEffective': False, 'witnessProtectedPhysical': False, 'witnessProtectedVirtual': False})
  Details of the RDF group.


  async (, bool, )
    Flag sets to true when an SRDF pair is in async mode.


  biasConfigured (, bool, )
    Flag for configured bias.


  biasEffective (, bool, )
    Flag for effective bias.


  device_polarity (, str, )
    Type of device polarity.


  hardware_compression (, bool, )
    Flag for hardware compression.


  label (, str, )
    RDF group label.


  link_limbo (, int, )
    The amount of time that the operating environment of the array waits after the SRDF link goes down before updating the status of the link. The link limbo value can be set from 0 to 120 seconds. The default value is 10 seconds.


  localOnlinePorts (, list, )
    List of local online ports.


  localPorts (, list, )
    List of local ports.


  metro (, list, )
    Flag for Metro configuration.


  modes (, str, )
    Mode of the SRDF link.


  numDevices (, int, )
    Number of devices involved in the pairing.


  offline (, bool, )
    Offline flag.


  rdfa_properties (, list, )
    Properties associated with the RDF group.


    average_cycle_time (, int, )
      Average cycle time in seconds that the session configured for.


    consistency_exempt_volumes (, bool, )
      Flag that indicates if consistency is exempt.


    cycle_number (, int, )
      Number of cycles in seconds.


    dse_active (, bool, )
      Flag for active Delta Set Extension.


    dse_autostart (, str, )
      Indicates DSE autostart state.


    dse_threshold (, int, )
      Flag for DSE threshold.


    duration_of_last_cycle (, int, )
      The cycle time in seconds of the most recently completed cycle.


    duration_of_last_transmit_cycle (, int, )
      Duration of last transmitted cycle in seconds.


    r1_to_r2_lag_time (, int, )
      Time that R2 is behind R1 in seconds.


    session_priority (, int, )
      Priority used to determine which RDFA sessions to drop if cache becomes full. Values range from 1 to 64, with 1 being the highest priority, meaning it is the last to be dropped.


    session_uncommitted_tracks (, int, )
      Number of uncommitted session tracks.


    transmit_idle_state (, str, )
      Indicates RDFA transmit idle state.


    transmit_idle_time (, int, )
      Time the transmit cycle has been idle.


    transmit_queue_depth (, int, )
      The transmitted queue depth of disks.



  rdfgNumber (, int, )
    RDF group number on primary device.


  remoteOnlinePorts (, list, )
    List of remote online ports.


  remotePorts (, list, )
    List of remote ports.


  remoteRdfgNumber (, int, )
    RDF group number at remote device.


  remoteSymmetrix (, int, )
    Remote device ID.


  software_compression (, bool, )
    Flag for software compression.


  totalDeviceCapacity (, int, )
    Total capacity of RDF group in GB.


  type (, str, )
    Type of RDF group.


  vasa_group (, bool, )
    Flag for VASA group member.


  witness (, bool, )
    Flag for witness.


  witnessConfigured (, bool, )
    Flag for configured witness.


  witnessDegraded (, bool, )
    Flag for degraded witness.


  witnessEffective (, bool, )
    Flag for effective witness.


  witnessProtectedPhysical (, bool, )
    Flag for physically protected witness.


  witnessProtectedVirtual (, bool, )
    Flag for virtually protected witness.


  RDFGroupVolumes (, list, )
    List of various properties of RDF group volumes.


    largerRdfSide (, str, )
      Larger RDF side among the devices.


    localRdfGroupNumber (, int, )
      RDF group number at primary device.


    localSymmetrixId (, int, )
      Primary device ID.


    localVolumeName (, str, )
      Volume name at primary device.


    localVolumeState (, str, )
      Volume state at primary device.


    local_wwn_external (, int, )
      External WWN of volume at primary device.


    rdfMode (, str, )
      SRDF mode of pairing.


    rdfpairState (, str, )
      SRDF state of pairing.


    remoteRdfGroupNumber (, int, )
      RDF group number at remote device.


    remoteSymmetrixId (, int, )
      Remote device ID.


    remoteVolumeName (, str, )
      Volume name at remote device.


    remoteVolumeState (, str, )
      Volume state at remote device.


    remote_wwn_external (, int, )
      External WWN of volume at remote device.


    volumeConfig (, str, )
      Type of volume.




RDFGroupVolumeDetails (When the RDF group volume exist., complex, {'largerRdfSide': 'Equal', 'localRdfGroupNumber': 1, 'localSymmetrixId': '0001XXX', 'localVolumeName': 'test_vol', 'localVolumeState': 'Ready', 'local_wwn_external': '00000001111', 'rdfMode': 'Active', 'rdfpairState': 'ActiveBias', 'remoteRdfGroupNumber': 63, 'remoteSymmetrixId': '0002XXX', 'remoteVolumeName': 'test_vol_1', 'remoteVolumeState': 'Ready', 'remote_wwn_external': '11111111', 'volumeConfig': 'RDFXXXXX'})
  RDF group volume details.


  largerRdfSide (, str, )
    Larger RDF side among the devices.


  localRdfGroupNumber (, int, )
    RDF group number at primary device.


  localSymmetrixId (, int, )
    Primary device ID.


  localVolumeName (, str, )
    Volume name at primary device.


  localVolumeState (, str, )
    Volume state at primary device.


  local_wwn_external (, int, )
    External WWN of volume at primary device.


  rdfMode (, str, )
    SRDF mode of pairing.


  rdfpairState (, str, )
    SRDF state of pairing.


  remoteRdfGroupNumber (, int, )
    RDF group number at remote device.


  remoteSymmetrixId (, int, )
    Remote device ID.


  remoteVolumeName (, str, )
    Volume name at remote device.


  remoteVolumeState (, str, )
    Volume state at remote device.


  remote_wwn_external (, int, )
    External WWN of volume at remote device.


  volumeConfig (, str, )
    Type of volume.






Status
------





Authors
~~~~~~~

- Arindam Datta (@dattaarindam) <ansible.team@dell.com>
- Ananthu S Kuttattu (@kuttattz) <ansible.team@dell.com>
- Pavan Mudunuri (@Pavan-Mudunuri) <ansible.team@dell.com>

