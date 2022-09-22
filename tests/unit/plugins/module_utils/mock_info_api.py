# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""
Mock Info Api for Info Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockInfoApi:
    INFO_COMMON_ARGS = {
        "gateway_host": "**.***.**.***",
        "serial_no": None,
        "tdev_volumes": None,
        "gather_subset": [],
        "filters": None
    }

    MASKING_VIEW_LIST = [
        'EMBEDDED_NAS_DM_MV'
    ]

    MASKING_VIEW_CONNECTIONS_LIST = [
        {
            "alias": "100000xxxx/100000xxxxxxxxx",
            "cap_gb": "10.0",
            "dir_port": "XX-XX:11",
            "host_lun_address": "0001",
            "initiatorId": "100000aaaaaaa",
            "logged_in": True,
            "on_fabric": True,
            "volumeId": "000XX"
        }
    ]

    @staticmethod
    def get_exception_response(response_type):
        if response_type == 'get_details_mv_connections':
            return "Get Masking View Connections for array None failed with error "
