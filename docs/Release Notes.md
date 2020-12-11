
**Ansible Modules for Dell EMC PowerMax** 
=========================================
### Release Notes 1.3

>   © 2020 Dell Inc. or its subsidiaries. All rights reserved. Dell,
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Content
-------
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
| November 2020 | 01 | Ansible Modules for Dell EMC PowerMax release 1.3 |

Product Description
-------------------

The Ansible Modules for Dell EMC PowerMax are used for managing volumes,
storage groups, ports, port groups, host, host groups, masking views,
SRDF Links, RDF Groups, and snapshots for PowerMax arrays. The modules
use playbooks to list, show, create, delete, and modify each of the
entities.

The Ansible Modules for Dell EMC PowerMax supports the following
features:

-   Create volumes, storage groups, hosts, host groups, port groups,
    masking views, and snapshots of a storage group. 
-   Modify volumes, storage groups, hosts, host groups, and port
    groups in the array.
-   Delete volumes, storage groups, hosts, host groups, port groups,
    masking views, and snapshots of a storage group.
-   Get details of a port.
-   Get entities of the array.

New Features & Enhancements
---------------------------

The Ansible Modules for Dell EMC PowerMax release 1.3 supports the
following features:

- The following enhancements have been made to the gatherfacts module:
   - Get list of alerts present on the PowerMax array.
     > **NOTE:** Supports PyU4V 9.2.0 and above for alerts.

-   Support for Unisphere 9.1 and above
-   Support for Python version 2.8 and above
-   Support for PyU4V python library version 9.1.2.0 and above

> **NOTE:** Unisphere Version 9.1 is compatible with PowerMax Python
> library version 9.1.x.x and similarly Unisphere versions later than 9.1 will
> only work with Python library versions later than 9.1.x.x.

Known issues
------------
There are no known issues.

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
