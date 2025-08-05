# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Info Api for Info Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockMetroDRApi:

    STORAGE_GROUP_RDF_GROUP_VOLUME_DETAILS = {
        "rdfgNumber": 21,
        "label": "Col2",
        "remoteRdfgNumber": 25,
        "remoteSymmetrix": "000297900330",
        "numDevices": 1,
        "totalDeviceCapacity": 1.23,
        "localPorts": [
            "RF-1E:7"
        ],
        "remotePorts": [
            "RF-1F:7"
        ],
        "modes": [
            "Asynchronous"
        ],
        "type": "MetroDR_DR",
        "metro": False,
        "async": True,
        "witness": False,
        "witnessProtectedPhysical": False,
        "witnessProtectedVirtual": False,
        "witnessConfigured": False,
        "witnessEffective": False,
        "biasConfigured": False,
        "biasEffective": False,
        "witnessDegraded": False,
        "localOnlinePorts": [
            "RF-1E:7"
        ],
        "remoteOnlinePorts": [
            "RF-1F:7"
        ],
        "vasa_group": False,
        "link_limbo": 10,
        "hardware_compression": False,
        "software_compression": False,
        "device_polarity": "RDF2",
        "offline": False,
        "rdfa_properties": {
            "session_uncommitted_tracks": 0,
            "r1_to_r2_lag_time": 29,
            "duration_of_last_cycle": 15,
            "average_cycle_time": 15,
            "duration_of_last_transmit_cycle": 15,
            "transmit_queue_depth": 1,
            "cycle_number": 4763,
            "transmit_idle_state": "Enabled",
            "transmit_idle_time": 0,
            "consistency_protection": "Enabled",
            "dse_active": True,
            "dse_threshold": 50,
            "dse_autostart": "Enabled",
            "session_priority": 33,
            "consistency_exempt_volumes": False
        }
    }

    STORAGE_GROUP_RDF_GROUP_VOLUME_ACTIVE_DETAILS = {
        "rdfgNumber": 21,
        "label": "Col2",
        "remoteRdfgNumber": 25,
        "remoteSymmetrix": "000297900330",
        "numDevices": 1,
        "totalDeviceCapacity": 1.23,
        "localPorts": [
            "RF-1E:7"
        ],
        "remotePorts": [
            "RF-1F:7"
        ],
        "modes": [
            "Active"
        ],
        "states": [],
        "type": "MetroDR_DR",
        "metro": False,
        "async": True,
        "witness": False,
        "witnessProtectedPhysical": False,
        "witnessProtectedVirtual": False,
        "witnessConfigured": False,
        "witnessEffective": False,
        "biasConfigured": False,
        "biasEffective": False,
        "witnessDegraded": False,
        "localOnlinePorts": [
            "RF-1E:7"
        ],
        "remoteOnlinePorts": [
            "RF-1F:7"
        ],
        "vasa_group": False,
        "link_limbo": 10,
        "hardware_compression": False,
        "software_compression": False,
        "device_polarity": "RDF2",
        "offline": False,
        "rdfa_properties": {
            "session_uncommitted_tracks": 0,
            "r1_to_r2_lag_time": 29,
            "duration_of_last_cycle": 15,
            "average_cycle_time": 15,
            "duration_of_last_transmit_cycle": 15,
            "transmit_queue_depth": 1,
            "cycle_number": 4763,
            "transmit_idle_state": "Enabled",
            "transmit_idle_time": 0,
            "consistency_protection": "Enabled",
            "dse_active": True,
            "dse_threshold": 50,
            "dse_autostart": "Enabled",
            "session_priority": 33,
            "consistency_exempt_volumes": False
        }
    }

    STORAGE_GROUP_RDF_GROUP_VOLUME_LIST = [
        {
            "rdfgNumber": 1,
            "label": "PMG_SDFU_S",
            "remote_symmetrix_id": "000297901493",
            "group_type": "Dynamic"
        },
    ]

    METRO_DR_ENV_DETAILS = {
        "name": "REST_RDFG_MDR",
        "valid": True,
        "environment_exempt": False,
        "environment_state": "Normal",
        "capacity_gb": 3.005,
        "metro_state": "Suspended",
        "metro_link_state": "Online",
        "metro_exempt": False,
        "metro_service_state": "Inactive",
        "metro_witness_state": "Available",
        "metro_r1_array_health": "Normal",
        "metro_r2_array_health": "Normal",
        "dr_state": "Suspended",
        "dr_link_state": "Online",
        "dr_exempt": False,
        "dr_service_state": "Inactive",
        "dr_rdf_mode": "Adaptive Copy"
    }

    METRO_DR_ENV_DETAILS_FORCE_SPLIT = {
        "name": "REST_RDFG_MDR",
        "valid": True,
        "environment_exempt": False,
        "environment_state": "Normal",
        "capacity_gb": 3.005,
        "metro_state": "Split",
        "metro_link_state": "Online",
        "metro_exempt": False,
        "metro_service_state": "Inactive",
        "metro_witness_state": "Available",
        "metro_r1_array_health": "Normal",
        "metro_r2_array_health": "Normal",
        "dr_state": "Split",
        "dr_link_state": "Online",
        "dr_exempt": False,
        "dr_service_state": "Inactive",
        "dr_rdf_mode": "Adaptive Copy"
    }

    METRO_DR_ENV_DETAILS_FORCE_SYNC = {
        "name": "REST_RDFG_MDR",
        "valid": True,
        "environment_exempt": False,
        "environment_state": "Normal",
        "capacity_gb": 3.005,
        "metro_state": "Suspended",
        "metro_link_state": "Online",
        "metro_exempt": False,
        "metro_service_state": "Inactive",
        "metro_witness_state": "Available",
        "metro_r1_array_health": "Normal",
        "metro_r2_array_health": "Normal",
        "dr_state": "Synchronized",
        "dr_link_state": "Online",
        "dr_exempt": False,
        "dr_service_state": "Inactive",
        "dr_rdf_mode": "Adaptive Copy"
    }

    @staticmethod
    def get_exception_response(response_type):
        if response_type == 'get_storage_group_srdf_group_list':
            return "Failed to get SRDF group list error:"
        elif response_type == 'get_storage_group_srdf_details':
            return "Failed to get SRDF details error:"
        elif response_type == 'get_rdf_group':
            return "Failed to get RDF group details error:"
        elif response_type == 'pre_check_srdf_group':
            return "SG: test_sg does not have srdf group"
        elif response_type == 'convert_to_metrodr_env':
            return "Failed to convert SG to metro DR environment error:"
        elif response_type == 'pre_checks_for_modify_split_mode':
            return "replication_mode required only with srdf_state 'SetMode'"
        elif response_type == 'pre_checks_for_modify_keep_r2':
            return "keep_r2 can be True only with srdf_state 'Suspend'"
        elif response_type == 'modify_metrodr_env':
            return "Failed to modify metro DR environment error:"
        elif response_type == 'delete_metrodr_env':
            return "Failed to delete metro DR environment error:"
