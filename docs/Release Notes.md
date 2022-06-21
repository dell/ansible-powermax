
**Ansible Modules for Dell Technologies PowerMax** 
=========================================
### Release Notes 1.8.0

>   © 2022 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
--------
These release notes contain supplemental information about Ansible
Modules for Dell Technologies (Dell) PowerMax.

-   [Revision History](#revision-history)
-   [Product Description](#product-description)
-   [New Features & Enhancements](#new-features--enhancements)
-   [Known Issues](#known-issues)
-   [Limitations](#limitations)
-   [Distribution](#distribution)
-   [Documentation](#documentation)

Revision History
----------------

| **Date** | **Document revision** | **Description of changes** |
|----------|-----------------------|----------------------------|
| Jun 2022 | 01 | Ansible Modules for Dell PowerMax release 1.8.0 |

Product Description
-------------------

The Ansible Modules for Dell PowerMax are used for managing volumes,
storage groups, ports, port groups, host, host groups, masking views, initiators,
SRDF links, RDF groups, snapshots, job, snapshot policies, storage pools, role for automatic volume provisioning and Metro DR environments for PowerMax
arrays. The modules use playbooks to list, show, create, delete, and modify
each of the entities.

The Ansible Modules for Dell PowerMax supports the following
features:

-   Create volumes, storage groups, hosts, host groups, port groups,
    masking views, Metro DR environments, snapshot policies,
    and snapshots of a storage group.
-   Modify volumes, storage groups, hosts, host groups, Metro DR environments,
    snapshot policies, initiators and port groups in the array.
-   Delete volumes, storage groups, hosts, host groups, port groups,
    masking views, Metro DR environments, snapshot policies, and snapshots of a storage group.
-   Get details of volumes, storage groups, hosts, host groups, port,
    port groups, masking views, Metro DR environments, Job, RDF groups, 
    snapshot policies, storage pools, initiators and snapshots of a storage group.

New Features and Enhancements
---------------------------

The Ansible Modules for Dell PowerMax release has the following
changes:
- Enhanced storage group module to support moving volumes to destination storage group.
- Enhanced volume module to support renaming volumes created without a name.
- Renamed metro DR module input parameters.
- Added execution environment manifest file to support building an execution environment with ansible-builder.

> **NOTE:** Unisphere Version 9.1 is compatible with PowerMax Python
> library version 9.1.x.x and similarly Unisphere versions later than 9.1 will
> only work with Python library versions later than 9.1.x.x.

Known issues
------------
- Using automation, when the user tries to create a host with invalid initiators, an empty host is created even though it generates an error. However, when a modify scenario is run on this host without a pause, it generates an error saying "The requested host resource already exists.". Workaround is to add a pause(~20) between the two tasks.

Limitations
-----------
There are no known limitations.

Distribution
------------
The software package is available for download from the [Ansible Modules
for PowerMax GitHub](https://github.com/dell/ansible-powermax/tree/1.8.0) page.

Documentation
-------------
The documentation is available on the [Ansible Modules for PowerMax GitHub](../docs)
page. It includes the following:

   - README
   - Release Notes (this document)
   - Product Guide
