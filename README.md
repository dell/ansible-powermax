# Ansible Modules for Dell Technologies PowerMax

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](https://github.com/dell/ansible-powermax/blob/main/docs/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/github/license/dell/ansible-powermax)](https://github.com/dell/ansible-powermax/blob/main/LICENSE)
[![Python version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ansible version](https://img.shields.io/badge/ansible-2.17+-blue.svg)](https://pypi.org/project/ansible/)
[![PyU4V](https://img.shields.io/github/v/release/dell/PyU4V?include_prereleases&label=PyU4V&style=flat-square)](https://github.com/dell/PyU4V/releases)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/dell/ansible-powermax?include_prereleases&label=latest&style=flat-square)](https://github.com/dell/ansible-powermax/releases)
[![codecov](https://codecov.io/gh/dell/ansible-powermax/branch/main/graph/badge.svg)](https://app.codecov.io/gh/dell/ansible-powermax)

The Ansible modules for Dell Technologies (Dell) PowerMax allow data center and IT administrators to use RedHat Ansible to automate and orchestrate the configuration and management of Dell PowerMax arrays.

The capabilities of Ansible modules are managing volumes, storage groups, ports, port groups, hosts, host groups, masking views, initiators, snapshots, SRDF links, RDF groups, Metro DR environments, jobs, snapshot policies, storage pools and gathering high-level facts about the arrays. The options available for each capability are list, show, create, delete, and modify. These tasks are performed by running simple playbooks written in YAML syntax. The modules are written so that all the operations are idempotent, therefore making multiple identical requests has the same effect as making a single request.

## Table of contents

* [Code of conduct](https://github.com/dell/ansible-powermax/blob/main/docs/CODE_OF_CONDUCT.md)
* [Maintainer guide](https://github.com/dell/ansible-powermax/blob/main/docs/MAINTAINER_GUIDE.md)
* [Committer guide](https://github.com/dell/ansible-powermax/blob/main/docs/COMMITTER_GUIDE.md)
* [Contributing guide](https://github.com/dell/ansible-powermax/blob/main/docs/CONTRIBUTING.md)
* [Branching strategy](https://github.com/dell/ansible-powermax/blob/main/docs/BRANCHING.md)
* [List of adopters](https://github.com/dell/ansible-powermax/blob/main/docs/ADOPTERS.md)
* [Maintainers](https://github.com/dell/ansible-powermax/blob/main/docs/MAINTAINERS.md)
* [Support](https://github.com/dell/ansible-powermax/blob/main/docs/SUPPORT.md)
* [Security](https://github.com/dell/ansible-powermax/blob/main/docs/SECURITY.md)
* [License](#license)
* [Supported platforms](#supported-platforms)
* [Prerequisites](#prerequisites)
* [List of Ansible modules for Dell PowerMax](#list-of-ansible-modules-for-dell-powermax)
* [Installation and execution of Ansible modules for Dell PowerMax](#installation-and-execution-of-ansible-modules-for-dell-powermax)
* [Maintenance](#maintenance)

## Requirements
This table provides information about the software prerequisites for the Ansible Modules for Dell PowerMax.

| **Ansible modules** | **Unisphere version** | **PowerMaxOS** | **Python version**            | **Python library version** | **Ansible**              |
|---------------------|-----------------------|----------------|-------------------------------|----------------------------|--------------------------|
| v4.0.1              | 10.1 <br> 10.2 | 5978.444.444 <br> 5978.669.669 <br> 5978.711.711 <br> 6079.xxx.xxx | 3.11.x <br> 3.12.x | 10.1.x.x <br> 10.2.x.x | 2.17 <br> 2.18 <br> 2.19 |

* Follow PyU4V installation instructions on [PyU4V Documentation](https://pyu4v.readthedocs.io/)

## Installation and execution of Ansible modules for Dell PowerMax
The installation and execution steps of Ansible modules for Dell PowerMax can be found [here](https://github.com/dell/ansible-powermax/blob/main/docs/INSTALLATION.md).

## Use Cases
Refer the [example playbooks](https://github.com/dell/ansible-powermax/tree/main/docs/samples) on how the collection can be used for [modules.](https://github.com/dell/ansible-powermax/tree/main/plugins/modules)

## Testing
The following tests are done on ansible-powermax collection

* Unit tests.
* Integration tests.

## Support
Refer [Support](https://github.com/dell/ansible-powermax/blob/main/docs/SUPPORT.md) documenetation for more information on the support from Dell Technologies.

## Release, Maintenance and Deprecation
Ansible Modules for Dell Technologies PowerStore follows [Semantic Versioning](https://semver.org/).

New version will be release regularly if significant changes (bug fix or new feature) are made in the collection.

Released code versions are located on "release" branches with names of the form "release-x.y.z" where x.y.z corresponds to the version number. More information on branching strategy followed can be found [here](https://github.com/dell/ansible-powermax/blob/main/docs/BRANCHING.md).

Ansible Modules for Dell Technologies PowerStore deprecation cycle is aligned with that of [Ansible](https://docs.ansible.com/ansible/latest/dev_guide/module_lifecycle.html).

See [change logs](https://github.com/dell/ansible-powermax/blob/main/CHANGELOG.rst) for more information on what is new in the releases.

## Related Information

## Idempotency
The modules are written in such a way that all requests are idempotent and hence fault-tolerant. This means that the result of a successfully performed request is independent of the number of times it is performed.

## List of Ansible modules for Dell PowerMax
  * [Volume module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/volume.rst)
  * [Host module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/host.rst)
  * [Host Group module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/hostgroup.rst)
  * [Snapshot module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/snapshot.rst)
  * [Masking View module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/maskingview.rst)
  * [Port module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/port.rst)
  * [Port Group module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/portgroup.rst)
  * [Storage Group module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/storagegroup.rst)
  * [Info module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/info.rst)
  * [SRDF module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/srdf.rst)
  * [RDF Group module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/rdfgroup.rst)
  * [Metro DR module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/metrodr.rst)
  * [Job module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/job.rst)
  * [Snapshot Policy module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/snapshotpolicy.rst)
  * [Storage Pool module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/storagepool.rst)
  * [Process Storage Pool module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/process_storage_pool_dict.rst)
  * [Initiator module](https://github.com/dell/ansible-powermax/blob/main/docs/modules/initiator.rst)
  * [Intelligent Volume Placement](https://github.com/dell/ansible-powermax/blob/main/docs/modules/capacity_role.rst)

## License
Ansible collection for PowerMax is released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powermax/blob/main/LICENSE) for the full terms. Ansible modules and modules utilities that are part of the Ansible collection for PowerMax are released and licensed under the GPL-3.0 license. See [LICENSE](https://github.com/dell/ansible-powermax/blob/main/LICENSE) for the full terms.
