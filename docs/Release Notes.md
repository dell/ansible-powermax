
**Ansible modules for Dell Technologies PowerMax** 
=========================================
### Release Notes 3.1.0

>   © 2022 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
--------
These release notes contain supplemental information about Ansible
modules for Dell Technologies (Dell) PowerMax.

-   [Revision History](#revision-history)
-   [Product Description](#product-description)
-   [New Features & Enhancements](#new-features--enhancements)
-   [Known Issues](#known-issues)
-   [Limitations](#limitations)
-   [Distribution](#distribution)
-   [Documentation](#documentation)

Revision History
----------------

| **Date**     | **Document revision** | **Description of changes**                      |
|------------  |-----------------------|-------------------------------------------------|
| July 2024 | 01                    | Ansible modules for Dell PowerMax release 3.1.0 |

Product Description
-------------------

The Ansible modules for Dell PowerMax are used for managing volumes,
storage groups, ports, port groups, host, host groups, masking views, initiators,
SRDF links, RDF groups, snapshots, job, snapshot policies, storage pools, role for automatic volume provisioning and Metro DR environments for PowerMax
arrays. The modules use playbooks to list, show, create, delete, and modify
each of the entities.

The Ansible modules for Dell PowerMax supports the following
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

The Ansible modules for Dell PowerMax release has the following
changes:
- Added Unisphere port parameter.
- Added support for restoration of storage group from a snapshot using Snapshot module.

> **NOTE:** Unisphere Version 9.1 is compatible with PowerMax Python
> library version 9.1.x.x and similarly Unisphere versions later than 9.1 will
> only work with Python library versions later than 9.1.x.x.

Known issues
------------
- When the user tries to create a host with invalid initiators using automation, an empty host is created despite generating an error. However, when a modify scenario is run on this host without a pause, it generates an error saying "The requested host resource already exists.". A workaround is to add a pause(~20) between the two tasks.

Limitations
-----------
There are no known limitations.

Distribution
------------
The software package is available for download from the [Ansible modules
for PowerMax GitHub](https://github.com/dell/ansible-powermax/tree/main) page.

Documentation
-------------
The documentation is available on the [Ansible modules for PowerMax GitHub](../docs)
page. It includes the following:

   - README
   - Release Notes (this document)
