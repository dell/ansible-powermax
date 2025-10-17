==============================
Dellemc.Powermax Release Notes
==============================

.. contents:: Topics
v4.0.1
======
- Bugfix for Github Issue 82

v4.0.0
======

Major Changes
-------------

- Added support for PowerMax 10.2.0.
- Removed deprecated field universion.

Minor Changes
-------------

- Added support to starting lun address when creating a masking view
- Bugfixes (Maskng view, SRDF, IOPs)
- Extended support for protected storage group
- Updates on Secuirty and Unit test coverage

v3.1.0
======

Minor Changes
-------------

- Added support for restoration of storage group from a snapshot using Snapshot module.
- Added unisphere port parameter.

v3.0.0
======

Major Changes
-------------

- Added support for PowerMax 10.1.0.

Minor Changes
-------------

- Added bug fix for SRDF module.
- Added support for connection timeout for all modules.

v2.2.1
======

Minor Changes
-------------

- Added fix for storagegroup_id keyword in storage group module.
- Added support for masking_view_name for listing masking view connections through info module.

v2.1.1
======

Minor Changes
-------------

- Added a note on idempotency for the storage group module.

v2.1.0
======

Minor Changes
-------------

- Added support of case insensitivity of host WWN to the host, and masking view module.
- Enhanced info module to get detail of volumes.
- Enhanced storage group module to support for making volume name as an optional parameter while adding a new volume to storage group.

v2.0.0
======

Major Changes
-------------

- Added support for PowerMax 10.0.0.

Minor Changes
-------------

- Enhanced RDF group module to get volume pair information for an SRDF group.
- Enhanced info module to get masking view connection information.
- Enhanced storage group module to support for setting host I/O limits for existing storage groups and added ability to force move devices between storage groups with SRDF protection.
- Enhanced verifycert parameter in all modules to support file path for custom certificate location.
- Enhanced volume module to support cylinders option to specify size while creating LUN and added ability to create volumes with identifier_name and volume_id.

v1.8.0
======

Minor Changes
-------------

- Added execution environment manifest file to support building an execution environment with ansible-builder.
- Enhanced storage group module to support moving volumes to destination storage group.
- Enhanced volume module to support renaming volumes created without a name.
- Renamed metro DR module input parameters.

v1.7.0
======

Minor Changes
-------------

- Added rotating file handler for log files.
- Enhanced host module to add or remove initiators to or from host using alias.
- Enhanced info module to list the initiators.
- Names of previously released modules have been changed from dellemc_powermax_\<module name> to \<module name>.
- Renamed gatherfacts module to info module.

New Modules
-----------

- dellemc.powermax.initiator - Manage initiators on PowerMax/VMAX Storage System

v1.6.1
======

Minor Changes
-------------

- Fixed bugs in snapshot policy and masking view modules.

v1.6.0
======

Minor Changes
-------------

- Added dual licensing.
- Enabled the check mode feature for the storage group, port group, snapshot, snapshot policy, masking view, SRDF and metroDR modules.

v1.5.0
======

Minor Changes
-------------

- Added the Ansible role for automatic volume placement.
- Enabled the check mode feature for the host, host group and volume modules.
- Enhanced the gatherfacts module to list the snapshot policies.
- Enhanced the snapshot module to include the new parameter snapshot_id.
- Enhanced the storagegroup module to associate or disassociate the snapshot policy to or from a storage group.

New Modules
-----------

- dellemc.powermax.process_storage_pool_dict - Process storage pools on PowerMax/VMAX Storage System
- dellemc.powermax.snapshotpolicy - Manage snapshot policy on PowerMax/VMAX Storage System
- dellemc.powermax.storagepool - Manage storage pools on PowerMax/VMAX storage system

v1.4.0
======

Minor Changes
-------------

- Enhanced the gatherfacts module to list metro DR environments.
- Enhanced the host group module to set the host flags for the host group by specifying the host_type.
- Enhanced the host module to set the host flags for the host explicitly by specifying the host_type.

New Modules
-----------

- dellemc.powermax.job - Gets the detail information about a Job of a PowerMax/VMAX storage system
- dellemc.powermax.metrodr - Manage metro DR environment on PowerMax/VMAX Storage System

v1.3.0
======

Minor Changes
-------------

- Enhanced the gatherfacts module to list alerts.

v1.2.0
======

Minor Changes
-------------

- Enhanced the SRDF module to support CRUD operations for concurrent configuration.
- Enhanced the storage group module to add or remove volumes to or from the SRDF protected storage group.
- Enhanced the storage group module to add or remove volumes to or from the SRDF protected storage group.
- Enhanced the volume module to add new volume to the SRDF protected storage group and expand the volume which is part of the storage group.

v1.1.0
======

Minor Changes
-------------

- Enhanced the gatherfacts module to list RDF Groups.
- Enhanced the volume module to support operations such as get, expand, move, rename and delete through WWN.

New Modules
-----------

- dellemc.powermax.rdfgroup - Gets the detail information about RDF Groups of a PowerMax or VMAX storage system
- dellemc.powermax.srdf - Manage SRDF pair on PowerMax/VMAX Storage System

v1.0.0
======

New Modules
-----------

- dellemc.powermax.host - Manage host (initiator group) on PowerMax/VMAX Storage System
- dellemc.powermax.hostgroup - Manage a host group (cascaded initiator group) on a PowerMax/VMAX storage system
- dellemc.powermax.info - Gathers information about PowerMax or VMAX storage entities
- dellemc.powermax.maskingview - Managing masking views on PowerMax/VMAX Storage System
- dellemc.powermax.port - Manage ports on PowerMax/VMAX Storage System
- dellemc.powermax.portgroup - Manage port groups on PowerMax/VMAX Storage System
- dellemc.powermax.snapshot - Manage Snapshots on PowerMax/VMAX Storage System
- dellemc.powermax.storagegroup - Manage storage groups on PowerMax or VMAX Storage System
- dellemc.powermax.volume - Manage volumes on PowerMax Storage System
