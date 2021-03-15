**Ansible Modules for Dell EMC PowerMax** 
=========================================
### Product Guide 1.4

>   © 2021 Dell Inc. or its subsidiaries. All rights reserved. Dell
>   EMC, and other trademarks are trademarks of Dell Inc. or its
>   subsidiaries. Other trademarks may be trademarks of their respective
>   owners.

Contents
--------
-   [Common Parameters](#common-parameters)
-   [Gatherfacts Module](#gatherfacts-module)
    -   [Synopsis](#synopsis)			 
    -   [Parameters](#parameters)
    -   [Examples](#examples)
    -   [Return Values](#return-values)
    -   [Authors](#authors)
-   [Host Module](#host-module)																										 
    -   [Synopsis](#synopsis-1)
    -   [Parameters](#parameters-1)
    -   [Notes](#notes)
    -   [Examples](#examples-1)
    -   [Return Values](#return-values-1)
    -   [Authors](#authors-1)						   
-   [Host Group Module](#host-group-module)
    -   [Synopsis](#synopsis-2)
    -   [Parameters](#parameters-2)
    -   [Notes](#notes-1)
    -   [Examples](#examples-2)
    -   [Return Values](#return-values-2)
    -   [Authors](#authors-2)
-   [Masking View Module](#masking-view-module)															   
    -   [Synopsis](#synopsis-3)	   
    -   [Parameters](#parameters-3)
    -   [Examples](#examples-3)
    -   [Return Values](#return-values-3)
    -   [Authors](#authors-3)
-   [Port Module](#port-module)																  
    -   [Synopsis](#synopsis-4)	   
    -   [Parameters](#parameters-4)
    -   [Examples](#examples-4)
    -   [Return Values](#return-values-4)
    -   [Authors](#authors-4)
-   [Port Group Module](#port-group-module)																 
    -   [Synopsis](#synopsis-5)
    -   [Parameters](#parameters-5)
    -   [Examples](#examples-5)
    -   [Return Values](#return-values-5)
    -   [Authors](#authors-5)
-   [RDF Group Module](#rdf-group-module)																								
    -   [Synopsis](#synopsis-6)
    -   [Parameters](#parameters-6)
    -   [Examples](#examples-6)
    -   [Return Values](#return-values-6)
    -   [Authors](#authors-6)
-   [Snapshot Module](#snapshot-module)
    -   [Synopsis](#synopsis-7)
    -   [Parameters](#parameters-7)
    -   [Examples](#examples-7)
    -   [Return Values](#return-values-7)
    -   [Authors](#authors-7)
-   [SRDF Module](#srdf-module)																  
    -   [Synopsis](#synopsis-8)	   
    -   [Parameters](#parameters-8)
    -   [Examples](#examples-8)
    -   [Return Values](#return-values-8)
    -   [Authors](#authors-8)
-   [Storage Group Module](#storage-group-module)																   
    -   [Synopsis](#synopsis-9)
    -   [Parameters](#parameters-9)
    -   [Examples](#examples-9)
    -   [Return Values](#return-values-9)
    -   [Authors](#authors-9)
-   [Volume Module](#volume-module)														  
    -   [Synopsis](#synopsis-10)
    -   [Parameters](#parameters-10)
    -   [Notes](#notes-2)
    -   [Examples](#examples-10)
    -   [Return Values](#return-values-10)
    -   [Authors](#authors-10)
-   [Metro DR Module](#metro-dr-module)
    -   [Synopsis](#synopsis-11)
    -   [Parameters](#parameters-11)
    -   [Examples](#examples-11)
    -   [Return Values](#return-values-11)
    -   [Authors](#authors-11)
-   [Job Module](#job-module)
    -   [Synopsis](#synopsis-12)
    -   [Parameters](#parameters-12)
    -   [Examples](#examples-12)
    -   [Return Values](#return-values-12)
    -   [Authors](#authors-12)

Common Parameters
=================
These parameters are applicable to all modules, along with module-specific parameters.

**NOTE:** If the parameter is mandatory, then required=true else it is an optional parameter. This is applicable to all the module specific parameters also.

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-password"></div>
                <b>password</b>
                <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The password of the Unisphere host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-serial_no"></div>
                <b>serial_no</b>
                <a class="ansibleOptionLink" href="#parameter-serial_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The serial number of the PowerMax/VMAX array. It is a required parameter for all array-specific operations except for getting a list of arrays in the Gatherfacts module.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-unispherehost"></div>
                <b>unispherehost</b>
                <a class="ansibleOptionLink" href="#parameter-unispherehost" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>IP or FQDN of the Unisphere host</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-universion"></div>
                <b>universion</b>
                <a class="ansibleOptionLink" href="#parameter-universion" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>                   </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>91</li>
                                                                                                                                                                                            <li>92</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Unisphere version, currently &#x27;91&#x27; and &#x27;92&#x27; versions are supported.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-user"></div>
                <b>user</b>
                <a class="ansibleOptionLink" href="#parameter-user" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The username of the Unisphere host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-verifycert"></div>
                <b>verifycert</b>
                <a class="ansibleOptionLink" href="#parameter-verifycert" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>,                    
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable to specify whether to validate SSL certificate or not.</div>
                                        <div>True - indicates that the SSL certificate should be verified.</div>
                                        <div>False - indicates that the SSL certificate should not be verified.</div>
                                                    </td>
        </tr>
                    </table>

Gatherfacts Module
==================

Synopsis
--------

Gathers the list of specified PowerMax/VMAX Storage System entities,
such as the list of registered arrays, storage groups, hosts, host
groups, storage groups, storage resource pools, port groups, masking
views, array health status, alerts and metro DR environments, etc.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-filters"></div>
                <b>filters</b>
                <a class="ansibleOptionLink" href="#parameter-filters" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                    <br>
                    <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>List of filters to support filtered output for storage entities.</div>
                                        <div>Each filter is a tuple of {filter_key, filter_operator, filter_value}.</div>
                                        <div>Supports passing of multiple filters.</div>
                                        <div>The storage entities, &#x27;rdf&#x27; and &#x27;metro_dr_env&#x27;, does not support filters. Filters will be ignored if passed.</div>
                                                    </td>
        </tr>
                                    <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filters/filter_key"></div>
                <b>filter_key</b>
                <a class="ansibleOptionLink" href="#parameter-filters/filter_key" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name identifier of the filter.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filters/filter_operator"></div>
                <b>filter_operator</b>
                <a class="ansibleOptionLink" href="#parameter-filters/filter_operator" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>equal</li>
                                                                                                                                                                                            <li>greater</li>
                                                                                                                                                                                            <li>lesser</li>
                                                                                                                                                                                            <li>like</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Operation to be performed on filter key.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-filters/filter_value"></div>
                <b>filter_value</b>
                <a class="ansibleOptionLink" href="#parameter-filters/filter_value" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Value of the filter key.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-gather_subset"></div>
                <b>gather_subset</b>
                <a class="ansibleOptionLink" href="#parameter-gather_subset" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                    <br>
                    <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>alert</li>
                                                                                                                                                                                            <li>health</li>
                                                                                                                                                                                            <li>vol</li>
                                                                                                                                                                                            <li>srp</li>
                                                                                                                                                                                            <li>sg</li>
                                                                                                                                                                                            <li>pg</li>
                                                                                                                                                                                            <li>host</li>
                                                                                                                                                                                            <li>hg</li>
                                                                                                                                                                                            <li>port</li>
                                                                                                                                                                                            <li>mv</li>
                                                                                                                                                                                            <li>rdf</li>
                                                                                                                                                                                            <li>metro_dr_env</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>List of string variables to specify the PowerMax/VMAX entities for which information is required.</div>
                                        <div>Required only if the serial_no is present</div>
                                        <div>List of all PowerMax/VMAX entities supported by the module</div>
                                        <div>alert - gets alert summary information</div>
                                        <div>health - health status of a specific PowerMax array</div>
                                        <div>vol - volumes</div>
                                        <div>srp - storage resource pools</div>
                                        <div>sg - storage groups</div>
                                        <div>pg - port groups</div>
                                        <div>host - hosts</div>
                                        <div>hg -  host groups</div>
                                        <div>port - ports</div>
                                        <div>mv - masking views</div>
                                        <div>rdf - rdf groups</div>
                                        <div>metro_dr_env - metro DR environments</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-serial_no"></div>
                <b>serial_no</b>
                <a class="ansibleOptionLink" href="#parameter-serial_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The serial number of the PowerMax/VMAX array. It is not required for getting the list of arrays.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-tdev_volumes"></div>
                <b>tdev_volumes</b>
                <a class="ansibleOptionLink" href="#parameter-tdev_volumes" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Boolean variable to filter the volume list. This will have a small performance impact. By default it is set to true, only TDEV volumes will be returned.</div>
                                        <div>True - Will return only the TDEV volumes.</div>
                                        <div>False - Will return all the volumes.</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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
```

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="4">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-Alerts"></div>
                <b>Alerts</b>
                <a class="ansibleOptionLink" href="#return-Alerts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the alert exists.</td>
            <td>
                                        <div>Alert summary of the array.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/acknowledged"></div>
                <b>acknowledged</b>
                <a class="ansibleOptionLink" href="#return-Alerts/acknowledged" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether or not this alert is acknowledged.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/alertId"></div>
                <b>alertId</b>
                <a class="ansibleOptionLink" href="#return-Alerts/alertId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique ID of alert.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/array"></div>
                <b>array</b>
                <a class="ansibleOptionLink" href="#return-Alerts/array" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Array serial no.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/created_date"></div>
                <b>created_date</b>
                <a class="ansibleOptionLink" href="#return-Alerts/created_date" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Creation Date.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/created_date_milliseconds"></div>
                <b>created_date_milliseconds</b>
                <a class="ansibleOptionLink" href="#return-Alerts/created_date_milliseconds" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Creation Date in milliseconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/description"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#return-Alerts/description" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Description about the alert</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/object"></div>
                <b>object</b>
                <a class="ansibleOptionLink" href="#return-Alerts/object" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Object description</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/object_type"></div>
                <b>object_type</b>
                <a class="ansibleOptionLink" href="#return-Alerts/object_type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Resource class</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/severity"></div>
                <b>severity</b>
                <a class="ansibleOptionLink" href="#return-Alerts/severity" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Severity of the alert</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#return-Alerts/state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>State of the alert</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Alerts/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-Alerts/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of the alert</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-Arrays"></div>
                <b>Arrays</b>
                <a class="ansibleOptionLink" href="#return-Arrays" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the Unisphere exist.</td>
            <td>
                                        <div>List of arrays in the Unisphere.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-Health"></div>
                <b>Health</b>
                <a class="ansibleOptionLink" href="#return-Health" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When the array exist.</td>
            <td>
                                        <div>Health status of the array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric"></div>
                <b>health_score_metric</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Overall health score for the specified Symmetrix.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric/cached_date"></div>
                <b>cached_date</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric/cached_date" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date Time stamp in epoch format when it was cached.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric/data_date"></div>
                <b>data_date</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric/data_date" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date Time stamp in epoch format when it was collected.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric/expired"></div>
                <b>expired</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric/expired" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag to indicate the expiry of the score.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric/health_score"></div>
                <b>health_score</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric/health_score" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Overall health score in numbers.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric/instance_metrics"></div>
                <b>instance_metrics</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric/instance_metrics" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Metrics about a specific instance.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric/instance_metrics/health_score_instance_metric"></div>
                <b>health_score_instance_metric</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric/instance_metrics/health_score_instance_metric" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Health score of a specific instance.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Health/health_score_metric/metric"></div>
                <b>metric</b>
                <a class="ansibleOptionLink" href="#return-Health/health_score_metric/metric" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Information about which sub system , such as SYSTEM_UTILIZATION, CONFIGURATION,CAPACITY, and so on.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Health/num_failed_disks"></div>
                <b>num_failed_disks</b>
                <a class="ansibleOptionLink" href="#return-Health/num_failed_disks" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Numbers of the disk failure in this system.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-HostGroups"></div>
                <b>HostGroups</b>
                <a class="ansibleOptionLink" href="#return-HostGroups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the hostgroups exist.</td>
            <td>
                                        <div>List of host groups present on the array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-Hosts"></div>
                <b>Hosts</b>
                <a class="ansibleOptionLink" href="#return-Hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the hosts exist.</td>
            <td>
                                        <div>List of hosts present on the array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-MaskingViews"></div>
                <b>MaskingViews</b>
                <a class="ansibleOptionLink" href="#return-MaskingViews" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the masking views exist.</td>
            <td>
                                        <div>List of masking views present on the array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-MetroDREnvironments"></div>
                <b>MetroDREnvironments</b>
                <a class="ansibleOptionLink" href="#return-MetroDREnvironments" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When environment exists.</td>
            <td>
                                        <div>List of metro DR environments on the array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-PortGroups"></div>
                <b>PortGroups</b>
                <a class="ansibleOptionLink" href="#return-PortGroups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the port groups exist.</td>
            <td>
                                        <div>List of port groups on the array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-Ports"></div>
                <b>Ports</b>
                <a class="ansibleOptionLink" href="#return-Ports" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When the ports exist.</td>
            <td>
                                        <div>List of ports on the array.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Ports/directorId"></div>
                <b>directorId</b>
                <a class="ansibleOptionLink" href="#return-Ports/directorId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Director ID of the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-Ports/portId"></div>
                <b>portId</b>
                <a class="ansibleOptionLink" href="#return-Ports/portId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Port number of the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-RDFGroups"></div>
                <b>RDFGroups</b>
                <a class="ansibleOptionLink" href="#return-RDFGroups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When the RDF groups exist.</td>
            <td>
                                        <div>List of RDF groups on the array.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-RDFGroups/label"></div>
                <b>label</b>
                <a class="ansibleOptionLink" href="#return-RDFGroups/label" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the RDF group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-RDFGroups/rdfgNumber"></div>
                <b>rdfgNumber</b>
                <a class="ansibleOptionLink" href="#return-RDFGroups/rdfgNumber" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier of the RDF group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-StorageGroups"></div>
                <b>StorageGroups</b>
                <a class="ansibleOptionLink" href="#return-StorageGroups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the storage groups exist.</td>
            <td>
                                        <div>List of storage groups on the array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools"></div>
                <b>StorageResourcePools</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When the storage pools exist.</td>
            <td>
                                        <div>List of storage pools on the array.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/diskGroupId"></div>
                <b>diskGroupId</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/diskGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>ID of the disk group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/emulation"></div>
                <b>emulation</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/emulation" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of volume emulation.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/num_of_disk_groups"></div>
                <b>num_of_disk_groups</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/num_of_disk_groups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of disk groups.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/rdfa_dse"></div>
                <b>rdfa_dse</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/rdfa_dse" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for RDFA Delta Set Extension.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/reserved_cap_percent"></div>
                <b>reserved_cap_percent</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/reserved_cap_percent" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Reserved capacity percentage.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity"></div>
                <b>srp_capacity</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dict</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Different entities to measure SRP capacity.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity/effective_used_capacity_percent"></div>
                <b>effective_used_capacity_percent</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity/effective_used_capacity_percent" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Percentage of effectively used capacity.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity/snapshot_modified_tb"></div>
                <b>snapshot_modified_tb</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity/snapshot_modified_tb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Snapshot modified in TB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity/snapshot_total_tb"></div>
                <b>snapshot_total_tb</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity/snapshot_total_tb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Total snapshot size in TB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity/subscribed_allocated_tb"></div>
                <b>subscribed_allocated_tb</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity/subscribed_allocated_tb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Subscribed allocated size in TB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity/subscribed_total_tb"></div>
                <b>subscribed_total_tb</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity/subscribed_total_tb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Subscribed total size in TB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity/usable_total_tb"></div>
                <b>usable_total_tb</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity/usable_total_tb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Usable total size in TB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_capacity/usable_used_tb"></div>
                <b>usable_used_tb</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_capacity/usable_used_tb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Usable used size in TB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_efficiency"></div>
                <b>srp_efficiency</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_efficiency" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dict</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Different entities to measure SRP efficiency.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_efficiency/compression_state"></div>
                <b>compression_state</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_efficiency/compression_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Depicts the compression state of the SRP.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_efficiency/data_reduction_enabled_percent"></div>
                <b>data_reduction_enabled_percent</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_efficiency/data_reduction_enabled_percent" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Percentage of data reduction enabled in the SRP.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_efficiency/data_reduction_ratio_to_one"></div>
                <b>data_reduction_ratio_to_one</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_efficiency/data_reduction_ratio_to_one" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Data reduction ratio of SRP.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_efficiency/overall_efficiency_ratio_to_one"></div>
                <b>overall_efficiency_ratio_to_one</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_efficiency/overall_efficiency_ratio_to_one" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Overall effectively ratio of SRP.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_efficiency/snapshot_savings_ratio_to_one"></div>
                <b>snapshot_savings_ratio_to_one</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_efficiency/snapshot_savings_ratio_to_one" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Snapshot savings ratio of SRP.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srp_efficiency/virtual_provisioning_savings_ratio_to_one"></div>
                <b>virtual_provisioning_savings_ratio_to_one</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srp_efficiency/virtual_provisioning_savings_ratio_to_one" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Virtual provisioning savings ratio of SRP.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/srpId"></div>
                <b>srpId</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/srpId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique Identifier for SRP.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-StorageResourcePools/total_srdf_dse_allocated_cap_gb"></div>
                <b>total_srdf_dse_allocated_cap_gb</b>
                <a class="ansibleOptionLink" href="#return-StorageResourcePools/total_srdf_dse_allocated_cap_gb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Total srdf dse allocated capacity in GB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-Volumes"></div>
                <b>Volumes</b>
                <a class="ansibleOptionLink" href="#return-Volumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the volumes exist.</td>
            <td>
                                        <div>List of volumes on the array.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Arindam Datta (@dattaarindam) &lt;<ansible.team@dell.com>&gt;
-   Rajshree Khare (@kharer5) &lt;<ansible.team@dell.com>&gt;

Host Module
===========

Synopsis
--------

Managing hosts on a PowerMax storage system includes creating a host
with a set of initiators and host flags, adding and removing
initiators to or from a host, modifying host flag values, renaming a
host, and deleting a host.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
                <b>host_flags</b>
                <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=dictionary</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Input as a yaml dictionary</div>
                                        <div>List of all host_flags-</div>
                                        <div>1. volume_set_addressing</div>
                                        <div>2. disable_q_reset_on_ua</div>
                                        <div>3. environ_set</div>
                                        <div>4. avoid_reset_broadcast</div>
                                        <div>5. openvms</div>
                                        <div>6. scsi_3</div>
                                        <div>7. spc2_protocol_version</div>
                                        <div>8. scsi_support1</div>
                                        <div>9. consistent_lun</div>
                                        <div>Possible values are true, false, unset(default state)</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the host. No Special Character support except for _. Case sensitive for REST Calls.</div>
                                        <div>Creation of an empty host is allowed</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_type"></div>
                <b>host_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>default</li>
                                                                                                                                                                                            <li>hpux</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Describing the OS type (default or hpux)</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-initiator_state"></div>
                <b>initiator_state</b>
                <a class="ansibleOptionLink" href="#parameter-initiator_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-host</li>
                                                                                                                                                                                            <li>absent-in-host</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the initiators should be present or absent on the host.</div>
                                        <div>present-in-host - indicates that the initiators should exist on the host</div>
                                        <div>absent-in-host - indicates that the initiators should not exist on the host</div>
                                        <div>Required when creating a host with initiators or adding and removing initiators to or from an existing host</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-initiators"></div>
                <b>initiators</b>
                <a class="ansibleOptionLink" href="#parameter-initiators" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                    <br>
                    <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>List of Initiator WWN or IQN to be added to the host or removed from the host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_name"></div>
                <b>new_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new name of the host for the renaming function. No Special Character support except for _. Case sensitive for REST Calls</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the host should exist or not.</div>
                                        <div>present - indicates that the host should exist in the system</div>
                                        <div>absent - indicates that the host should not exist in the system</div>
                                                    </td>
        </tr>
                    </table>

Notes
-----

- host\_flags and host\_type are mutually exclusive parameters.

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-host_details"></div>
                <b>host_details</b>
                <a class="ansibleOptionLink" href="#return-host_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When host exist.</td>
            <td>
                                        <div>Details of the host.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/consistent_lun"></div>
                <b>consistent_lun</b>
                <a class="ansibleOptionLink" href="#return-host_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for consistent LUN in host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/disabled_flags"></div>
                <b>disabled_flags</b>
                <a class="ansibleOptionLink" href="#return-host_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of any disabled port flags overridden by the initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/enabled_flags"></div>
                <b>enabled_flags</b>
                <a class="ansibleOptionLink" href="#return-host_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of any enabled port flags overridden by the initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/hostgroup"></div>
                <b>hostgroup</b>
                <a class="ansibleOptionLink" href="#return-host_details/hostgroup" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of host groups that the host is associated with.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/hostId"></div>
                <b>hostId</b>
                <a class="ansibleOptionLink" href="#return-host_details/hostId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Host ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/initiator"></div>
                <b>initiator</b>
                <a class="ansibleOptionLink" href="#return-host_details/initiator" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of initiators present in the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/maskingview"></div>
                <b>maskingview</b>
                <a class="ansibleOptionLink" href="#return-host_details/maskingview" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of masking view in which the host group is present.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/num_of_hostgroups"></div>
                <b>num_of_hostgroups</b>
                <a class="ansibleOptionLink" href="#return-host_details/num_of_hostgroups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of host groups associated with the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/num_of_initiators"></div>
                <b>num_of_initiators</b>
                <a class="ansibleOptionLink" href="#return-host_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of initiators present in the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/num_of_masking_views"></div>
                <b>num_of_masking_views</b>
                <a class="ansibleOptionLink" href="#return-host_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of masking views associated with the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/num_of_powerpath_hosts"></div>
                <b>num_of_powerpath_hosts</b>
                <a class="ansibleOptionLink" href="#return-host_details/num_of_powerpath_hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of PowerPath hosts associated with the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/port_flags_override"></div>
                <b>port_flags_override</b>
                <a class="ansibleOptionLink" href="#return-host_details/port_flags_override" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether any of the initiator port flags are overridden.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-host_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-host_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of initiator.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Vasudevu Lakhinana (@unknown) &lt;<ansible.team@dell.com>&gt;
-   Manisha Agrawal (@agrawm3) &lt;<ansible.team@dell.com>&gt;

Host Group Module
=================

Synopsis
--------

Managing a host group on a PowerMax storage system includes creating
a host group with a set of hosts, adding or removing hosts to or
from a host group, renaming a host group, modifying host flags of a
host group, and deleting a host group.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_flags"></div>
                <b>host_flags</b>
                <a class="ansibleOptionLink" href="#parameter-host_flags" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=dictionary</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>input as an yaml dictionary</div>
                                        <div>List of all host_flags -</div>
                                        <div>1. volume_set_addressing</div>
                                        <div>2. disable_q_reset_on_ua</div>
                                        <div>3. environ_set</div>
                                        <div>4. avoid_reset_broadcast</div>
                                        <div>5. openvms</div>
                                        <div>6. scsi_3</div>
                                        <div>7. spc2_protocol_version</div>
                                        <div>8. scsi_support1</div>
                                        <div>9. consistent_lun</div>
                                        <div>Possible values are true, false, unset(default state)</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_state"></div>
                <b>host_state</b>
                <a class="ansibleOptionLink" href="#parameter-host_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-group</li>
                                                                                                                                                                                            <li>absent-in-group</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the host should be present or absent in the host group.</div>
                                        <div>present-in-group - indicates that the hosts should exist in the host group</div>
                                        <div>absent-in-group - indicates that the hosts should not exist in the host group</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_type"></div>
                <b>host_type</b>
                <a class="ansibleOptionLink" href="#parameter-host_type" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>default</li>
                                                                                                                                                                                            <li>hpux</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Describing the OS type (default or hpux)</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-hostgroup_name"></div>
                <b>hostgroup_name</b>
                <a class="ansibleOptionLink" href="#parameter-hostgroup_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the host group. No Special Character support except for _. Case sensitive for REST Calls.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-hosts"></div>
                <b>hosts</b>
                <a class="ansibleOptionLink" href="#parameter-hosts" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                    <br>
                    <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>List of host names to be added to the host group or removed from the host group.</div>
                                        <div>Creation of an empty host group is allowed.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_name"></div>
                <b>new_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new name for the host group for the renaming function. No Special Character support except for _. Case sensitive for REST Calls</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the host group should be present or absent on the system.</div>
                                        <div>present - indicates that the host group should be present on the system</div>
                                        <div>absent - indicates that the host group should be absent on the system</div>
                                                    </td>
        </tr>
                    </table>

Notes
-----

- In the gather facts module, empty host groups will be listed as
hosts.
- host\_flags and host\_type are mutually exclusive parameters.
- Hostgroups with 'default' host\_type will have 'default' hosts.
- Hostgroups with 'hpux' host\_type will have 'hpux' hosts.

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details"></div>
                <b>hostgroup_details</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When host group exist.</td>
            <td>
                                        <div>Details of the host group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/consistent_lun"></div>
                <b>consistent_lun</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/consistent_lun" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for consistent LUN in the host group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/disabled_flags"></div>
                <b>disabled_flags</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/disabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of any disabled port flags overridden by the initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/enabled_flags"></div>
                <b>enabled_flags</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/enabled_flags" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of any enabled port flags overridden by the initiator.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host"></div>
                <b>host</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of hosts present in the host group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host/hostId"></div>
                <b>hostId</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host/hostId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier for the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/host/initiator"></div>
                <b>initiator</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/host/initiator" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of initiators present in the host.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/hostGroupId"></div>
                <b>hostGroupId</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/hostGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Host group ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/maskingview"></div>
                <b>maskingview</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/maskingview" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Masking view in which host group is present.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_hosts"></div>
                <b>num_of_hosts</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_hosts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of hosts in the host group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_initiators"></div>
                <b>num_of_initiators</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_initiators" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of initiators in the host group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/num_of_masking_views"></div>
                <b>num_of_masking_views</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of masking views associated with the host group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/port_flags_override"></div>
                <b>port_flags_override</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/port_flags_override" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Whether any of the initiator&#x27;s port flags are overridden.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-hostgroup_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-hostgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of initiator.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Vasudevu Lakhinana (@unknown) &lt;<ansible.team@dell.com>&gt;
-   Manisha Agrawal (@agrawm3) &lt;<ansible.team@dell.com>&gt;

Masking View Module
===================

Synopsis
--------

-   Managing masking views on PowerMax storage system includes, creating
    masking view with port group, storage group and host or host group,
    renaming masking view and deleting masking view.
-   For creating a masking view -
    - portgroup\_name
    - sg\_name and
    - any one of host\_name or hostgroup\_name is required.
-   All three entities must be present on the array.
-   For renaming a masking view, the 'new\_mv\_name' is required. After
    a masking view is created, only its name can be changed. No
    underlying entity (portgroup, storagegroup, host or hostgroup) can
    be changed on the masking view.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
                <b>host_name</b>
                <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the existing host. This parameter is to create an exclusive or host export</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-hostgroup_name"></div>
                <b>hostgroup_name</b>
                <a class="ansibleOptionLink" href="#parameter-hostgroup_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the existing host group. This parameter is used to create cluster export</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-mv_name"></div>
                <b>mv_name</b>
                <a class="ansibleOptionLink" href="#parameter-mv_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the masking view. No Special Character support except for _. Case sensitive for REST Calls.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_mv_name"></div>
                <b>new_mv_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_mv_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new name for the renaming function. No Special Character support except for _. Case sensitive for REST Calls.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-portgroup_name"></div>
                <b>portgroup_name</b>
                <a class="ansibleOptionLink" href="#parameter-portgroup_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the existing port group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sg_name"></div>
                <b>sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the existing storage group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Defines whether the masking view should exist or not.</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-create_mv"></div>
                <b>create_mv</b>
                <a class="ansibleOptionLink" href="#return-create_mv" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When masking view is created.</td>
            <td>
                                        <div>Flag sets to true when a new masking view is created.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-delete_mv"></div>
                <b>delete_mv</b>
                <a class="ansibleOptionLink" href="#return-delete_mv" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When masking view is deleted.</td>
            <td>
                                        <div>Flag sets to true when a masking view is deleted.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-modify_mv"></div>
                <b>modify_mv</b>
                <a class="ansibleOptionLink" href="#return-modify_mv" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When masking view is modified.</td>
            <td>
                                        <div>Flag sets to true when a masking view is modified.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-mv_details"></div>
                <b>mv_details</b>
                <a class="ansibleOptionLink" href="#return-mv_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When masking view exist.</td>
            <td>
                                        <div>Details of masking view.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-mv_details/hostId"></div>
                <b>hostId</b>
                <a class="ansibleOptionLink" href="#return-mv_details/hostId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Host group present in the masking view.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-mv_details/maskingViewId"></div>
                <b>maskingViewId</b>
                <a class="ansibleOptionLink" href="#return-mv_details/maskingViewId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Masking view ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-mv_details/portGroupId"></div>
                <b>portGroupId</b>
                <a class="ansibleOptionLink" href="#return-mv_details/portGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Port group present in the masking view.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-mv_details/storageGroupId"></div>
                <b>storageGroupId</b>
                <a class="ansibleOptionLink" href="#return-mv_details/storageGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Storage group present in the masking view.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Vasudevu Lakhinana (@unknown) &lt;<ansible.team@dell.com>&gt;
-   Prashant Rakheja (@prashant-dell) &lt;<ansible.team@dell.com>&gt;

Port Module
===========

Synopsis
--------

Managing ports on PowerMax storage system includes getting details
of a port.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-ports"></div>
                <b>ports</b>
                <a class="ansibleOptionLink" href="#parameter-ports" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>,
                    <br>
                    <span style="color: purple">elements=dictionary</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>List of port director and port id</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="4">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="4">
                <div class="ansibleOptionAnchor" id="return-port_details"></div>
                <b>port_details</b>
                <a class="ansibleOptionLink" href="#return-port_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the port exist.</td>
            <td>
                                        <div>Details of the port.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort"></div>
                <b>symmetrixPort</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of volume.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/aclx"></div>
                <b>aclx</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/aclx" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether access control logic is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/avoid_reset_broadcast"></div>
                <b>avoid_reset_broadcast</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/avoid_reset_broadcast" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Avoid Reset Broadcasting feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/common_serial_number"></div>
                <b>common_serial_number</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/common_serial_number" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Common Serial Number feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/director_status"></div>
                <b>director_status</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/director_status" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Director status.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/disable_q_reset_on_ua"></div>
                <b>disable_q_reset_on_ua</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/disable_q_reset_on_ua" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Disable Q Reset on UA (Unit Attention) is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/enable_auto_negotiate"></div>
                <b>enable_auto_negotiate</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/enable_auto_negotiate" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Enable Auto Negotiate feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/environ_set"></div>
                <b>environ_set</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/environ_set" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the environmental error reporting feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/hp_3000_mode"></div>
                <b>hp_3000_mode</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/hp_3000_mode" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether HP 3000 Mode is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/identifier"></div>
                <b>identifier</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/identifier" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier for port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/init_point_to_point"></div>
                <b>init_point_to_point</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/init_point_to_point" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether Init Point to Point is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/iscsi_target"></div>
                <b>iscsi_target</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/iscsi_target" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether ISCSI target is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/maskingview"></div>
                <b>maskingview</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/maskingview" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of Masking views that the port is a part of.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/max_speed"></div>
                <b>max_speed</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/max_speed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Maximum port speed in GB/Second.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/negotiate_reset"></div>
                <b>negotiate_reset</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/negotiate_reset" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Negotiate Reset feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/negotiated_speed"></div>
                <b>negotiated_speed</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/negotiated_speed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Negotiated speed in GB/Second.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/no_participating"></div>
                <b>no_participating</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/no_participating" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the No Participate feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/num_of_cores"></div>
                <b>num_of_cores</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/num_of_cores" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of cores for the director.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/num_of_mapped_vols"></div>
                <b>num_of_mapped_vols</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/num_of_mapped_vols" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of volumes mapped with the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/num_of_masking_views"></div>
                <b>num_of_masking_views</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of masking views associated with the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/num_of_port_groups"></div>
                <b>num_of_port_groups</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/num_of_port_groups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of port groups associated with the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/port_status"></div>
                <b>port_status</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/port_status" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Port status, ON/OFF.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/portgroup"></div>
                <b>portgroup</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/portgroup" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of masking views associated with the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/scsi_3"></div>
                <b>scsi_3</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/scsi_3" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the SCSI-3 protocol is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/scsi_support1"></div>
                <b>scsi_support1</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/scsi_support1" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the SCSI Support1 is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/siemens"></div>
                <b>siemens</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/siemens" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Siemens feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/soft_reset"></div>
                <b>soft_reset</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/soft_reset" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Soft Reset feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/spc2_protocol_version"></div>
                <b>spc2_protocol_version</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/spc2_protocol_version" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the SPC2 Protocol Version feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/sunapee"></div>
                <b>sunapee</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/sunapee" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Sunapee feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/symmetrixPortKey"></div>
                <b>symmetrixPortKey</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/symmetrixPortKey" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Symmetrix system director and port in the port group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/symmetrixPortKey/drectorId"></div>
                <b>drectorId</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/symmetrixPortKey/drectorId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Director ID of the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/symmetrixPortKey/portId"></div>
                <b>portId</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/symmetrixPortKey/portId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Port number of the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/unique_wwn"></div>
                <b>unique_wwn</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/unique_wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the Unique WWN feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/vnx_attached"></div>
                <b>vnx_attached</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/vnx_attached" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the VNX attached feature is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/volume_set_addressing"></div>
                <b>volume_set_addressing</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/volume_set_addressing" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether Volume Vet Addressing is enabled or disabled.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-port_details/symmetrixPort/wwn_node"></div>
                <b>wwn_node</b>
                <a class="ansibleOptionLink" href="#return-port_details/symmetrixPort/wwn_node" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>WWN node of port.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Ashish Verma (@vermaa31) &lt;<ansible.team@dell.com>&gt;

Port Group Module
=================

Synopsis
--------

Managing port groups on a PowerMax storage system includes creating a
port group with a set of ports, adding or removing single or
multiple ports to or from the port group, renaming the port group and
deleting the port group.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_name"></div>
                <b>new_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>New name of the port group while renaming. No Special Character support except for _. Case sensitive for REST Calls.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-port_state"></div>
                <b>port_state</b>
                <a class="ansibleOptionLink" href="#parameter-port_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-group</li>
                                                                                                                                                                                            <li>absent-in-group</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the port should be present or absent in the port group.</div>
                                        <div>present-in-group - indicates that the ports should be present on a port group object</div>
                                        <div>absent-in-group - indicates that the ports should not be present on a port group object</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-portgroup_name"></div>
                <b>portgroup_name</b>
                <a class="ansibleOptionLink" href="#parameter-portgroup_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the port group. No Special Character support except for _. Case sensitive for REST Calls.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-ports"></div>
                <b>ports</b>
                <a class="ansibleOptionLink" href="#parameter-ports" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                    <br>
                    <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>List of directors and ports to be added or removed to or from the port group</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the port group should exist or not.</div>
                                        <div>present - indicates that the port group should be present on the system</div>
                                        <div>absent - indicates that the port group should not be present on the system</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-portgroup_details"></div>
                <b>portgroup_details</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the port group exist.</td>
            <td>
                                        <div>Details of the port group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-portgroup_details/num_of_masking_views"></div>
                <b>num_of_masking_views</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of masking views in where port group is associated.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-portgroup_details/num_of_ports"></div>
                <b>num_of_ports</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details/num_of_ports" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of ports in the port group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-portgroup_details/portGroupId"></div>
                <b>portGroupId</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details/portGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Port group ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-portgroup_details/symmetrixPortKey"></div>
                <b>symmetrixPortKey</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details/symmetrixPortKey" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Symmetrix system director and port in the port group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-portgroup_details/symmetrixPortKey/directorId"></div>
                <b>directorId</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details/symmetrixPortKey/directorId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Director ID of the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-portgroup_details/symmetrixPortKey/portId"></div>
                <b>portId</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details/symmetrixPortKey/portId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Port number of the port.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-portgroup_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-portgroup_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of ports in port group.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Vasudevu Lakhinana (@unknown) &lt;<ansible.team@dell.com>&gt;
-   Ashish Verma (@vermaa31) &lt;<ansible.team@dell.com>&gt;
-   Rajshree Khare (@khareRajshree) &lt;<ansible.team@dell.com>&gt;

RDF Group Module
================

Synopsis
--------

-   Gets details of an RDF Group from a specified PowerMax/VMAX storage
    system.
-   Lists the volumes of an RDF Group from a specified PowerMax/VMAX
    storage system

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-rdfgroup_number"></div>
                <b>rdfgroup_number</b>
                <a class="ansibleOptionLink" href="#parameter-rdfgroup_number" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Identifier of an RDF Group of type string</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails"></div>
                <b>RDFGroupDetails</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When the RDF group exist.</td>
            <td>
                                        <div>Details of the RDF group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/async"></div>
                <b>async</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/async" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag sets to true when an SRDF pair is in async mode.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/biasConfigured"></div>
                <b>biasConfigured</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/biasConfigured" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for configured bias.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/biasEffective"></div>
                <b>biasEffective</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/biasEffective" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for effective bias.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/device_polarity"></div>
                <b>device_polarity</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/device_polarity" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of device polarity.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/hardware_compression"></div>
                <b>hardware_compression</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/hardware_compression" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for hardware compression.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/label"></div>
                <b>label</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/label" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDF group label.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/link_limbo"></div>
                <b>link_limbo</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/link_limbo" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The amount of time that the array&#x27;s operating environment waits after the SRDF link goes down before updating the link&#x27;s status. The link limbo value can be set from 0 to 120 seconds. The default value is 10 seconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/localOnlinePorts"></div>
                <b>localOnlinePorts</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/localOnlinePorts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of local online ports.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/localPorts"></div>
                <b>localPorts</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/localPorts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of local ports.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/metro"></div>
                <b>metro</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/metro" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for metro configuration.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/modes"></div>
                <b>modes</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/modes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Mode of the SRDF link.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/numDevices"></div>
                <b>numDevices</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/numDevices" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of devices involved in the pairing.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/offline"></div>
                <b>offline</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/offline" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Offline flag.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties"></div>
                <b>rdfa_properties</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Properties associated with the RDF group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/average_cycle_time"></div>
                <b>average_cycle_time</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/average_cycle_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Average cycle time (seconds) configured for this session in seconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/consistency_exempt_volumes"></div>
                <b>consistency_exempt_volumes</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/consistency_exempt_volumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag that indicates if consistency is exempt.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/cycle_number"></div>
                <b>cycle_number</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/cycle_number" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of cycles in seconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/dse_active"></div>
                <b>dse_active</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/dse_active" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for active Delta Set Extension.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/dse_autostart"></div>
                <b>dse_autostart</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/dse_autostart" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates DSE autostart state.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/dse_threshold"></div>
                <b>dse_threshold</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/dse_threshold" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for DSE threshold.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/duration_of_last_cycle"></div>
                <b>duration_of_last_cycle</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/duration_of_last_cycle" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The cycle time (in secs) of the most recently completed cycle.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/duration_of_last_transmit_cycle"></div>
                <b>duration_of_last_transmit_cycle</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/duration_of_last_transmit_cycle" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Duration of last transmitted cycle in seconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/r1_to_r2_lag_time"></div>
                <b>r1_to_r2_lag_time</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/r1_to_r2_lag_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Time that R2 is behind R1 in seconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/session_priority"></div>
                <b>session_priority</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/session_priority" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Priority used to determine which RDFA sessions to drop if cache becomes full. Values range from 1 to 64, with 1 being the highest priority (last to be dropped).</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/session_uncommitted_tracks"></div>
                <b>session_uncommitted_tracks</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/session_uncommitted_tracks" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of uncommitted session tracks.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/transmit_idle_state"></div>
                <b>transmit_idle_state</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/transmit_idle_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates RDFA transmit idle state.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/transmit_idle_time"></div>
                <b>transmit_idle_time</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/transmit_idle_time" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Time the transmit cycle has been idle.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfa_properties/transmit_queue_depth"></div>
                <b>transmit_queue_depth</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfa_properties/transmit_queue_depth" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The transmitted queue depth of disks.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/rdfgNumber"></div>
                <b>rdfgNumber</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/rdfgNumber" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDF group number on primary device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes"></div>
                <b>RDFGroupVolumes</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of various properties of RDF group volume(s).</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/largerRdfSide"></div>
                <b>largerRdfSide</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/largerRdfSide" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Larger RDF side among the devices.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/local_wwn_external"></div>
                <b>local_wwn_external</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/local_wwn_external" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>External WWN of volume at primary device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/localRdfGroupNumber"></div>
                <b>localRdfGroupNumber</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/localRdfGroupNumber" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDF group number at primary device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/localSymmetrixId"></div>
                <b>localSymmetrixId</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/localSymmetrixId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Primary device ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/localVolumeName"></div>
                <b>localVolumeName</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/localVolumeName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume name at primary device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/localVolumeState"></div>
                <b>localVolumeState</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/localVolumeState" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume state at primary device</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/rdfMode"></div>
                <b>rdfMode</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/rdfMode" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>SRDF mode of pairing.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/rdfpairState"></div>
                <b>rdfpairState</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/rdfpairState" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>SRDF state of pairing.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/remote_wwn_external"></div>
                <b>remote_wwn_external</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/remote_wwn_external" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>External WWN of volume at remote device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/remoteRdfGroupNumber"></div>
                <b>remoteRdfGroupNumber</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/remoteRdfGroupNumber" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDF group number at remote device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/remoteSymmetrixId"></div>
                <b>remoteSymmetrixId</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/remoteSymmetrixId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Remote device ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/remoteVolumeName"></div>
                <b>remoteVolumeName</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/remoteVolumeName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume name at remote device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/remoteVolumeState"></div>
                <b>remoteVolumeState</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/remoteVolumeState" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume state at remote device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/RDFGroupVolumes/volumeConfig"></div>
                <b>volumeConfig</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/RDFGroupVolumes/volumeConfig" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/remoteOnlinePorts"></div>
                <b>remoteOnlinePorts</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/remoteOnlinePorts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of remote online ports.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/remotePorts"></div>
                <b>remotePorts</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/remotePorts" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of remote ports.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/remoteRdfgNumber"></div>
                <b>remoteRdfgNumber</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/remoteRdfgNumber" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDF group number at remote device.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/remoteSymmetrix"></div>
                <b>remoteSymmetrix</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/remoteSymmetrix" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Remote device ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/software_compression"></div>
                <b>software_compression</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/software_compression" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for software compression.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/totalDeviceCapacity"></div>
                <b>totalDeviceCapacity</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/totalDeviceCapacity" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Total capacity of RDF group in GB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of RDF group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/vasa_group"></div>
                <b>vasa_group</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/vasa_group" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for VASA group member.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/witness"></div>
                <b>witness</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/witness" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for witness.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/witnessConfigured"></div>
                <b>witnessConfigured</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/witnessConfigured" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for configured witness.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/witnessDegraded"></div>
                <b>witnessDegraded</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/witnessDegraded" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for degraded witness.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/witnessEffective"></div>
                <b>witnessEffective</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/witnessEffective" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for effective witness.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/witnessProtectedPhysical"></div>
                <b>witnessProtectedPhysical</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/witnessProtectedPhysical" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for physically protected witness.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-RDFGroupDetails/witnessProtectedVirtual"></div>
                <b>witnessProtectedVirtual</b>
                <a class="ansibleOptionLink" href="#return-RDFGroupDetails/witnessProtectedVirtual" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for virtually protected witness.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Arindam Datta (@dattaarindam) &lt;<ansible.team@dell.com>&gt;

Snapshot Module
===============

Synopsis
--------

Managing snapshots on a PowerMax storage system includes creating a
new storage group (SG) snapshot, getting details of the SG snapshot,
renaming the SG snapshot, changing the snapshot link status, and
deleting an existing storage group snapshot.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-generation"></div>
                <b>generation</b>
                <a class="ansibleOptionLink" href="#parameter-generation" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The generation number of the Snapshot.</div>
                                        <div>Generation is mandatory for link, unlink, rename and delete operations.</div>
                                        <div>Optional for Get snapshot details.</div>
                                        <div>Create snapshot will always create a new snapshot with generation number 0.</div>
                                        <div>Rename is supported only for generation number 0.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-link_status"></div>
                <b>link_status</b>
                <a class="ansibleOptionLink" href="#parameter-link_status" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>linked</li>
                                                                                                                                                                                            <li>unlinked</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Describes the link status of the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_snapshot_name"></div>
                <b>new_snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new name of the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sg_name"></div>
                <b>sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the storage group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
                <b>snapshot_name</b>
                <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the snapshot.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: purple">required=true</span>                    </div>
                                </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the snapshot should exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-target_sg_name"></div>
                <b>target_sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-target_sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The target storage group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-ttl"></div>
                <b>ttl</b>
                <a class="ansibleOptionLink" href="#parameter-ttl" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The Time To Live (TTL) value for the snapshot.</div>
                                        <div>If the ttl is not specified, the storage group snap details would be returned.</div>
                                        <div>However, to create a SG snap - TTL must be given.</div>
                                        <div>If the SG snap should not have any TTL - specify TTL as &quot;None&quot;</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-ttl_unit"></div>
                <b>ttl_unit</b>
                <a class="ansibleOptionLink" href="#parameter-ttl_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>hours</li>
                                                                                                                                                                                            <li><div style="color: blue"><b>days</b>&nbsp;&larr;</div></li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The unit for the ttl.</div>
                                        <div>If no ttl_unit is specified, &#x27;days&#x27; is taken as default ttl_unit.</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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

- name: Delete Storage Group Snapshot
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

- name: Rename Storage Group Snapshot
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

- name: Change Snapshot Link Status to Linked
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

- name: Change Snapshot Link Status to UnLinked
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
```

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="3">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-create_sg_snap"></div>
                <b>create_sg_snap</b>
                <a class="ansibleOptionLink" href="#return-create_sg_snap" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When snapshot is created.</td>
            <td>
                                        <div>Flag sets to true when the snapshot is created.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-delete_sg_snap"></div>
                <b>delete_sg_snap</b>
                <a class="ansibleOptionLink" href="#return-delete_sg_snap" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When snapshot is deleted.</td>
            <td>
                                        <div>Flag sets to true when the snapshot is deleted.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-rename_sg_snap"></div>
                <b>rename_sg_snap</b>
                <a class="ansibleOptionLink" href="#return-rename_sg_snap" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When snapshot is renamed.</td>
            <td>
                                        <div>Flag sets to true when the snapshot is renamed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="3">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details"></div>
                <b>sg_snap_details</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When snapshot exists.</td>
            <td>
                                        <div>Details of the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/generation"></div>
                <b>generation</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/generation" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The generation number of the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/isExpired"></div>
                <b>isExpired</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/isExpired" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the snapshot is expired or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/isLinked"></div>
                <b>isLinked</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/isLinked" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the snapshot is linked or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/isRestored"></div>
                <b>isRestored</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/isRestored" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Indicates whether the snapshot is restored or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/nonSharedTracks"></div>
                <b>nonSharedTracks</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/nonSharedTracks" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of non-shared tracks.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/numSharedTracks"></div>
                <b>numSharedTracks</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/numSharedTracks" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of shared tracks.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/numSourceVolumes"></div>
                <b>numSourceVolumes</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/numSourceVolumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of source volumes.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/numStorageGroupVolumes"></div>
                <b>numStorageGroupVolumes</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/numStorageGroupVolumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of storage group volumes.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/numUniqueTracks"></div>
                <b>numUniqueTracks</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/numUniqueTracks" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of unique tracks.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/sourceVolume"></div>
                <b>sourceVolume</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/sourceVolume" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Source volume details.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/sourceVolume/capacity"></div>
                <b>capacity</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/sourceVolume/capacity" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume capacity.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/sourceVolume/capacity_gb"></div>
                <b>capacity_gb</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/sourceVolume/capacity_gb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume capacity in GB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/sourceVolume/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/sourceVolume/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>State of the snapshot.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/timestamp"></div>
                <b>timestamp</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/timestamp" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Snapshot time stamp.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/timestamp_utc"></div>
                <b>timestamp_utc</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/timestamp_utc" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Snapshot time stamp specified in UTC.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/timeToLiveExpiryDate"></div>
                <b>timeToLiveExpiryDate</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/timeToLiveExpiryDate" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Time to live expiry date.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-sg_snap_details/tracks"></div>
                <b>tracks</b>
                <a class="ansibleOptionLink" href="#return-sg_snap_details/tracks" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of tracks.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Prashant Rakheja (@prashant-dell) &lt;<ansible.team@dell.com>&gt;

SRDF Module
===========

Synopsis
--------

Managing SRDF link on a PowerMax storage system includes creating an
SRDF pair for a storage group, modifying the SRDF mode, modifying
the SRDF state of an existing SRDF pair, and deleting an SRDF pair.
All create and modify calls are asynchronous by default.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-job_id"></div>
                <b>job_id</b>
                <a class="ansibleOptionLink" href="#parameter-job_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Job ID of an asynchronous task. Can be used to get details of a job.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_rdf_group"></div>
                <b>new_rdf_group</b>
                <a class="ansibleOptionLink" href="#parameter-new_rdf_group" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Overrides the SRDF group selection functionality and forces the creation of a new SRDF group.</div>
                                        <div>PowerMax has a limited number of RDF groups. If this flag is set to True, and the RDF groups are exhausted, then SRDF link creation will fail.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-rdfg_no"></div>
                <b>rdfg_no</b>
                <a class="ansibleOptionLink" href="#parameter-rdfg_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=integer</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The RDF group number.</div>
                                        <div>Optional parameter for each call. For a create operation, if specified, the array will reuse the RDF group, otherwise an error is returned. For modify and delete operations, if the RFD group number is not specified, and the storage group is protected by multiple RDF groups, then an error is raised.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-remote_serial_no"></div>
                <b>remote_serial_no</b>
                <a class="ansibleOptionLink" href="#parameter-remote_serial_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Integer 12-digit serial number of remote PowerMax or VMAX array.</div>
                                        <div>Required while creating an SRDF link.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-serial_no"></div>
                <b>serial_no</b>
                <a class="ansibleOptionLink" href="#parameter-serial_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The serial number will refer to the source PowerMax/VMAX array when protecting a storage group. However srdf_state operations may be issued from primary or remote array.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sg_name"></div>
                <b>sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of storage group. SRDF pairings are managed at a storage group level.</div>
                                        <div>Required to identify the SRDF link.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-srdf_mode"></div>
                <b>srdf_mode</b>
                <a class="ansibleOptionLink" href="#parameter-srdf_mode" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>Active</li>
                                                                                                                                                                                            <li>Adaptive Copy</li>
                                                                                                                                                                                            <li>Synchronous</li>
                                                                                                                                                                                            <li>Asynchronous</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The replication mode of the SRDF pair.</div>
                                        <div>Required when creating an SRDF pair.</div>
                                        <div>Can be modified by providing a required value.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-srdf_state"></div>
                <b>srdf_state</b>
                <a class="ansibleOptionLink" href="#parameter-srdf_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>Establish</li>
                                                                                                                                                                                            <li>Resume</li>
                                                                                                                                                                                            <li>Restore</li>
                                                                                                                                                                                            <li>Suspend</li>
                                                                                                                                                                                            <li>Swap</li>
                                                                                                                                                                                            <li>Split</li>
                                                                                                                                                                                            <li>Failback</li>
                                                                                                                                                                                            <li>Failover</li>
                                                                                                                                                                                            <li>Setbias</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Desired state of the SRDF pairing. While creating a new SRDF pair, allowed values are &#x27;Establish&#x27; and &#x27;Suspend&#x27;. If the state is not specified, the pair will be created in a &#x27;Suspended&#x27; state. When modifying the state, only certain changes are allowed.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the SRDF pairing should exist or not.</div>
                                        <div>present indicates that the SRDF pairing should exist in system.</div>
                                        <div>absent indicates that the SRDF pairing should not exist in system.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-wait_for_completion"></div>
                <b>wait_for_completion</b>
                <a class="ansibleOptionLink" href="#parameter-wait_for_completion" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Flag to indicate if the operation should be run synchronously or asynchronously. True signifies synchronous execution. By default, all create and update operations will be run asynchronously.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-witness"></div>
                <b>witness</b>
                <a class="ansibleOptionLink" href="#parameter-witness" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Flag to specify use of Witness for a Metro configuration. Setting to True signifies to use Witness, setting it to False signifies to use Bias. It is recommended to configure a witness for SRDF Metro in a production environment, this is configured via Unisphere for PowerMax UI or REST.</div>
                                        <div>The flag can be set only for modifying srdf_state to either Establish, Suspend, or Restore.</div>
                                        <div>While creating a Metro configuration, the witness flag must be set to True.</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Job_details"></div>
                <b>Job_details</b>
                <a class="ansibleOptionLink" href="#return-Job_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When job exist.</td>
            <td>
                                        <div>Details of the job.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/completed_date_milliseconds"></div>
                <b>completed_date_milliseconds</b>
                <a class="ansibleOptionLink" href="#return-Job_details/completed_date_milliseconds" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date of job completion in milliseconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/jobId"></div>
                <b>jobId</b>
                <a class="ansibleOptionLink" href="#return-Job_details/jobId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/last_modified_date"></div>
                <b>last_modified_date</b>
                <a class="ansibleOptionLink" href="#return-Job_details/last_modified_date" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Last modified date of job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/last_modified_date_milliseconds"></div>
                <b>last_modified_date_milliseconds</b>
                <a class="ansibleOptionLink" href="#return-Job_details/last_modified_date_milliseconds" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Last modified date of job in milliseconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Job_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/resourceLink"></div>
                <b>resourceLink</b>
                <a class="ansibleOptionLink" href="#return-Job_details/resourceLink" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Resource link w.r.t Unisphere.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/result"></div>
                <b>result</b>
                <a class="ansibleOptionLink" href="#return-Job_details/result" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Job description</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/status"></div>
                <b>status</b>
                <a class="ansibleOptionLink" href="#return-Job_details/status" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/task"></div>
                <b>task</b>
                <a class="ansibleOptionLink" href="#return-Job_details/task" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details about the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/username"></div>
                <b>username</b>
                <a class="ansibleOptionLink" href="#return-Job_details/username" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unisphere username.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details"></div>
                <b>SRDF_link_details</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When SRDF link exists.</td>
            <td>
                                        <div>Details of the SRDF link.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/hop2Modes"></div>
                <b>hop2Modes</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/hop2Modes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>SRDF hop2 mode.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/hop2Rdfgs"></div>
                <b>hop2Rdfgs</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/hop2Rdfgs" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Hop2 RDF group number.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/hop2States"></div>
                <b>hop2States</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/hop2States" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>SRDF hop2 state.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/largerRdfSides"></div>
                <b>largerRdfSides</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/largerRdfSides" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Larger volume side of the link.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/localR1InvalidTracksHop1"></div>
                <b>localR1InvalidTracksHop1</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/localR1InvalidTracksHop1" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of invalid R1 tracks on local volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/localR2InvalidTracksHop1"></div>
                <b>localR2InvalidTracksHop1</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/localR2InvalidTracksHop1" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of invalid R2 tracks on local volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/modes"></div>
                <b>modes</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/modes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Mode of the SRDF pair.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/rdfGroupNumber"></div>
                <b>rdfGroupNumber</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/rdfGroupNumber" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDF group number of the pair.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/remoteR1InvalidTracksHop1"></div>
                <b>remoteR1InvalidTracksHop1</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/remoteR1InvalidTracksHop1" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of invalid R1 tracks on remote volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/remoteR2InvalidTracksHop1"></div>
                <b>remoteR2InvalidTracksHop1</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/remoteR2InvalidTracksHop1" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of invalid R2 tracks on remote volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/remoteSymmetrix"></div>
                <b>remoteSymmetrix</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/remoteSymmetrix" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Remote symmetrix ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/states"></div>
                <b>states</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/states" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>State of the SRDF pair.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/storageGroupName"></div>
                <b>storageGroupName</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/storageGroupName" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of storage group that is SRDF protected.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/symmetrixId"></div>
                <b>symmetrixId</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/symmetrixId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Primary symmetrix ID.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/totalTracks"></div>
                <b>totalTracks</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/totalTracks" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Total number of tracks in the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-SRDF_link_details/volumeRdfTypes"></div>
                <b>volumeRdfTypes</b>
                <a class="ansibleOptionLink" href="#return-SRDF_link_details/volumeRdfTypes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDF type of volume.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Manisha Agrawal (@agrawm3) &lt;<ansible.team@dell.com>&gt;
-   Rajshree Khare (@khareRajshree) &lt;<ansible.team@dell.com>&gt;

Storage Group Module
====================

Synopsis
--------

Managing storage groups on a PowerMax storage system includes
listing the volumes of a storage group, creating a new storage
group, deleting an existing storage group, adding existing volumes
to an existing storage group, removing existing volumes from an
existing storage group, creating new volumes in an existing storage
group, modifying existing storage group attributes, adding child
storage groups inside an existing storage group (parent), and
removing a child storage group from an existing parent storage
group.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-child_sg_state"></div>
                <b>child_sg_state</b>
                <a class="ansibleOptionLink" href="#parameter-child_sg_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-group</li>
                                                                                                                                                                                            <li>absent-in-group</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Describes the state of CSG inside parent SG</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-child_storage_groups"></div>
                <b>child_storage_groups</b>
                <a class="ansibleOptionLink" href="#parameter-child_storage_groups" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                    <br>
                    <span style="color: purple">elements=string</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This is a list of child storage groups</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-compression"></div>
                <b>compression</b>
                <a class="ansibleOptionLink" href="#parameter-compression" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>compression on storage group.</div>
                                        <div>Compression parameter is ignored if service_level is not specified.</div>
                                        <div>Default is true.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_sg_name"></div>
                <b>new_sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new name of the storage group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-service_level"></div>
                <b>service_level</b>
                <a class="ansibleOptionLink" href="#parameter-service_level" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The Name of SLO.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sg_name"></div>
                <b>sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the storage group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-srp"></div>
                <b>srp</b>
                <a class="ansibleOptionLink" href="#parameter-srp" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the storage resource pool.</div>
                                        <div>This parameter is ignored if service_level is not specified.</div>
                                        <div>Default is to use whichever is the default SRP on the array.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Define whether the storage group should exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_state"></div>
                <b>vol_state</b>
                <a class="ansibleOptionLink" href="#parameter-vol_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>present-in-group</li>
                                                                                                                                                                                            <li>absent-in-group</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Describes the state of volumes inside the SG.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-volumes"></div>
                <b>volumes</b>
                <a class="ansibleOptionLink" href="#parameter-volumes" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=list</span>
                    <br>
                    <span style="color: purple">elements=dictionary</span>                                            </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>This is a list of volumes.</div>
                                        <div>Each volume has four attributes-</div>
                                        <div>vol_name</div>
                                        <div>size</div>
                                        <div>cap_unit</div>
                                        <div>vol_id.</div>
                                        <div>Either the volume ID must be provided for existing volumes, or the name and size must be provided to add new volumes to SG. The unit is optional.</div>
                                        <div>vol_name - Represents the name of the volume</div>
                                        <div>size - Represents the volume size</div>
                                        <div>cap_unit - The unit in which size is represented. Default unit is GB. Choices are MB, GB, TB.</div>
                                        <div>vol_id - This is the volume ID</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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
```

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-add_child_sg"></div>
                <b>add_child_sg</b>
                <a class="ansibleOptionLink" href="#return-add_child_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when a child SG is added.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-add_new_vols_to_sg"></div>
                <b>add_new_vols_to_sg</b>
                <a class="ansibleOptionLink" href="#return-add_new_vols_to_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when new volumes are added to the SG.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-add_vols_to_sg"></div>
                <b>add_vols_to_sg</b>
                <a class="ansibleOptionLink" href="#return-add_vols_to_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when existing volumes are added to the SG.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-added_vols_details"></div>
                <b>added_vols_details</b>
                <a class="ansibleOptionLink" href="#return-added_vols_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Volume IDs of the volumes added.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-create_sg"></div>
                <b>create_sg</b>
                <a class="ansibleOptionLink" href="#return-create_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when a new SG is created.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-delete_sg"></div>
                <b>delete_sg</b>
                <a class="ansibleOptionLink" href="#return-delete_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when an SG is deleted.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-modify_sg"></div>
                <b>modify_sg</b>
                <a class="ansibleOptionLink" href="#return-modify_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when an SG is modified.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-remove_child_sg"></div>
                <b>remove_child_sg</b>
                <a class="ansibleOptionLink" href="#return-remove_child_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when a child SG is removed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-remove_vols_from_sg"></div>
                <b>remove_vols_from_sg</b>
                <a class="ansibleOptionLink" href="#return-remove_vols_from_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when volumes are removed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-removed_vols_details"></div>
                <b>removed_vols_details</b>
                <a class="ansibleOptionLink" href="#return-removed_vols_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Volume IDs of the volumes removed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-rename_sg"></div>
                <b>rename_sg</b>
                <a class="ansibleOptionLink" href="#return-rename_sg" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Sets to true when an SG is renamed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-storage_group_details"></div>
                <b>storage_group_details</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When storage group exists.</td>
            <td>
                                        <div>Details of the storage group.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/base_slo_name"></div>
                <b>base_slo_name</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/base_slo_name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Base Service Level Objective (SLO) of a storage group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/cap_gb"></div>
                <b>cap_gb</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/cap_gb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Storage group capacity in GB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/compression"></div>
                <b>compression</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/compression" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Compression flag.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/device_emulation"></div>
                <b>device_emulation</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/device_emulation" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Device emulation type.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/num_of_child_sgs"></div>
                <b>num_of_child_sgs</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/num_of_child_sgs" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of child storage groups.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/num_of_masking_views"></div>
                <b>num_of_masking_views</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/num_of_masking_views" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of masking views associated with the storage group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/num_of_parent_sgs"></div>
                <b>num_of_parent_sgs</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/num_of_parent_sgs" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of parent storage groups.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/num_of_snapshots"></div>
                <b>num_of_snapshots</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/num_of_snapshots" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of snapshots for the storage group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/num_of_vols"></div>
                <b>num_of_vols</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/num_of_vols" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of volumes in the storage group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/service_level"></div>
                <b>service_level</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/service_level" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of service level.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/slo"></div>
                <b>slo</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/slo" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Service level objective (SLO) type.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/slo_compliance"></div>
                <b>slo_compliance</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/slo_compliance" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of SLO compliance.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/srp"></div>
                <b>srp</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/srp" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Storage resource pool.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/storageGroupId"></div>
                <b>storageGroupId</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/storageGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Id for the storage group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>type of storage group.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/unprotected"></div>
                <b>unprotected</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/unprotected" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for storage group protection.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_details/vp_saved_percent"></div>
                <b>vp_saved_percent</b>
                <a class="ansibleOptionLink" href="#return-storage_group_details/vp_saved_percent" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Percentage saved for virtual pools.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-storage_group_volumes"></div>
                <b>storage_group_volumes</b>
                <a class="ansibleOptionLink" href="#return-storage_group_volumes" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>When value exists.</td>
            <td>
                                        <div>Volume IDs of storage group volumes.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-storage_group_volumes_details"></div>
                <b>storage_group_volumes_details</b>
                <a class="ansibleOptionLink" href="#return-storage_group_volumes_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When storage group volumes exists.</td>
            <td>
                                        <div>Details of the storage group volumes.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_volumes_details/effective_wwn"></div>
                <b>effective_wwn</b>
                <a class="ansibleOptionLink" href="#return-storage_group_volumes_details/effective_wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Effective WWN of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_volumes_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-storage_group_volumes_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_volumes_details/volume_identifier"></div>
                <b>volume_identifier</b>
                <a class="ansibleOptionLink" href="#return-storage_group_volumes_details/volume_identifier" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name associated with the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_volumes_details/volumeId"></div>
                <b>volumeId</b>
                <a class="ansibleOptionLink" href="#return-storage_group_volumes_details/volumeId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique ID of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-storage_group_volumes_details/wwn"></div>
                <b>wwn</b>
                <a class="ansibleOptionLink" href="#return-storage_group_volumes_details/wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>WWN of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Vasudevu Lakhinana (@unknown) &lt;<ansible.team@dell.com>&gt;
-   Prashant Rakheja (@prashant-dell) &lt;<ansible.team@dell.com>&gt;
-   Ambuj Dubey (@AmbujDube) &lt;<ansible.team@dell.com>&gt;

Volume Module
=============

Synopsis
--------

Managing volumes on PowerMax storage system includes creating a
volume, renaming a volume, expanding a volume, and deleting a
volume.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-cap_unit"></div>
                <b>cap_unit</b>
                <a class="ansibleOptionLink" href="#parameter-cap_unit" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>MB</li>
                                                                                                                                                                                            <li><div style="color: blue"><b>GB</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>TB</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>volume capacity units</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_name"></div>
                <b>new_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new volume identifier for the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-new_sg_name"></div>
                <b>new_sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-new_sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the target storage group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-sg_name"></div>
                <b>sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the storage group.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-size"></div>
                <b>size</b>
                <a class="ansibleOptionLink" href="#parameter-size" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=float</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The new size of existing volume.</div>
                                        <div>Required for create and expand volume operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Defines whether the volume should exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_id"></div>
                <b>vol_id</b>
                <a class="ansibleOptionLink" href="#parameter-vol_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The native id of the volume.</div>
                                        <div>Required for rename and delete volume operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_name"></div>
                <b>vol_name</b>
                <a class="ansibleOptionLink" href="#parameter-vol_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The name of the volume.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-vol_wwn"></div>
                <b>vol_wwn</b>
                <a class="ansibleOptionLink" href="#parameter-vol_wwn" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>The WWN of the volume.</div>
                                                    </td>
        </tr>
                    </table>

Notes
-----

- To expand a volume, either provide vol\_id or vol\_name or vol\_wwn
and sg\_name
- size is required to create/expand a volume
- vol\_id is required to rename/delete a volume
- vol\_name, sg\_name and new\_sg\_name is required to move volumes between storage groups
- Deletion of volume will fail if the storage group is part of a masking
view

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-volume_details"></div>
                <b>volume_details</b>
                <a class="ansibleOptionLink" href="#return-volume_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">complex</span>
                                      </div>
                                </td>
            <td>When volume exists.</td>
            <td>
                                        <div>Details of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/allocated_percent"></div>
                <b>allocated_percent</b>
                <a class="ansibleOptionLink" href="#return-volume_details/allocated_percent" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Allocated percentage the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/cap_cyl"></div>
                <b>cap_cyl</b>
                <a class="ansibleOptionLink" href="#return-volume_details/cap_cyl" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of cylinders.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/cap_gb"></div>
                <b>cap_gb</b>
                <a class="ansibleOptionLink" href="#return-volume_details/cap_gb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume capacity in GB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/cap_mb"></div>
                <b>cap_mb</b>
                <a class="ansibleOptionLink" href="#return-volume_details/cap_mb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume capacity in MB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/effective_wwn"></div>
                <b>effective_wwn</b>
                <a class="ansibleOptionLink" href="#return-volume_details/effective_wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Effective WWN of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/emulation"></div>
                <b>emulation</b>
                <a class="ansibleOptionLink" href="#return-volume_details/emulation" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume emulation type.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/encapsulated"></div>
                <b>encapsulated</b>
                <a class="ansibleOptionLink" href="#return-volume_details/encapsulated" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for encapsulation.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/has_effective_wwn"></div>
                <b>has_effective_wwn</b>
                <a class="ansibleOptionLink" href="#return-volume_details/has_effective_wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for effective WWN presence.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/mobility_id_enabled"></div>
                <b>mobility_id_enabled</b>
                <a class="ansibleOptionLink" href="#return-volume_details/mobility_id_enabled" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag for enabling mobility.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/num_of_front_end_paths"></div>
                <b>num_of_front_end_paths</b>
                <a class="ansibleOptionLink" href="#return-volume_details/num_of_front_end_paths" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of front end paths in the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/num_of_storage_groups"></div>
                <b>num_of_storage_groups</b>
                <a class="ansibleOptionLink" href="#return-volume_details/num_of_storage_groups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Number of storage groups in which volume is present.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/pinned"></div>
                <b>pinned</b>
                <a class="ansibleOptionLink" href="#return-volume_details/pinned" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Pinned flag.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/rdfGroupId"></div>
                <b>rdfGroupId</b>
                <a class="ansibleOptionLink" href="#return-volume_details/rdfGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>RDFG number for volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/reserved"></div>
                <b>reserved</b>
                <a class="ansibleOptionLink" href="#return-volume_details/reserved" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Reserved flag.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/snapvx_source"></div>
                <b>snapvx_source</b>
                <a class="ansibleOptionLink" href="#return-volume_details/snapvx_source" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Source SnapVX flag.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/snapvx_target"></div>
                <b>snapvx_target</b>
                <a class="ansibleOptionLink" href="#return-volume_details/snapvx_target" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Target SnapVX flag.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/ssid"></div>
                <b>ssid</b>
                <a class="ansibleOptionLink" href="#return-volume_details/ssid" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>SSID of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/status"></div>
                <b>status</b>
                <a class="ansibleOptionLink" href="#return-volume_details/status" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Volume status.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/storage_groups"></div>
                <b>storage_groups</b>
                <a class="ansibleOptionLink" href="#return-volume_details/storage_groups" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>List of storage groups for the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/storageGroupId"></div>
                <b>storageGroupId</b>
                <a class="ansibleOptionLink" href="#return-volume_details/storageGroupId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Storage group ID of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/type"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#return-volume_details/type" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Type of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/volume_identifier"></div>
                <b>volume_identifier</b>
                <a class="ansibleOptionLink" href="#return-volume_details/volume_identifier" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name identifier for the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/volumeId"></div>
                <b>volumeId</b>
                <a class="ansibleOptionLink" href="#return-volume_details/volumeId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique ID of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-volume_details/wwn"></div>
                <b>wwn</b>
                <a class="ansibleOptionLink" href="#return-volume_details/wwn" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>WWN of the volume.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Vasudevu Lakhinana (@unknown) &lt;<ansible.team@dell.com>&gt;
-   Akash Shendge (@shenda1) &lt;<ansible.team@dell.com>&gt;
-   Ambuj Dubey (@AmbujDube) &lt;<ansible.team@dell.com>&gt;

Metro DR Module
===============

Synopsis
--------

Managing a metro DR environment on a PowerMax storage system
includes getting details of any specific metro DR environment,
creating a metro DR environment, converting an existing SG into a
metro DR environment, modifying metro DR environment attributes and
deleting a metro DR environment.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-dr_serial_no"></div>
                <b>dr_serial_no</b>
                <a class="ansibleOptionLink" href="#parameter-dr_serial_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Serial number of the DR array.</div>
                                        <div>It is required in create and convert operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-env_name"></div>
                <b>env_name</b>
                <a class="ansibleOptionLink" href="#parameter-env_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the metro DR environment.</div>
                                        <div>Metro DR environment name will be unique across PowerMax.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-metro_serial_no"></div>
                <b>metro_serial_no</b>
                <a class="ansibleOptionLink" href="#parameter-metro_serial_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Serial number of the remote metro array.</div>
                                        <div>It is required only in create and convert operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-new_rdf_group_r1"></div>
                <b>new_rdf_group_r1</b>
                <a class="ansibleOptionLink" href="#parameter-new_rdf_group_r1" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The flag indicates whether or not to create a new RDFG for a Metro R1 array to a DR array, or to autoselect from an existing one.</div>
                                        <div>Used in only create operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-new_rdf_group_r2"></div>
                <b>new_rdf_group_r2</b>
                <a class="ansibleOptionLink" href="#parameter-new_rdf_group_r2" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>no</li>
                                                                                                                                                                                            <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The flag indicates whether or not to create a new RDFG for a Metro R2 array to a DR array, or to autoselect from an existing one.</div>
                                        <div>It is used only in create operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-remove_r1_dr_rdfg"></div>
                <b>remove_r1_dr_rdfg</b>
                <a class="ansibleOptionLink" href="#parameter-remove_r1_dr_rdfg" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The flag indicates whether or not to override default behavior and delete R11-R2 RDFG from the metro R1 side.</div>
                                        <div>It is used only in delete operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-replication_mode"></div>
                <b>replication_mode</b>
                <a class="ansibleOptionLink" href="#parameter-replication_mode" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>Asynchronous</li>
                                                                                                                                                                                            <li>Adaptive Copy</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>Replication mode whose value will indicate how the data will be replicated.</div>
                                        <div>It is required in create and modify operations.</div>
                                        <div>It is a mandatory parameter in a create operation but optional in a modify operation.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-serial_no"></div>
                <b>serial_no</b>
                <a class="ansibleOptionLink" href="#parameter-serial_no" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Serial number of the primary metro array.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-sg_name"></div>
                <b>sg_name</b>
                <a class="ansibleOptionLink" href="#parameter-sg_name" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Name of the storage group.</div>
                                        <div>Storage group will be present on the primary metro array and a storage group with the same name will be created on remote and DR arrays in a create operation.</div>
                                        <div>Storage group name is required in &#x27;create metro DR environment&#x27; and &#x27;convert SG into metro DR environment&#x27; operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-srdf_param"></div>
                <b>srdf_param</b>
                <a class="ansibleOptionLink" href="#parameter-srdf_param" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=dictionary</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>It contains parameters related to SRDF links.</div>
                                        <div>It is used only in modify operations.</div>
                                                    </td>
        </tr>
                                    <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-srdf_param/dr"></div>
                <b>dr</b>
                <a class="ansibleOptionLink" href="#parameter-srdf_param/dr" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The flag indicates whether or not to direct srdf_state change towards device pairs on the disaster recovery leg of the metro DR environment.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-srdf_param/keep_r2"></div>
                <b>keep_r2</b>
                <a class="ansibleOptionLink" href="#parameter-srdf_param/keep_r2" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The flag indicates whether or not in the case of srdf state suspend to make R2 data on metro available to the host.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-srdf_param/metro"></div>
                <b>metro</b>
                <a class="ansibleOptionLink" href="#parameter-srdf_param/metro" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The flag indicates whether or not to direct srdf_state change towards the R1--R2 Metro Device leg of the metro DR environment.</div>
                                                    </td>
        </tr>
                            <tr>
                                                <td class="elbow-placeholder"></td>
                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-srdf_param/srdf_state"></div>
                <b>srdf_state</b>
                <a class="ansibleOptionLink" href="#parameter-srdf_param/srdf_state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>Split</li>
                                                                                                                                                                                            <li>Restore</li>
                                                                                                                                                                                            <li>SetMode</li>
                                                                                                                                                                                            <li>Failback</li>
                                                                                                                                                                                            <li>Failover</li>
                                                                                                                                                                                            <li>Establish</li>
                                                                                                                                                                                            <li>Suspend</li>
                                                                                                                                                                                            <li>UpdateR1</li>
                                                                                                                                                                                            <li>Recover</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State of the SRDF link.</div>
                                        <div>It is a mandatory parameter for modify operations.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-state"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li>absent</li>
                                                                                                                                                                                            <li>present</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>State variable to determine whether metro DR environment will exist or not.</div>
                                                    </td>
        </tr>
                            <tr>
                                                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-wait_for_completion"></div>
                <b>wait_for_completion</b>
                <a class="ansibleOptionLink" href="#parameter-wait_for_completion" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=boolean</span>
                                                                </div>
                                                    </td>
                            <td>
                                                                                                                                                                                                                <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                            <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                            <li>yes</li>
                                                                                </ul>
                                                                        </td>
                                                            <td>
                                        <div>The flag indicates if the operation should be run synchronously or asynchronously.</div>
                                        <div>True signifies synchronous execution.</div>
                                        <div>By default, create and convert are asynchronous operations, whereas modify is a synchronous operation.</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
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

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Job_details"></div>
                <b>Job_details</b>
                <a class="ansibleOptionLink" href="#return-Job_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                      </div>
                                </td>
            <td>When job exist.</td>
            <td>
                                        <div>Details of the job.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/completed_date_milliseconds"></div>
                <b>completed_date_milliseconds</b>
                <a class="ansibleOptionLink" href="#return-Job_details/completed_date_milliseconds" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date of job completion in milliseconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/jobId"></div>
                <b>jobId</b>
                <a class="ansibleOptionLink" href="#return-Job_details/jobId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/last_modified_date"></div>
                <b>last_modified_date</b>
                <a class="ansibleOptionLink" href="#return-Job_details/last_modified_date" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Last modified date of job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/last_modified_date_milliseconds"></div>
                <b>last_modified_date_milliseconds</b>
                <a class="ansibleOptionLink" href="#return-Job_details/last_modified_date_milliseconds" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Last modified date of job in milliseconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Job_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/resourceLink"></div>
                <b>resourceLink</b>
                <a class="ansibleOptionLink" href="#return-Job_details/resourceLink" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Resource link w.r.t Unisphere.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/result"></div>
                <b>result</b>
                <a class="ansibleOptionLink" href="#return-Job_details/result" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Job description</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/status"></div>
                <b>status</b>
                <a class="ansibleOptionLink" href="#return-Job_details/status" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/task"></div>
                <b>task</b>
                <a class="ansibleOptionLink" href="#return-Job_details/task" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br>
                  <span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details about the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/username"></div>
                <b>username</b>
                <a class="ansibleOptionLink" href="#return-Job_details/username" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unisphere username.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details"></div>
                <b>metrodr_env_details</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                      </div>
                                </td>
            <td>When environment exists.</td>
            <td>
                                        <div>Details of the metro DR environment link.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/capacity_gb"></div>
                <b>capacity_gb</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/capacity_gb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">float</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Size of volume in GB.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/dr_exempt"></div>
                <b>dr_exempt</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/dr_exempt" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag to indication that if there are exempt devices (volumes) in the DR site or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/dr_link_state"></div>
                <b>dr_link_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/dr_link_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of DR site.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/dr_percent_complete"></div>
                <b>dr_percent_complete</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/dr_percent_complete" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Percentage synchronized in DR session.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/dr_rdf_mode"></div>
                <b>dr_rdf_mode</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/dr_rdf_mode" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Replication mode with DR site.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/dr_remain_capacity_to_copy_mb"></div>
                <b>dr_remain_capacity_to_copy_mb</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/dr_remain_capacity_to_copy_mb" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Remaining capacity to copy at DR site.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/dr_service_state"></div>
                <b>dr_service_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/dr_service_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The HA state of the DR session.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/dr_state"></div>
                <b>dr_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/dr_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The pair states of the DR session.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/environment_exempt"></div>
                <b>environment_exempt</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/environment_exempt" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag to indication that if there are exempt devices (volumes) in the environment or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/environment_state"></div>
                <b>environment_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/environment_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The state of the smart DR environment.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/metro_exempt"></div>
                <b>metro_exempt</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/metro_exempt" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag to indication that if there are exempt devices (volumes) in the DR site or not.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/metro_link_state"></div>
                <b>metro_link_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/metro_link_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of metro site.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/metro_r1_array_health"></div>
                <b>metro_r1_array_health</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/metro_r1_array_health" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Health status of metro R1 array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/metro_r2_array_health"></div>
                <b>metro_r2_array_health</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/metro_r2_array_health" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Health status of metro R1 array.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/metro_service_state"></div>
                <b>metro_service_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/metro_service_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The HA state of the metro session.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/metro_state"></div>
                <b>metro_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/metro_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The pair states of the metro session.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/metro_witness_state"></div>
                <b>metro_witness_state</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/metro_witness_state" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The witness state of the metro session.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>The smart DR environment name.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-metrodr_env_details/valid"></div>
                <b>valid</b>
                <a class="ansibleOptionLink" href="#return-metrodr_env_details/valid" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Flag to indicate whether valid environment or not.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Vivek Soni (@v-soni11) &lt;<ansible.team@dell.com>&gt;
-   Rajshree Khare (@khareRajshree) &lt;<ansible.team@dell.com>&gt;

Job Module
==========

Synopsis
--------

-   Gets details of a Job from a specified PowerMax/VMAX storage system.
-   The details listed are of an asynchronous task.

Parameters
----------

<table  border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="1">Parameter</th>
        <th>Choices/<font color="blue">Defaults</font></th>
                    <th width="100%">Comments</th>
    </tr>
                <tr>
                                                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="parameter-job_id"></div>
                <b>job_id</b>
                <a class="ansibleOptionLink" href="#parameter-job_id" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">type=string</span>,
                    <br>
                    <span style="color: red">required=true</span>                    </div>
                                                    </td>
                            <td>
                                                                                                                                                        </td>
                                                            <td>
                                        <div>Job ID of an asynchronous task, used for getting details of a job.</div>
                                                    </td>
        </tr>
                    </table>

Examples
--------

``` yaml+jinja
- name: Get the details of a Job.
  dellemc_powermax_job:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    job_id: "1570622921504"
```

Return Values
-------------

The following are the return value fields unique to this module:

<table border=0 cellpadding=0 class="documentation-table">
    <tr>
        <th colspan="2">Key</th>
        <th>Returned</th>
        <th width="100%">Description</th>
    </tr>
                <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-changed"></div>
                <b>changed</b>
                <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=boolean</span>
                                      </div>
                                </td>
            <td>always</td>
            <td>
                                        <div>Whether or not the resource has changed.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                            <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-Job_details"></div>
                <b>Job_details</b>
                <a class="ansibleOptionLink" href="#return-Job_details" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=dictionary</span>
                                      </div>
                                </td>
            <td>When job exist.</td>
            <td>
                                        <div>Details of the job.</div>
                                    <br/>
                                </td>
        </tr>
                                    <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/completed_date_milliseconds"></div>
                <b>completed_date_milliseconds</b>
                <a class="ansibleOptionLink" href="#return-Job_details/completed_date_milliseconds" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Date of job completion in milliseconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/jobId"></div>
                <b>jobId</b>
                <a class="ansibleOptionLink" href="#return-Job_details/jobId" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unique identifier of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/last_modified_date"></div>
                <b>last_modified_date</b>
                <a class="ansibleOptionLink" href="#return-Job_details/last_modified_date" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Last modified date of job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/last_modified_date_milliseconds"></div>
                <b>last_modified_date_milliseconds</b>
                <a class="ansibleOptionLink" href="#return-Job_details/last_modified_date_milliseconds" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=integer</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Last modified date of job in milliseconds.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/name"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#return-Job_details/name" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Name of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/resourceLink"></div>
                <b>resourceLink</b>
                <a class="ansibleOptionLink" href="#return-Job_details/resourceLink" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Resource link w.r.t Unisphere.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/result"></div>
                <b>result</b>
                <a class="ansibleOptionLink" href="#return-Job_details/result" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Job description</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/status"></div>
                <b>status</b>
                <a class="ansibleOptionLink" href="#return-Job_details/status" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Status of the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/task"></div>
                <b>task</b>
                <a class="ansibleOptionLink" href="#return-Job_details/task" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=list</span>
                  <br><span style="color: purple">elements=string</span>                    </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Details about the job.</div>
                                    <br/>
                                </td>
        </tr>
                            <tr>
                                <td class="elbow-placeholder">&nbsp;</td>
                            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-Job_details/username"></div>
                <b>username</b>
                <a class="ansibleOptionLink" href="#return-Job_details/username" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">type=string</span>
                                      </div>
                                </td>
            <td>success</td>
            <td>
                                        <div>Unisphere username.</div>
                                    <br/>
                                </td>
        </tr>
                    </table>

Authors
-------

-   Rajshree Khare (@kharer5) &lt;<ansible.team@dell.com>&gt;
