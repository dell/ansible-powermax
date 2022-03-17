#!/usr/bin/python
# Copyright: (c) 2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r"""
---
module: metrodr
version_added: '1.4.0'
short_description: Manage metro DR environment on PowerMax/VMAX Storage
                   System
description:
- Managing a metro DR environment on a PowerMax storage system includes
  getting details of any specific metro DR environment, creating a metro DR
  environment, converting an existing SG into a metro DR environment,
  modifying metro DR environment attributes and deleting a metro DR
  environment.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
  - dellemc.powermax.dellemc_powermax.powermax_serial_no
author:
- Vivek Soni (@v-soni11) <ansible.team@dell.com>
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

options:
  env_name:
    description:
    - Name of the metro DR environment.
    - Metro DR environment name will be unique across PowerMax.
    required: True
    type: str
  sg_name:
    description:
    - Name of the storage group.
    - Storage group will be present on the primary metro array and a storage
      group with the same name will be created on remote and DR arrays in a
      create operation.
    - Storage group name is required in 'create metro DR environment' and
      'convert SG into metro DR environment' operations.
    required: False
    type: str
  serial_no:
    description:
    - Serial number of the primary metro array.
    required: True
    type: str
  metro_serial_no:
    description:
      - Serial number of the remote metro array.
      - It is required only in create and convert operations.
    required: False
    type: str
  dr_serial_no:
    description:
      - Serial number of the DR array.
      - It is required in create and convert operations.
    required: False
    type: str
  replication_mode:
    description:
    - Replication mode whose value will indicate how the data will be
      replicated.
    - It is required in create and modify operations.
    - It is a mandatory parameter in a create operation but optional in
      a modify operation.
    required: False
    type: str
    choices: ["Asynchronous", "Adaptive Copy"]
  wait_for_completion:
    description:
    - The flag indicates if the operation should be run synchronously or
      asynchronously.
    - True signifies synchronous execution.
    - By default, create and convert are asynchronous operations, whereas
      modify is a synchronous operation.
    required: False
    type: bool
    default: False
  new_rdf_group_r1:
    description:
    - The flag indicates whether or not to create a new RDFG for a Metro R1
      array to a DR array, or to autoselect from an existing one.
    - Used in only create operation.
    required: False
    type: bool
    default: True
  new_rdf_group_r2:
    description:
    - The flag indicates whether or not to create a new RDFG for a Metro R2
      array to a DR array, or to autoselect from an existing one.
    - It is used only in create operation.
    required: False
    type: bool
    default: True
  remove_r1_dr_rdfg:
    description:
    - The flag indicates whether or not to override default behavior and
      delete R11-R2 RDFG from the metro R1 side.
    - It is used only in delete operations.
    required: False
    type: bool
    default: False
  srdf_param:
    description:
    - It contains parameters related to SRDF links.
    - It is used only in modify operations.
    required: False
    type: dict
    suboptions:
      srdf_state:
        description:
        - State of the SRDF link.
        - It is a mandatory parameter for modify operations.
        required: True
        type: str
        choices: ["Split", "Restore", "SetMode", "Failback", "Failover",
                  "Establish", "Suspend", "UpdateR1", "Recover"]
      metro:
        description:
        - The flag indicates whether or not to direct srdf_state change
          towards the R1--R2 Metro Device leg of the metro DR environment.
        required: False
        type: bool
        default: False
      dr:
        description:
        - The flag indicates whether or not to direct srdf_state change
          towards device pairs on the disaster recovery leg of the metro DR
          environment.
        required: False
        type: bool
        default: False
      keep_r2:
        description:
        - The flag indicates whether or not in the case of srdf state suspend
          to make R2 data on metro available to the host.
        required: False
        type: bool
        default: False
  state:
    description:
    - State variable to determine whether metro DR environment will exist or
      not.
    required: True
    type: str
    choices: ['absent', 'present']
"""

EXAMPLES = r"""
- name: Get metro environment details
  dellemc.powermax.metrodr:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    env_name: "ansible_metrodr_env"
    state: "present"

- name: Convert SG to metro DR environment
  dellemc.powermax.metrodr:
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
  dellemc.powermax.metrodr:
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
  dellemc.powermax.metrodr:
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
  dellemc.powermax.metrodr:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    serial_no: "{{serial_no}}"
    env_name: "ansible_metrodr_env"
    remove_r1_dr_rdfg: True
    state: 'absent'
"""

RETURN = r"""
changed:
    description: Whether or not the resource has changed.
    returned: always
    type: bool
Job_details:
    description: Details of the job.
    returned: When job exist.
    type: dict
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
metrodr_env_details:
    description: Details of the metro DR environment link.
    returned: When environment exists.
    type: dict
    contains:
        capacity_gb:
            description: Size of volume in GB.
            type: float
        dr_exempt:
            description: Flag to indication that if there are exempt devices
                         (volumes) in the DR site or not.
            type: bool
        dr_link_state:
            description: Status of DR site.
            type: str
        dr_percent_complete:
            description: Percentage synchronized in DR session.
            type: int
        dr_rdf_mode:
            description: Replication mode with DR site.
            type: str
        dr_remain_capacity_to_copy_mb:
            description: Remaining capacity to copy at DR site.
            type: int
        dr_service_state:
            description: The HA state of the DR session.
            type: str
        dr_state:
            description: The pair states of the DR session.
            type: str
        environment_exempt:
            description: Flag to indication that if there are exempt devices
                         (volumes) in the environment or not.
            type: bool
        environment_state:
            description: The state of the smart DR environment.
            type: str
        metro_exempt:
            description: Flag to indication that if there are exempt devices
                         (volumes) in the DR site or not.
            type: bool
        metro_link_state:
            description: Status of metro site.
            type: str
        metro_r1_array_health:
            description: Health status of metro R1 array.
            type: str
        metro_r2_array_health:
            description: Health status of metro R1 array.
            type: str
        metro_service_state:
            description: The HA state of the metro session.
            type: str
        metro_state:
            description: The pair states of the metro session.
            type: str
        metro_witness_state:
            description: The witness state of the metro session.
            type: str
        name:
            description: The smart DR environment name.
            type: str
        valid:
            description: Flag to indicate whether valid environment or not.
            type: bool
"""

from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger(module_name="metro")

HAS_PYU4V = utils.has_pyu4v_sdk()
PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'

# DO NOT CHANGE BELOW REPLICATION_MODES SEQUENCE AS ITS USED IN SCRIPT
# USING INDEX
REPLICATION_MODES = ["Asynchronous", "Adaptive Copy"]

# ADAPTIVE_COPY_DISK used in SDK
ADAPTIVE_COPY_DISK = "AdaptiveCopyDisk"

# DO NOT CHANGE BELOW SRDF_STATES SEQUENCE AS ITS USED IN SCRIPT USING INDEX
SRDF_STATES = ["Split", "Restore", "SetMode", "Failback", "Failover",
               "Establish", "Suspend", "UpdateR1", "Recover"]

# State idempotency mapping
# keys are actual string received from powermax api response
# values are list of strings provided as input from playbook
IDEMPOTENCY_STATES = {
    "Synchronized": ["Establish", "Restore"],
    "Consistent": ["Establish", "Restore"],
    "Suspended": ["Suspend"],
    "Failed Over": ["Failover", "Split"],
    "SyncInProg": ["Establish"],
    "ActiveActive": ["Establish", "Restore"],
    "ActiveBias": ["Establish", "Restore"],
    "Split": ["Split"],
    "R1 Updated": ["UpdateR1"]
}


class MetroDR(object):

    def __init__(self):
        """ Initialises attributes required for metro DR environment
        operations """

        self.module_params = utils.get_powermax_management_host_parameters()
        self.module_params.update(get_metrodr_parameters())

        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=True)

        if HAS_PYU4V is False:
            msg = "Ansible modules for PowerMax require the PyU4V python " \
                  "library to be installed. Please install the library " \
                  "before using these modules"
            self.show_error_exit(msg, close_conn=False)

        if PYU4V_VERSION_CHECK is not None:
            self.show_error_exit(PYU4V_VERSION_CHECK, close_conn=False)

        self.pre_check_for_PyU4V_version()

        if self.module.params["universion"] is not None:
            universion_details = utils.universion_check(
                self.module.params["universion"])
            LOG.info("universion_details: %s", universion_details)

            if not universion_details["is_valid_universion"]:
                self.show_error_exit(
                    universion_details["user_message"], close_conn=False)

        try:
            self.conn = utils.get_U4V_connection(
                self.module.params, application_type=APPLICATION_TYPE)
            self.metro = self.conn.metro_dr
            self.provisioning = self.conn.provisioning
            self.replication = self.conn.replication
        except Exception as e:
            self.show_error_exit(str(e))
        LOG.info('Check Mode flag is %s', self.module.check_mode)
        LOG.info("Got PyU4V instance for metro DR on PowerMax")

    def pre_check_for_PyU4V_version(self):
        """ Performs pre-check for PyU4V version"""
        curr_version = utils.PyU4V.__version__
        supp_version = "9.2"
        is_supported_version = utils.pkg_resources.parse_version(
            curr_version) >= utils.pkg_resources.parse_version(supp_version)

        if not is_supported_version:
            msg = "This functionality is not supported by PyU4V version " \
                  "{0}".format(curr_version)
            self.show_error_exit(msg, close_conn=False)

    def close_connection(self):
        try:
            LOG.info("Closing unisphere connection %s", self.conn)
            utils.close_connection(self.conn)
            LOG.info("Connection closed successfully")
        except Exception as e:
            err_msg = ("Failed to close unisphere connection with error:"
                       " %s", str(e))
            LOG.error(err_msg)

    def show_error_exit(self, msg, close_conn=True):
        """ Log error message, closes the connection object and exit program

        :param msg: Error message to be displayed
        :type msg: str
        :param close_conn: Indicated whether to close connection or not
        :type close_conn: bool
        """
        if close_conn:
            self.close_connection()
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def get_metrodr_env(self):
        """ Get the details of metro DR environment

        :return: Metro DR environment details if exists or None
        :rtype: dict or None
        """
        try:
            LOG.info("Getting metro DR environment details for: %s",
                     self.module.params['env_name'])
            metrodr_env_details = self.metro.get_metrodr_environment_details(
                self.module.params['env_name'])

            LOG.info("Successfully got metro DR environment details")
            return metrodr_env_details
        except utils.ResourceNotFoundException as e:
            error_message = "Failed to get details of environment " \
                            "{0} with error {1}" \
                .format(self.module.params['env_name'], str(e))
            LOG.error(error_message)
            return None
        except Exception as e:
            self.show_error_exit(
                "Failed to get metro DR environment error: %s" % str(e))

    def pre_checks_for_create(self):
        """ Performs prechecks required for convert SG to metro DR
        environment """
        LOG.info("Prechecking for create metro DR environment")

        for k in ("metro_serial_no", "dr_serial_no", "replication_mode"):
            if not self.module.params[k]:
                self.show_error_exit("Please provide value for: '%s' for "
                                     "creating metro DR environment" % k)
        LOG.info("Successfully prechecked for create metro DR environment")

    def create_metrodr_env(self):
        """ Create metro DR environment

        :return: Job details & metro DR environment details
                 Job details - if operation is ASYNC else None -- dict
                 metrodr environment details - if operation is SYNC
                                               else None -- dict
        :rtype: tuple containing dictionaries
        """
        try:
            self.pre_checks_for_create()
            param = {
                "storage_group_name": self.module.params["sg_name"],
                "environment_name": self.module.params["env_name"],
                "metro_r1_array_id": self.module.params["serial_no"],
                "metro_r2_array_id": self.module.params["metro_serial_no"],
                "dr_array_id": self.module.params["dr_serial_no"],
                "dr_replication_mode": self.module.params["replication_mode"],
                "force_new_metro_r1_dr_rdfg": self.module.params[
                    "new_rdf_group_r1"],
                "force_new_metro_r2_dr_rdfg": self.module.params[
                    "new_rdf_group_r2"],
                "_async": not self.module.params['wait_for_completion']
            }
            resp = {}
            if param["dr_replication_mode"] == REPLICATION_MODES[1]:
                param["dr_replication_mode"] = ADAPTIVE_COPY_DISK
            LOG.info("Creating metro DR environment: %s param: %s",
                     self.module.params['env_name'], param)
            if not self.module.check_mode:
                resp = self.metro.create_metrodr_environment(**param)
            LOG.info("Successfully created metro DR environment")
            if param["_async"]:
                return resp, None
            return None, resp
        except Exception as e:
            self.show_error_exit(
                "Failed to create metro DR environment error: %s" % str(e))

    def get_storage_group_details(self):
        """ Provides details of given storage group

        :return: Storage group details
        :rtype: dict
        """
        try:
            if self.module.params['sg_name']:
                LOG.info("Getting storage group details")
                sg_details = self.provisioning.get_storage_group(
                    self.module.params['sg_name'])
                LOG.info("Successfully got storage group details")
                return sg_details
            else:
                LOG.info("No SG given or associated with the environment")
                return None
        except Exception as e:
            self.show_error_exit(
                "Failed to get storage group details error: %s" % str(e))

    def get_storage_group_srdf_group_list(self):
        """ Provides list of SRDF group associated with given storage group

        :return: SRDF group list
        :rtype: list
        """
        try:
            LOG.info("Getting SRDF group list")
            srdf_gr_list = self.replication.get_storage_group_srdf_group_list(
                self.module.params['sg_name'])
            LOG.info("Successfully got SRDf group list")
            return srdf_gr_list
        except Exception as e:
            self.show_error_exit(
                "Failed to get SRDF group list error: %s" % str(e))

    def get_storage_group_srdf_details(self, srdf_gr):
        """ Provides details of given SRDF group number

        :param srdf_gr: SRDF group number
        :type srdf_gr: int
        :return: SRDF group details
        :rtype: dict
        """
        try:
            LOG.info("Getting SRDF details for: %s", srdf_gr)
            srdf_detail = self.replication.get_storage_group_srdf_details(
                self.module.params['sg_name'], srdf_gr)
            LOG.info("Successfully got SRDF details")
            return srdf_detail
        except Exception as e:
            self.show_error_exit(
                "Failed to get SRDF details error: %s" % str(e))

    def get_rdf_group(self, gr):
        """ Provides details of given RDF group

        :param gr: RDF group number
        :type gr: int
        :return: SRDF group details
        :rtype: dict
        """
        try:
            LOG.info("Getting RDF group details for: %s", gr)
            rdf_group_details = self.replication.get_rdf_group(gr)
            LOG.info("Successfully got RDF group details")
            return rdf_group_details
        except Exception as e:
            self.show_error_exit(
                "Failed to get RDF group details error: %s" % str(e))

    def pre_checks_for_convert(self):
        """ Performs prechecks required for convert SG to metro DR
        environment """
        LOG.info("Prechecking for converting SG to metro DR environment")

        # pre-checks:
        # 1) The target SG is protected with SRDF/Metro and has an
        # Asynchronous SRDF session or Adaptive Copy Disk session
        # 2) The existing Async or ACP_Disk session must be from the R1
        # array (Concurrent)
        # 3) The Metro Session must be configured using a witness
        # 4) User role must be at least StorageAdmin or RemoteRep

        # precheck: 1 - SG should protected with srdf
        srdf_gr_list = self.get_storage_group_srdf_group_list()
        if not srdf_gr_list:
            self.show_error_exit(
                "SG: %s does not have srdf group" % self.module.params[
                    'sg_name'])

        is_srdf_adp_or_asyn = False
        is_srdf_active = False
        req_metro_states = ["Active", "SyncInProg", "Suspended"]
        for srdf_gr in srdf_gr_list:
            if is_srdf_adp_or_asyn and is_srdf_active:
                LOG.info("SRDF links satisfy condition of convert")
                break
            srdf_detail = self.get_storage_group_srdf_details(srdf_gr)
            # precheck: 2
            if "Adaptive Copy" in srdf_detail['modes'] or "Asynchronous" in\
                    srdf_detail['modes']:
                LOG.info("SRDF mode is asynchronous/adaptive_copy")
                if self.module.params["dr_serial_no"]:
                    LOG.info("Validating given dr_serial_no")
                    if self.get_rdf_group(srdf_gr)["remoteSymmetrix"] \
                            == self.module.params["dr_serial_no"]:
                        LOG.info("Given dr_serial_no matches with rdfg")
                        is_srdf_adp_or_asyn = True
                    else:
                        LOG.info("Given dr_serial_no not matches with rdfg")
                else:
                    is_srdf_adp_or_asyn = True
            # precheck: 3
            elif "Active" in srdf_detail['modes'] and \
                    not (set(req_metro_states) & set(srdf_detail['states'])):
                LOG.info("SRDF metro mode is active")
                if self.module.params["metro_serial_no"]:
                    LOG.info("Validating given metro_serial_no")
                    if self.get_rdf_group(srdf_gr)["remoteSymmetrix"] \
                            == self.module.params["metro_serial_no"]:
                        LOG.info("Given metro_serial_no matches with rdfg")
                        is_srdf_active = True
                    else:
                        LOG.info("Given metro_serial_no not matches with "
                                 "rdfg")
                else:
                    is_srdf_active = True

        if is_srdf_adp_or_asyn is False or is_srdf_active is False:
            self.show_error_exit("Pre-check for convert not satisfied. "
                                 "Asynchronous or AC SRDF_link found: %s "
                                 "Active metro_link found: %s, "
                                 "both should be True."
                                 % (is_srdf_adp_or_asyn, is_srdf_active))

        LOG.info("Successfully prechecked for converting SG to metro DR"
                 " environment")

    def convert_to_metrodr_env(self):
        """ Convert given SG to metro DR environment

        :return: Job details & metro DR environment details
                 Job details - if operation is ASYNC else None -- dict
                 metrodr environment details - if operation is SYNC
                                               else None -- dict
        :rtype: tuple containing dictionaries
        """
        try:
            self.pre_checks_for_convert()
            resp = {}
            param = {
                "storage_group_name": self.module.params['sg_name'],
                "environment_name": self.module.params['env_name'],
                "_async": not self.module.params['wait_for_completion']
            }
            LOG.info("Converting SG: %s to metro DR environment: %s with "
                     "param: %s",
                     self.module.params['sg_name'],
                     self.module.params['env_name'], param)
            if not self.module.check_mode:
                resp = self.metro.convert_to_metrodr_environment(**param)
            LOG.info("Successfully converted to metro DR environment")
            if param["_async"]:
                return resp, None
            return None, resp
        except Exception as e:
            self.show_error_exit(
                "Failed to convert SG to metro DR environment error: %s"
                % str(e))

    def pre_checks_for_modify(self):
        """ Performs prechecks required for modifying metro DR environment """
        # Pre-check 1: replication_mode should be given only incase of
        # srdf_state is 'SetMode'
        if self.module.params['replication_mode'] and self.module.params[
           'srdf_param']['srdf_state'] != SRDF_STATES[2]:  # SetMode
            self.show_error_exit(
                "replication_mode required only with srdf_state 'SetMode'")

        # Pre-check 2: keep_r2 to be True only with srdf state suspend
        if self.module.params['srdf_param']['keep_r2']:
            if self.module.params['srdf_param']['srdf_state'] \
                    != SRDF_STATES[6]:  # Suspend
                self.show_error_exit(
                    "keep_r2 can be True only with srdf_state 'Suspend'")

    def get_modify_dict(self, metrodr_env_details):
        """ Provides the parameters to be modified based on comparison

        :param metrodr_env_details: Metro DR environment details
        :type metrodr_env_details: dict
        :return: Parameters to be modified, which are aligned with SDK
        :rtype: dict
        """
        modify_dict = {}

        LOG.info("Fetching modify_dict")
        # comparing replication_mode
        if self.module.params["replication_mode"]:
            if self.module.params["replication_mode"] != \
                    metrodr_env_details["dr_rdf_mode"]:
                if self.module.params["replication_mode"] == \
                        REPLICATION_MODES[1]:
                    modify_dict["dr_replication_mode"] = ADAPTIVE_COPY_DISK
                else:
                    modify_dict["dr_replication_mode"] = \
                        self.module.params["replication_mode"]
            else:
                LOG.info("Replication mode is already: %s",
                         self.module.params['replication_mode'])

        # comparing srdf_state
        if self.module.params["srdf_param"]["srdf_state"]:  # mandatory param
            # dr-true, metro-true
            if self.module.params["srdf_param"]["metro"] \
                    and self.module.params["srdf_param"]["dr"]:
                # Idempotency check for 'Establish', 'Suspend' and 'Recover'
                # states
                if ((self.module.params["srdf_param"]["srdf_state"] in
                        IDEMPOTENCY_STATES[
                            metrodr_env_details["dr_state"]])
                    and (self.module.params["srdf_param"]["srdf_state"] in
                         IDEMPOTENCY_STATES[
                             metrodr_env_details["metro_state"]])):
                    LOG.info("Given srdf_state is already maintained by "
                             "DR and Metro arrays")
                else:
                    modify_dict["action"] = \
                        self.module.params["srdf_param"]["srdf_state"]
            # dr-false, metro-false --> No change in states
            elif not self.module.params["srdf_param"]["metro"] \
                    and not self.module.params["srdf_param"]["dr"]:
                LOG.info("Given srdf_state is already maintained by "
                         "DR and Metro arrays")
            elif self.module.params["srdf_param"]["metro"]:
                if metrodr_env_details["metro_state"] in IDEMPOTENCY_STATES:
                    if self.module.params["srdf_param"]["srdf_state"] in \
                            IDEMPOTENCY_STATES[
                                metrodr_env_details["metro_state"]]:
                        LOG.info("Given srdf_state is already maintained by "
                                 "Metro array")
                    else:
                        modify_dict["action"] = \
                            self.module.params["srdf_param"]["srdf_state"]
                else:
                    self.show_error_exit(
                        "Mapping of %s to invalid state"
                        % metrodr_env_details["metro_state"])
            elif self.module.params["srdf_param"]["dr"]:
                if metrodr_env_details["dr_state"] in IDEMPOTENCY_STATES:
                    if self.module.params["srdf_param"]["srdf_state"] in \
                            IDEMPOTENCY_STATES[
                                metrodr_env_details["dr_state"]]:
                        LOG.info("Given srdf_state is already maintained by "
                                 "DR array")
                    else:
                        modify_dict["action"] = \
                            self.module.params["srdf_param"]["srdf_state"]
                else:
                    self.show_error_exit(
                        "Mapping of %s to invalid state"
                        % metrodr_env_details["metro_state"])

        LOG.info("Successfully fetched modify_dict: %s", modify_dict)
        return modify_dict

    def modify_metrodr_env(self, metrodr_env_details):
        """ Convert given SG to metro DR environment

        :param metrodr_env_details: Metro DR environment details
        :type metrodr_env_details: dict
        :return: Changed, job details & metro DR environment details
                 Changed - True if environment is modified else False -- bool
                 Job details - if operation is ASYNC else None -- dict
                 metrodr environment details - if operation is SYNC
                                               else None -- dict
        :rtype: tuple containing 3 elements in order: bool, {}, {}
        """
        if not self.module.params["srdf_param"] \
                or not self.module.params["srdf_param"]["srdf_state"]:
            LOG.info("Modify not required, as its GET operation")
            return False, None, metrodr_env_details

        self.pre_checks_for_modify()

        modify_dict = self.get_modify_dict(metrodr_env_details)
        if not modify_dict:
            LOG.info("Nothing to modify, its idempotency case")
            return False, None, metrodr_env_details

        modify_dict["metro"] = self.module.params["srdf_param"]["metro"]
        modify_dict["dr"] = self.module.params["srdf_param"]["dr"]
        modify_dict["keep_r2"] = self.module.params["srdf_param"]["keep_r2"]
        modify_dict["_async"] = self.module.params["wait_for_completion"]

        try:
            # State changes that require 'force' flag enabled explicitly.

            # 'Suspend-Split' for 'dr' with 'force' flag when
            # replication_mode is 'Adaptive Copy'
            if metrodr_env_details["dr_rdf_mode"] == "Adaptive Copy" \
                    and metrodr_env_details["dr_state"] == "Suspended" \
                    and modify_dict["dr"] \
                    and modify_dict["action"] == "Split":
                modify_dict["force"] = True

            # 'Establish-Failover' for 'dr' with 'force' flag when
            # replication_mode is 'Adaptive Copy'
            if metrodr_env_details["dr_rdf_mode"] == "Adaptive Copy" \
                    and metrodr_env_details["dr_state"] == "Synchronized" \
                    and modify_dict["dr"] \
                    and modify_dict["action"] == "Failover":
                modify_dict["force"] = True

            # 'Establish-Split' for 'dr' with 'force' flag when
            # replication_mode is 'Adaptive Copy'
            if metrodr_env_details["dr_rdf_mode"] == "Adaptive Copy" \
                    and metrodr_env_details["dr_state"] == "Synchronized" \
                    and modify_dict["dr"] \
                    and modify_dict["action"] == "Split":
                modify_dict["force"] = True

            # 'Suspend-Failover' for 'dr' with 'force' flag when
            # replication_mode is 'Adaptive Copy'
            if metrodr_env_details["dr_rdf_mode"] == "Adaptive Copy" \
                    and metrodr_env_details["dr_state"] == "Suspended" \
                    and modify_dict["dr"] \
                    and modify_dict["action"] == "Failover":
                modify_dict["force"] = True

            # 'Split-Failover' for 'dr' with 'force' flag
            if metrodr_env_details["dr_state"] == "Split" \
                    and modify_dict["dr"] \
                    and modify_dict["action"] == "Failover":
                modify_dict["force"] = True

            # 'Split-Restore' for 'dr' with 'force' flag
            if metrodr_env_details["dr_state"] == "Split" \
                    and modify_dict["dr"] \
                    and modify_dict["action"] == "Restore":
                modify_dict["force"] = True

            # Idempotency check for 'SetMode'
            if (modify_dict["action"] == "SetMode"
                    and self.module.params['replication_mode']
                    == metrodr_env_details["dr_rdf_mode"]):
                LOG.info(
                    "Given replication_mode is already maintained by "
                    "DR array")
                return False, None, self.get_metrodr_env()

            LOG.info("Modifying metro DR environment with param: %s",
                     modify_dict)
            resp = metrodr_env_details
            if not self.module.check_mode:
                resp = self.metro.modify_metrodr_environment(
                    self.module.params['env_name'],
                    **modify_dict)
            LOG.info("Successfully modified metro DR environment")

            if self.module.params["wait_for_completion"]:
                return True, resp, None
            return True, None, self.get_metrodr_env()
        except Exception as e:
            if isinstance(e, utils.PyU4V.utils.exception.PyU4VException) and \
                    "No recovery of the metro DR environment is required" \
                    in str(e):
                LOG.info("No recovery of the metro DR environment is required")
                return False, None, self.get_metrodr_env()

            self.show_error_exit(
                "Failed to modify metro DR environment error: %s" % str(e))

    def delete_metrodr_env(self):
        """ Delete given metro DR environment """
        try:
            LOG.info("Deleting metro DR environment: %s",
                     self.module.params['env_name'])
            if not self.module.check_mode:
                self.metro.delete_metrodr_environment(
                    self.module.params['env_name'],
                    self.module.params['remove_r1_dr_rdfg'])
            LOG.info("Successfully deleted metro DR environment")
        except Exception as e:
            self.show_error_exit(
                "Failed to delete metro DR environment error: %s" % str(e))

    def convert_or_create(self):
        """ Based on given storage group it calls either create_metrodr_env()
            or convert_to_metrodr_env()

        :return: Changed, job details & metro DR environment details
                 Changed - True -- bool
                 Job details - if operation is ASYNC else None -- dict
                 metrodr environment details - if operation is SYNC
                                               else None -- dict
        :rtype: tuple containing 3 elements in order: bool, {}, {}
        """
        # Before making call to create or convert, checking if SG exists
        # or not
        sg_detail = self.get_storage_group_details()
        if sg_detail:
            if sg_detail["unprotected"]:
                LOG.info("Given sg in unprotected, so creating a metro DR "
                         "environment")
                job_details, metrodr_env_details = self.create_metrodr_env()
            else:
                LOG.info("Given sg is protected, so converting a metro DR "
                         "environment")
                # Given storage is protected, so it is a convert call
                job_details, metrodr_env_details \
                    = self.convert_to_metrodr_env()
            return True, job_details, metrodr_env_details
        else:
            return False, None, None

    def perform_module_operation(self):
        """ Perform metro DR environment operation based on playbook task """

        # Get metro DR environment
        result = {'changed': False,
                  'metrodr_env_details': self.get_metrodr_env(),
                  'Job_details': None}

        if self.module.params['state'] == "present":
            if not result['metrodr_env_details']:
                # Create or convert metro DR environment
                result['changed'], result['Job_details'], result[
                    'metrodr_env_details'] = self.convert_or_create()
            elif result['metrodr_env_details']:
                # Modify metro DR environment
                result['changed'], result['Job_details'], result[
                    'metrodr_env_details'] = self.modify_metrodr_env(
                    result['metrodr_env_details'])
        elif self.module.params['state'] == "absent":
            if result['metrodr_env_details']:
                # Delete metro DR environment
                self.delete_metrodr_env()
                result['metrodr_env_details'], result['changed'] = None, True

        self.close_connection()
        self.module.exit_json(**result)


def get_metrodr_parameters():
    return dict(
        env_name=dict(required=True, type='str'),
        sg_name=dict(required=False, type='str'),
        serial_no=dict(required=True, type='str'),
        metro_serial_no=dict(required=False, type='str'),
        dr_serial_no=dict(required=False, type='str'),
        replication_mode=dict(required=False, type='str',
                              choices=REPLICATION_MODES),
        wait_for_completion=dict(type='bool', required=False, default=False),
        new_rdf_group_r1=dict(type='bool', required=False, default=True),
        new_rdf_group_r2=dict(type='bool', required=False, default=True),
        remove_r1_dr_rdfg=dict(type='bool', required=False, default=False),
        srdf_param=dict(type='dict', required=False, options=dict(
            srdf_state=dict(required=True, type='str', choices=SRDF_STATES),
            metro=dict(type='bool', required=False, default=False),
            dr=dict(type='bool', required=False, default=False),
            keep_r2=dict(type='bool', required=False, default=False),)),
        state=dict(required=True, type='str', choices=['present', 'absent']))


def main():
    """ Create PowerMaxMetroDR object and perform action on it
        based on user input from playbook """
    obj = MetroDR()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
