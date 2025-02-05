# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Job Api for Job Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockJobApi:
    JOB_COMMON_ARGS = {
        "job_id": "100000000"
    }

    @staticmethod
    def get_error_message(response_type, job_id=None):
        error_msg = {"invalid_job_id": f"Invalid job_id: {job_id}",
                     "get_job_by_id_exception": f"Get Job details for job_id {job_id} failed with error ",
                     "exit_exception": "Failed to close unisphere connection with error: SDK Error message",
                     "get_no_job_detail": f"Failed to find the job with specified job_id: {job_id}"}
        return error_msg[response_type]
