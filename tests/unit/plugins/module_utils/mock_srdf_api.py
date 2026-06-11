# Copyright: (c) 2024-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock SRDF Api for SRDF Test module on PowerMax
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockSRDFApi:
    SRDF_COMMON_ARGS = {
        "sg_name": "test_sg",
        "remote_serial_no": "000297900330",
        "state": "present",
        "srdf_state": "Establish",
        "srdf_mode": "Synchronous",
        "rdfg_no": 1,
        "wait_for_completion": False,
        "witness": True,
        "job_id": None,
        "rdf_target_sg_name": None,
    }

    SRDF_LINK_DETAILS = {
        "storageGroupName": "test_sg",
        "symmetrixId": "000197600156",
        "rdfGroupNumber": 1,
        "modes": ["Synchronous"],
        "states": ["Synchronized"],
        "remoteSymmetrix": "000297900330",
        "totalTracks": 1000,
        "volumeRdfTypes": ["R1"],
    }

    SRDF_LINK_DETAILS_LIST = [SRDF_LINK_DETAILS]

    RDF_GROUP_DETAILS = {
        "rdfgNumber": 1,
        "remoteSymmetrix": "000297900330",
        "label": "test_rdfg",
        "numDevices": 5,
        "modes": ["Synchronous"],
        "states": ["Synchronized"],
    }

    JOB_DETAILS = {
        "jobId": "12345",
        "status": "SUCCEEDED",
        "result": "created",
        "resourceLink": "/resource/link",
        "task": [{"description": "SRDF protect Storage Group test_sg"}],
    }

    REPLICATION_DETAILS_WITH_REMOTE_SGS = {
        "storageGroupName": "test_sg",
        "rdf_groups": [{"rdfGroupNumber": 1}],
        "remote_storage_groups": [
            {
                "rdfGroupNumber": 1,
                "remoteStorageGroupName": "DR_test_sg",
                "remoteSymmetrixId": "000297900330",
            }
        ],
    }

    REPLICATION_DETAILS_MULTI_RDFG = {
        "storageGroupName": "test_sg",
        "rdf_groups": [{"rdfGroupNumber": 1}, {"rdfGroupNumber": 2}],
        "remote_storage_groups": [
            {
                "rdfGroupNumber": 1,
                "remoteStorageGroupName": "DR_test_sg_1",
                "remoteSymmetrixId": "000297900330",
            },
            {
                "rdfGroupNumber": 2,
                "remoteStorageGroupName": "DR_test_sg_2",
                "remoteSymmetrixId": "000297900331",
            },
        ],
    }

    REPLICATION_DETAILS_EMPTY_REMOTE_SGS = {
        "storageGroupName": "test_sg",
        "rdf_groups": [{"rdfGroupNumber": 1}],
        "remote_storage_groups": [],
    }

    @staticmethod
    def get_error_message(response_type, sg_name=None):
        error_msg = {
            "create_srdf_exception": f"Create srdf_link for sg {sg_name} failed with error",
            "get_srdf_exception": f"Getting SRDF details for storage group {sg_name}",
            "delete_srdf_exception": f"Delete srdf_link for sg {sg_name} failed with error",
            "missing_params": "Mandatory parameters not found",
            "bias_not_allowed": "Create SRDF link operation failed as Ansible modules v1.1 does not allow creation of SRDF links using Bias",
        }
        return error_msg[response_type]
