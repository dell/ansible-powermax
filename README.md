# Ansible Modules for Dell Technologies PowerMax

The Ansible Modules for Dell Technologies (Dell) PowerMax allow data center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell PowerMax arrays.

The capabilities of Ansible modules are managing volumes, storage groups, ports, port groups, hosts, host groups, masking views, initiators, snapshots, SRDF links, RDF groups, metro DR environments, jobs, snapshot policies, storage pools and gathering high-level facts about the arrays. The options available for each capability are list, show, create, delete, and modify. These tasks are performed by running simple playbooks written in YAML syntax. The modules are written so that all the operations are idempotent, therefore making multiple identical requests has the same effect as making a single request.

## License
Ansible collection for PowerMax is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powermax/blob/1.8.0/LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerMax are released and licensed under the Apache 2.0 license. See [MODULE-LICENSE](https://github.com/dell/ansible-powermax/blob/1.8.0/MODULE-LICENSE) for the full terms.

## Support
Ansible collection for PowerMax is supported by Dell Technologies and is provided under the terms of the license attached to the collection. Please see the [LICENSE](#license) section for the full terms. Dell Technologies does not provide any support for the source code modifications. For any Ansible modules issues, questions or feedback, join the [Dell Automation community](https://www.dell.com/community/Automation/bd-p/Automation).

## Supported Platforms
Dell PowerMax and VMAX All Flash arrays support Unisphere version 9.1 and later.

## Prerequisites
This table provides information about the software prerequisites for the Ansible Modules for Dell PowerMax.

| **Ansible Modules** | **Unisphere Version** | **PowerMaxOS** | **Red Hat Enterprise Linux** | **Python version** | **Python library version** | **Ansible** |
|---------------------|-----------------------|----------------|------------------------------|--------------------|----------------------------|-------------|
| v1.8.0 | 9.1 <br> 9.2 | 5978.221.221 <br> 5978.444.444 <br> 5978.669.669 <br> 5978.711.711 |	8.4 <br> 8.5 | 3.8.x <br> 3.9.x <br> 3.10.x | 9.1.x.x <br> 9.2.x.x | 2.11 <br> 2.12 <br> 2.13 |

  * Follow PyU4V installation instructions on [PyU4V Documentation](https://pyu4v.readthedocs.io/)

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. This means that the result of a successfully performed request is independent of the number of times it is executed.

## List of Ansible Modules for Dell PowerMax
  * [Volume module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#volume-module)
  * [Host module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#host-module)
  * [Host Group module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#host-group-module)
  * [Snapshot module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#snapshot-module)
  * [Masking View module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#masking-view-module)
  * [Port module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#port-module)
  * [Port Group module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#port-group-module)
  * [Storage Group module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#storage-group-module)  
  * [Info module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#info-module)
  * [SRDF module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#srdf-module)
  * [RDF Group module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#rdf-group-module)
  * [Metro DR module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#metro-dr-module)
  * [Job module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#job-module)
  * [Snapshot Policy module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#snapshot-policy-module)
  * [Storage Pool module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#storage-pool-module)
  * [Process Storage Pool module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#process-storage-pool-dict-module)
  * [Initiator module](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#initiator-module)
  * [Intelligent Volume Placement](https://github.com/dell/ansible-powermax/blob/1.8.0/docs/Product%20Guide.md#intelligent-volume-placement)

## Installation of SDK
Install the python [sdk](https://pypi.org/project/PyU4V/) named 'PyU4V'. It can be installed using pip, based on the appropriate python version.

## Building Collections
  * Use the following command to build the collection from source code:
    
        ansible-galaxy collection build

   For more details on how to build a tar ball, see: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)

## Installing Collections
#### Online Installation of Collections 
  * Use the following command to install the latest collection hosted in galaxy:

	      ansible-galaxy collection install dellemc.powermax -p <install_path>

#### Offline Installation of Collections
 * Download the latest tar build from any of the available distribution channels [Ansible Galaxy](https://galaxy.ansible.com/dellemc/powermax) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/powermax). Use the following command to install the collection anywhere in your system:

        ansible-galaxy collection install dellemc-powermax-1.8.0.tar.gz -p <install_path>

 * Set the environment variable:

        export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using Collections

* In order to use any Ansible module, ensure that the importing of a proper Fully Qualified Collection Name(FQCN) must be embedded in the playbook. Consider the following example:

        collections:
        - dellemc.powermax

* In order to use an installed collection specific to the task use a proper FQCN. Consider the following example:

        tasks:
        - name: Get Volume details
          dellemc.powermax.volume

* For generating Ansible documentation for a specific module, embed the FQCN  before the module name. Consider to the following example:

        ansible-doc dellemc.powermax.info

## Running Ansible Modules

The Ansible server must be configured with python library for Unisphere to run the Ansible playbooks. The [Documents](docs) provide information on different Ansible modules along with their functions and syntax. The parameters table in the product guide provides information on various parameters that need to be configured before running the modules.

## SSL Certificate Validation

* Copy the CA certificate to the "/etc/pki/ca-trust/source/anchors" path of the host by any external means.
* Set the "REQUESTS_CA_BUNDLE" environment variable to the path of the SSL certificate using the following command:

        export REQUESTS_CA_BUNDLE=/etc/pki/ca-trust/source/anchors/<<Certificate_Name>>*
* Import the SSL certificate to the host using the following command:

        update-ca-trust extract*
* If "TLS CA certificate bundle error" occurs, then follow below steps:

        cd /etc/pki/tls/certs/
        openssl x509 -in ca-bundle.crt -text -noout

## Results
Each module returns the updated state and details of the entity. For example, if you are using the Volume module, all calls returns the updated details of the volume. A sample result is shown in each module documentation.

## Ansible Execution Environment

Ansible can also be installed in a container environment. Ansible Builder provides the ability to create reproducible, self-contained environments as container images that can be run as Ansible execution environments.
* Install the Ansible Builder package using the command:

        pip3 install ansible-builder
* Create the execution environment using the command:

        ansible-builder build --tag <tag_name> --container-runtime docker
* Run the container after the image is built using the command:

        docker run -it <tag_name> /bin/bash
* Verify collection installation using the command:

        ansible-galaxy collection list
* Run the playbook on the container using the command:

        docker run --rm -v $(pwd):/runner <tag_name> ansible-playbook info_test.yml

## Maintanence
Ansible Modules for Dell Technologies PowerMax deprecation cycle is aligned with [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).
