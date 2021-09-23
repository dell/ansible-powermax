# Ansible Modules for Dell EMC PowerMax
## Product Guide 1.6.0
© 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.

--------------
## Contents
*   [Gatherfacts Module](#gatherfacts-module)
    *   [Synopsis](#synopsis)
    *   [Parameters](#parameters)
    *   [Notes](#notes)
    *   [Examples](#examples)
    *   [Return Values](#return-values)
    *   [Authors](#authors)
*   [Snapshot Module](#snapshot-module)
    *   [Synopsis](#synopsis-1)
    *   [Parameters](#parameters-1)
    *   [Notes](#notes-1)
    *   [Examples](#examples-1)
    *   [Return Values](#return-values-1)
    *   [Authors](#authors-1)
*   [Storage Pool Module](#storage-pool-module)
    *   [Synopsis](#synopsis-2)
    *   [Parameters](#parameters-2)
    *   [Examples](#examples-2)
    *   [Return Values](#return-values-2)
    *   [Authors](#authors-2)
*   [Volume Module](#volume-module)
    *   [Synopsis](#synopsis-3)
    *   [Parameters](#parameters-3)
    *   [Notes](#notes-2)
    *   [Examples](#examples-3)
    *   [Return Values](#return-values-3)
    *   [Authors](#authors-3)
*   [SRDF Module](#srdf-module)
    *   [Synopsis](#synopsis-4)
    *   [Parameters](#parameters-4)
    *   [Examples](#examples-4)
    *   [Return Values](#return-values-4)
    *   [Authors](#authors-4)
*   [Storage Group Module](#storage-group-module)
    *   [Synopsis](#synopsis-5)
    *   [Parameters](#parameters-5)
    *   [Examples](#examples-5)
    *   [Return Values](#return-values-5)
    *   [Authors](#authors-5)
*   [Host Group Module](#host-group-module)
    *   [Synopsis](#synopsis-6)
    *   [Parameters](#parameters-6)
    *   [Notes](#notes-3)
    *   [Examples](#examples-6)
    *   [Return Values](#return-values-6)
    *   [Authors](#authors-6)
*   [Port Module](#port-module)
    *   [Synopsis](#synopsis-7)
    *   [Parameters](#parameters-7)
    *   [Examples](#examples-7)
    *   [Return Values](#return-values-7)
    *   [Authors](#authors-7)
*   [Metro DR Module](#metro-dr-module)
    *   [Synopsis](#synopsis-8)
    *   [Parameters](#parameters-8)
    *   [Examples](#examples-8)
    *   [Return Values](#return-values-8)
    *   [Authors](#authors-8)
*   [Job Module](#job-module)
    *   [Synopsis](#synopsis-9)
    *   [Parameters](#parameters-9)
    *   [Examples](#examples-9)
    *   [Return Values](#return-values-9)
    *   [Authors](#authors-9)
*   [Masking View Module](#masking-view-module)
    *   [Synopsis](#synopsis-10)
    *   [Parameters](#parameters-10)
    *   [Examples](#examples-10)
    *   [Return Values](#return-values-10)
    *   [Authors](#authors-10)
*   [Port Group Module](#port-group-module)
    *   [Synopsis](#synopsis-11)
    *   [Parameters](#parameters-11)
    *   [Examples](#examples-11)
    *   [Return Values](#return-values-11)
    *   [Authors](#authors-11)
*   [Process Storage Pool Dict Module](#process-storage-pool-dict-module)
    *   [Synopsis](#synopsis-12)
    *   [Parameters](#parameters-12)
    *   [Examples](#examples-12)
    *   [Return Values](#return-values-12)
    *   [Authors](#authors-12)
*   [Host Module](#host-module)
    *   [Synopsis](#synopsis-13)
    *   [Parameters](#parameters-13)
    *   [Notes](#notes-4)
    *   [Examples](#examples-13)
    *   [Return Values](#return-values-13)
    *   [Authors](#authors-13)
*   [RDF Group Module](#rdf-group-module)
    *   [Synopsis](#synopsis-14)
    *   [Parameters](#parameters-14)
    *   [Examples](#examples-14)
    *   [Return Values](#return-values-14)
    *   [Authors](#authors-14)
*   [Snapshot Policy Module](#snapshot-policy-module)
    *   [Synopsis](#synopsis-15)
    *   [Parameters](#parameters-15)
    *   [Notes](#notes-5)
    *   [Examples](#examples-15)
    *   [Return Values](#return-values-15)
    *   [Authors](#authors-15)

--------------

# Gatherfacts Module

Gathers information about PowerMax/VMAX Storage entities

### Synopsis
 Gathers the list of specified PowerMax/VMAX storage system entities, such as the list of registered arrays, storage groups, hosts, host groups, storage groups, storage resource pools, port groups, masking views, array health status, alerts and metro DR environments, so on.

### Parameters
                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=2 > serial_no</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is not required for getting the list of arrays. </td>
        </tr>
                    <tr>
            <td colspan=2 > tdev_volumes</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to filter the volume list. This will have a small performance impact. By default it is set to true, only TDEV volumes will be returned.  <br> True - Will return only the TDEV volumes.  <br> False - Will return all the volumes. </td>
        </tr>
                    <tr>
            <td colspan=2 > gather_subset</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td> <ul> <li>alert</li>  <li>health</li>  <li>vol</li>  <li>srp</li>  <li>sg</li>  <li>pg</li>  <li>host</li>  <li>hg</li>  <li>port</li>  <li>mv</li>  <li>rdf</li>  <li>metro_dr_env</li>  <li>snapshot_policies</li> </ul></td>
            <td> <br> List of string variables to specify the PowerMax/VMAX entities for which information is required.  <br> Required only if the serial_no is present  <br> List of all PowerMax/VMAX entities supported by the module  <br> alert - gets alert summary information  <br> health - health status of a specific PowerMax array  <br> vol - volumes  <br> srp - storage resource pools  <br> sg - storage groups  <br> pg - port groups  <br> host - hosts  <br> hg -  host groups  <br> port - ports  <br> mv - masking views  <br> rdf - rdf groups  <br> metro_dr_env - metro DR environments  <br> snapshot_policies - snapshot policies </td>
        </tr>
                    <tr>
            <td colspan=2 > filters</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of filters to support filtered output for storage entities.  <br> Each filter is a tuple of {filter_key, filter_operator, filter_value}.  <br> Supports passing of multiple filters.  <br> The storage entities, 'rdf', 'health', 'snapshot_policies' and 'metro_dr_env', does not support filters. Filters will be ignored if passed. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_key </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Name identifier of the filter.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_operator </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td> <ul> <li>equal</li>  <li>greater</li>  <li>lesser</li>  <li>like</li> </ul></td>
                <td>  <br> Operation to be performed on filter key.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > filter_value </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td></td>
                <td>  <br> Value of the filter key.  </td>
            </tr>
                            <tr>
            <td colspan=2 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=2 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                                                    </table>

### Notes
* Filter functionality will be supported only for the following 'filter_key' against specific 'gather_subset'.
* vol - allocated_percent, associated, available_thin_volumes, bound_tdev, cap_cyl, cap_gb, cap_mb, cap_tb, cu_image_num, cu_image_ssid, data_volume, dld, drv, effective_wwn, emulation, encapsulated, encapsulated_wwn, gatekeeper, has_effective_wwn, mapped, mobility_id_enabled, num_of_front_end_paths, num_of_masking_views, num_of_storage_groups, oracle_instance_name, physical_name, pinned, private_volumes, rdf_group_number, reserved, split_name, status, storageGroupId, symmlun, tdev, thin_bcv, type, vdev, virtual_volumes, volume_identifier, wwn
* srp - compression_state, description, effective_used_capacity_percent, emulation, num_of_disk_groups, num_of_srp_sg_demands, num_of_srp_slo_demands, rdfa_dse, reserved_cap_percent, total_allocated_cap_gb, total_srdf_dse_allocated_cap_gb, total_subscribed_cap_gb, total_usable_cap_gb
* sg - base_slo_name, cap_gb, child, child_sg_name, ckd, compression, compression_ratio_to_one, fba, num_of_child_sgs, num_of_masking_views, num_of_parent_sgs, num_of_snapshots, num_of_vols, parent, parent_sg_name, slo_compliance, slo_name, srp_name, storageGroupId, tag, volumeId
* pg - dir_port, fibre, iscsi, num_of_masking_views, num_of_ports
* host - host_group_name, num_of_host_groups, num_of_initiators, num_of_masking_views, num_of_powerpath_hosts, powerPathHostId
* hg - host_name, num_of_hosts, num_of_masking_views
* port - aclx, avoid_reset_broadcast, common_serial_number, director_status, disable_q_reset_on_ua, enable_auto_negotive, environ_set, hp_3000_mode, identifier, init_point_to_point, ip_list, ipv4_address, ipv6_address, iscsi_target, max_speed, negotiated_speed, neqotiate_reset, no_participating, node_wwn, num_of_cores, num_of_hypers, num_of_mapped_vols, num_of_masking_views, num_of_port_groups, port_interface, port_status, rdf_hardware_compression, rdf_hardware_compression_supported, rdf_software_compression, rdf_software_compression_supported, scsi_3, scsi_support1, siemens, soft_reset, spc2_protocol_version, sunapee, type, unique_wwn, vcm_state, vnx_attached, volume_set_addressing, wwn_node
* mv - host_or_host_group_name, port_group_name, protocol_endpoint_masking_view, storage_group_name
* alert - acknowledged, array, created_date, created_date_milliseconds, description, object, object_type, severity, state, type

### Examples
```
- name: Get list of volumes with filter -- all TDEV volumes of size equal
        to 5GB
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - vol
    filters:
      - filter_key: "tdev"
        filter_operator: "equal"
        filter_value: "True"
      - filter_key: "cap_gb"
        filter_operator: "equal"
        filter_value: "5"

- name: Get list of volumes and storage groups with filter
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - vol
      - sg
    filters:
      - filter_key: "tdev"
        filter_operator: "equal"
        filter_value: "True"
      - filter_key: "cap_gb"
        filter_operator: "equal"
        filter_value: "5"

- name: Get list of storage groups with capacity between 2GB to 10GB
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
      - sg
    filters:
      - filter_key: "cap_gb"
        filter_operator: "greater"
        filter_value: "2"
      - filter_key: "cap_gb"
        filter_operator: "lesser"
        filter_value: "10"

- name: Get the list of arrays for a given Unisphere host
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
  register: array_list
- debug:
    var: array_list

- name: Get list of tdev-volumes
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    tdev_volumes: True
    gather_subset:
      - vol

- name: Get the list of arrays for a given Unisphere host
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"

- name: Get array health status
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - health

- name: Get array alerts summary
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - alert

- name: Get the list of metro DR environments for a given Unisphere host
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - metro_dr_env

- name: Get list of Storage groups
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - sg

- name: Get list of Storage Resource Pools
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - srp

- name: Get list of Ports
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - port

- name: Get list of Port Groups
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - pg

- name: Get list of Hosts
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - host

- name: Get list of Host Groups
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - hg

- name: Get list of Masking Views
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - mv

- name: Get list of RDF Groups
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
       - rdf

- name: Get list of snapshot policies
  dellemc_powermax_gatherfacts:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    gather_subset:
     - snapshot_policies
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=4 > Alerts </td>
            <td>  list </td>
            <td> When the alert exists. </td>
            <td> Alert summary of the array. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > acknowledged </td>
                <td> str </td>
                <td>success</td>
                <td> Whether or not this alert is acknowledged. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > alertId </td>
                <td> str </td>
                <td>success</td>
                <td> Unique ID of alert. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > array </td>
                <td> str </td>
                <td>success</td>
                <td> Array serial no. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > created_date </td>
                <td> str </td>
                <td>success</td>
                <td> Creation Date. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > created_date_milliseconds </td>
                <td> str </td>
                <td>success</td>
                <td> Creation Date in milliseconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > description </td>
                <td> str </td>
                <td>success</td>
                <td> Description about the alert </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > object </td>
                <td> str </td>
                <td>success</td>
                <td> Object description </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > object_type </td>
                <td> str </td>
                <td>success</td>
                <td> Resource class </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > severity </td>
                <td> str </td>
                <td>success</td>
                <td> Severity of the alert </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > state </td>
                <td> str </td>
                <td>success</td>
                <td> State of the alert </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of the alert </td>
            </tr>
                                        <tr>
            <td colspan=4 > Arrays </td>
            <td>  list </td>
            <td> When the Unisphere exist. </td>
            <td> List of arrays in the Unisphere. </td>
        </tr>
                    <tr>
            <td colspan=4 > Health </td>
            <td>  complex </td>
            <td> When the array exist. </td>
            <td> Health status of the array. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > health_score_metric </td>
                <td> list </td>
                <td>success</td>
                <td> Overall health score for the specified Symmetrix. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > cached_date </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Date Time stamp in epoch format when it was cached. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > data_date </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Date Time stamp in epoch format when it was collected. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > expired </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Flag to indicate the expiry of the score. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > health_score </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Overall health score in numbers. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > instance_metrics </td>
                    <td> list </td>
                    <td>success</td>
                    <td> Metrics about a specific instance. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > health_score_instance_metric </td>
                        <td> int </td>
                        <td>success</td>
                        <td> Health score of a specific instance. </td>
                    </tr>
                                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > metric </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Information about which sub system , such as SYSTEM_UTILIZATION, CONFIGURATION,CAPACITY, and so on. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > num_failed_disks </td>
                <td> int </td>
                <td>success</td>
                <td> Numbers of the disk failure in this system. </td>
            </tr>
                                        <tr>
            <td colspan=4 > HostGroups </td>
            <td>  list </td>
            <td> When the hostgroups exist. </td>
            <td> List of host groups present on the array. </td>
        </tr>
                    <tr>
            <td colspan=4 > Hosts </td>
            <td>  list </td>
            <td> When the hosts exist. </td>
            <td> List of hosts present on the array. </td>
        </tr>
                    <tr>
            <td colspan=4 > MaskingViews </td>
            <td>  list </td>
            <td> When the masking views exist. </td>
            <td> List of masking views present on the array. </td>
        </tr>
                    <tr>
            <td colspan=4 > MetroDREnvironments </td>
            <td>  list </td>
            <td> When environment exists. </td>
            <td> List of metro DR environments on the array. </td>
        </tr>
                    <tr>
            <td colspan=4 > PortGroups </td>
            <td>  list </td>
            <td> When the port groups exist. </td>
            <td> List of port groups on the array. </td>
        </tr>
                    <tr>
            <td colspan=4 > Ports </td>
            <td>  complex </td>
            <td> When the ports exist. </td>
            <td> List of ports on the array. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > directorId </td>
                <td> str </td>
                <td>success</td>
                <td> Director ID of the port. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > portId </td>
                <td> str </td>
                <td>success</td>
                <td> Port number of the port. </td>
            </tr>
                                        <tr>
            <td colspan=4 > RDFGroups </td>
            <td>  complex </td>
            <td> When the RDF groups exist. </td>
            <td> List of RDF groups on the array. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > label </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the RDF group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rdfgNumber </td>
                <td> int </td>
                <td>success</td>
                <td> Unique identifier of the RDF group. </td>
            </tr>
                                        <tr>
            <td colspan=4 > SnapshotPolicies </td>
            <td>  list </td>
            <td> When snapshot policy exists. </td>
            <td> List of snapshot policies on the array. </td>
        </tr>
                    <tr>
            <td colspan=4 > StorageGroups </td>
            <td>  list </td>
            <td> When the storage groups exist. </td>
            <td> List of storage groups on the array. </td>
        </tr>
                    <tr>
            <td colspan=4 > StorageResourcePools </td>
            <td>  complex </td>
            <td> When the storage pools exist. </td>
            <td> List of storage pools on the array. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > diskGroupId </td>
                <td> list </td>
                <td>success</td>
                <td> ID of the disk group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > emulation </td>
                <td> str </td>
                <td>success</td>
                <td> Type of volume emulation. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > num_of_disk_groups </td>
                <td> int </td>
                <td>success</td>
                <td> Number of disk groups. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rdfa_dse </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for RDFA Delta Set Extension. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > reserved_cap_percent </td>
                <td> int </td>
                <td>success</td>
                <td> Reserved capacity percentage. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > srpId </td>
                <td> str </td>
                <td>success</td>
                <td> Unique Identifier for SRP. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > srp_capacity </td>
                <td> dict </td>
                <td>success</td>
                <td> Different entities to measure SRP capacity. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > effective_used_capacity_percent </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Percentage of effectively used capacity. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > snapshot_modified_tb </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Snapshot modified in TB. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > snapshot_total_tb </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Total snapshot size in TB. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > subscribed_allocated_tb </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Subscribed allocated size in TB. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > subscribed_total_tb </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Subscribed total size in TB. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > usable_total_tb </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Usable total size in TB. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > usable_used_tb </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Usable used size in TB. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > srp_efficiency </td>
                <td> dict </td>
                <td>success</td>
                <td> Different entities to measure SRP efficiency. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > compression_state </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Depicts the compression state of the SRP. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > data_reduction_enabled_percent </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Percentage of data reduction enabled in the SRP. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > data_reduction_ratio_to_one </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Data reduction ratio of SRP. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > overall_efficiency_ratio_to_one </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Overall effectively ratio of SRP. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > snapshot_savings_ratio_to_one </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Snapshot savings ratio of SRP. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > virtual_provisioning_savings_ratio_to_one </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Virtual provisioning savings ratio of SRP. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > total_srdf_dse_allocated_cap_gb </td>
                <td> int </td>
                <td>success</td>
                <td> Total srdf dse allocated capacity in GB. </td>
            </tr>
                                        <tr>
            <td colspan=4 > Volumes </td>
            <td>  list </td>
            <td> When the volumes exist. </td>
            <td> List of volumes on the array. </td>
        </tr>
                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Snapshot Module

Manage Snapshots on PowerMax/VMAX Storage System

### Synopsis
 Managing snapshots on a PowerMax storage system includes creating a new storage group (SG) snapshot, getting details of the SG snapshot, renaming the SG snapshot, changing the snapshot link status, and deleting an existing SG snapshot.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > sg_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the storage group. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > ttl</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The Time To Live (TTL) value for the snapshot.  <br> If the TTL is not specified, the storage group snap details are returned.  <br> However, to create a SG snap - TTL must be given.  <br> If the SG snap should not have any TTL - specify TTL as "None" </td>
        </tr>
                    <tr>
            <td colspan=1 > ttl_unit</td>
            <td> str  </td>
            <td></td>
            <td> days </td>
            <td> <ul> <li>hours</li>  <li>days</li> </ul></td>
            <td> <br> The unit for the ttl.  <br> If no ttl_unit is specified, 'days' is taken as default ttl_unit. </td>
        </tr>
                    <tr>
            <td colspan=1 > generation</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The generation number of the snapshot.  <br> Generation is required for link, unlink, rename and delete operations.  <br> Optional for Get snapshot details.  <br> Create snapshot will always create a new snapshot with a generation number 0.  <br> Rename is supported only for generation number 0. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_id</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Unique ID of the snapshot.  <br> snapshot_id is required for link, unlink, rename and delete operations.  <br> Optional for Get snapshot details. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_snapshot_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > target_sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The target storage group. </td>
        </tr>
                    <tr>
            <td colspan=1 > link_status</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>linked</li>  <li>unlinked</li> </ul></td>
            <td> <br> Describes the link status of the snapshot. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the snapshot should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                                    </table>

### Notes
* Paramters 'generation' and 'snapshot_id' are mutually exclusive.
* If 'generation' or 'snapshot_id' is not provided then a list of generation versus snapshot_id is returned.
* Use of 'snapshot_id' over 'generation' is preferably recommended for PowerMax microcode version 5978.669.669 and onwards.

### Examples
```
- name: Create a Snapshot for a Storage Group
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    ttl: "2"
    ttl_unit: "days"
    state: "present"

- name: Get Storage Group Snapshot details
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    state: "present"

- name: Get Storage Group Snapshot details using generation
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    generation: 1
    state: "present"

- name: Get Storage Group Snapshot details using snapshot_id
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    snapshot_id: 135023964929
    state: "present"

- name: Rename Storage Group Snapshot using generation
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    new_snapshot_name: "ansible_snap_new"
    generation: 0
    state: "present"

- name: Rename Storage Group Snapshot using snapshot_id
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    new_snapshot_name: "ansible_snap_new"
    snapshot_id: 135023964929
    state: "present"

- name: Change Snapshot Link Status to Linked using generation
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    generation: 1
    target_sg_name: "ansible_sg_target"
    link_status: "linked"
    state: "present"

- name: Change Snapshot Link Status to UnLinked using generation
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    generation: 1
    target_sg_name: "ansible_sg_target"
    link_status: "unlinked"
    state: "present"

- name: Change Snapshot Link Status to Linked using snapshot_id
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    snapshot_id: 135023964515
    target_sg_name: "ansible_sg_target"
    link_status: "linked"
    state: "present"

- name: Change Snapshot Link Status to UnLinked using snapshot_id
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_snap_new"
    snapshot_id: 135023964515
    target_sg_name: "ansible_sg_target"
    link_status: "unlinked"
    state: "present"

- name: Delete Storage Group Snapshot using generation
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    generation: 1
    state: "absent"

- name: Delete Storage Group Snapshot using snapshot_id
  dellemc_powermax_snapshot:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    snapshot_name: "ansible_sg_snap"
    snapshot_id: 135023964929
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=3 > create_sg_snap </td>
            <td>  bool </td>
            <td> When snapshot is created. </td>
            <td> Flag sets to true when the snapshot is created. </td>
        </tr>
                    <tr>
            <td colspan=3 > delete_sg_snap </td>
            <td>  bool </td>
            <td> When snapshot is deleted. </td>
            <td> Flag sets to true when the snapshot is deleted. </td>
        </tr>
                    <tr>
            <td colspan=3 > rename_sg_snap </td>
            <td>  bool </td>
            <td> When snapshot is renamed. </td>
            <td> Flag sets to true when the snapshot is renamed. </td>
        </tr>
                    <tr>
            <td colspan=3 > sg_snap_details </td>
            <td>  complex </td>
            <td> When snapshot exists. </td>
            <td> Details of the snapshot. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > expired </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether the snapshot is expired or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > generation/snapid </td>
                <td> int </td>
                <td>success</td>
                <td> The generation/snapshot ID of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > linked </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether the snapshot is linked or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > non_shared_tracks </td>
                <td> int </td>
                <td>success</td>
                <td> Number of non-shared tracks. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_source_volumes </td>
                <td> int </td>
                <td>success</td>
                <td> Number of source volumes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_storage_group_volumes </td>
                <td> int </td>
                <td>success</td>
                <td> Number of storage group volumes. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > restored </td>
                <td> bool </td>
                <td>success</td>
                <td> Indicates whether the snapshot is restored or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > source_volume </td>
                <td> list </td>
                <td>success</td>
                <td> Source volume details. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > capacity </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Volume capacity. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > capacity_gb </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Volume capacity in GB. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Volume ID. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > state </td>
                <td> str </td>
                <td>success</td>
                <td> State of the snapshot. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > time_to_live_expiry_date </td>
                <td> str </td>
                <td>success</td>
                <td> Time to live expiry date. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > timestamp </td>
                <td> str </td>
                <td>success</td>
                <td> Snapshot time stamp. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > timestamp_utc </td>
                <td> int </td>
                <td>success</td>
                <td> Snapshot time stamp specified in UTC. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > tracks </td>
                <td> int </td>
                <td>success</td>
                <td> Number of tracks. </td>
            </tr>
                                        </table>

### Authors
* Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Storage Pool Module

Manage storage pools on PowerMax/VMAX storage system

### Synopsis
 Managing storage pools on PowerMax storage system includes getting details of storage pools.

### Parameters
                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > pool</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the storage pool. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> State variable to determine whether storage pool will exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get specific storage pool details
  dellemc_powermax_storagepool:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    pool: "SRP_1"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=4 > pool_details </td>
            <td>  complex </td>
            <td> When storage pool exist. </td>
            <td> Details of the storage pool. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > serial_no </td>
                <td> str </td>
                <td>success</td>
                <td> The PowerMax array on which storage pool resides </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > service_levels </td>
                <td> list </td>
                <td>success</td>
                <td> The service levels supported by storage pool </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > srpId </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the storage pool </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > srp_capacity </td>
                <td> complex </td>
                <td>success</td>
                <td> SRP capacity details </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > effective_used_capacity_percent </td>
                    <td> int </td>
                    <td>success</td>
                    <td> The effective used capacity, expressed as a percentage </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > usable_total_tb </td>
                    <td> float </td>
                    <td>success</td>
                    <td> Usable capacity of the storage pool in TB </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > usable_used_tb </td>
                    <td> float </td>
                    <td>success</td>
                    <td> Used capacity of the storage pool in TB </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > srp_efficiency </td>
                <td> complex </td>
                <td>success</td>
                <td> SRP efficiency details </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > compression_state </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Indicates whether compression is enabled or disabled for this storage resource pool. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > total_free_tb </td>
                <td> str </td>
                <td>success</td>
                <td> Free capacity of the storage pool in TB </td>
            </tr>
                                        </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Volume Module

Manage volumes on PowerMax Storage System

### Synopsis
 Managing volumes on PowerMax storage system includes creating a volume, renaming a volume, expanding a volume, and deleting a volume.

### Parameters
                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > vol_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the volume. </td>
        </tr>
                    <tr>
            <td colspan=1 > sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the storage group. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the target storage group. </td>
        </tr>
                    <tr>
            <td colspan=1 > vol_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The native id of the volume.  <br> Required for rename and delete volume operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > size</td>
            <td> float  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new size of existing volume.  <br> Required for create and expand volume operations. </td>
        </tr>
                    <tr>
            <td colspan=1 > cap_unit</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>MB</li>  <li>GB</li>  <li>TB</li> </ul></td>
            <td> <br> volume capacity units  <br> If not specified, default value is GB. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new volume identifier for the volume. </td>
        </tr>
                    <tr>
            <td colspan=1 > vol_wwn</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The WWN of the volume. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Defines whether the volume should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                                    </table>

### Notes
* To expand a volume, either provide vol_id or vol_name or vol_wwn and sg_name
* size is required to create/expand a volume
* vol_id is required to rename/delete a volume
* vol_name, sg_name and new_sg_name is required to move volumes between storage groups
* Deletion of volume will fail if the storage group is part of a masking view

### Examples
```
- name: Create volume
  dellemc_powermax_volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    vol_name: "{{vol_name}}"
    sg_name: "{{sg_name}}"
    size: 1
    cap_unit: "{{cap_unit}}"
    state: 'present'

- name: Expanding volume size
  dellemc_powermax_volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    size:  3
    cap_unit: "{{cap_unit}}"
    vol_id: "0059B"
    state: 'present'

- name: Renaming volume
  dellemc_powermax_volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    new_name:  "Test_GOLD_vol_Renamed"
    vol_id: "0059B"
    state: 'present'

- name: Delete volume using volume ID
  dellemc_powermax_volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    vol_id: "0059B"
    state: 'absent'

- name: Delete volume using volume WWN
  dellemc_powermax_volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    vol_wwn: "60000970000197900237533030303246"
    state: 'absent'

- name: Move volume between storage group
  dellemc_powermax_volume:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    vol_name: "{{vol_name}}"
    sg_name: "{{sg_name}}"
    new_sg_name: "{{new_sg_name}}"
    state: 'present'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > volume_details </td>
            <td>  complex </td>
            <td> When volume exists. </td>
            <td> Details of the volume. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > allocated_percent </td>
                <td> int </td>
                <td>success</td>
                <td> Allocated percentage the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > cap_cyl </td>
                <td> int </td>
                <td>success</td>
                <td> Number of cylinders. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > cap_gb </td>
                <td> int </td>
                <td>success</td>
                <td> Volume capacity in GB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > cap_mb </td>
                <td> int </td>
                <td>success</td>
                <td> Volume capacity in MB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > effective_wwn </td>
                <td> str </td>
                <td>success</td>
                <td> Effective WWN of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > emulation </td>
                <td> str </td>
                <td>success</td>
                <td> Volume emulation type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > encapsulated </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for encapsulation. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > has_effective_wwn </td>
                <td> str </td>
                <td>success</td>
                <td> Flag for effective WWN presence. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > mobility_id_enabled </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for enabling mobility. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > num_of_front_end_paths </td>
                <td> int </td>
                <td>success</td>
                <td> Number of front end paths in the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > num_of_storage_groups </td>
                <td> int </td>
                <td>success</td>
                <td> Number of storage groups in which volume is present. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > pinned </td>
                <td> bool </td>
                <td>success</td>
                <td> Pinned flag. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > rdfGroupId </td>
                <td> int </td>
                <td>success</td>
                <td> RDFG number for volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > reserved </td>
                <td> bool </td>
                <td>success</td>
                <td> Reserved flag. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snapvx_source </td>
                <td> bool </td>
                <td>success</td>
                <td> Source SnapVX flag. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snapvx_target </td>
                <td> bool </td>
                <td>success</td>
                <td> Target SnapVX flag. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > ssid </td>
                <td> str </td>
                <td>success</td>
                <td> SSID of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > status </td>
                <td> str </td>
                <td>success</td>
                <td> Volume status. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storageGroupId </td>
                <td> str </td>
                <td>success</td>
                <td> Storage group ID of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storage_groups </td>
                <td> list </td>
                <td>success</td>
                <td> List of storage groups for the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > volumeId </td>
                <td> str </td>
                <td>success</td>
                <td> Unique ID of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > volume_identifier </td>
                <td> str </td>
                <td>success</td>
                <td> Name identifier for the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > wwn </td>
                <td> str </td>
                <td>success</td>
                <td> WWN of the volume. </td>
            </tr>
                                        </table>

### Authors
* Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
* Akash Shendge (@shenda1) <ansible.team@dell.com>
* Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>

--------------------------------
# SRDF Module

Manage SRDF pair on PowerMax/VMAX Storage System

### Synopsis
 Managing SRDF link on a PowerMax storage system includes creating an SRDF pair for a storage group, modifying the SRDF mode, modifying the SRDF state of an existing SRDF pair, and deleting an SRDF pair. All create and modify calls are asynchronous by default.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of storage group. SRDF pairings are managed at a storage group level.  <br> Required to identify the SRDF link. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number will refer to the source PowerMax/VMAX array when protecting a storage group. However srdf_state operations may be issued from primary or remote array. </td>
        </tr>
                    <tr>
            <td colspan=1 > remote_serial_no</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Integer 12-digit serial number of remote PowerMax or VMAX array.  <br> Required while creating an SRDF link. </td>
        </tr>
                    <tr>
            <td colspan=1 > rdfg_no</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The RDF group number.  <br> Optional parameter for each call. For a create operation, if specified, the array will reuse the RDF group, otherwise an error is returned. For modify and delete operations, if the RFD group number is not specified, and the storage group is protected by multiple RDF groups, then an error is raised. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the SRDF pairing should exist or not.  <br> present indicates that the SRDF pairing should exist in system.  <br> absent indicates that the SRDF pairing should not exist in system. </td>
        </tr>
                    <tr>
            <td colspan=1 > srdf_mode</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Active</li>  <li>Adaptive Copy</li>  <li>Synchronous</li>  <li>Asynchronous</li> </ul></td>
            <td> <br> The replication mode of the SRDF pair.  <br> Required when creating an SRDF pair.  <br> Can be modified by providing a required value. </td>
        </tr>
                    <tr>
            <td colspan=1 > srdf_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Establish</li>  <li>Resume</li>  <li>Restore</li>  <li>Suspend</li>  <li>Swap</li>  <li>Split</li>  <li>Failback</li>  <li>Failover</li>  <li>Setbias</li> </ul></td>
            <td> <br> Desired state of the SRDF pairing. While creating a new SRDF pair, allowed values are 'Establish' and 'Suspend'. If the state is not specified, the pair will be created in a 'Suspended' state. When modifying the state, only certain changes are allowed. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_rdf_group</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Overrides the SRDF group selection functionality and forces the creation of a new SRDF group.  <br> PowerMax has a limited number of RDF groups. If this flag is set to True, and the RDF groups are exhausted, then SRDF link creation will fail.  <br> If not specified, default value is 'false'. </td>
        </tr>
                    <tr>
            <td colspan=1 > wait_for_completion</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> Flag to indicate if the operation should be run synchronously or asynchronously. True signifies synchronous execution. By default, all create and update operations will be run asynchronously. </td>
        </tr>
                    <tr>
            <td colspan=1 > job_id</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Job ID of an asynchronous task. Can be used to get details of a job. </td>
        </tr>
                    <tr>
            <td colspan=1 > witness</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Flag to specify use of Witness for a Metro configuration. Setting to True signifies to use Witness, setting it to False signifies to use Bias. It is recommended to configure a witness for SRDF Metro in a production environment, this is configured via Unisphere for PowerMax UI or REST.  <br> The flag can be set only for modifying srdf_state to either Establish, Suspend, or Restore.  <br> While creating a Metro configuration, the witness flag must be set to True. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create and establish storagegroup SRDF/a pairing
  register: Job_details_body
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    remote_serial_no: "{{remote_serial_no}}"
    srdf_mode: 'Asynchronous'
    srdf_state: 'Establish'
    state: 'present'

- name: Create storagegroup SRDF/s pair in default suspended mode as an
        Synchronous task
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name2}}"
    remote_serial_no: "{{remote_serial_no}}"
    state: 'present'
    srdf_mode: 'Synchronous'
    wait_for_completion: True

- name: Create storagegroup Metro SRDF pair with Witness for resiliency
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    remote_serial_no: "{{remote_serial_no}}"
    state: 'present'
    srdf_mode: 'Active'
    wait_for_completion: True
    srdf_state: 'Establish'

- name: Suspend storagegroup Metro SRDF pair
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    remote_serial_no: "{{remote_serial_no}}"
    state: 'present'
    srdf_state: 'Suspend'

- name: Establish link for storagegroup Metro SRDF pair and use Bias for
        resiliency
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    remote_serial_no: "{{remote_serial_no}}"
    state: 'present'
    wait_for_completion: False
    srdf_state: 'Establish'
    witness: False

- name: Get SRDF details
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    state: 'present'

- name: Modify SRDF mode
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    srdf_mode: 'Synchronous'
    state: 'present'

- name: Failover SRDF link
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    srdf_state: 'Failover'
    state: 'present'

- name: Get SRDF Job status
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    job_id: "{{Job_details_body.Job_details.jobId}}"
    state: 'present'

- name: Establish SRDF link
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name2}}"
    srdf_state: 'Establish'
    state: 'present'

- name: Suspend SRDF link
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name2}}"
    srdf_state: 'Suspend'
    state: 'present'

- name: Delete SRDF link
  dellemc_powermax_srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    state: 'absent'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > Job_details </td>
            <td>  list </td>
            <td> When job exist. </td>
            <td> Details of the job. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > completed_date_milliseconds </td>
                <td> int </td>
                <td>success</td>
                <td> Date of job completion in milliseconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > jobId </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_modified_date </td>
                <td> str </td>
                <td>success</td>
                <td> Last modified date of job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_modified_date_milliseconds </td>
                <td> int </td>
                <td>success</td>
                <td> Last modified date of job in milliseconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > resourceLink </td>
                <td> str </td>
                <td>success</td>
                <td> Resource link w.r.t Unisphere. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > result </td>
                <td> str </td>
                <td>success</td>
                <td> Job description </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > status </td>
                <td> str </td>
                <td>success</td>
                <td> Status of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > task </td>
                <td> list </td>
                <td>success</td>
                <td> Details about the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > username </td>
                <td> str </td>
                <td>success</td>
                <td> Unisphere username. </td>
            </tr>
                                        <tr>
            <td colspan=2 > SRDF_link_details </td>
            <td>  complex </td>
            <td> When SRDF link exists. </td>
            <td> Details of the SRDF link. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hop2Modes </td>
                <td> str </td>
                <td>success</td>
                <td> SRDF hop2 mode. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hop2Rdfgs </td>
                <td> str </td>
                <td>success</td>
                <td> Hop2 RDF group number. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hop2States </td>
                <td> str </td>
                <td>success</td>
                <td> SRDF hop2 state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > largerRdfSides </td>
                <td> str </td>
                <td>success</td>
                <td> Larger volume side of the link. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > localR1InvalidTracksHop1 </td>
                <td> int </td>
                <td>success</td>
                <td> Number of invalid R1 tracks on local volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > localR2InvalidTracksHop1 </td>
                <td> int </td>
                <td>success</td>
                <td> Number of invalid R2 tracks on local volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > modes </td>
                <td> str </td>
                <td>success</td>
                <td> Mode of the SRDF pair. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > rdfGroupNumber </td>
                <td> int </td>
                <td>success</td>
                <td> RDF group number of the pair. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > remoteR1InvalidTracksHop1 </td>
                <td> int </td>
                <td>success</td>
                <td> Number of invalid R1 tracks on remote volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > remoteR2InvalidTracksHop1 </td>
                <td> int </td>
                <td>success</td>
                <td> Number of invalid R2 tracks on remote volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > remoteSymmetrix </td>
                <td> str </td>
                <td>success</td>
                <td> Remote symmetrix ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > states </td>
                <td> str </td>
                <td>success</td>
                <td> State of the SRDF pair. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storageGroupName </td>
                <td> str </td>
                <td>success</td>
                <td> Name of storage group that is SRDF protected. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > symmetrixId </td>
                <td> str </td>
                <td>success</td>
                <td> Primary symmetrix ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > totalTracks </td>
                <td> int </td>
                <td>success</td>
                <td> Total number of tracks in the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > volumeRdfTypes </td>
                <td> str </td>
                <td>success</td>
                <td> RDF type of volume. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Storage Group Module

Manage storage groups on PowerMax/VMAX Storage System

### Synopsis
 Managing storage groups on a PowerMax storage system includes listing the volumes of a storage group, creating a new storage group, deleting an existing storage group, adding existing volumes to an existing storage group, removing existing volumes from an existing storage group, creating new volumes in an existing storage group, modifying existing storage group attributes, adding child storage groups inside an existing storage group (parent), and removing a child storage group from an existing parent storage group.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > sg_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the storage group. </td>
        </tr>
                    <tr>
            <td colspan=1 > service_level</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The Name of SLO. </td>
        </tr>
                    <tr>
            <td colspan=1 > srp</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the storage resource pool.  <br> This parameter is ignored if service_level is not specified.  <br> Default is to use whichever is the default SRP on the array. </td>
        </tr>
                    <tr>
            <td colspan=1 > compression</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> compression on storage group.  <br> Compression parameter is ignored if service_level is not specified.  <br> Default is true. </td>
        </tr>
                    <tr>
            <td colspan=1 > volumes</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is a list of volumes.  <br> Each volume has four attributes-  <br> vol_name  <br> size  <br> cap_unit  <br> vol_id.  <br> Either the volume ID must be provided for existing volumes, or the name and size must be provided to add new volumes to SG. The unit is optional.  <br> vol_name - Represents the name of the volume  <br> size - Represents the volume size  <br> cap_unit - The unit in which size is represented. Default unit is GB. Choices are MB, GB, TB.  <br> vol_id - This is the volume ID </td>
        </tr>
                    <tr>
            <td colspan=1 > vol_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> Describes the state of volumes inside the SG. </td>
        </tr>
                    <tr>
            <td colspan=1 > child_storage_groups</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> This is a list of child storage groups </td>
        </tr>
                    <tr>
            <td colspan=1 > child_sg_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> Describes the state of CSG inside parent SG </td>
        </tr>
                    <tr>
            <td colspan=1 > new_sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of the storage group. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_policies</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of snapshot policy(s). </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_policy_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> Describes the state of snapshot policy for an SG </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the storage group should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get storage group details including volumes
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    state: "present"

- name: Create empty storage group
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "foo"
    service_level:  "Diamond"
    srp: "SRP_1"
    compression: True
    state: "present"

- name: Delete the storage Group
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "foo"
    state: "absent"

- name: Adding existing volume(s) to existing SG
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "foo"
    state: "present"
    volumes:
    - vol_id: "00028"
    - vol_id: "00018"
    - vol_id: "00025"
    vol_state: "present-in-group"

- name: Create new volumes for existing SG
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "foo"
    state: "present"
    volumes:
    - vol_name: "foo"
      size: 1
      cap_unit: "GB"
    - vol_name: "bar"
      size: 1
      cap_unit: "GB"
    vol_state: "present-in-group"

- name: Remove volume(s) from existing SG
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "foo"
    state: "present"
    volumes:
    - vol_id: "00028"
    - vol_id: "00018"
    - vol_name: "ansible-vol"
    vol_state: "absent-in-group"

- name: Adding child SG to parent SG
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "parent_sg"
    state: "present"
    child_storage_groups:
    - "pie"
    - "bar"
    child_sg_state: "present-in-group"

- name: Removing child SG from parent SG
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "parent_sg"
    state: "present"
    child_storage_groups:
    - "pie"
    - "bar"
    child_sg_state: "absent-in-group"

- name: Rename Storage Group
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_sg"
    new_sg_name: "ansible_sg_renamed"
    state: "present"

- name: Create a storage group with snapshot policies
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_test_sg"
    service_level: "Diamond"
    srp: "SRP_1"
    compression: True
    snapshot_policies:
      - "10min_policy"
      - "30min_policy"
    snapshot_policy_state: "present-in-group"
    state: "present"

- name: Add snapshot policy to a storage group
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_test_sg"
    snapshot_policies:
      - "15min_policy"
    snapshot_policy_state: "present-in-group"
    state: "present"

- name: Remove snapshot policy from a storage group
  dellemc_powermax_storagegroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "ansible_test_sg"
    snapshot_policies:
      - "15min_policy"
    snapshot_policy_state: "absent-in-group"
    state: "present"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=3 > add_child_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when a child SG is added. </td>
        </tr>
                    <tr>
            <td colspan=3 > add_new_vols_to_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when new volumes are added to the SG. </td>
        </tr>
                    <tr>
            <td colspan=3 > add_snapshot_policy_to_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when snapshot policy(s) is added to SG. </td>
        </tr>
                    <tr>
            <td colspan=3 > add_vols_to_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when existing volumes are added to the SG. </td>
        </tr>
                    <tr>
            <td colspan=3 > added_vols_details </td>
            <td>  list </td>
            <td> When value exists. </td>
            <td> Volume IDs of the volumes added. </td>
        </tr>
                    <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=3 > create_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when a new SG is created. </td>
        </tr>
                    <tr>
            <td colspan=3 > delete_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when an SG is deleted. </td>
        </tr>
                    <tr>
            <td colspan=3 > modify_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when an SG is modified. </td>
        </tr>
                    <tr>
            <td colspan=3 > remove_child_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when a child SG is removed. </td>
        </tr>
                    <tr>
            <td colspan=3 > remove_snapshot_policy_to_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to false when snapshot policy(s) is removed from SG. </td>
        </tr>
                    <tr>
            <td colspan=3 > remove_vols_from_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when volumes are removed. </td>
        </tr>
                    <tr>
            <td colspan=3 > removed_vols_details </td>
            <td>  list </td>
            <td> When value exists. </td>
            <td> Volume IDs of the volumes removed. </td>
        </tr>
                    <tr>
            <td colspan=3 > rename_sg </td>
            <td>  bool </td>
            <td> When value exists. </td>
            <td> Sets to true when an SG is renamed. </td>
        </tr>
                    <tr>
            <td colspan=3 > snapshot_policy_compliance_details </td>
            <td>  complex </td>
            <td> When snapshot policy associated.. </td>
            <td> The compliance status of this storage group. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > compliance </td>
                <td> str </td>
                <td>success</td>
                <td> Compliance status </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sl_compliance </td>
                <td> complex </td>
                <td>success</td>
                <td> Compliance details </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > compliance </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Compliance status </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > sl_name </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Name of the snapshot policy </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > sl_count </td>
                <td> int </td>
                <td>success</td>
                <td> Number of snapshot policies associated with storage group </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storage_group_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the storage group </td>
            </tr>
                                        <tr>
            <td colspan=3 > storage_group_details </td>
            <td>  complex </td>
            <td> When storage group exists. </td>
            <td> Details of the storage group. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > base_slo_name </td>
                <td> str </td>
                <td>success</td>
                <td> Base Service Level Objective (SLO) of a storage group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > cap_gb </td>
                <td> int </td>
                <td>success</td>
                <td> Storage group capacity in GB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > compression </td>
                <td> bool </td>
                <td>success</td>
                <td> Compression flag. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > device_emulation </td>
                <td> str </td>
                <td>success</td>
                <td> Device emulation type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_child_sgs </td>
                <td> int </td>
                <td>success</td>
                <td> Number of child storage groups. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_masking_views </td>
                <td> int </td>
                <td>success</td>
                <td> Number of masking views associated with the storage group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_parent_sgs </td>
                <td> int </td>
                <td>success</td>
                <td> Number of parent storage groups. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_snapshots </td>
                <td> int </td>
                <td>success</td>
                <td> Number of snapshots for the storage group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_vols </td>
                <td> int </td>
                <td>success</td>
                <td> Number of volumes in the storage group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > service_level </td>
                <td> str </td>
                <td>success</td>
                <td> Type of service level. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > slo </td>
                <td> str </td>
                <td>success</td>
                <td> Service level objective (SLO) type. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > slo_compliance </td>
                <td> str </td>
                <td>success</td>
                <td> Type of SLO compliance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > srp </td>
                <td> str </td>
                <td>success</td>
                <td> Storage resource pool. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > storageGroupId </td>
                <td> str </td>
                <td>success</td>
                <td> Id for the storage group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> type of storage group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > unprotected </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for storage group protection. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > vp_saved_percent </td>
                <td> int </td>
                <td>success</td>
                <td> Percentage saved for virtual pools. </td>
            </tr>
                                        <tr>
            <td colspan=3 > storage_group_volumes </td>
            <td>  list </td>
            <td> When value exists. </td>
            <td> Volume IDs of storage group volumes. </td>
        </tr>
                    <tr>
            <td colspan=3 > storage_group_volumes_details </td>
            <td>  complex </td>
            <td> When storage group volumes exists. </td>
            <td> Details of the storage group volumes. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > effective_wwn </td>
                <td> str </td>
                <td>success</td>
                <td> Effective WWN of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > volumeId </td>
                <td> str </td>
                <td>success</td>
                <td> Unique ID of the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > volume_identifier </td>
                <td> str </td>
                <td>success</td>
                <td> Name associated with the volume. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > wwn </td>
                <td> str </td>
                <td>success</td>
                <td> WWN of the volume. </td>
            </tr>
                                        </table>

### Authors
* Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
* Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>
* Ambuj Dubey (@AmbujDube) <ansible.team@dell.com>

--------------------------------
# Host Group Module

Manage a host group (cascaded initiator group) on a PowerMax/VMAX storage system

### Synopsis
 Managing a host group on a PowerMax storage system includes creating a host group with a set of hosts, adding or removing hosts to or from a host group, renaming a host group, modifying host flags of a host group, and deleting a host group.

### Parameters
                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > hostgroup_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the host group. No Special Character support except for _. Case sensitive for REST Calls. </td>
        </tr>
                    <tr>
            <td colspan=1 > hosts</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of host names to be added to the host group or removed from the host group.  <br> Creation of an empty host group is allowed. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the host group should be present or absent on the system.  <br> present - indicates that the host group should be present on the system  <br> absent - indicates that the host group should be absent on the system </td>
        </tr>
                    <tr>
            <td colspan=1 > host_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> Define whether the host should be present or absent in the host group.  <br> present-in-group - indicates that the hosts should exist in the host group  <br> absent-in-group - indicates that the hosts should not exist in the host group </td>
        </tr>
                    <tr>
            <td colspan=1 > host_flags</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> input as an yaml dictionary  <br> List of all host_flags -  <br> 1. volume_set_addressing  <br> 2. disable_q_reset_on_ua  <br> 3. environ_set  <br> 4. avoid_reset_broadcast  <br> 5. openvms  <br> 6. scsi_3  <br> 7. spc2_protocol_version  <br> 8. scsi_support1  <br> 9. consistent_lun  <br> Possible values are true, false, unset(default state) </td>
        </tr>
                    <tr>
            <td colspan=1 > host_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>default</li>  <li>hpux</li> </ul></td>
            <td> <br> Describing the OS type (default or hpux) </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name for the host group for the renaming function. No Special Character support except for _. Case sensitive for REST Calls </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                                    </table>

### Notes
* In the gather facts module, empty host groups will be listed as hosts.
* host_flags and host_type are mutually exclusive parameters.
* Hostgroups with 'default' host_type will have 'default' hosts.
* Hostgroups with 'hpux' host_type will have 'hpux' hosts.

### Examples
```
- name: Create host group with 'default' host_type
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    host_type: "default"
    hosts:
      - ansible_test_1
    host_state: 'present-in-group'
    state: 'present'

- name: Create host group with 'hpux' host_type
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_2"
    host_type: "hpux"
    hosts:
      - ansible_test_2
    host_state: 'present-in-group'
    state: 'present'

- name: Create host group with host_flags
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_3"
    hosts:
      - ansible_test_3
    state: 'present'
    host_state: 'present-in-group'
    host_flags:
      spc2_protocol_version: true
      consistent_lun: true
      volume_set_addressing: 'unset'
      disable_q_reset_on_ua: false
      openvms: 'unset'

- name: Get host group details
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    state: 'present'

- name: Adding host to host group
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    hosts:
      - Ansible_Testing_host2
    state: 'present'
    host_state: 'present-in-group'

- name: Removing host from host group
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    hosts:
      - Ansible_Testing_host2
    state: 'present'
    host_state: 'absent-in-group'

- name: Modify host group using host_type
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    host_type: "hpux"
    state: 'present'

- name: Modify host group using host_flags
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    host_flags:
      spc2_protocol_version: unset
      disable_q_reset_on_ua: false
      openvms: false
      avoid_reset_broadcast: true
    state: 'present'

- name: Rename host group
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_HG_1"
    new_name: "ansible_test_hostgroup_1"
    state: 'present'

- name: Delete host group
  dellemc_powermax_hostgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    hostgroup_name: "ansible_test_hostgroup_1"
    state: 'absent'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=3 > hostgroup_details </td>
            <td>  complex </td>
            <td> When host group exist. </td>
            <td> Details of the host group. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > consistent_lun </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for consistent LUN in the host group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > disabled_flags </td>
                <td> list </td>
                <td>success</td>
                <td> List of any disabled port flags overridden by the initiator. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > enabled_flags </td>
                <td> list </td>
                <td>success</td>
                <td> List of any enabled port flags overridden by the initiator. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > host </td>
                <td> list </td>
                <td>success</td>
                <td> List of hosts present in the host group. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > hostId </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier for the host. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > initiator </td>
                    <td> list </td>
                    <td>success</td>
                    <td> List of initiators present in the host. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > hostGroupId </td>
                <td> str </td>
                <td>success</td>
                <td> Host group ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > maskingview </td>
                <td> list </td>
                <td>success</td>
                <td> Masking view in which host group is present. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_hosts </td>
                <td> int </td>
                <td>success</td>
                <td> Number of hosts in the host group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_initiators </td>
                <td> int </td>
                <td>success</td>
                <td> Number of initiators in the host group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_masking_views </td>
                <td> int </td>
                <td>success</td>
                <td> Number of masking views associated with the host group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > port_flags_override </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether any of the initiator's port flags are overridden. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of initiator of the hosts of the host group. </td>
            </tr>
                                        </table>

### Authors
* Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# Port Module

Manage ports on PowerMax/VMAX Storage System

### Synopsis
 Managing ports on PowerMax storage system includes getting details of a port.

### Parameters
                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > ports</td>
            <td> list   <br> elements: dict </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> List of port director and port id </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get details of single/multiple ports
  dellemc_powermax_port:
    unispherehost: "{{unispherehost}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    ports:
    - director_id: "FA-1D"
      port_id: "5"
    - director_id: "SE-1F"
      port_id: "29"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=4 > port_details </td>
            <td>  list </td>
            <td> When the port exist. </td>
            <td> Details of the port. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > symmetrixPort </td>
                <td> list </td>
                <td>success</td>
                <td> Type of volume. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > aclx </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether access control logic is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > avoid_reset_broadcast </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Avoid Reset Broadcasting feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > common_serial_number </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Common Serial Number feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > director_status </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Director status. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > disable_q_reset_on_ua </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Disable Q Reset on UA (Unit Attention) is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > enable_auto_negotiate </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Enable Auto Negotiate feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > environ_set </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the environmental error reporting feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > hp_3000_mode </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether HP 3000 Mode is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > identifier </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Unique identifier for port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > init_point_to_point </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether Init Point to Point is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > iscsi_target </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether ISCSI target is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > maskingview </td>
                    <td> list </td>
                    <td>success</td>
                    <td> List of Masking views that the port is a part of. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > max_speed </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Maximum port speed in GB/Second. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > negotiate_reset </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Negotiate Reset feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > negotiated_speed </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Negotiated speed in GB/Second. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > no_participating </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the No Participate feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > num_of_cores </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of cores for the director. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > num_of_mapped_vols </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of volumes mapped with the port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > num_of_masking_views </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of masking views associated with the port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > num_of_port_groups </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of port groups associated with the port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > port_status </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Port status, ON/OFF. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > portgroup </td>
                    <td> list </td>
                    <td>success</td>
                    <td> List of masking views associated with the port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > scsi_3 </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the SCSI-3 protocol is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > scsi_support1 </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the SCSI Support1 is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > siemens </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Siemens feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > soft_reset </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Soft Reset feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > spc2_protocol_version </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the SPC2 Protocol Version feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > sunapee </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Sunapee feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > symmetrixPortKey </td>
                    <td> list </td>
                    <td>success</td>
                    <td> Symmetrix system director and port in the port group. </td>
                </tr>
                                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > drectorId </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Director ID of the port. </td>
                    </tr>
                                    <tr>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td class="elbow-placeholder">&nbsp;</td>
                        <td colspan=1 > portId </td>
                        <td> str </td>
                        <td>success</td>
                        <td> Port number of the port. </td>
                    </tr>
                                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > type </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Type of port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > unique_wwn </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the Unique WWN feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > vnx_attached </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether the VNX attached feature is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > volume_set_addressing </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Indicates whether Volume Vet Addressing is enabled or disabled. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > wwn_node </td>
                    <td> str </td>
                    <td>success</td>
                    <td> WWN node of port. </td>
                </tr>
                                                                    </table>

### Authors
* Ashish Verma (@vermaa31) <ansible.team@dell.com>

--------------------------------
# Metro DR Module

Manage metro DR environment on PowerMax/VMAX Storage System

### Synopsis
 Managing a metro DR environment on a PowerMax storage system includes getting details of any specific metro DR environment, creating a metro DR environment, converting an existing SG into a metro DR environment, modifying metro DR environment attributes and deleting a metro DR environment.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=2 > env_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Name of the metro DR environment.  <br> Metro DR environment name will be unique across PowerMax. </td>
        </tr>
                    <tr>
            <td colspan=2 > sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the storage group.  <br> Storage group will be present on the primary metro array and a storage group with the same name will be created on remote and DR arrays in a create operation.  <br> Storage group name is required in 'create metro DR environment' and 'convert SG into metro DR environment' operations. </td>
        </tr>
                    <tr>
            <td colspan=2 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Serial number of the primary metro array. </td>
        </tr>
                    <tr>
            <td colspan=2 > metro_serial_no</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Serial number of the remote metro array.  <br> It is required only in create and convert operations. </td>
        </tr>
                    <tr>
            <td colspan=2 > dr_serial_no</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Serial number of the DR array.  <br> It is required in create and convert operations. </td>
        </tr>
                    <tr>
            <td colspan=2 > replication_mode</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>Asynchronous</li>  <li>Adaptive Copy</li> </ul></td>
            <td> <br> Replication mode whose value will indicate how the data will be replicated.  <br> It is required in create and modify operations.  <br> It is a mandatory parameter in a create operation but optional in a modify operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > wait_for_completion</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> The flag indicates if the operation should be run synchronously or asynchronously.  <br> True signifies synchronous execution.  <br> By default, create and convert are asynchronous operations, whereas modify is a synchronous operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > new_rdf_group_r1</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td></td>
            <td> <br> The flag indicates whether or not to create a new RDFG for a Metro R1 array to a DR array, or to autoselect from an existing one.  <br> Used in only create operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > new_rdf_group_r2</td>
            <td> bool  </td>
            <td></td>
            <td> True </td>
            <td></td>
            <td> <br> The flag indicates whether or not to create a new RDFG for a Metro R2 array to a DR array, or to autoselect from an existing one.  <br> It is used only in create operation. </td>
        </tr>
                    <tr>
            <td colspan=2 > remove_r1_dr_rdfg</td>
            <td> bool  </td>
            <td></td>
            <td> False </td>
            <td></td>
            <td> <br> The flag indicates whether or not to override default behavior and delete R11-R2 RDFG from the metro R1 side.  <br> It is used only in delete operations. </td>
        </tr>
                    <tr>
            <td colspan=2 > srdf_param</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> It contains parameters related to SRDF links.  <br> It is used only in modify operations. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > srdf_state </td>
                <td> str  </td>
                <td> True </td>
                <td></td>
                <td> <ul> <li>Split</li>  <li>Restore</li>  <li>SetMode</li>  <li>Failback</li>  <li>Failover</li>  <li>Establish</li>  <li>Suspend</li>  <li>UpdateR1</li>  <li>Recover</li> </ul></td>
                <td>  <br> State of the SRDF link.  <br> It is a mandatory parameter for modify operations.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro </td>
                <td> bool  </td>
                <td> False </td>
                <td> False </td>
                <td></td>
                <td>  <br> The flag indicates whether or not to direct srdf_state change towards the R1--R2 Metro Device leg of the metro DR environment.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr </td>
                <td> bool  </td>
                <td> False </td>
                <td> False </td>
                <td></td>
                <td>  <br> The flag indicates whether or not to direct srdf_state change towards device pairs on the disaster recovery leg of the metro DR environment.  </td>
            </tr>
                    <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > keep_r2 </td>
                <td> bool  </td>
                <td> False </td>
                <td> False </td>
                <td></td>
                <td>  <br> The flag indicates whether or not in the case of srdf state suspend to make R2 data on metro available to the host.  </td>
            </tr>
                            <tr>
            <td colspan=2 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> State variable to determine whether metro DR environment will exist or not. </td>
        </tr>
                    <tr>
            <td colspan=2 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=2 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=2 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=2 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=2 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get metro environment details
  dellemc_powermax_metrodr:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    env_name: "ansible_metrodr_env"
    state: "present"

- name: Convert SG to metro DR environment
  dellemc_powermax_metrodr:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    sg_name: "ansible_sg"
    env_name: "ansible_metrodr_env"
    serial_no: "{{serial_no}}"
    metro_serial_no: "{{metro_serial_no}}"
    dr_serial_no: "{{dr_serial_no}}"
    replication_mode: "Asynchronous"
    wait_for_completion: False
    state: "present"

- name: Create metro DR environment
  dellemc_powermax_metrodr:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    sg_name: "ansible_sg"
    env_name: "ansible_metrodr_env"
    serial_no: "{{serial_no}}"
    metro_serial_no: "{{metro_serial_no}}"
    dr_serial_no: "{{dr_serial_no}}"
    replication_mode: "Asynchronous"
    new_rdf_group_r1: True
    new_rdf_group_r2: True
    wait_for_completion: False
    state: "present"

- name: Modify metro DR environment
  dellemc_powermax_metrodr:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    env_name: "ansible_metrodr_env"
    srdf_param:
      srdf_state: "Suspend"
      metro: True
      dr: True
      keep_r2: True
    wait_for_completion: True
    state: "present"

- name: Delete metro DR environment
  dellemc_powermax_metrodr:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    env_name: "ansible_metrodr_env"
    remove_r1_dr_rdfg: True
    state: 'absent'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > Job_details </td>
            <td>  dict </td>
            <td> When job exist. </td>
            <td> Details of the job. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > completed_date_milliseconds </td>
                <td> int </td>
                <td>success</td>
                <td> Date of job completion in milliseconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > jobId </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_modified_date </td>
                <td> str </td>
                <td>success</td>
                <td> Last modified date of job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_modified_date_milliseconds </td>
                <td> int </td>
                <td>success</td>
                <td> Last modified date of job in milliseconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > resourceLink </td>
                <td> str </td>
                <td>success</td>
                <td> Resource link w.r.t Unisphere. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > result </td>
                <td> str </td>
                <td>success</td>
                <td> Job description </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > status </td>
                <td> str </td>
                <td>success</td>
                <td> Status of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > task </td>
                <td> list </td>
                <td>success</td>
                <td> Details about the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > username </td>
                <td> str </td>
                <td>success</td>
                <td> Unisphere username. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > metrodr_env_details </td>
            <td>  dict </td>
            <td> When environment exists. </td>
            <td> Details of the metro DR environment link. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > capacity_gb </td>
                <td> float </td>
                <td>success</td>
                <td> Size of volume in GB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr_exempt </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag to indication that if there are exempt devices (volumes) in the DR site or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr_link_state </td>
                <td> str </td>
                <td>success</td>
                <td> Status of DR site. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr_percent_complete </td>
                <td> int </td>
                <td>success</td>
                <td> Percentage synchronized in DR session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr_rdf_mode </td>
                <td> str </td>
                <td>success</td>
                <td> Replication mode with DR site. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr_remain_capacity_to_copy_mb </td>
                <td> int </td>
                <td>success</td>
                <td> Remaining capacity to copy at DR site. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr_service_state </td>
                <td> str </td>
                <td>success</td>
                <td> The HA state of the DR session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > dr_state </td>
                <td> str </td>
                <td>success</td>
                <td> The pair states of the DR session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > environment_exempt </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag to indication that if there are exempt devices (volumes) in the environment or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > environment_state </td>
                <td> str </td>
                <td>success</td>
                <td> The state of the smart DR environment. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro_exempt </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag to indication that if there are exempt devices (volumes) in the DR site or not. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro_link_state </td>
                <td> str </td>
                <td>success</td>
                <td> Status of metro site. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro_r1_array_health </td>
                <td> str </td>
                <td>success</td>
                <td> Health status of metro R1 array. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro_r2_array_health </td>
                <td> str </td>
                <td>success</td>
                <td> Health status of metro R1 array. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro_service_state </td>
                <td> str </td>
                <td>success</td>
                <td> The HA state of the metro session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro_state </td>
                <td> str </td>
                <td>success</td>
                <td> The pair states of the metro session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > metro_witness_state </td>
                <td> str </td>
                <td>success</td>
                <td> The witness state of the metro session. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> The smart DR environment name. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > valid </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag to indicate whether valid environment or not. </td>
            </tr>
                                        </table>

### Authors
* Vivek Soni (@v-soni11) <ansible.team@dell.com>
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Job Module

Gets the detail information about a Job of a PowerMax/VMAX storage system

### Synopsis
 Gets details of a Job from a specified PowerMax/VMAX storage system.
 The details listed are of an asynchronous task.

### Parameters
                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > job_id</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Job ID of an asynchronous task, used for getting details of a job. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get the details of a Job.
  dellemc_powermax_job:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    job_id: "1570622921504"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > Job_details </td>
            <td>  dict </td>
            <td> When job exist. </td>
            <td> Details of the job. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > completed_date_milliseconds </td>
                <td> int </td>
                <td>success</td>
                <td> Date of job completion in milliseconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > jobId </td>
                <td> str </td>
                <td>success</td>
                <td> Unique identifier of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_modified_date </td>
                <td> str </td>
                <td>success</td>
                <td> Last modified date of job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_modified_date_milliseconds </td>
                <td> int </td>
                <td>success</td>
                <td> Last modified date of job in milliseconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > resourceLink </td>
                <td> str </td>
                <td>success</td>
                <td> Resource link w.r.t Unisphere. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > result </td>
                <td> str </td>
                <td>success</td>
                <td> Job description </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > status </td>
                <td> str </td>
                <td>success</td>
                <td> Status of the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > task </td>
                <td> list </td>
                <td>success</td>
                <td> Details about the job. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > username </td>
                <td> str </td>
                <td>success</td>
                <td> Unisphere username. </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Masking View Module

Managing masking views on PowerMax/VMAX Storage System

### Synopsis
 Managing masking views on PowerMax storage system includes, creating masking view with port group, storage group and host or host group, renaming masking view and deleting masking view.
 For creating a masking view -
 (i) portgroup_name,
 (ii) sg_name and
 (iii) any one of host_name or hostgroup_name is required.
 All three entities must be present on the array.
 For renaming a masking view, the 'new_mv_name' is required. After a masking view is created, only its name can be changed. No underlying entity (portgroup, storagegroup, host or hostgroup) can be changed on the masking view.

### Parameters
                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > mv_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the masking view. No Special Character support except for _. Case sensitive for REST Calls. </td>
        </tr>
                    <tr>
            <td colspan=1 > portgroup_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the existing port group. </td>
        </tr>
                    <tr>
            <td colspan=1 > host_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the existing host. This parameter is to create an exclusive or host export </td>
        </tr>
                    <tr>
            <td colspan=1 > hostgroup_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the existing host group. This parameter is used to create cluster export </td>
        </tr>
                    <tr>
            <td colspan=1 > sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The name of the existing storage group. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_mv_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name for the renaming function. No Special Character support except for _. Case sensitive for REST Calls. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Defines whether the masking view should exist or not. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create MV with hostgroup
  dellemc_powermax_maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "{{mv_name}}"
    portgroup_name: "Ansible_Testing_portgroup"
    hostgroup_name: "Ansible_Testing_hostgroup"
    sg_name: "Ansible_Testing_SG"
    state: "present"

- name: Create MV with host
  dellemc_powermax_maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "{{mv_name}}"
    portgroup_name: "Ansible_Testing_portgroup"
    host_name: "Ansible_Testing_host"
    sg_name: "Ansible_Testing_SG"
    state: "present"

- name: Rename host masking view
  dellemc_powermax_maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "{{mv_name}}"
    new_mv_name: "Ansible_Testing_mv_renamed"
    state: "present"

- name: Delete host masking view
  dellemc_powermax_maskingview:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    mv_name: "Ansible_Testing_mv_renamed"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > create_mv </td>
            <td>  bool </td>
            <td> When masking view is created. </td>
            <td> Flag sets to true when a new masking view is created. </td>
        </tr>
                    <tr>
            <td colspan=2 > delete_mv </td>
            <td>  bool </td>
            <td> When masking view is deleted. </td>
            <td> Flag sets to true when a masking view is deleted. </td>
        </tr>
                    <tr>
            <td colspan=2 > modify_mv </td>
            <td>  bool </td>
            <td> When masking view is modified. </td>
            <td> Flag sets to true when a masking view is modified. </td>
        </tr>
                    <tr>
            <td colspan=2 > mv_details </td>
            <td>  list </td>
            <td> When masking view exist. </td>
            <td> Details of masking view. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hostId </td>
                <td> str </td>
                <td>success</td>
                <td> Host group present in the masking view. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > maskingViewId </td>
                <td> str </td>
                <td>success</td>
                <td> Masking view ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > portGroupId </td>
                <td> str </td>
                <td>success</td>
                <td> Port group present in the masking view. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storageGroupId </td>
                <td> str </td>
                <td>success</td>
                <td> Storage group present in the masking view. </td>
            </tr>
                                        </table>

### Authors
* Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
* Prashant Rakheja (@prashant-dell) <ansible.team@dell.com>

--------------------------------
# Port Group Module

Manage port groups on PowerMax/VMAX Storage System

### Synopsis
 Managing port groups on a PowerMax storage system includes creating a port group with a set of ports, adding or removing single or multiple ports to or from the port group, renaming the port group and deleting the port group.

### Parameters
                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > portgroup_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the port group. No Special Character support except for _. Case sensitive for REST Calls. </td>
        </tr>
                    <tr>
            <td colspan=1 > ports</td>
            <td> list   <br> elements: dict </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of directors and ports to be added or removed to or from the port group </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the port group while renaming. No Special Character support except for _. Case sensitive for REST Calls. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the port group should exist or not.  <br> present - indicates that the port group should be present on the system  <br> absent - indicates that the port group should not be present on the system </td>
        </tr>
                    <tr>
            <td colspan=1 > port_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-group</li>  <li>absent-in-group</li> </ul></td>
            <td> <br> Define whether the port should be present or absent in the port group.  <br> present-in-group - indicates that the ports should be present on a port group object  <br> absent-in-group - indicates that the ports should not be present on a port group object </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                            </table>


### Examples
```
- name: Create port group without ports
  dellemc_powermax_portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "{{portgroup_name}}"
    state: "present"

- name: Create port group with ports
  dellemc_powermax_portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "{{portgroup_name}}"
    state: "present"
    ports:
    - director_id: "FA-1D"
      port_id: "5"
    - director_id: "FA-2D"
      port_id: "5"
    port_state: "present-in-group"

- name: Add ports to port group
  dellemc_powermax_portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "{{portgroup_name}}"
    state: "present"
    ports:
    - director_id: "FA-2D"
      port_id: "8"
    - director_id: "FA-2D"
      port_id: "9"
    port_state: "present-in-group"

- name: Remove ports from port group
  dellemc_powermax_portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "{{portgroup_name}}"
    state: "present"
    ports:
    - director_id: "FA-2D"
      port_id: "8"
    - director_id: "FA-2D"
      port_id: "9"
    port_state: "absent-in-group"

- name: Modify port group
  dellemc_powermax_portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "{{portgroup_name}}"
    state: "present"
    new_name: "{{new_name}}"

- name: Delete port group
  dellemc_powermax_portgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{array_id}}"
    portgroup_name: "{{portgroup_name}}"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=3>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=3 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=3 > portgroup_details </td>
            <td>  list </td>
            <td> When the port group exist. </td>
            <td> Details of the port group. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_masking_views </td>
                <td> int </td>
                <td>success</td>
                <td> Number of masking views in where port group is associated. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > num_of_ports </td>
                <td> int </td>
                <td>success</td>
                <td> Number of ports in the port group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > portGroupId </td>
                <td> str </td>
                <td>success</td>
                <td> Port group ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > symmetrixPortKey </td>
                <td> list </td>
                <td>success</td>
                <td> Symmetrix system director and port in the port group. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > directorId </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Director ID of the port. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=1 > portId </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Port number of the port. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=2 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of ports in port group. </td>
            </tr>
                                        </table>

### Authors
* Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
* Ashish Verma (@vermaa31) <ansible.team@dell.com>
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
# Process Storage Pool Dict Module

Process storage pools on PowerMax/VMAX Storage System

### Synopsis
 Process storage pools on PowerMax/VMAX storage system to find out the storage pool with maximum free storage

### Parameters
                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > pool_data</td>
            <td> list   <br> elements: dict </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Storage pool details including service levels, usable total space, usable free space, total free space. </td>
        </tr>
                    <tr>
            <td colspan=1 > size</td>
            <td> float  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Size of the storage group in GB </td>
        </tr>
                    <tr>
            <td colspan=1 > sg_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Name of the storage group </td>
        </tr>
                    <tr>
            <td colspan=1 > service_level</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Service level of the storage group </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get best suitable Pool using our python sorting module
  register: assigned_pool
  process_storage_pool_dict:
    unispherehost: "{{unispherehost}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    pool_data: "{{ pools_list }}"
    size: 40
    service_level: "Diamond"
    sg_name: "intellgent_provisioning"
```

### Return Values
                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=2 > all_pools </td>
            <td>  list </td>
            <td> when pool exists </td>
            <td> List of all pools on unisphere </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > serial_no </td>
                <td> str </td>
                <td>success</td>
                <td> The PowerMax array on which storage pool resides </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storage_pool </td>
                <td> str </td>
                <td>success</td>
                <td> The ID of the storage pool </td>
            </tr>
                                        <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > serial_no </td>
            <td>  str </td>
            <td> when array satisfies the given criteria </td>
            <td> The PowerMax array on which storage pool resides </td>
        </tr>
                    <tr>
            <td colspan=2 > storage_group </td>
            <td>  str </td>
            <td> when storage group exists satisfying the given criteria </td>
            <td> Name of the storage group </td>
        </tr>
                    <tr>
            <td colspan=2 > storage_pool </td>
            <td>  str </td>
            <td> when storage pool exists satisfying the given criteria </td>
            <td> The ID of the storage pool </td>
        </tr>
                    </table>

### Authors
* Akash Shendge (@shenda1) <ansible.team@dell.com>

--------------------------------
# Host Module

Manage host (initiator group) on PowerMax/VMAX Storage System

### Synopsis
 Managing hosts on a PowerMax storage system includes creating a host with a set of initiators and host flags, adding and removing initiators to or from a host, modifying host flag values, renaming a host, and deleting a host.

### Parameters
                                                                                                                                                                                                                                                                                                                    
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > host_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The name of the host. No Special Character support except for _. Case sensitive for REST Calls.  <br> Creation of an empty host is allowed </td>
        </tr>
                    <tr>
            <td colspan=1 > initiators</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of Initiator WWN or IQN to be added to the host or removed from the host. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>absent</li>  <li>present</li> </ul></td>
            <td> <br> Define whether the host should exist or not.  <br> present - indicates that the host should exist in the system  <br> absent - indicates that the host should not exist in the system </td>
        </tr>
                    <tr>
            <td colspan=1 > initiator_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-host</li>  <li>absent-in-host</li> </ul></td>
            <td> <br> Define whether the initiators should be present or absent on the host.  <br> present-in-host - indicates that the initiators should exist on the host  <br> absent-in-host - indicates that the initiators should not exist on the host  <br> Required when creating a host with initiators or adding and removing initiators to or from an existing host </td>
        </tr>
                    <tr>
            <td colspan=1 > host_flags</td>
            <td> dict  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Input as a yaml dictionary  <br> List of all host_flags-  <br> 1. volume_set_addressing  <br> 2. disable_q_reset_on_ua  <br> 3. environ_set  <br> 4. avoid_reset_broadcast  <br> 5. openvms  <br> 6. scsi_3  <br> 7. spc2_protocol_version  <br> 8. scsi_support1  <br> 9. consistent_lun  <br> Possible values are true, false, unset (default state) </td>
        </tr>
                    <tr>
            <td colspan=1 > host_type</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>default</li>  <li>hpux</li> </ul></td>
            <td> <br> Describing the OS type (default or hpux) </td>
        </tr>
                    <tr>
            <td colspan=1 > new_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The new name of the host for the renaming function. No Special Character support except for _. Case sensitive for REST Calls </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                                    </table>

### Notes
* host_flags and host_type are mutually exclusive parameters.

### Examples
```
- name: Create host with host_type 'default'
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    host_type: "default"
    state: 'present'

- name: Create host with host_type 'hpux'
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_2"
    host_type: "hpux"
    state: 'present'

- name: Create host with host_flags
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_3"
    initiators:
      - 10000090fa7b4e85
    host_flags:
      spc2_protocol_version: true
      consistent_lun: true
      volume_set_addressing: 'unset'
      disable_q_reset_on_ua: false
      openvms: 'unset'
    state: 'present'
    initiator_state: 'present-in-host'

- name: Get host details
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    state: 'present'

- name: Adding initiator to host
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    initiators:
      - 10000090fa3d303e
    initiator_state: 'present-in-host'
    state: 'present'

- name: Removing initiator from host
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    initiators:
      - 10000090fa3d303e
    initiator_state: 'absent-in-host'
    state: 'present'

- name: Modify host using host_type
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    host_type: "hpux"
    state: 'present'

- name: Modify host using host_flags
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    host_flags:
      spc2_protocol_version: unset
      consistent_lun: unset
      volume_set_addressing: true
      disable_q_reset_on_ua: false
      openvms: false
      avoid_reset_broadcast: true
    state: 'present'

- name: Rename host
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1"
    new_name: "ansible_test_1_host"
    state: 'present'

- name: Delete host
  dellemc_powermax_host:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    host_name: "ansible_test_1_host"
    state: 'absent'
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > host_details </td>
            <td>  complex </td>
            <td> When host exist. </td>
            <td> Details of the host. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > bw_limit </td>
                <td> int </td>
                <td>success</td>
                <td> Bandwidth limit of the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > consistent_lun </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for consistent LUN in host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > disabled_flags </td>
                <td> list </td>
                <td>success</td>
                <td> List of any disabled port flags overridden by the initiator. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > enabled_flags </td>
                <td> list </td>
                <td>success</td>
                <td> List of any enabled port flags overridden by the initiator. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hostId </td>
                <td> str </td>
                <td>success</td>
                <td> Host ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > hostgroup </td>
                <td> list </td>
                <td>success</td>
                <td> List of host groups that the host is associated with. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > initiator </td>
                <td> list </td>
                <td>success</td>
                <td> List of initiators present in the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > maskingview </td>
                <td> list </td>
                <td>success</td>
                <td> List of masking view in which the host group is present. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > num_of_hostgroups </td>
                <td> int </td>
                <td>success</td>
                <td> Number of host groups associated with the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > num_of_initiators </td>
                <td> int </td>
                <td>success</td>
                <td> Number of initiators present in the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > num_of_masking_views </td>
                <td> int </td>
                <td>success</td>
                <td> Number of masking views associated with the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > num_of_powerpath_hosts </td>
                <td> int </td>
                <td>success</td>
                <td> Number of PowerPath hosts associated with the host. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > port_flags_override </td>
                <td> bool </td>
                <td>success</td>
                <td> Whether any of the initiator port flags are overridden. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of initiator. </td>
            </tr>
                                        </table>

### Authors
* Vasudevu Lakhinana (@unknown) <ansible.team@dell.com>
* Manisha Agrawal (@agrawm3) <ansible.team@dell.com>

--------------------------------
# RDF Group Module

Gets the detail information about RDF Groups of a PowerMax/VMAX storage system

### Synopsis
 Gets details of an RDF Group from a specified PowerMax/VMAX storage system.
 Lists the volumes of an RDF Group from a specified PowerMax/VMAX storage system

### Parameters
                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > rdfgroup_number</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Identifier of an RDF Group of type string </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>91</li>  <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '91' and '92' versions are supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                            </table>


### Examples
```
- name: Get the details of rdf group and volumes
  dellemc_powermax_rdfgroup:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    rdfgroup_number: "{{rdfgroup_id}}"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=4>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                    <tr>
            <td colspan=4 > RDFGroupDetails </td>
            <td>  list </td>
            <td> When the RDF group exist. </td>
            <td> Details of the RDF group. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > RDFGroupVolumes </td>
                <td> list </td>
                <td>success</td>
                <td> List of various properties of RDF group volume(s). </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > largerRdfSide </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Larger RDF side among the devices. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > localRdfGroupNumber </td>
                    <td> int </td>
                    <td>success</td>
                    <td> RDF group number at primary device. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > localSymmetrixId </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Primary device ID. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > localVolumeName </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Volume name at primary device. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > localVolumeState </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Volume state at primary device </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > local_wwn_external </td>
                    <td> int </td>
                    <td>success</td>
                    <td> External WWN of volume at primary device. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > rdfMode </td>
                    <td> str </td>
                    <td>success</td>
                    <td> SRDF mode of pairing. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > rdfpairState </td>
                    <td> str </td>
                    <td>success</td>
                    <td> SRDF state of pairing. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > remoteRdfGroupNumber </td>
                    <td> int </td>
                    <td>success</td>
                    <td> RDF group number at remote device. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > remoteSymmetrixId </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Remote device ID. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > remoteVolumeName </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Volume name at remote device. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > remoteVolumeState </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Volume state at remote device. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > remote_wwn_external </td>
                    <td> int </td>
                    <td>success</td>
                    <td> External WWN of volume at remote device. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > volumeConfig </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Type of volume. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > async </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag sets to true when an SRDF pair is in async mode. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > biasConfigured </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for configured bias. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > biasEffective </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for effective bias. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > device_polarity </td>
                <td> str </td>
                <td>success</td>
                <td> Type of device polarity. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > hardware_compression </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for hardware compression. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > label </td>
                <td> str </td>
                <td>success</td>
                <td> RDF group label. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > link_limbo </td>
                <td> int </td>
                <td>success</td>
                <td> The amount of time that the array's operating environment waits after the SRDF link goes down before updating the link's status. The link limbo value can be set from 0 to 120 seconds. The default value is 10 seconds. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > localOnlinePorts </td>
                <td> list </td>
                <td>success</td>
                <td> List of local online ports. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > localPorts </td>
                <td> list </td>
                <td>success</td>
                <td> List of local ports. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > metro </td>
                <td> list </td>
                <td>success</td>
                <td> Flag for metro configuration. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > modes </td>
                <td> str </td>
                <td>success</td>
                <td> Mode of the SRDF link. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > numDevices </td>
                <td> int </td>
                <td>success</td>
                <td> Number of devices involved in the pairing. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > offline </td>
                <td> bool </td>
                <td>success</td>
                <td> Offline flag. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rdfa_properties </td>
                <td> list </td>
                <td>success</td>
                <td> Properties associated with the RDF group. </td>
            </tr>
                                         <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > average_cycle_time </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Average cycle time (seconds) configured for this session in seconds. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > consistency_exempt_volumes </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Flag that indicates if consistency is exempt. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > cycle_number </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of cycles in seconds. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > dse_active </td>
                    <td> bool </td>
                    <td>success</td>
                    <td> Flag for active Delta Set Extension. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > dse_autostart </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Indicates DSE autostart state. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > dse_threshold </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Flag for DSE threshold. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > duration_of_last_cycle </td>
                    <td> int </td>
                    <td>success</td>
                    <td> The cycle time (in secs) of the most recently completed cycle. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > duration_of_last_transmit_cycle </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Duration of last transmitted cycle in seconds. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > r1_to_r2_lag_time </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Time that R2 is behind R1 in seconds. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > session_priority </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Priority used to determine which RDFA sessions to drop if cache becomes full. Values range from 1 to 64, with 1 being the highest priority (last to be dropped). </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > session_uncommitted_tracks </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Number of uncommitted session tracks. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > transmit_idle_state </td>
                    <td> str </td>
                    <td>success</td>
                    <td> Indicates RDFA transmit idle state. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > transmit_idle_time </td>
                    <td> int </td>
                    <td>success</td>
                    <td> Time the transmit cycle has been idle. </td>
                </tr>
                                             <tr>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td class="elbow-placeholder">&nbsp;</td>
                    <td colspan=2 > transmit_queue_depth </td>
                    <td> int </td>
                    <td>success</td>
                    <td> The transmitted queue depth of disks. </td>
                </tr>
                                                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > rdfgNumber </td>
                <td> int </td>
                <td>success</td>
                <td> RDF group number on primary device. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > remoteOnlinePorts </td>
                <td> list </td>
                <td>success</td>
                <td> List of remote online ports. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > remotePorts </td>
                <td> list </td>
                <td>success</td>
                <td> List of remote ports. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > remoteRdfgNumber </td>
                <td> int </td>
                <td>success</td>
                <td> RDF group number at remote device. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > remoteSymmetrix </td>
                <td> int </td>
                <td>success</td>
                <td> Remote device ID. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > software_compression </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for software compression. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > totalDeviceCapacity </td>
                <td> int </td>
                <td>success</td>
                <td> Total capacity of RDF group in GB. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > type </td>
                <td> str </td>
                <td>success</td>
                <td> Type of RDF group. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > vasa_group </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for VASA group member. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > witness </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for witness. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > witnessConfigured </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for configured witness. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > witnessDegraded </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for degraded witness. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > witnessEffective </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for effective witness. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > witnessProtectedPhysical </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for physically protected witness. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=3 > witnessProtectedVirtual </td>
                <td> bool </td>
                <td>success</td>
                <td> Flag for virtually protected witness. </td>
            </tr>
                                        <tr>
            <td colspan=4 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    </table>

### Authors
* Arindam Datta (@dattaarindam) <ansible.team@dell.com>

--------------------------------
# Snapshot Policy Module

Manage snapshot policy on PowerMax/VMAX Storage System

### Synopsis
 Managing a snapshot policy on a PowerMax storage system includes getting details of any specific snapshot policy, creating a snapshot policy, modifying snapshot policy attributes, modifying snapshot policy state, associating or disassociating storage groups to or from snapshot policy and deleting a snapshot policy.

### Parameters
                                                                                                                                                                                                                                                                                                                                                                                                                        
<table>
    <tr>
        <th colspan=1>Parameter</th>
        <th width="20%">Type</th>
        <th>Required</th>
        <th>Default</th>
        <th>Choices</th>
        <th width="80%">Description</th>
    </tr>
                                                            <tr>
            <td colspan=1 > universion</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>92</li> </ul></td>
            <td> <br> Unisphere version, currently '92' version is supported. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_policy_name</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> Name of the snapshot policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > interval</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>10 Minutes</li>  <li>12 Minutes</li>  <li>15 Minutes</li>  <li>20 Minutes</li>  <li>30 Minutes</li>  <li>1 Hour</li>  <li>2 Hours</li>  <li>3 Hours</li>  <li>4 Hours</li>  <li>6 Hours</li>  <li>8 Hours</li>  <li>12 Hours</li>  <li>1 Day</li>  <li>7 Days</li> </ul></td>
            <td> <br> The value of the interval counter for snapshot policy execution. </td>
        </tr>
                    <tr>
            <td colspan=1 > secure</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Secure snapshots may only be terminated after they expire or by Dell EMC support.  <br> If not specified, default value is False. </td>
        </tr>
                    <tr>
            <td colspan=1 > snapshot_count</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> The max snapshot count of the policy.  <br> Max value is 1024. </td>
        </tr>
                    <tr>
            <td colspan=1 > offset_mins</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> Defines when, within the interval the snapshots will be taken for a specified snapshot policy.  <br> The offset must be less than the interval of the snapshot policy.  <br> The format must be in minutes.  <br> If not specified, default value is 0. </td>
        </tr>
                    <tr>
            <td colspan=1 > compliance_count_warning</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> If the number of valid snapshots falls below this number, the compliance changes to warning (yellow). </td>
        </tr>
                    <tr>
            <td colspan=1 > compliance_count_critical</td>
            <td> int  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> If the number of valid snapshots falls below this number, the compliance changes to critical (red). </td>
        </tr>
                    <tr>
            <td colspan=1 > storage_groups</td>
            <td> list   <br> elements: str </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> List of storage groups. </td>
        </tr>
                    <tr>
            <td colspan=1 > storage_group_state</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>present-in-policy</li>  <li>absent-in-policy</li> </ul></td>
            <td> <br> The state of the storage group with regard to the snapshot policy.  <br> present-in-policy indicates associate SG to SP.  <br> absent-in-policy indicates disassociate SG from SP. </td>
        </tr>
                    <tr>
            <td colspan=1 > suspend</td>
            <td> bool  </td>
            <td></td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Suspend the snapshot policy.  <br> True indicates snapshot policy is in suspend state.  <br> False indicates snapshot policy is in resume state. </td>
        </tr>
                    <tr>
            <td colspan=1 > new_snapshot_policy_name</td>
            <td> str  </td>
            <td></td>
            <td></td>
            <td></td>
            <td> <br> New name of the snapshot policy. </td>
        </tr>
                    <tr>
            <td colspan=1 > state</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>present</li>  <li>absent</li> </ul></td>
            <td> <br> Shows if the snapshot policy should be present or absent. </td>
        </tr>
                    <tr>
            <td colspan=1 > unispherehost</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> IP or FQDN of the Unisphere host </td>
        </tr>
                    <tr>
            <td colspan=1 > verifycert</td>
            <td> bool  </td>
            <td> True </td>
            <td></td>
            <td> <ul> <li>True</li>  <li>False</li> </ul></td>
            <td> <br> Boolean variable to specify whether to validate SSL certificate or not.  <br> True - indicates that the SSL certificate should be verified.  <br> False - indicates that the SSL certificate should not be verified. </td>
        </tr>
                    <tr>
            <td colspan=1 > user</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The username of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > password</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The password of the Unisphere host. </td>
        </tr>
                    <tr>
            <td colspan=1 > serial_no</td>
            <td> str  </td>
            <td> True </td>
            <td></td>
            <td></td>
            <td> <br> The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module. </td>
        </tr>
                                                    </table>

### Notes
* The max number of snapshot policies on an array is limited to 20.
* At most four snapshot policies can be associated with a storage group.
* compliance_count_critical <= compliance_count_warning < total snapshot_count for the policy.

### Examples
```
- name: Create a snapshot policy
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    interval: "10 Minutes"
    secure: false
    snapshot_count: 10
    offset_mins: 2
    compliance_count_warning: 6
    compliance_count_critical: 4
    state: "present"

- name: Create a snapshot policy and associate storage groups to it
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_2"
    interval: "10 Minutes"
    secure: false
    snapshot_count: 12
    offset_mins: 5
    compliance_count_warning: 8
    compliance_count_critical: 4
    storage_groups:
      - "11_ansible_test_1"
      - "11_ansible_test_2"
    storage_group_state: "present-in-policy"
    state: "present"

- name: Get snapshot policy details
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_2"
    state: "present"

- name: Modify snapshot policy attributes
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_2"
    new_snapshot_policy_name: "10min_policy_2_new"
    interval: "10 Minutes"
    snapshot_count: 16
    offset_mins: 8
    compliance_count_warning: 9
    compliance_count_critical: 7
    state: "present"

- name: Modify snapshot policy, associate to storage groups
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    storage_groups:
      - "11_ansible_test_1"
      - "11_ansible_test_2"
    storage_group_state: "present-in-policy"
    state: "present"

- name: Modify snapshot policy, disassociate from storage groups
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    storage_groups:
      - "11_ansible_test_1"
      - "11_ansible_test_2"
    storage_group_state: "absent-in-policy"
    state: "present"

- name: Modify snapshot policy state to suspend
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    suspend: true
    state: "present"

- name: Modify snapshot policy state to resume
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    suspend: false
    state: "present"

- name: Delete a snapshot policy
  dellemc_powermax_snapshotpolicy:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    snapshot_policy_name: "10min_policy_1"
    state: "absent"
```

### Return Values
                                                                                                                                                                                                                                                                                                                                                                                                            
<table>
    <tr>
        <th colspan=2>Key</th>
        <th>Type</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                                                                                            <tr>
            <td colspan=2 > changed </td>
            <td>  bool </td>
            <td> always </td>
            <td> Whether or not the resource has changed. </td>
        </tr>
                    <tr>
            <td colspan=2 > snapshot_policy_details </td>
            <td>  complex </td>
            <td> When snapshot policy exists. </td>
            <td> Details of the snapshot policy. </td>
        </tr>
                            <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > compliance_count_critical </td>
                <td> int </td>
                <td>success</td>
                <td> The number of valid snapshots that have critical compliance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > compliance_count_warning </td>
                <td> int </td>
                <td>success</td>
                <td> The number of valid snapshots that have warning compliance. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > interval_minutes </td>
                <td> int </td>
                <td>success</td>
                <td> The interval minutes for snapshot policy execution. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > last_time_used </td>
                <td> str </td>
                <td>success</td>
                <td> The timestamp indicating the last time snapshot policy was used. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > offset_minutes </td>
                <td> int </td>
                <td>success</td>
                <td> It is the time in minutes within the interval when the snapshots will be taken for a specified Snapshot Policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > secure </td>
                <td> bool </td>
                <td>success</td>
                <td> True value indicates that the secure snapshots may only be terminated after they expire or by Dell EMC support. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snapshot_count </td>
                <td> int </td>
                <td>success</td>
                <td> It is the max snapshot count of the policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > snapshot_policy_name </td>
                <td> str </td>
                <td>success</td>
                <td> Name of the snapshot policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storage_group </td>
                <td> list </td>
                <td>success</td>
                <td> The list of storage groups associated with the snapshot policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storage_group_count </td>
                <td> int </td>
                <td>success</td>
                <td> The number of storage groups associated with the snapshot policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > storage_group_snapshotID </td>
                <td> list </td>
                <td>success</td>
                <td> Pair of storage group and list of snapshot IDs associated with the snapshot policy. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > suspended </td>
                <td> bool </td>
                <td>success</td>
                <td> The state of the snapshot policy, true indicates policy is in suspend state. </td>
            </tr>
                                <tr>
                <td class="elbow-placeholder">&nbsp;</td>
                <td colspan=1 > symmetrixID </td>
                <td> str </td>
                <td>success</td>
                <td> The symmetrix on which snapshot policy exists. </td>
            </tr>
                                        </table>

### Authors
* Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

--------------------------------
