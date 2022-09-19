# ansible-powermax Change Log
## Version 2.0.0 - released on 27/09/22
- Enhanced RDF group module to get volume pair information for an SRDF group.
- Enhanced storage group module to support for setting host I/O limits for existing storage groups and added ability to force move devices between storage groups with SRDF protection.
- Enhanced volume module to support cylinders option to specify size while creating LUN and added ability to create volumes with identifier_name and volume_id.
- Enhanced verifycert parameter in all modules to support file path for custom certificate location.
- Enhanced info module to get masking view connection information.

## Version 1.8.0 - released on 28/06/22
- Enhanced storage group module to support moving volumes to destination storage group.
- Enhanced volume module to support renaming volumes created without a name.
- Renamed metro DR module input parameters.
- Added execution environment manifest file to support building an execution environment with ansible-builder.

## Version 1.7.0 - released on 25/03/22
- Added initiator module to get initiator details and rename initiator alias.
- Added rotating file handler for log files.
- Renamed gatherfacts module to info module.
- Enhanced info module to list the initiators.
- Enhanced host module to add or remove initiators to or from host using alias.
- Removed dellemc_powermax prefix from module names.

## Version 1.6.1 - released on 16/12/21
- Fixed bugs in snapshot policy and masking view modules.

## Version 1.6.0 - released on 23/09/21
- Enabled the check mode feature for the storage group, port group, snapshot, snapshot policy, masking view, SRDF and metroDR modules.
- Added dual licensing.

## Version 1.5.0 - released on 18/06/21
- Added CRUD operations for the snapshot policy.
- Added get operation for storage pool.
- Enhanced the gatherfacts module to list the snapshot policies.
- Enhanced the storagegroup module to associate or disassociate the snapshot policy to or from a storage group.
- Enhanced the snapshot module to include the new parameter snapshot_id.
- Added the Ansible role for automatic volume placement.
- Enabled the check mode feature for the host, host group and volume modules.

## Version 1.4.0 - released on 15/03/21
- Added CRUD operations for Metro DR.
- Added the get operation for the job module.
- Enhanced the gatherfacts module to list metro DR environments.
- Enhanced the host module to set the host flags for the host explicitly by specifying the host_type.
- Enhanced the host group module to set the host flags for the host group by specifying the host_type.


## Version 1.3.0 - released on 11/12/20
- Enhanced the gatherfacts module to list alerts.

## Version 1.2.0 - released on 29/09/20
- Enhanced the storage group module to add or remove volumes to or from the SRDF protected storage group.
- Enhanced the volume module to add new volume to the SRDF protected storage group and expand the volume which is part of the storage group.
- Enhanced the SRDF module to support CRUD operations for concurrent configuration.
- Enhanced the gatherfacts module to get health status and support generic filters.

## Version 1.1.0 - released on 16/12/19
- Added CRUD operations for SRDF.
- Added get operation for RDF groups.
- Enhanced the volume module to support operations such as get, expand, move, rename and delete through WWN.
- Enhanced the gatherfacts module to list RDF groups.


## Version 1.0.0 - released on 17/07/19
- Added CRUD operations for host, host group, volume, storage group, masking view, snapshot, port group.
- Added get operation for port.
- Added gatherfacts module to list hosts, host groups, volumes, storage groups, masking views, snapshots, port groups and ports. 