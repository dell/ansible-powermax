#!/usr/bin/python
# Copyright: (c) 2019, DellEMC

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import dellemc_ansible_utils as utils
import logging

__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'
                    }

DOCUMENTATION = r'''
---
module: dellemc_powermax_srdf
version_added: '2.6'
short_description:  Manage SRDF pair on PowerMax/VMAX Storage
                    System
description:
- Managing SRDF link on PowerMax Storage System includes creating SRDF pair for
  a storage group, modify SRDF mode, modify SRDF state of an existing
  SRDF pair and delete SRDF pair. All create and modify calls are asynchronous
  by default.
extends_documentation_fragment:
  - dellemc.dellemc_powermax
author:
- Manisha Agrawal (manisha.agrawal@dell.com)

options:
  sg_name:
    description:
    - Name of Storage Group. SRDF Pairings are managed at a storage group level.
    - Required to identify the SRDF link.
    type: string
    default: None
  serial_no:
    description:
    - The serial number will refer to the source (R1) PowerMax/VMAX array when
      protecting a storage group. However srdf_state operations may be issued
      from R1 or R2 array.  
    type: string
    default: None
  remote_serial_no:
    description:
    - Integer 12 Digit Serial Number of remote PowerMAX or VMAX array (R2).
    - Required while creating an SRDF link.
    type: string
    default: None
  rdfg_no:
    description:
    - The RDF group number.
    - Optional parameter for each call. For create, if specified, the array
      will reuse the RDF group, otherwise return error. For modify and delete
      operations, if the RFD group number is not specified, and the storage
      group is protected by multiple RDF Groups, then an error will be raised.
    type: number
    default: None
  state:
    description:
    - Define whether the SRDF pairing should exist or not.
    - present indicates that the SRDF pairing should exist in system.
    - absent indicates that the SRDF pairing should not exist in system.
    required: true
    choices: [absent, present]
  srdf_mode:
    description:
    - The replication mode of the SRDF pair.
    - Required when creating SRDF pair.
    - Can be modified by providing required value.
    choices: [Active, Adaptive Copy, Synchronous, Asynchronous]
    type: string
    default: None
  srdf_state:
    description:
    - Desired state of the SRDF pairing. While creating a new SRDF pair, allowed
      values are 'Establish' and 'Suspend'. If state is not specified, the pair
      will be created in 'Suspended' state. When modifying the state, only
      certain changes are allowed.
    choices: [Establish, Resume, Restore, Suspend, Swap, Split, Failback,
             Failover, Setbias]
  new_rdf_group:
    description:
    - Overrides the SRDF Group selection functionality and forces the creation
      of a new SRDF Group.
    default: false
    type: bool
  wait_for_completion:
    description:
    - Flag to indicate if the operation should be run synchronously or 
      asynchronously. True signifies synchronous execution. By default, all
      create and update operations will be run asynchronously.
    default: False
    type: bool
  job_id:
    description:
    - Job ID of an Asynchronous task. Can be used to get details of a job.
    default: None
    type: str
  witness:
    description:
    - Flag to specify use of Witness for a Metro configuration. Setting to True
      signifies to use Witness, setting it to False signifies to use Bias. It
      is recommended to configure a witness for SRDF Metro in a production
      environment, this is configured via Unipshere for PowerMAX UI or REST.
    - The flag can be set only for modifying srdf_state to either Establish,
      Suspend or Restore.
    - While creating a Metro configuration, witness flag must be set to True.
    default: None
    type: bool
  '''
  

EXAMPLES = r'''
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
'''

RETURN = r'''
changed: [localhost] => {
    "Job_details": {
        "completed_date_milliseconds": 0,
        "jobId": "1570622921504",
        "last_modified_date": "Oct-09-2019 08:08:41.505",
        "last_modified_date_milliseconds": 1570622921505,
        "name": "Protect Storage Group - SRDF Ansible_Test_SRDF2",
        "resourceLink": "https://xxx:8443/univmax/restapi/90/replication
                        /symmetrix/xx/storagegroup/x/rdf_group/x",
        "result": "Started job execution on Wed 9 Oct 2019 08:08:43 EDT",
        "status": "RUNNING",
        "task": [
            {
                "description": "SRDF protect Storage Group Ansible_Test_SRDF2
                to remote array xx, mode = Synchronous, establish = false,
                remote Storage Group = Ansible_Test_SRDF2",
                "execution_order": 1
            }
        ],
        "username": "C:xxx\\********"
    },
    "SRDF_link_details": {
        "hop2Modes": [],
        "hop2Rdfgs": [],
        "hop2States": [],
        "largerRdfSides": [
            "Equal"
        ],
        "localR1InvalidTracksHop1": 0,
        "localR2InvalidTracksHop1": 0,
        "modes": [
            "Asynchronous"
        ],
        "rdfGroupNumber": 25,
        "remoteR1InvalidTracksHop1": 0,
        "remoteR2InvalidTracksHop1": 0,
        "states": [
            "Consistent"
        ],
        "storageGroupName": "Ansible_Test_SRDF",
        "symmetrixId": "xxx",
        "totalTracks": 8205,
        "volumeRdfTypes": [
            "R1"
        ]
    },
    "changed": true,
    "invocation": {
        "module_args": {
            "wait_for_completion": true,
            "new_rdf_group": false,
            "job_id": null,
            "password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
            "rdfg_no": null,
            "remote_serial_no": "xx",
            "serial_no": "xx",
            "sg_name": "Ansible_Test_SRDF",
            "srdf_mode": "Asynchronous",
            "srdf_state": "Establish",
            "state": "present",
            "unispherehost": "xx",
            "universion": 90,
            "user": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER",
            "verifycert": false
        }
    }
}
'''
LOG = utils.get_logger(
    module_name='dellemc_powermax_srdf',
    log_devel=logging.INFO)

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.1'


class PowerMax_SRDF(object):

    '''Class with srdf operations'''

    def __init__(self):
        ''' Define all parameters required by this module'''
        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(self.get_powermax_srdf_pair_parameters())
        # initialize the ansible module
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False
        )
        # result is a dictionary that contains changed status, srdf_link
        # and job details
        self.result = {
            "changed": False,
            "SRDF_link_details": {},
            "Job_details": {}}
        if HAS_PYU4V is False:
            self.module.fail_json(msg="Ansible modules for PowerMax require "
                                      "the PyU4V python library to be "
                                      "installed. Please install the library "
                                      "before using these modules.")

        if PYU4V_VERSION_CHECK is not None:
            self.module.fail_json(msg=PYU4V_VERSION_CHECK)
            LOG.error(PYU4V_VERSION_CHECK)

        universion_details = utils.universion_check(
                             self.module.params['universion'])
        LOG.info("universion_details: {0}".format(universion_details))

        if not universion_details['is_valid_universion']:
            self.module.fail_json(msg=universion_details['user_message'])

        self.u4v_conn = utils.get_U4V_connection(
            self.module.params, application_type=APPLICATION_TYPE)
        self.replication = self.u4v_conn.replication
        LOG.info('Got PyU4V instance for replication on PowerMax ')
        self.idempotency_dict = {
            'Synchronized': ['Establish', 'Resume'],
            'Consistent': ['Establish', 'Resume'],
            'Suspended': ['Suspend', 'Failover'],
            'Failed Over': ['Suspend', 'Failover'],
            'SyncInProg': ['Establish', 'Resume'],
        }
        
        self.idempotency_dict_metro = {
            'Suspended': ['Suspend'],
            'SyncInProg': ['Establish'],
            'ActiveActive': ['Establish'],
            'ActiveBias': ['Establish']
        }

    def get_powermax_srdf_pair_parameters(self):
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
            srdf_mode=dict(required=False, type='str', choices=['Active',
                                                                'Adaptive Copy',
                                                                'Synchronous',
                                                                'Asynchronous']),
            rdfg_no=dict(type='int', required=False, default=None),
            wait_for_completion=dict(type='bool', required=False, default=False),
            new_rdf_group=dict(type='bool', required=False, default=False),
            witness=dict(type='bool', required=False, default=None),
            job_id=dict(type='str', required=False, default=None))

    def get_srdf_link(self, sg_name):
        '''
        Get details of a given srdf_link
        '''
        rdfg_number = self.module.params['rdfg_no']
        if not rdfg_number:
            rdfg_list = self.replication.get_storagegroup_srdfg_list(sg_name)
            if len(rdfg_list) == 0:
                error_msg = 'No RDF group exists for the given storage group'
                LOG.info(error_msg)
                return None
            elif len(rdfg_list) > 1:
                error_msg = ("Multiple RDF groups exists for the given storage"
                             " group. Please specify RDF number")
                LOG.error(error_msg)
                self.module.fail_json(msg=error_msg)
            else:
                rdfg_number = rdfg_list[0]

        try:
            # check for Concurrent/star configuration,
            if self.module.params['remote_serial_no']:
                remote_serial_no = self.module.params['remote_serial_no']
                try:
                    rdfg_details = self.replication.get_rdf_group(rdfg_number)
                    if rdfg_details['remoteSymmetrix'] != remote_serial_no:
                        error_msg = (
                            "Remote array for the RDF group number {0} does"
                            " not match with the given Remote array {1}. Please"
                            " specify RDF group you want to use. Also note, Ansible"
                            " modules v1.1 do not support Concurrent SRDF"
                            " configurations.".format(
                                rdfg_number, remote_serial_no))
                        LOG.error(error_msg)
                        self.module.fail_json(msg=error_msg)
                except Exception as e:
                    error_msg = (
                        "Got error {0} while getting RDF group details for "
                        "rdfg number {1}" .format(str(e), rdfg_number))
                    LOG.error(error_msg)
                    self.module.fail_json(msg=error_msg)

            LOG.info(
                "Getting srdf details for storage group {0} with rdfg number"
                "{1}".format(
                    sg_name, rdfg_number))
            srdf_linkFromGet = self.replication.get_storagegroup_srdf_details(
                storagegroup_id=sg_name, rdfg_num=rdfg_number)
            if srdf_linkFromGet:
                LOG.info('SRDF link details fetched are: {0}'.format(
                    srdf_linkFromGet))
                return srdf_linkFromGet
        except Exception as e:
            LOG.error(
                "Got error {0} while getting SRDF details for storage group "
                "{1} with rdfg number {2}" .format(
                    str(e), sg_name, rdfg_number))
            return None

    def create_srdf_link(self):
        '''
        Create srdf_link for given storagegroup_id group and remote array
        '''
        sg_name = self.module.params['sg_name']
        remote_serial_no = self.module.params['remote_serial_no']
        srdf_mode = self.module.params['srdf_mode']
        if (remote_serial_no is None or srdf_mode is None):
            error_msg = (
                "Mandatory parameters not found. Required parameters "
                "for creating an SRDF link are remote array serial number "
                "and SRDF mode")
            LOG.error(error_msg)
            self.module.fail_json(msg=error_msg)
        try:
            establish_flag = self._compute_required_establish_flag(
                self.module.params['srdf_state'])
            rdfg_number = self.module.params['rdfg_no']
            forceNewRdfGroup = self.module.params['new_rdf_group']
            async_flag = not(self.module.params['wait_for_completion'])
            witness = self.module.params['witness']
            
            if witness is False:
                errorMsg = ("Create SRDF link operation failed as Ansible"
                            " modules v1.1 does not allow creation of SRDF"
                            " links using Bias for resiliency.")
                LOG.error(errorMsg)
                self.module.fail_json(msg=errorMsg)

            msg = (
                "Creating srdf_link with parameters:sg_name={0}, "
                "remote_serial_no={1}, srdfmode={2}, establish_flag={3}, "
                "rdfgroup_no={4}, new_rdf_group={5}, async_flag={6}")
            LOG.info(
                msg.format(
                    sg_name,
                    remote_serial_no,
                    srdf_mode,
                    establish_flag,
                    rdfg_number,
                    forceNewRdfGroup,
                    async_flag))
            resp = self.replication.create_storagegroup_srdf_pairings(
                storagegroup_id=sg_name,
                remote_sid=remote_serial_no,
                srdfmode=srdf_mode,
                establish=establish_flag,
                forceNewRdfGroup=forceNewRdfGroup,
                rdfg_number=rdfg_number,
                _async=async_flag)
            LOG.info('Response from create SRDF link call {0}'.format(resp))
            if async_flag:
                self.result['Job_details'] = resp
                self.result['SRDF_link_details'] = None
            else:
                self.result['SRDF_link_details'] = resp
                self.result['Job_details'] = None
            return True

        except Exception as e:
            errorMsg = 'Create srdf_link for sg {0} failed with error {1}'.format(
                sg_name, str(e))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

    def _compute_required_establish_flag(self, srdf_state):
        if (srdf_state is None or srdf_state == 'Suspend'):
            return False
        elif srdf_state == 'Establish':
            return True
        else:
            errorMsg = (
                "Creation of SRDF link failed. Allowed states while "
                "creating SRDF link are only Establish or Suspend. Got {0}".format(srdf_state))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

    def modify_srdf_mode(self, srdf_mode):
        async_flag = not(self.module.params['wait_for_completion'])
        srdf_link = self.result['SRDF_link_details']
        if srdf_mode == 'Adaptive Copy':
            srdf_mode = 'AdaptiveCopyDisk'
        try:
            resp = self.replication.modify_storagegroup_srdf(
                storagegroup_id=srdf_link['storageGroupName'],
                rdfg=srdf_link['rdfGroupNumber'],
                action='SetMode',
                options={
                    'setMode': {
                        'mode': srdf_mode}},
                _async=async_flag)
            if async_flag:
                self.result['Job_details'] = resp
                self.result['SRDF_link_details'] = None
            else:
                self.result['SRDF_link_details'] = resp
                self.result['Job_details'] = None
            return True
        except Exception as e:
            errorMsg = ("Modifying SRDF mode of srdf_link from {0} to {1} for "
                        "SG {2} failed with error {3}".format(
                            srdf_link['modes'][0], srdf_mode,
                            srdf_link['storageGroupName'], str(e)))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

    def modify_srdf_state(self, action):
        modify_body = {}

        async_flag = not(self.module.params['wait_for_completion'])
        srdf_link = self.result['SRDF_link_details']

        modify_body['storagegroup_id'] = srdf_link['storageGroupName']
        modify_body['rdfg'] = srdf_link['rdfGroupNumber']
        modify_body['action'] = action
        modify_body['_async'] = async_flag

        if self.module.params['witness'] is not None:
            if srdf_link['modes'][0] != 'Active':
                errorMsg = ("witness flag can not be used for non-Metro "
                            "configurations.")
                LOG.error(errorMsg)
                self.module.fail_json(msg=errorMsg)
            elif action not in ['Establish', 'Restore', 'Suspend']:
                errorMsg = ("witness flag can be used only for 3 actions:"
                            " Establish, Restore and Suspend")
                LOG.error(errorMsg)
                self.module.fail_json(msg=errorMsg)
            else:
                modify_body['options'] = {
                    action.lower(): {
                        'metroBias': not(self.module.params['witness'])}}

        try:
            LOG.info('The modify_body is {0}:'.format(modify_body))
            resp = self.replication.modify_storagegroup_srdf(**modify_body)

            if async_flag:
                self.result['Job_details'] = resp
                self.result['SRDF_link_details'] = None
            else:
                self.result['SRDF_link_details'] = resp
                self.result['Job_details'] = None
            return True
        except Exception as e:
            errorMsg = ("Modifying SRDF state of srdf_link for storage group "
                        "{0} failed with error {1}".format(
                            srdf_link['storageGroupName'], str(e)))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

    def _check_for_SRDF_state_modification(self, new_operation):
        srdf_link = self.result['SRDF_link_details']
        current_state = srdf_link['states'][0]
        changed = False
        
        if (srdf_link['modes'][0] == 'Active' and 
            current_state in self.idempotency_dict_metro and
            new_operation in self.idempotency_dict_metro[current_state]
            ):
            LOG.info('Modification of SRDF state not required')
            changed = False
            
        elif (srdf_link['modes'][0] != 'Active' and 
              current_state in self.idempotency_dict and 
              new_operation in self.idempotency_dict[current_state]):
            LOG.info('Modification of SRDF state not required')
            changed = False
        else:
            LOG.info('Modifying SRDF state from {0} to {1}'.format(
                current_state, new_operation))

            changed = self.modify_srdf_state(new_operation)

        return changed

    def delete_srdf_link(self):
        '''
        Delete srdf_link from system
        '''
        srdf_link = self.result['SRDF_link_details']
        try:
            self.replication.delete_storagegroup_srdf(
                srdf_link['storageGroupName'], int(
                    srdf_link['rdfGroupNumber']))
            self.result['SRDF_link_details'] = {}
            return True
        except Exception as e:
            errorMsg = ('Delete srdf_link {0} failed with error {1}'.format(
                srdf_link['storageGroupName'], str(e)))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

    def get_job_details(self, job_id):
        try:
            self.result['Job_details'] = self.u4v_conn.common.get_job_by_id(
                job_id)
        except Exception as e:
            errorMsg = (
                'Get Job details for job_id {0} failed with error {1}'.format(
                    job_id, str(e)))
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

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

        if (job_id and sg_name) or (not job_id and not sg_name):
            errorMsg = 'Please specify either job ID or SG name in one Ansible task'
            LOG.error(errorMsg)
            self.module.fail_json(msg=errorMsg)

        if job_id:
            if state == 'present':
                LOG.info('Geting details of the Job {0}'.format(job_id))
                self.get_job_details(job_id)
            else:
                errorMsg = 'Set state=present for getting Job status'
                LOG.error(errorMsg)
                self.module.fail_json(msg=errorMsg)
        else:
            srdf_link = self.get_srdf_link(sg_name)
            self.result['SRDF_link_details'] = srdf_link
            if state == 'present' and not self.result['SRDF_link_details']:
                changed = self.create_srdf_link()

            elif state == 'present' and self.result['SRDF_link_details']:
                if (srdf_mode !=
                        self.result['SRDF_link_details']['modes'][0] and srdf_mode):
                    LOG.info('Modifying SRDF mode from {0} to {1}'.format(
                        self.result['SRDF_link_details']['modes'][0], srdf_mode))
                    changed = self.modify_srdf_mode(srdf_mode) or changed

                if srdf_state is not None:
                    changed = self._check_for_SRDF_state_modification(
                        srdf_state) or changed

            elif state == 'absent' and self.result['SRDF_link_details']:
                LOG.info('Deleting srdf_link with SG {0} '.format(sg_name))
                changed = self.delete_srdf_link() or changed

        # Update the module's final state
        LOG.info('changed {0}'.format(changed))
        self.result['changed'] = changed
        self.module.exit_json(**self.result)


def main():
    ''' Create PowerMax_srdf object and perform action on it
        based on user input from playbook'''
    obj = PowerMax_SRDF()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
