# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Volume Api for Volume Test module on PowerMax"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def get_vol_details():
    return {"allocated_percent": 0,
            "cap_cyl": 10,
            "cap_gb": 0.02,
            "cap_mb": 19,
            "effective_wwn": "00000970000197902573533030373245",
            "emulation": "FBA",
            "encapsulated": False,
            "has_effective_wwn": False,
            "mobility_id_enabled": False,
            "num_of_front_end_paths": 0,
            "num_of_storage_groups": 1,
            "pinned": False,
            "reserved": False,
            "snapvx_source": False,
            "snapvx_target": False,
            "storage_groups": [{
                "storage_group_name": "Test_SG",
                "portId": "01"
            }],
            "storageGroupId": ["Test_SG"],
            "ssid": "FFFFFFFF",
            "status": "Ready",
            "type": "TDEV",
            "unreducible_data_gb": 0.0,
            "volumeId": "0072E",
            "volume_identifier": "vol_test_52",
            "wwn": "60000970000197902573533030373245"}


def get_vol_list():
    return [{"allocated_percent": 0,
             "cap_cyl": 10,
             "cap_gb": 0.02,
             "cap_mb": 19,
             "effective_wwn": "00000970000197902573533030373245",
             "emulation": "FBA",
             "encapsulated": False,
             "has_effective_wwn": False,
             "mobility_id_enabled": False,
             "num_of_front_end_paths": 0,
             "num_of_storage_groups": 1,
             "pinned": False,
             "reserved": False,
             "snapvx_source": False,
             "snapvx_target": False,
             "storage_groups": [{"storage_group_name": "Test_SG",
                                 "portId": "01"}],
             "storageGroupId": ["Test_SG"],
             "ssid": "FFFFFFFF",
             "status": "Ready",
             "type": "TDEV",
             "unreducible_data_gb": 0.0,
             "volumeId": "0072E",
             "volume_identifier": "vol_test_52",
             "wwn": "60000970000197902573533030373245"}]


def create_vol_exception(vol_name):
    return 'Create volume ' + vol_name + ' failed with error'


def expand_vol_exception(new_size):
    return 'Current volume size 0.02 GB is greater than ' + new_size + ' GB specified.'
