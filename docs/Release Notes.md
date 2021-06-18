
**Ansible Modules for Dell EMC PowerMax** 
=========================================
### Release Notes 1.5.0

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
--------
These release notes contain supplemental information about Ansible
Modules for Dell EMC PowerMax.

-   Revision History
-   Product Description
-   New Features & Enhancements
-   Known issues
-   Limitations
-   Distribution
-   Documentation

Revision History
----------------

| **Date** | **Document revision** | **Description of changes** |
|----------|-----------------------|----------------------------|
| May 2021 | 01 | Ansible Modules for Dell EMC PowerMax release 1.5.0 |

Product Description
-------------------

The Ansible Modules for Dell EMC PowerMax are used for managing volumes,
storage groups, ports, port groups, host, host groups, masking views,
SRDF links, RDF groups, snapshots, job, snapshot policies, storage pools, role for automatic volume provisioning and Metro DR environments for PowerMax
arrays. The modules use playbooks to list, show, create, delete, and modify
each of the entities.

The Ansible Modules for Dell EMC PowerMax supports the following
features:

-   Create volumes, storage groups, hosts, host groups, port groups,
    masking views, Metro DR environments, snapshot policies,
    and snapshots of a storage group.
-   Modify volumes, storage groups, hosts, host groups, Metro DR environments,
    snapshot policies, and port groups in the array.
-   Delete volumes, storage groups, hosts, host groups, port groups,
    masking views, Metro DR environments, snapshot policies, and snapshots of a storage group.
-   Get details of volumes, storage groups, hosts, host groups, port,
    port groups, masking views, Metro DR environments, Job, RDF groups, 
    snapshot policies, storage pools, and snapshots of a storage group.

New Features & Enhancements
---------------------------

The Ansible Modules for Dell EMC PowerMax release 1.5.0 supports the
following features:

- The Snapshot policy module supports the following functionalities:
    - Create a snapshot policy.
    - Get details of any specific snapshot policy.
    - Modify the snapshot policy attributes.
    - Delete a snapshot policy.
      > **NOTE:** Supports PyU4V 9.2.1.3 and above.
- The storage pool module supports the following functionality:
    - Get storage pool details for a given storage pool.
- The following enhancements have been made to the gatherfacts module:
   - Get list of snapshot policies present on the PowerMax array.
     > **NOTE:** Supports PyU4V 9.2.1.3 and above for getting snapshot policy details
       and PyU4V 9.2.0.8 and above for getting snapshot details.
- The following enhancements have been made to the storage group module:
    - Snapshot policy can be associated/disassociated to/from a storage group.
      > **NOTE:** Supports PyU4V 9.2.1.3 and above.
- The following enhancements have been made to the snapshot module:
    - New parameter 'snapshot_id' has been added which indicates unique ID of snapshot.
    - snapshot_id is required for link, unlink, rename and delete operations.It is
      optional for getting details of snapshot.
      > **NOTE:** Supports PyU4V 9.2.0.8 and above.
- Following functionalities are available for ansible role for automatic volume placement:
    - Finding if there is enough capacity of the given service level in any array.
    - If multiple arrays available, return which is least used as 'assigned_pool'.
    - assigned_pool includes:
       - serial_no
       - srp_id
       - sg_name (if passed)
- The following enhancements have been made to the host module:
    - Check mode feature of ansible is enabled for host module.
- The following enhancements have been made to the host group module:
    - Check mode feature of ansible is enabled for host group module.    
- The following enhancements have been made to the volume module:
    - Check mode feature of ansible is enabled for volume module.
-   Support for Unisphere 9.1 and above
-   Support for Python version 2.8 and above
-   Support for PyU4V python library version 9.1.2.0 and above

> **NOTE:** Unisphere Version 9.1 is compatible with PowerMax Python
> library version 9.1.x.x and similarly Unisphere versions later than 9.1 will
> only work with Python library versions later than 9.1.x.x.

Known issues
------------
- Modify state operation from Establish to Suspend in Adaptive Copy mode in presence of force flag is not implemented. 
  The REST API does not support this hence Python SDK (PyU4V) has no support for this operation.
  
- Task to link a snapshot to a target storage group which is already linked is not implemented.
  The REST API does not support this hence Python SDK (PyU4V) has no support for this operation.

Limitations
-----------
There are no known limitations.

Distribution
------------
The software package is available for download from the [Ansible Modules
for PowerMax GitHub](https://github.com/dell/ansible-powermax) page.

Documentation
-------------
The documentation is available on [Ansible Modules for PowerMax GitHub](https://github.com/dell/ansible-powermax)
page. It includes the following:

   - README
   - Release Notes (this document)
   - Product Guide
