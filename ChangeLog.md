# ansible-powermax Change Log
## Version 1.6.0 - released on 23/09/21
- The check mode feature is enabled for the storage group, port group, snapshot, snapshot policy, masking view, SRDF and metroDR modules.
- Added dual licensing.

## Version 1.5.0 - released on 18/06/21
- Added CRUD operations for the snapshot policy.
- Added get operation for storage pool.
- Enhanced the gatherfacts module to list the snapshot policies.
- Enhanced the storagegroup module to associate/disassociate the snapshot policy to/from a storage group.
- Enhanced the snapshot module to include the new parameter snapshot_id.
- Added the ansible role for automatic volume placement.
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
- Enhanced the storage group module to add/remove volumes to/from the SRDF protected storage group.
- Enhanced the volume module to add new volume to the SRDF protected storage group, to expand the volume which is part of the storage group.
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