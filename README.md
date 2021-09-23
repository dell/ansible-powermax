# Ansible Modules for Dell EMC PowerMax

The Ansible Modules for Dell EMC PowerMax allow data center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell EMC PowerMax arrays.

The capabilities of Ansible modules are managing volumes, storage groups, ports, port groups, hosts, host groups, masking views, snapshots, SRDF links, RDF groups, metro DR environments, jobs, snapshot policies, storage pools and gathering high-level facts about the arrays. The options available for each capability are list, show, create, delete, and modify. These tasks can be executed by running simple playbooks written in yaml syntax. The modules are written so that all the operations are idempotent, therefore making multiple identical requests has the same effect as making a single request.

## License
Ansible collection for PowerMax is released and licensed under the GPL-3.0 license. See [LICENSE](LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerMax are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](MODULE-LICENSE) for the full terms.

## Support
Ansible collection for PowerMax are supported by Dell EMC and are provided under the terms of the license attached to the collection. Please see the [LICENSE](#license) section for the full terms. Dell EMC does not provide any support for the source code modifications. For any Ansible modules issues, questions or feedback, join the [Dell EMC Automation community](https://www.dell.com/community/Automation/bd-p/Automation).

## Supported Platforms
  * Dell EMC PowerMax and VMAX All Flash arrays with Unisphere version 9.1 and later.

## Prerequisites
This table provides information about the software prerequisites for the Ansible Modules for Dell EMC PowerMax.

| **Ansible Modules** | **Unisphere Version** | **PowerMaxOS** | **Red Hat Enterprise Linux** | **Python version** | **Python library version** | **Ansible** |
|---------------------|-----------------------|----------------|------------------------------|--------------------|----------------------------|-------------|
| v1.6.0 | 9.1 <br> 9.2 | 5978.221.221 <br> 5978.444.444 <br> 5978.669.669 <br> 5978.711.711 |	7.5 <br> 7.6, 7.7, 7.8, and 8.2 | 2.7.12 <br> 3.5.2 <br> 3.6.x <br> 3.7.x | 9.1.x.x <br> 9.2.x.x | 2.9 and 2.10 | 

  * Please follow PyU4V installation instructions on [PyU4V Documentation](https://pyu4v.readthedocs.io/)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. This means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell EMC PowerMax
  * Volume module
  * Host module
  * Host Group module
  * Snapshot module
  * Masking View module
  * Port module
  * Port Group module
  * Storage Group module  
  * Gatherfacts module
  * SRDF module
  * RDF Group module
  * Metro DR module
  * Job module
  * Snapshot Policy module
  * Storage Pool module
  * Process Storage Pool module

## Installation of SDK
Install the python [sdk](https://pypi.org/project/PyU4V/) named 'PyU4V'. It can be installed using pip, based on the appropriate python version.

## Building Collections
  1. Use the following command to build the collection from source code:
    
    ansible-galaxy collection build

   For more details on how to build a tar ball, refer: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing Collections
#### Online Installation of Collections 
  1. Use the following command to install the latest collection hosted in galaxy:

	ansible-galaxy collection install dellemc.powermax -p <install_path>

#### Offline Installation of Collections
  1. Download the latest tar build from any of the available distribution channel [Ansible Galaxy](https://galaxy.ansible.com/dellemc/powermax) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/powermax) and use the following command to install the collection anywhere in your system:

	ansible-galaxy collection install dellemc-powermax-1.6.0.tar.gz -p <install_path>

  2. Set the environment variable:

	export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using Collections

 1. In order to use any Ansible module, ensure that the importing of a proper FQCN (Fully Qualified Collection Name) must be embedded in the playbook. Refer to the following example:

	collections:
	- dellemc.powermax

  2. In order to use an installed collection specific to the task use a proper FQCN (Fully Qualified Collection Name). Refer to the following example:

	tasks:
    - name: Get Volume details
	  dellemc.powermax.dellemc_powermax_volume

  3. For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Refer to the following example:

	ansible-doc dellemc.powermax.dellemc_powermax_gatherfacts

## Running Ansible Modules

The Ansible server must be configured with Python library for Unisphere to run the Ansible playbooks. The [Documents]( https://github.com/dell/ansible-powermax/tree/1.6.0/docs ) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which need to be configured before running the modules.

## SSL Certificate Validation

* Copy the CA certificate to the "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
* Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the following command:
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>*
* Import the SSL certificate to the host using the following command:
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *update-ca-trust extract*
* If "TLS CA certificate bundle error" occurs, then follow below steps:
    * cd /etc/pki/tls/certs/
    * openssl x509 -in ca-bundle.crt -text -noout

## Results
Each module returns the updated state and details of the entity, for example, if you are using the Volume module, all calls will return the updated details of the volume. A sample result is shown in each module's documentation.
