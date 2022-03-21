#!/usr/bin/python
# Copyright: (c) 2019-2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: srdf
version_added: '1.3.0'
short_description:  Manage SRDF pair on PowerMax/VMAX Storage
                    System
description:
- Managing SRDF link on a PowerMax storage system includes creating an SRDF
  pair for a storage group, modifying the SRDF mode, modifying the SRDF state
  of an existing SRDF pair, and deleting an SRDF pair. All create and modify
  calls are asynchronous by default.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Manisha Agrawal (@agrawm3) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

options:
  sg_name:
    description:
    - Name of storage group. SRDF pairings are managed at a storage group
      level.
    - Required to identify the SRDF link.
    required: false
    type: str
  serial_no:
    description:
    - The serial number will refer to the source PowerMax/VMAX array when
      protecting a storage group. However srdf_state operations may be issued
      from primary or remote array.
    required: true
    type: str
  remote_serial_no:
    description:
    - Integer 12-digit serial number of remote PowerMax or VMAX array.
    - Required while creating an SRDF link.
    required: false
    type: str
  rdfg_no:
    description:
    - The RDF group number.
    - Optional parameter for each call. For a create operation, if specified,
      the array will reuse the RDF group, otherwise an error is returned. For
      modify and delete operations, if the RFD group number is not specified,
      and the storage group is protected by multiple RDF groups, then an error
      is raised.
    required: false
    type: int
  state:
    description:
    - Define whether the SRDF pairing should exist or not.
    - present indicates that the SRDF pairing should exist in system.
    - absent indicates that the SRDF pairing should not exist in system.
    required: true
    type: str
    choices: [absent, present]
  srdf_mode:
    description:
    - The replication mode of the SRDF pair.
    - Required when creating an SRDF pair.
    - Can be modified by providing a required value.
    choices: [Active, Adaptive Copy, Synchronous, Asynchronous]
    required: false
    type: str
  srdf_state:
    description:
    - Desired state of the SRDF pairing. While creating a new SRDF pair,
      allowed values are 'Establish' and 'Suspend'. If the state is not
      specified, the pair will be created in a 'Suspended' state. When
      modifying the state, only certain changes are allowed.
    required: false
    type: str
    choices: [Establish, Resume, Restore, Suspend, Swap, Split, Failback,
             Failover, Setbias]
  new_rdf_group:
    description:
    - Overrides the SRDF group selection functionality and forces the creation
      of a new SRDF group.
    - PowerMax has a limited number of RDF groups. If this flag is set to True,
      and the RDF groups are exhausted, then SRDF link creation will fail.
    - If not specified, default value is 'false'.
    required: false
    type: bool
  wait_for_completion:
    description:
    - Flag to indicate if the operation should be run synchronously or
      asynchronously. True signifies synchronous execution. By default, all
      create and update operations will be run asynchronously.
    required: false
    default: False
    type: bool
  job_id:
    description:
    - Job ID of an asynchronous task. Can be used to get details of a job.
    required: false
    type: str
  witness:
    description:
    - Flag to specify use of Witness for a Metro configuration. Setting to
      True signifies to use Witness, setting it to False signifies to use
      Bias. It is recommended to configure a witness for SRDF Metro in a
      production environment, this is configured via Unisphere for PowerMax UI
      or REST.
    - The flag can be set only for modifying srdf_state to either Establish,
      Suspend, or Restore.
    - While creating a Metro configuration, the witness flag must be set to
      True.
    required: false
    type: bool
'''

EXAMPLES = r'''
- name: Create and establish storagegroup SRDF/a pairing
  register: Job_details_body
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    state: 'present'

- name: Modify SRDF mode
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    job_id: "{{Job_details_body.Job_details.jobId}}"
    state: 'present'

- name: Establish SRDF link
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
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
  dellemc.powermax.srdf:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    sg_name: "{{sg_name}}"
    state: 'absent'
'''

RETURN = r'''
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
Job_details:
    description: Details of the job.
    returned: When job exist.
    type: list
    contains:
        completed_date_milliseconds:
            description: Date of job completion in milliseconds.
            type: int
        jobId:
            description: Unique identifier of the job.
            type: str
        last_modified_date:
            description: Last modified date of job.
            type: str
        last_modified_date_milliseconds:
            description: Last modified date of job in milliseconds.
            type: int
        name:
            description: Name of the job.
            type: str
        resourceLink:
            description: Resource link w.r.t Unisphere.
            type: str
        result:
            description: Job description
            type: str
        status:
            description: Status of the job.
            type: str
        task:
            description: Details about the job.
            type: list
        username:
            description: Unisphere username.
            type: str
SRDF_link_details:
    description: Details of the SRDF link.
    returned: When SRDF link exists.
    type: complex
    contains:
        hop2Modes:
            description: SRDF hop2 mode.
            type: str
        hop2Rdfgs:
            description: Hop2 RDF group number.
            type: str
        hop2States:
            description: SRDF hop2 state.
            type: str
        largerRdfSides:
            description: Larger volume side of the link.
            type: str
        localR1InvalidTracksHop1:
            description: Number of invalid R1 tracks on local volume.
            type: int
        localR2InvalidTracksHop1:
            description: Number of invalid R2 tracks on local volume.
            type: int
        modes:
            description: Mode of the SRDF pair.
            type: str
        rdfGroupNumber:
            description: RDF group number of the pair.
            type: int
        remoteR1InvalidTracksHop1:
            description: Number of invalid R1 tracks on remote volume.
            type: int
        remoteR2InvalidTracksHop1:
            description: Number of invalid R2 tracks on remote volume.
            type: int
        remoteSymmetrix:
            description: Remote symmetrix ID.
            type: str
        states:
            description: State of the SRDF pair.
            type: str
        storageGroupName:
            description: Name of storage group that is SRDF protected.
            type: str
        symmetrixId:
            description: Primary symmetrix ID.
            type: str
        totalTracks:
            description: Total number of tracks in the volume.
            type: int
        volumeRdfTypes:
            description: RDF type of volume.
            type: str
'''

import logging
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger(module_name='srdf')

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class SRDF(object):

    '''Class with srdf operations'''

    u4v_conn = None

    def __init__(self):
        ''' Define all parameters required by this module'''
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(self.get_srdf_pair_parameters())
        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True
        )
        # result is a dictionary that contains changed status, srdf_link
        # and job details
        self.result = {
            "changed": False,
            "SRDF_link_details": {},
            "Job_details": {}}
        if HAS_PYU4V is False:
            self.show_error_exit(msg="Ansible modules for PowerMax require "
                                 "the PyU4V python library to be "
                                 "installed. Please install the library "
                                 "before using these modules.")

        if PYU4V_VERSION_CHECK is not None:
            self.show_error_exit(msg=PYU4V_VERSION_CHECK)

        if self.module.params['universion'] is not None:
            universion_details = utils.universion_check(
                self.module.params['universion'])
            LOG.info("universion_details: %s", universion_details)

            if not universion_details['is_valid_universion']:
                self.show_error_exit(msg=universion_details['user_message'])

        try:
            self.u4v_conn = utils.get_U4V_connection(
                self.module.params, application_type=APPLICATION_TYPE)
        except Exception as e:
            self.show_error_exit(msg=str(e))
        self.replication = self.u4v_conn.replication
        LOG.info('Check Mode flag is %s', self.module.check_mode)
        LOG.info('Got PyU4V instance for replication on PowerMax ')
        self.idempotency_dict = {
            'Synchronized': ['Establish', 'Resume'],
            'Consistent': ['Establish', 'Resume'],
            'Suspended': ['Suspend'],
            'Failed Over': ['Failover'],
            'SyncInProg': ['Establish', 'Resume'],
        }

        self.idempotency_dict_metro = {
            'Suspended': ['Suspend'],
            'SyncInProg': ['Establish'],
            'ActiveActive': ['Establish'],
            'ActiveBias': ['Establish']
        }

        self.current_rdfg_no = None

    def get_srdf_pair_parameters(self):
        return dict(
            sg_name=dict(required=False, type='str'),
            remote_serial_no=dict(required=False, type='str'),
            state=dict(required=True, type='str', choices=['present',
                                                           'absent']),
            srdf_state=dict(required=False, type='str', choices=['Establish',
                                                                 'Resume',
                                                                 'Restore',
                                                                 'Suspend',
                                                                 'Swap',
                                                                 'Split',
                                                                 'Failback',
                                                                 'Failover',
                                                                 'Setbias']),
            srdf_mode=dict(required=False, type='str',
                           choices=['Active',
                                    'Adaptive Copy',
                                    'Synchronous',
                                    'Asynchronous']),
            rdfg_no=dict(type='int', required=False),
            wait_for_completion=dict(type='bool', required=False,
                                     default=False),
            new_rdf_group=dict(type='bool', required=False),
            witness=dict(type='bool', required=False),
            job_id=dict(type='str', required=False))

    def get_srdf_link(self, sg_name):
        '''
        Get details of a given srdf_link
        '''
        srdf_link_details = []
        rdfg_number = self.module.params['rdfg_no']
        try:
            if rdfg_number:
                LOG.info("Getting srdf details for storage group %s "
                         "with rdfg number: %s", sg_name, rdfg_number)
                srdf_linkFromGet = self.replication.\
                    get_storage_group_srdf_details(storage_group_id=sg_name,
                                                   rdfg_num=rdfg_number)
                if srdf_linkFromGet:
                    srdf_linkFromGet['remoteSymmetrix'] = \
                        self.get_remote_symmetrix_from_rdfg(rdfg_number)
                    srdf_link_details.append(srdf_linkFromGet)
            else:
                rdfg_list = self.replication\
                    .get_storage_group_srdf_group_list(
                        sg_name)
                if len(rdfg_list) == 0:
                    msg = 'No RDF group exists for the given storage group.'
                    LOG.info(msg)
                    return None
                else:
                    msg = '1 or more RDF group exists for the given storage '\
                          'group.'
                    LOG.info(msg)

                # Multisite configuration
                for num in rdfg_list:
                    LOG.info("Getting srdf details for storage group %s with"
                             " rdfg number: %s", sg_name, num)
                    srdf_linkFromGet = self.replication.\
                        get_storage_group_srdf_details(
                            storage_group_id=sg_name, rdfg_num=num)
                    if srdf_linkFromGet:
                        srdf_linkFromGet['remoteSymmetrix'] = \
                            self.get_remote_symmetrix_from_rdfg(num)
                        srdf_link_details.append(srdf_linkFromGet)
            return srdf_link_details
        except Exception as e:
            errMsg = ("Getting SRDF details for storage group "
                      "%s with rdfg number %s failed with error %s"
                      % (sg_name, rdfg_number, str(e)))
            LOG.error(errMsg)
            srdf_link_details = None
            return srdf_link_details

    def create_srdf_link(self):
        '''
        Create srdf_link for given storagegroup_id group and remote array
        '''
        sg_name = self.module.params['sg_name']
        remote_serial_no = self.module.params['remote_serial_no']
        srdf_mode = self.module.params['srdf_mode']
        if srdf_mode == 'Adaptive Copy':
            srdf_mode = 'AdaptiveCopyDisk'
        if (remote_serial_no is None or srdf_mode is None):
            error_msg = ("Mandatory parameters not found. Required parameters "
                         "for creating an SRDF link are remote array serial number "
                         "and SRDF mode")
            self.show_error_exit(msg=error_msg)
        try:
            establish_flag = self._compute_required_establish_flag(
                self.module.params['srdf_state'])
            rdfg_number = self.module.params['rdfg_no']
            forceNewRdfGroup = self.module.params['new_rdf_group']
            async_flag = not (self.module.params['wait_for_completion'])
            witness = self.module.params['witness']

            if witness is False:
                errorMsg = ("Create SRDF link operation failed as Ansible"
                            " modules v1.1 does not allow creation of SRDF"
                            " links using Bias for resiliency.")
                self.show_error_exit(msg=errorMsg)

            msg = ('Creating srdf_link with parameters:sg_name = ', sg_name,
                   ', remote_serial_no= ', remote_serial_no,
                   ', srdfmode= ', srdf_mode,
                   ', establish_flag= ', establish_flag,
                   ', rdfgroup_no= ', rdfg_number,
                   ', new_rdf_group= ', forceNewRdfGroup,
                   ', async_flag= ', async_flag
                   )
            LOG.info(msg)
            resp = {}
            if not self.module.check_mode:
                resp = self.replication.create_storage_group_srdf_pairings(
                    storage_group_id=sg_name,
                    remote_sid=remote_serial_no,
                    srdf_mode=srdf_mode,
                    establish=establish_flag,
                    force_new_rdf_group=forceNewRdfGroup,
                    rdfg_number=rdfg_number,
                    _async=async_flag)
            LOG.debug('Response from create SRDF link call %s', resp)
            if async_flag:
                self.result['Job_details'] = resp
                self.result['SRDF_link_details'] = None
            else:
                self.result['SRDF_link_details'] = resp
                self.result['Job_details'] = None
                self.result['SRDF_link_details']['remoteSymmetrix']\
                    = remote_serial_no
            return True

        except Exception as e:
            errorMsg = ("Create srdf_link for sg %s failed with error %s"
                        % (sg_name, str(e)))
            self.show_error_exit(msg=errorMsg)

    def _compute_required_establish_flag(self, srdf_state):
        if (srdf_state is None or srdf_state == 'Suspend'):
            return False
        elif srdf_state == 'Establish':
            return True
        else:
            errorMsg = ("Creation of SRDF link failed. Allowed states while "
                        "creating SRDF link are only Establish or Suspend. Got %s."
                        % srdf_state)
            self.show_error_exit(msg=errorMsg)

    def modify_srdf_mode(self, srdf_mode):
        async_flag = not (self.module.params['wait_for_completion'])
        for link in self.result['SRDF_link_details']:
            if link['rdfGroupNumber'] == self.current_rdfg_no:
                srdf_link = link
        resp = {}
        if srdf_mode == 'Adaptive Copy':
            srdf_mode = 'AdaptiveCopyDisk'
        try:
            if not self.module.check_mode:
                resp = self.replication.modify_storage_group_srdf(
                    storage_group_id=srdf_link['storageGroupName'],
                    srdf_group_number=self.current_rdfg_no,
                    action='SetMode',
                    options={
                        'setMode': {
                            'mode': srdf_mode}},
                    _async=async_flag)
            LOG.debug("resp %s", resp)
            if async_flag:
                self.result['Job_details'] = resp
                self.result['SRDF_link_details'] = None
            else:
                self.result['SRDF_link_details'] = resp
                self.result['Job_details'] = None
                self.result['SRDF_link_details'][
                    'remoteSymmetrix'] = \
                    self.get_remote_symmetrix_from_rdfg(self.current_rdfg_no)
            return True
        except Exception as e:
            errorMsg = ("Modifying SRDF mode of srdf_link from %s to %s for "
                        "SG %s failed with error %s"
                        % (srdf_link['modes'][0], srdf_mode,
                           srdf_link['storageGroupName'], str(e)))
            self.show_error_exit(msg=errorMsg)

    def modify_srdf_state(self, action):
        modify_body = {}

        async_flag = not (self.module.params['wait_for_completion'])
        for link in self.result['SRDF_link_details']:
            if link['rdfGroupNumber'] == self.current_rdfg_no:
                srdf_link = link

        modify_body['storage_group_id'] = srdf_link['storageGroupName']
        modify_body['srdf_group_number'] = self.current_rdfg_no
        modify_body['action'] = action
        modify_body['_async'] = async_flag
        resp = {}

        if self.module.params['witness'] is not None:
            if srdf_link['modes'][0] != 'Active':
                errorMsg = ("witness flag can not be used for non-Metro "
                            "configurations.")
                self.show_error_exit(msg=errorMsg)
            elif action not in ['Establish', 'Restore', 'Suspend']:
                errorMsg = ("witness flag can be used only for 3 actions:"
                            " Establish, Restore and Suspend")
                self.show_error_exit(msg=errorMsg)
            else:
                modify_body['options'] = {
                    action.lower(): {
                        'metroBias': not (self.module.params['witness'])}}

        try:
            LOG.info('The modify_body is %s:', modify_body)
            if not self.module.check_mode:
                resp = self.replication.modify_storage_group_srdf(**modify_body)

            if async_flag:
                self.result['Job_details'] = resp
                self.result['SRDF_link_details'] = None
            else:
                self.result['SRDF_link_details'] = resp
                self.result['Job_details'] = None
                self.result['SRDF_link_details']['remoteSymmetrix']\
                    = self.get_remote_symmetrix_from_rdfg(self.current_rdfg_no)
            return True
        except Exception as e:
            if isinstance(e, utils.PyU4V.utils.exception.PyU4VException) and \
                    "is already in the requested RDF state" in str(e):
                return False
            errorMsg = ("Modifying SRDF state of srdf_link for storage group "
                        "%s failed with error %s"
                        % (srdf_link['storageGroupName'], str(e)))
            self.show_error_exit(msg=errorMsg)

    def _check_for_SRDF_state_modification(self, new_operation):
        for link in self.result['SRDF_link_details']:
            if link['rdfGroupNumber'] == self.current_rdfg_no:
                srdf_link = link
        current_state = srdf_link['states'][0]
        changed = False

        if (srdf_link['modes'][0] == 'Active'
                and current_state in self.idempotency_dict_metro
                and new_operation in self.idempotency_dict_metro
                [current_state]):
            LOG.info('Modification of SRDF state not required')
            changed = False

        elif (srdf_link['modes'][0] != 'Active' and
              current_state in self.idempotency_dict and
              new_operation in self.idempotency_dict[current_state]):
            LOG.info('Modification of SRDF state not required')
            changed = False

        else:
            LOG.info('Modifying SRDF state from %s to %s',
                     current_state, new_operation)
            changed = self.modify_srdf_state(new_operation)
        return changed

    def get_remote_symmetrix_from_rdfg(self, rdfg_num):
        try:
            rdfg_details = self.replication.get_rdf_group(rdfg_num)
            return rdfg_details['remoteSymmetrix']
        except Exception as e:
            errorMsg = ("Getting rdf group details for %s failed"
                        "with error %s" % (rdfg_num, str(e)))
            self.show_error_exit(msg=errorMsg)

    def delete_srdf_link(self):
        '''
        Delete srdf_link from system
        '''
        for link in self.result['SRDF_link_details']:
            if link['rdfGroupNumber'] == self.current_rdfg_no:
                srdf_link = link
        try:
            if not self.module.check_mode:
                self.replication.delete_storage_group_srdf(
                    srdf_link['storageGroupName'], int(self.current_rdfg_no))
            self.result['SRDF_link_details'] = {}
            return True
        except Exception as e:
            errorMsg = ("Delete srdf_link %s failed with error %s"
                        % (srdf_link['storageGroupName'], str(e)))
            self.show_error_exit(msg=errorMsg)

    def get_job_details(self, job_id):
        try:
            self.result['Job_details'] = self.u4v_conn.common.get_job_by_id(
                job_id)
        except Exception as e:
            errorMsg = ("Get Job details for job_id %s failed with error %s"
                        % (job_id, str(e)))
            self.show_error_exit(msg=errorMsg)

    def check_for_multiple_rdf_groups(self, srdf_link=None, get_only=True):
        '''
        Check for correct RDF group among multiple RDF groups present for a
        storage group.
        '''
        rdfg_no = self.module.params['rdfg_no']
        found = False
        return_rdfg = None
        if srdf_link is None:
            msg = 'No RDF group exists for the given storage group.'
            LOG.info(msg)
            return None, None
        if rdfg_no:
            if len(srdf_link) >= 1:
                for link in srdf_link:
                    if link['rdfGroupNumber'] == rdfg_no:
                        LOG.debug('Correct RDF group number identified.')
                        return_rdfg = link['rdfGroupNumber']
                        found = True
                if found:
                    return return_rdfg
                else:
                    errorMsg = ("Please specify the correct RDF group "
                                "number.")
                    self.show_error_exit(msg=errorMsg)
        # When rdfg_no is not given and there exists SRDF link for the SG.
        else:
            if len(srdf_link) == 1:
                return_rdfg = srdf_link[0]['rdfGroupNumber']
            if len(srdf_link) > 1:
                if not get_only:
                    errorMsg = 'Please specify the RDF group number.'
                    self.show_error_exit(msg=errorMsg)
        return return_rdfg

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = ("Closing unisphere connection failed with error:"
                           " %s", str(e))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def perform_module_operation(self):
        '''
        Perform different actions on srdf_link based on user parameter
        chosen in playbook
        '''
        state = self.module.params['state']
        sg_name = self.module.params['sg_name']
        srdf_mode = self.module.params['srdf_mode']
        srdf_state = self.module.params['srdf_state']
        job_id = self.module.params['job_id']
        changed = False
        remoteSymmetrixIDs = []

        if (job_id and sg_name) or (not job_id and not sg_name):
            errorMsg = 'Please specify either job ID or SG name in one ' \
                       'Ansible task'
            self.show_error_exit(msg=errorMsg)

        if job_id:
            if state == 'present':
                LOG.info('Geting details of the Job %s', job_id)
                self.get_job_details(job_id)
            else:
                errorMsg = 'Set state=present for getting Job status'
                self.show_error_exit(msg=errorMsg)
        else:
            srdf_link = self.get_srdf_link(sg_name)
            self.result['SRDF_link_details'] = srdf_link
            LOG.debug('srdf_link details: %s',
                      self.result['SRDF_link_details'])

            self.current_rdfg_no\
                = self.check_for_multiple_rdf_groups(srdf_link)

            if state == 'present':
                if not self.result['SRDF_link_details']:
                    LOG.debug('srdf_link details not found.')
                    changed = self.create_srdf_link()

                # Create 2nd link for Multisite SRDF
                if self.result['SRDF_link_details']\
                        and self.module.params['remote_serial_no'] \
                        and not changed:
                    LOG.debug('srdf_link details found.')
                    remoteSymmetrixIDcount = len(srdf_link)
                    for id in range(remoteSymmetrixIDcount):
                        remoteSymmetrixIDs.append(
                            self.result['SRDF_link_details'][id]
                            ['remoteSymmetrix'])
                    remote_serial_no = self.module.params['remote_serial_no']
                    if remote_serial_no not in remoteSymmetrixIDs:
                        changed = self.create_srdf_link()

                if self.result['SRDF_link_details'] \
                        and (srdf_mode or srdf_state) and not changed:
                    LOG.info('Modifying SRDF mode/state')
                    self.current_rdfg_no\
                        = self.check_for_multiple_rdf_groups(srdf_link, False)
                    for link in self.result['SRDF_link_details']:
                        if link['rdfGroupNumber'] == self.current_rdfg_no:
                            if (srdf_mode != link['modes'][0] and srdf_mode):
                                LOG.info('Modifying SRDF mode from %s to %s',
                                         link['modes'][0], srdf_mode)
                                changed = self.modify_srdf_mode(srdf_mode) \
                                    or changed
                            else:
                                LOG.info('Modification of SRDF state not'
                                         ' required')

                    if srdf_state is not None:
                        changed = self._check_for_SRDF_state_modification(
                            srdf_state) or changed

            elif state == 'absent' and self.result['SRDF_link_details']:
                self.current_rdfg_no\
                    = self.check_for_multiple_rdf_groups(srdf_link, False)
                LOG.info('Deleting srdf_link with SG %s ', sg_name)
                changed = self.delete_srdf_link() or changed

        # Update the module's final state
        LOG.info('changed %s', changed)
        self.result['changed'] = changed
        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")
        self.module.exit_json(**self.result)


def main():
    ''' Create PowerMax_srdf object and perform action on it
        based on user input from playbook'''
    obj = SRDF()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
