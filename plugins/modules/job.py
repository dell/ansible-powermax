#!/usr/bin/python
# Copyright: (c) 2021, DellEMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: job
version_added: '1.4.0'
short_description: Gets the detail information about a Job of a PowerMax/VMAX
 storage system
description:
- Gets details of a Job from a specified PowerMax/VMAX storage system.
- The details listed are of an asynchronous task.
extends_documentation_fragment:
  - dellemc.powermax.dellemc_powermax.powermax
author:
- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>
options:
  job_id:
    description:
    - Job ID of an asynchronous task, used for getting details of a job.
    required: true
    type: str
'''

EXAMPLES = r'''
- name: Get the details of a Job.
  dellemc.powermax.job:
    unispherehost: "{{unispherehost}}"
    universion: "{{universion}}"
    verifycert: "{{verifycert}}"
    user: "{{user}}"
    password: "{{password}}"
    job_id: "1570622921504"
'''

RETURN = r'''
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
'''

import logging
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import dellemc_ansible_powermax_utils as utils
from ansible.module_utils.basic import AnsibleModule

LOG = utils.get_logger('job')

HAS_PYU4V = utils.has_pyu4v_sdk()

PYU4V_VERSION_CHECK = utils.pyu4v_version_check()

# Application Type
APPLICATION_TYPE = 'ansible_v1.7.0'


class Job(object):
    """Class with Job operations"""

    u4v_conn = None

    def __init__(self):
        """Define all the parameters required by this module"""

        self.module_params = utils.get_u4v_unisphere_connection_parameters()
        self.module_params.update(get_job_parameters())
        self.module = AnsibleModule(
            argument_spec=self.module_params,
            supports_check_mode=False)

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
            self.u4v_conn = utils.get_u4v_unisphere_connection(
                self.module.params, APPLICATION_TYPE)
            self.common = self.u4v_conn.common
            LOG.info("Got PyU4V Unisphere instance for common lib method "
                     "access on Powermax")
        except Exception as e:
            self.show_error_exit(msg=str(e))

    def get_job_details(self, job_id):
        """Get the Job details for a job from a given PowerMax/Vmax storage
        system

        :param job_id: Job ID
        :type job_id: str
        :return: Job ID details
        :rtype: dict
        """
        try:
            LOG.info('Getting Job Details for job_id %s ', job_id)
            job_details = self.common.get_job_by_id(job_id)
            if job_details:
                LOG.info('Successfully listed Job Details for job_id %s',
                         job_id)
                return job_details
            else:
                errorMsg = 'Failed to find the job with specified job_id: %s'\
                           % job_id
                self.show_error_exit(msg=errorMsg)
        except Exception as e:
            errorMsg = 'Get Job details for job_id %s failed with error %s' \
                       % (job_id, str(e))
            self.show_error_exit(msg=errorMsg)

    def show_error_exit(self, msg):
        if self.u4v_conn is not None:
            try:
                LOG.info("Closing unisphere connection %s", self.u4v_conn)
                utils.close_connection(self.u4v_conn)
                LOG.info("Connection closed successfully")
            except Exception as e:
                err_msg = ("Failed to close unisphere connection with error:"
                           " %s", str(e))
                LOG.error(err_msg)
        LOG.error(msg)
        self.module.fail_json(msg=msg)

    def perform_module_operation(self):

        job_id = self.module.params['job_id']
        if job_id and job_id.isdigit():
            job_details = self.get_job_details(job_id)
        else:
            errorMsg = 'Invalid job_id: %s' % job_id
            self.show_error_exit(msg=errorMsg)

        LOG.info("Closing unisphere connection %s", self.u4v_conn)
        utils.close_connection(self.u4v_conn)
        LOG.info("Connection closed successfully")

        self.module.exit_json(
            changed=False,
            Job_details=job_details
        )


def get_job_parameters():
    """This method provides the parameters required for the ansible job module
    of PowerMax. """
    return dict(
        job_id=dict(type='str', required=True)
    )


def main():
    """ Create PowerMax Job object and perform action on it
        based on user input from playbook """
    obj = Job()
    obj.perform_module_operation()


if __name__ == '__main__':
    main()
