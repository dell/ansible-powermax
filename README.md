# Ansible Modules for Dell EMC PowerMax

The Ansible Modules for Dell EMC PowerMax allow Data Center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC PowerMax arrays.

The capabilities of Ansible modules are managing volumes, storage groups, ports, port groups, hosts, host groups, masking views, snapshots, and gathering high-level facts about the arrays. The options available for each capability are list, show, create, delete, and modify. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, therefore making multiple identical requests has the same effect as making a single request.

## Support
Ansible modules for PowerMax are supported by Dell EMC and are provided under the terms of the license attached to the source code. Dell EMC does not provide support for any source code modifications. For any Ansible module issues, questions or feedback, join the [Dell EMC Automation community]( https://www.dell.com/community/Automation/bd-p/Automation ).

## Supported Platforms
  * Dell EMC PowerMax Arrays with Unisphere version 9.1 and above.

## Prerequisites
  * Ansible 2.9 or higher
  * Python 2.8 or higher
  * Red Hat Enterprise Linux 7.6/7.7/7.8/8.2
  * Python Library for PowerMax (PyU4V) 9.1 or higher
  * Please follow Py4UV installation instructions on [PyU4V Documentation](https://pyu4v.readthedocs.io/)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. This means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC PowerMax
  * Volume module
  * Host module
  * Host group module
  * Snapshot module
  * Maskingview module
  * Port module
  * Port group module
  * Storage group module  
  * Gather facts module
  * SRDF module
  * RDF module

## Installation of SDK
Install python [sdk](https://pypi.org/project/PyU4V/) named 'PyU4V'. It can be installed using pip, based on the appropriate python version.

## Installing Collections

  * Download the tar build and run the following command to install the collection anywhere in your system:
        ansible-galaxy collection install dellemc-powermax-1.3.0.tar.gz -p ./collections
  * Set the environment variable:
        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>/collections

## Using Collections

  * In order to use any Ansible module, ensure that the importation of the proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook. For example,
        collections:
        - dellemc.powermax
  * To generate Ansible documentation for a specific module, embed the FQCN before the module name. For example,
        ansible-doc dellemc.powermax.dellemc_powermax_gatherfacts

## Running Ansible Modules

The Ansible server must be configured with Python library for Unisphere to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-powermax/tree/1.3.0/dellemc_ansible/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which needs to be configured before running the modules.

## SSL Certificate Validation

* Copy the CA certificate to this "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
* Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the command "export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>"
* Import the SSL certificate to host using the command "update-ca-trust".

## Results
Each module returns the updated state and details of the entity, for example, if you are using the Volume module, all calls will return the updated details of the volume. A sample result is shown in each module's documentation.
