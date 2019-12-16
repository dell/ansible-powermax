# Ansible Modules for Dell EMC PowerMax

The Ansible Modules for Dell EMC PowerMax allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC PowerMax arrays.

The capabilities of Ansible modules are managing volumes, storage groups, ports, port groups, hosts, host groups, masking views, snapshots, SRDF,RDF group and gather high-level facts about the arrays. The options available for each capability are list, show, create, delete, and modify. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, so making multiple identical requests has the same effect as making a single request.

## Supported Platforms
  * Dell EMC PowerMax Arrays 5978.221.221 , 5978.444.444
  * Unisphere version 9.0 and 9.1

## Prerequisites
  * Ansible 2.6 or higher
  * Python 2.7 or 3.5
  * Red Hat Enterprise Linux 7.5
  * Python Library for PowerMax (PyU4V) 3.1.5 or higher
  * Please follow Py4UV installation instructions on https://pyu4v.readthedocs.io/

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It essentially means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC PowerMax
  * Volume module
  * Host module
  * Host group module
  * Snapshot module
  * Maskingview module
  * Port module
  * Port group module
  * Storage group module  
  * SRDF module
  * RDF group module
  * Gather facts module

## Installation
  
### For python 2.7 environment
  * Copy utils/dellemc_ansible_utils.py to  /usr/lib/python2.7/site-packages/ansible/module_utils/ 
  * Copy all module Python files in the 'powermax/library' folder to  /usr/lib/python2.7/site-packages/ansible/modules/storage/dellemc/
  * Copy dellemc.py from /doc_fragments folder to /usr/lib/python2.7/site-packages/ansible/plugins/doc_fragments/
### For python 3.5 environment
  * Copy utils/dellemc_ansible_utils.py to  /usr/lib/python3.5/site-packages/ansible/module_utils/
  * Copy all module Python files in the 'powermax/library' folder to  /usr/lib/python3.5/site-packages/ansible/modules/storage/dellemc/
  * Copy dellemc.py from /doc_fragments folder to /usr/lib/python3.5/site-packages/ansible/plugins/doc_fragments/
## Documentation

Check documentation from each module's file in /ansible-powermax/dellemc_ansible/powermax/library/

## Examples

Check examples from each module's file in /ansible-powermax/dellemc_ansible/powermax/library/


## Results
Each module returns the updated state and details of the entity, for example, if you are using the Volume module, all calls will return the updated details of the volume. Sample result is shown in each module's documentation.

## Support
Ansible for PowerMax Modules are supported by Dell EMC and are provided under the terms of the license attached to the source code.
For any setup, configuration issues, questions or feedback, join the [Dell EMC Automation community](https://www.dell.com/community/Automation/bd-p/Automation).
For any Dell EMC storage issues, please contact Dell support at: https://www.dell.com/support.
For clarity, Dell EMC does not provide support for any source code modifications.
