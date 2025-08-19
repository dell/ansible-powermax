# Copyright: (c) 2022-2025, Dell Technologies

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

    SG_LIST = [
        "00_Cloud_1",
        "BOH_PF_MDR_SG",
        "BOH_r21Casc_SG"
    ]

    SRP_LIST = [
        "SRP_0x10test",
        "SRP_1",
        "SRP_33"
    ]

    HOST_LIST = [
        "049-330_ORS_IG",
        "Aaron",
        "Aidan",
        "Andrew",
    ]

    ALERT_LIST = [
        "alert_1",
        "alert_2",
        "alert_3",
        "alert_4",
    ]

    HEALTH_CHECK = {
        "testResults": [
            {
                "item_name": "Vault State Test ",
                "result": True
            },
            {
                "item_name": "Spare Drives Test ",
                "result": True
            },
            {
                "item_name": "Memory Test ",
                "result": True
            },
            {
                "item_name": "Locks Test ",
                "result": True
            },
            {
                "item_name": "Emulations Test ",
                "result": False
            },
            {
                "item_name": "Environmentals Test ",
                "result": True
            },
            {
                "item_name": "Battery Test ",
                "result": True
            },
            {
                "item_name": "General Test ",
                "result": False
            },
            {
                "item_name": "Compression And Dedup Test ",
                "result": True
            }
        ],
        "execution_status": "FAILED",
        "symmetrixId": "000297900330",
        "description": "HealthCheck",
        "date": 1576504894065
    }

    PORT_GROUP_LIST = [
        "00000_PG",
        "0SDA_SRP_559_PG",
        "0SDA_SRP_961_PG",
        "0SDA_SRP_B2m_PG",
        "0SDA_SRP_b3F_PG",
        "0SDA_SRP_eXg_PG",
        "0SDA_SRP_KgY_PG",
        "0SDA_SRP_NBJ_PG",
        "0SDA_SRP_q10_PG",
        "0SDA_SRP_Zvr_PG"
    ]

    INITIATOR_LIST = [
        "FA-1D:4:10000000c953fa04",
        "FA-3D:5:10000000c953fa04",
        "FA-1D:4:10000000c953fa05",
        "FA-3D:5:10000000c953fa05",
        "FA-1D:5:10000000c971604b",
        "FA-1D:4:10000000c971604b",
        "FA-3D:5:10000000c971604b",
        "FA-4D:4:10000000c971604b",
        "FA-4D:4:10000000c975c697",
        "FA-1D:4:10000000c975c697",
    ]

    SNAPSHOT_POLICY_LIST = [
        "Weekly",
        "Brian_AllProperties",
        "10_mins_keep_3",
        "DailyDefault",
        "10_mins_secure",
        "HourlyDefault",
        "WeeklyDefault",
        "10Minutes"
    ]

    METRO_DR_ENV_LIST = [
        "BOH_MDR_SG",
        "Col1SG",
        "testsnOct55",
        "PF_MetroDR_2",
        "testsnOct31_Metr"
    ]

    SRDF_GROUP_LIST = {
        "rdfg_count": 4,
        "rdfGroupID": [
            {
                "rdfgNumber": 1,
                "label": "PMG_SDFU_S",
                "remote_symmetrix_id": "000297901493",
                "group_type": "Dynamic"
            },
            {
                "rdfgNumber": 2,
                "label": "shic_rdf_c",
                "remote_symmetrix_id": "000297901493",
                "group_type": "Metro"
            },
            {
                "rdfgNumber": 3,
                "label": "Paul",
                "remote_symmetrix_id": "000297901493",
                "group_type": "Dynamic"
            },
            {
                "rdfgNumber": 4,
                "label": "os-async",
                "remote_symmetrix_id": "000297901493",
                "group_type": "Dynamic"
            }
        ]
    }

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
        elif response_type == 'get_storage_group':
            return "Get Storage Group for array None failed with error "
        elif response_type == 'get_srp':
            return "Get Storage Resource Pool details for array None failed"
        elif response_type == 'get_port_group':
            return "Get Port Group for array None failed with error "
        elif response_type == 'get_host_list':
            return "Get Host for array None failed with error "
        elif response_type == 'get_host_group_list':
            return "Get Host Group for array None failed with error "
        elif response_type == 'get_port_list':
            return "Get Port for array None failed with error "
        elif response_type == 'get_rdf_group_list':
            return "Get rdf group for array None failed with error "
        elif response_type == 'get_metrodr_environment_list':
            return "Get Metro DR environment for array None failed with error "
        elif response_type == 'get_snapshot_policy_list':
            return "Get snapshot policies for array None failed with error "
        elif response_type == 'get_initiator_list':
            return "Get initiator details failed with error"
        elif response_type == 'get_masking_view_list':
            return "Get Masking View for array None failed with error "
        elif response_type == 'get_array_list':
            return "Get Array List for Unisphere host {'type': 'str', 'required': True, 'no_log': True} failed with error"
