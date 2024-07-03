# Copyright: (c) 2022-2024, Dell Technologies

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
