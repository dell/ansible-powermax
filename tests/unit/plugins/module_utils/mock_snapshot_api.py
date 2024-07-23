# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock API responses for PowerMax Snapshot module"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

MODULE_UTILS_PATH = 'ansible_collections.dellemc.powermax.plugins.modules.snapshot.utils'


class MockSnapshotApi:

    SNAPSHOT_NAME = "ansible_snap_test"
    SNAPSHOT_ID = 185950553857
    SG_NAME = "ansible_sg_test"

    SNAPSHOT_COMMON_ARGS = {
        "sg_name": None,
        "snapshot_name": None,
        "snapshot_id": None,
        "ttl": None,
        "ttl_unit": None,
        "generation": None,
        "state": None,
        "new_snapshot_name": None,
        "target_sg_name": None,
        "link_status": None,
        "restore": None
    }

    SNAPSHOT_DETAILS_1 = {
        "expired": False,
        "linked": False,
        "name": "ansible_snap_test",
        "non_shared_tracks": 0,
        "num_source_volumes": 1,
        "num_storage_group_volumes": 1,
        "restored": True,
        "snapid": 185950553857,
        "source_volume": [
            {
                "capacity": 547,
                "capacity_gb": 1.0015869,
                "name": "00205"
            }
        ],
        "state": [
            "Established",
            "Restored"
        ],
        "time_to_live_expiry_date": "12:31:51 Sat, 06 Jul 2024 +0000",
        "timestamp": "12:31:50 Fri, 05 Jul 2024 +0000",
        "timestamp_utc": 1720182710000,
        "tracks": 0
    }

    SNAPSHOT_DETAILS_2 = {
        "generation": 0,
        "isExpired": False,
        "isLinked": False,
        "isRestored": False,
        "name": "ansible_snap_test",
        "nonSharedTracks": 0,
        "numSharedTracks": 0,
        "numSourceVolumes": 1,
        "numStorageGroupVolumes": 1,
        "numUniqueTracks": 0,
        "snapid": 185950553857,
        "sourceVolume": [
            {
                "capacity": 547,
                "capacity_gb": 1.0015869,
                "name": "00205"
            }
        ],
        "state": [
            "Established"
        ],
        "timeToLiveExpiryDate": "17:41:40 Sun, 07 Jul 2024 +0000",
        "timestamp": "17:41:40 Sat, 06 Jul 2024 +0000",
        "timestamp_utc": 1720287700000,
        "tracks": 0
    }

    SNAPSHOT_GENERATION_DETAILS = [
        {
            "generation": 0,
            "snapid": 185950553857
        }
    ]

    SNAPSHOT_LINKED_1 = {
        "expired": False,
        "linked": True,
        "linked_storage_group": [
            {
                "linkedCreationTimestamp": "10:59:10 Tue, 09 Jul 2024 +0000",
                "linked_volume_name": "00206",
                "name": "ansible-snap-sg-target",
                "percentageCopied": 0,
                "source_volume_name": "00205",
                "trackSize": 131072,
                "tracks": 8205
            }
        ],
        "linked_storage_group_names": [
            "ansible-snap-sg-target"
        ],
        "name": "ansible_snap_test",
        "non_shared_tracks": 0,
        "num_source_volumes": 1,
        "num_storage_group_volumes": 1,
        "restored": False,
        "snapid": 186124647681,
        "source_volume": [
            {
                "capacity": 547,
                "capacity_gb": 1.0015869,
                "name": "00205"
            }
        ],
        "state": [
            "Established"
        ],
        "time_to_live_expiry_date": "10:58:56 Wed, 10 Jul 2024 +0000",
        "timestamp": "10:58:56 Tue, 09 Jul 2024 +0000",
        "timestamp_utc": 1720522736000,
        "tracks": 0
    }

    SNAPSHOT_LINKED_2 = {
        "expired": False,
        "isLinked": True,
        "linkedStorageGroup": [
            {
                "linkedCreationTimestamp": "10:59:10 Tue, 09 Jul 2024 +0000",
                "linked_volume_name": "00206",
                "name": "ansible-snap-sg-target",
                "percentageCopied": 0,
                "source_volume_name": "00205",
                "trackSize": 131072,
                "tracks": 8205
            }
        ],
        "linked_storage_group_names": [
            "ansible-snap-sg-target"
        ],
        "name": "ansible_snap_test",
        "non_shared_tracks": 0,
        "num_source_volumes": 1,
        "num_storage_group_volumes": 1,
        "restored": False,
        "snapid": 186124647681,
        "source_volume": [
            {
                "capacity": 547,
                "capacity_gb": 1.0015869,
                "name": "00205"
            }
        ],
        "state": [
            "Established"
        ],
        "time_to_live_expiry_date": "10:58:56 Wed, 10 Jul 2024 +0000",
        "timestamp": "10:58:56 Tue, 09 Jul 2024 +0000",
        "timestamp_utc": 1720522736000,
        "tracks": 0
    }

    GENERATION_LIST = ["0"]

    SNAP_ID_LIST = [185950553857]

    @staticmethod
    def get_error_message(response_type):
        error_msg = {"get_details_exception": "Got error: SDK Error message while getting details of storage group ansible_sg_test snapshot ansible_snap_test ",
                     "rename_exception": "Renaming Snapshot ansible_snap_test for Storage Group ansible_sg_test failed with error SDK Error message",
                     "create_exception": "Create Snapshot ansible_snap_test for SG ansible_sg_test failed with error SDK Error message",
                     "delete_exception": "Delete SG ansible_sg_test Snapshot ansible_snap_test failed with error SDK Error message",
                     "exit_exception": "Failed to close unisphere connection with error: SDK Error message",
                     "restore_exception": "Restore SG ansible_sg_test Snapshot ansible_snap_test failed with error: SDK Error message",
                     "link_exception": "Change SG ansible_sg_test Snapshot ansible_snap_test link status failed with error SDK Error message",
                     "no_id_exception": "Please specify a valid generation or a snapshot_id"}
        return error_msg[response_type]
