# Installation and execution of Ansible modules for Dell PowerMax

## Installation of SDK
Depending on which PowerMax Unisphere version is being used, follow this procedure to install SDK:

* For PowerMax Unisphere version 92, install Python [sdk](https://pypi.org/project/PyU4V/9.2.1.6/) named 'PyU4V 9.2.1.6': 
  
        pip install PyU4V==9.2.1.6
  
* For PowerMax Unisphere version 100 and above, install Python [sdk](https://pypi.org/project/PyU4V/10.0.0.16/) named 'PyU4V 10.0.0.16':
        
        pip install PyU4V==10.0.0.16

## Building collections
* Use this command to build the collection from source code:
    
        ansible-galaxy collection build

   For more details on how to build a tar ball, see: [Building the collection](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_distributing.html#building-your-collection-tarball)


## Installing collections
#### Online installation of collections 
* Use this command to install the latest collection hosted in galaxy:

	      ansible-galaxy collection install dellemc.powermax -p <install_path>

  #### Offline installation of collections
  1. Download the latest tar build from either of the available distribution channels [Ansible Galaxy](https://galaxy.ansible.com/dellemc/powermax) /[Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/dellemc/powermax)

  2. Use this command to install the collection anywhere in your system:

	      ansible-galaxy collection install dellemc-powermax-3.1.0.tar.gz -p <install_path>

  3. Set the environment variable:

	      export ANSIBLE_COLLECTIONS_PATHS=$ANSIBLE_COLLECTIONS_PATHS:<install_path>

## Using Collections

  * In order to use any Ansible module, ensure that the importing of a proper Fully Qualified Collection Name(FQCN) must be embedded in the playbook.
   For example:
 
        collections:
        - dellemc.powermax

  * Use a proper FQCN in order to use an installed collection specific to the task. For example:

        tasks:
        - name: Get filesystem details
          dellemc.powermax.filesystem
    
  * When generating Ansible documentation for a specific module, embed the FQCN  before the module name. For example:
        
        ansible-doc dellemc.powermax.info


## Running Ansible modules

The Ansible server must be configured with Python library for Unisphere to run the Ansible playbooks. The [Documents](https://github.com/dell/ansible-powermax/blob/main/docs) provide information on different Ansible modules along with their functions and syntax. The parameters table in the Product Guide provides information on various parameters which need to be configured before running the modules.

## SSL certificate validation

* Export the SSL certificate using KeyStore Explorer tool or from the browser in .crt format.
* Append the SSL certificate to the Certifi package file cacert.pem.
      * For Python 3.6 : cat <> >> /usr/local/lib/python3.6/dist-packages/certifi/cacert.pem

## Results
Each module returns the updated state and details of the entity. 
For example, if you are using the group module, all calls return the updated details of the group.
Sample result is shown in the documentation of each module.

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. It means that the result of a successfully performed request is independent of the number of times it is performed.

## Ansible execution environment

Ansible can also be installed in a container environment. Ansible Builder provides the ability to create reproducible, self-contained environments as container images that can be run as Ansible execution environments.
* Install the ansible builder package using:

         pip3 install ansible-builder

* Ensure that the execution-environment.yml is at the root of collection. Create the execution environment using:

         ansible-builder build --tag <tag_name> --container-runtime docker

* After the image is built, run the container using:

         docker run -it <tag_name> /bin/bash

* Verify the collection installation using command:

         ansible-galaxy collection list

* The playbook can run on the container using:

         docker run --rm -v $(pwd):/runner <tag_name> ansible-playbook info_tests.yml
