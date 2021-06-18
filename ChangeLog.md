# ansible-powermax Change Log
## Version 1.5.0 - released on 18/06/21
- Added CRUD operations for snapshot policy.
- Added get operation for storage pool.
- gatherfacts module is enhanced to list the snapshot policies.
- storagegroup module is enhanced to associate/disassociate snapshot policy to/from storage group.
- snapshot module is enhanced to include new parameter snapshot_id.
- Added ansible role for automatic volume placement.
- check mode feature is enabled for host, host group and volume module.

## Version 1.4.0 - released on 15/03/21
- Added CRUD operations for Metro DR.
- Added get operation for job module.
- gatherfacts module is enhanced to list metro DR environments.
- host module in enhanced to set the host flags for host explicitly by specifying host_type.
- host group module is enhanced to set the host flags for host group by specifying host_type.


## Version 1.3.0 - released on 11/12/20
- gatherfacts module is enhanced to list alerts.

## Version 1.2.0 - released on 29/09/20
- storage group module is enhanced to add/remove volumes to/from SRDF protected storage group.
- volume module is enhanced to add new volume to SRDF protected storage group, to expand volume which is part of storage group.
- SRDF module is enhanced to support CRUD operations for concurrent configuration.
- gatherfacts module is enhanced to get health status and supports generic filters.

## Version 1.1.0 - released on 16/12/19
- Added CRUD operations for SRDF.
- Added get operation for RDF groups.
- volume module is enhanced to support operations such as get, expand, move, rename and delete through WWN.
- gatherfacts module is enhanced to list RDF groups.


## Version 1.0.0 - released on 17/07/19
- Added CRUD operations for host, host group, volume, storage group, masking view, snapshot, port group.
- Added get operation for port.
- gatherfacts module is added to list hosts, host groups, volumes, storage groups, masking views, snapshots, port groups, ports. 