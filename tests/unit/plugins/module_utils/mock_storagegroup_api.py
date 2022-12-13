# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""
Mock StorageGroup Api for StorageGroup Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


SG_DETAILS = {
    "cap_gb": 5.01,
    "compression": False,
    "compression_ratio_to_one": 0.0,
    "device_emulation": "FBA",
    "num_of_child_sgs": 0,
    "num_of_masking_views": 0,
    "num_of_parent_sgs": 0,
    "num_of_snapshots": 0,
    "num_of_vols": 5,
    "slo": "NONE",
    "slo_compliance": "NONE",
    "srp": "SRP_1",
    "storageGroupId": "sample_sg",
    "type": "Standalone",
    "unprotected": True,
    "unreducible_data_gb": 0.0,
    "vp_saved_percent": 100.0
}


def get_storagegroup_details():
    return {'storageGroupId': 'Test',
            'slo': 'Diamond',
            'service_level': 'Diamond',
            'base_slo_name': 'Diamond',
            'srp': 'SRP_1',
            'slo_compliance': 'STABLE',
            'num_of_vols': 0, 'num_of_child_sgs': 0,
            'num_of_parent_sgs': 0,
            'num_of_masking_views': 0,
            'num_of_snapshots': 0,
            'cap_gb': 0.0,
            'type': 'Standalone',
            'unprotected': True,
            'hostIOLimit': {'host_io_limit_mb_sec': '100',
                            'host_io_limit_io_sec': '100',
                            'dynamicDistribution': 'Always'},
            'compression': True,
            'compression_ratio_to_one': 0.0,
            'unreducible_data_gb': 0.0}
