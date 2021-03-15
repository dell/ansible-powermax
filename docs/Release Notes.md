
**Ansible Modules for Dell EMC PowerMax** 
=========================================
### Release Notes 1.4

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
| February 2021 | 01 | Ansible Modules for Dell EMC PowerMax release 1.4 |

Product Description
-------------------

The Ansible Modules for Dell EMC PowerMax are used for managing volumes,
storage groups, ports, port groups, host, host groups, masking views,
SRDF links, RDF groups, snapshots, job and Metro DR environments for PowerMax
arrays. The modules use playbooks to list, show, create, delete, and modify
each of the entities.

The Ansible Modules for Dell EMC PowerMax supports the following
features:

-   Create volumes, storage groups, hosts, host groups, port groups,
    masking views, Metro DR environments, and snapshots of a storage group.
-   Modify volumes, storage groups, hosts, host groups, Metro DR environments,
    and port groups in the array.
-   Delete volumes, storage groups, hosts, host groups, port groups,
    masking views, Metro DR environments, and snapshots of a storage group.
-   Get details of volumes, storage groups, hosts, host groups, port,
    port groups, masking views, Metro DR environments, Job, RDF groups and
    snapshots of a storage group.

New Features & Enhancements
---------------------------

The Ansible Modules for Dell EMC PowerMax release 1.4 supports the
following features:

- The Metro DR module supports the following functionalities:
    - Create a Metro DR environment with the following replication modes:
        - Asynchronous
        - Adaptive copy
    - Get details of any specific Metro DR environment.
    - Convert an existing storage group into a Metro DR environment.
    - Modify Metro DR environment attributes.
    - Perform the following srdf_state change operations:
        - Split
        - Restore
        - SetMode
        - Failback
        - Failover
        - Establish
        - Suspend
        - UpdateR1
        - Recover
    - Delete a Metro DR environment.
- The Job module supports the following functionality:
    - Get Job details for a given Job ID.
- The following enhancements have been made to the gatherfacts module:
   - Get list of Metro DR environments present on the PowerMax array.
     > **NOTE:** Supports PyU4V 9.2.0 and above for Metro DR environments.
- The following enhancements have been made to the host module:
    - Host flags for host can be set explicitly by specifying the host_type.
- The following enhancements have been made to the host group module:
    - Host flags for host group can be set explicitly by specifying the host_type.
-   Support for Unisphere 9.1 and above
-   Support for Python version 2.8 and above
-   Support for PyU4V python library version 9.1.2.0 and above

> **NOTE:** Unisphere Version 9.1 is compatible with PowerMax Python
> library version 9.1.x.x and similarly Unisphere versions later than 9.1 will
> only work with Python library versions later than 9.1.x.x.

Known issues
------------
- Modify state operation from Establish to Suspend in Adaptive Copy mode in
  presence of force flag is not implemented. The REST API does not support
  this hence Python SDK (PyU4V) has no support for this operation.

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
