# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock RDFGroup Api for RDF Group Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockRDFGroupApi:
    RDFGROUP_COMMON_ARGS = {
        "gateway_host": "**.***.**.***",
        "serial_no": None,
        "rdfgroup_number": 1
    }

    RDF_GROUP_VOLUME_LIST = [
        'test_vol'
    ]

    RDF_GROUP_DETAILS = {
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

    RDF_GROUP_VOLUME_DETAILS = {
        "largerRdfSide": "Equal",
        "localRdfGroupNumber": 1,
        "localSymmetrixId": "0001XXX",
        "localVolumeName": "test_vol",
        "localVolumeState": "Ready",
        "local_wwn_external": "00000001111",
        "rdfMode": "Active",
        "rdfpairState": "ActiveBias",
        "remoteRdfGroupNumber": 63,
        "remoteSymmetrixId": "0002XXX",
        "remoteVolumeName": "test_vol_1",
        "remoteVolumeState": "Ready",
        "remote_wwn_external": "11111111",
        "volumeConfig": "RDFXXXXX"
    }

    @staticmethod
    def get_exception_response(response_type):
        if response_type == 'get_rdfgroup_volume_details':
            return "Get RDF Volume test_vol details for RDF Group 1 failed with error "
        elif response_type == 'get_rdf_volume_list':
            return "Get RDF Volumes List for RDF Group 1 failed with error"
        elif response_type == 'get_rdf_group_details':
            return "Get RDF Group 1 Details failed with error"
