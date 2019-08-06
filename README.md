Ansible Modules for Dell EMC PowerMax

Description

The Ansible Modules for Dell EMC PowerMax are used to automate and orchestrate the configuration, and deployment of the Dell EMC PowerMax arrays. The capabilities of Ansible modules are managing volumes, storage groups, ports, port group, hosts, host groups, masking views, snapshots, and gather high-level facts about the arrays. The options available for each capability are list, show, create, delete, and modify.

Prerequisites

Unisphere for PowerMax 9.0 to manage Dell EMC PowerMax arrays.
Ansible 2.6 or higher.
Red Hat Enterprise Linux 7.5.
Python 2.7.12 or higher.
Python library for Unisphere (PyU4V) 3.0.0.14 must be installed on the client operating system.
Please follow Py4UV installation instructions on https://pyu4v.readthedocs.io/

Running Ansible Modules

The Ansible server must be configured with Python library for Unisphere to run the Ansible playbooks. The [Product Guide](https://github.com/dell/ansible-powermax/blob/master/dellemc_ansible/docs/Ansible%20for%20Dell%20EMC%20PowerMax%20Product%20Guide.pdf) provides information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

Support

Ansible for PowerMax Modules are supported by Dell EMC and are provided under the terms of the license attached to the source code.
For any setup, configuration issues, questions or feedback, join the [Dell EMC Automation community](https://www.dell.com/community/Automation/bd-p/Automation).
For any Dell EMC storage issues, please contact Dell support at: https://www.dell.com/support.
For clarity, Dell EMC does not provide support for any source code modifications.
