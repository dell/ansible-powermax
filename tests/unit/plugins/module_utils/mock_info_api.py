# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

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
        "filters": None,
        "masking_view_name": None
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

    VOLUME_LIST = [
        '00809'
    ]

    VOLUME_DETAILS_LIST = [
        {
            "allocated_percent": 0,
            "cap_cyl": 10,
            "cap_gb": 10.0,
            "cap_mb": 100.0,
            "effective_wwn": "60000970000197902572533xxxxxxxxx",
            "emulation": "FBA",
            "encapsulated": False,
            "has_effective_wwn": True,
            "mobility_id_enabled": False,
            "nguid": "2572533030333035000097xxxxxxxxxx",
            "num_of_front_end_paths": 0,
            "num_of_storage_groups": 0,
            "pinned": False,
            "reserved": False,
            "snapvx_source": False,
            "snapvx_target": False,
            "ssid": "FFFFFFFF",
            "status": "Ready",
            "type": "TDEV",
            "unreducible_data_gb": 0.0,
            "volumeId": "000xx",
            "wwn": "60000970000197902572533xxxxxxxxx"
        }
    ]

    @staticmethod
    def get_exception_response(response_type):
        if response_type == 'get_details_mv_connections':
            return "Get Masking View Connections for array None failed with error "
        elif response_type == 'get_volume_details':
            return "Get Volumes for array None failed with error "
