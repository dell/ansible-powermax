
**Ansible Modules for Dell EMC PowerMax** 
=========================================
### Release Notes 1.6.0

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
| Sept 2021 | 01 | Ansible Modules for Dell EMC PowerMax release 1.6.0 |

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

The Ansible Modules for Dell EMC PowerMax release 1.6.0 supports the
following features:
- The following enhancements have been made to the storage group module:
    - Check mode feature of Ansible is enabled for the storage group module.    
- The following enhancements have been made to the port group module:
    - Check mode feature of Ansible is enabled for the port group module.   
- The following enhancements have been made to the snapshot module:
    - Check mode feature of Ansible is enabled for the snapshot module.
- The following enhancements have been made to the snapshot policy module:
    - Check mode feature of Ansible is enabled for the snapshot policy module. 
- The following enhancements have been made to the masking view module:
    - Check mode feature of Ansible is enabled for the masking view module.
- The following enhancements have been made to the SRDF module:
    - Check mode feature of Ansible is enabled for the SRDF module.
- The following enhancements have been made to the metroDR module:
    - Check mode feature of Ansible is enabled for the metroDR module.
- Added dual licensing.    
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

- Using automation, when the user tries to create a host with invalid initiators, an empty host is created even though it generates an error. However, when a modify scenario is run on this host without a pause, it generates an error saying "The requested host resource already exists.". Workaround is to add a pause(~20) between the two tasks.

Limitations
-----------
There are no known limitations.

Distribution
------------
The software package is available for download from the [Ansible Modules
for PowerMax GitHub](https://github.com/dell/ansible-powermax) page.

Documentation
-------------
The documentation is available on the [Ansible Modules for PowerMax GitHub](https://github.com/dell/ansible-powermax)
page. It includes the following:

   - README
   - Release Notes (this document)
   - Product Guide
