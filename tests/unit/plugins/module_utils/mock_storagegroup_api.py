# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock StorageGroup Api for StorageGroup Test module on PowerMax
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockStorageGroupApi:
    STORAGEGROUP_COMMON_ARGS = {
        "sg_name": "test_sg",
        "service_level": "None",
        "state": "present",
        "srp": None,
        "compression": None,
        "volumes": None,
        "vol_state": None,
        "child_storage_groups": None,
        "child_sg_state": None,
        "new_sg_name": None,
        "snapshot_policies": None,
        "snapshot_policy_state": None,
        "target_sg_name": None,
        "force": None,
        "host_io_limit": None
    }

    STORAGEGROUP_RESPONSE_DETAILS = {
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
        "storageGroupId": "test_sg",
        "type": "Standalone",
        "unprotected": True,
        "unreducible_data_gb": 0.0,
        "vp_saved_percent": 100.0
    }

    @staticmethod
    def get_error_message(response_type, sg_name=None):
        error_msg = {
            "unsupported_pyu4v_version": "This functionality is not supported by PyU4V version",
            "get_vol_exception": f"Getting volume details of storage group {sg_name} failed with error",
            "get_vol_list_exception": f"Getting list of volumes for storage group {sg_name} failed with error",
            "create_sg_exception": f"Create storage group {sg_name} failed with error",
            "move_srdf_vol_no_force": "Specify a force flag to move volumes to or from SRDF protected storage group",
            "delete_exception": f"Delete storage group {sg_name} failed with error",
            "duplicate_volume": "Duplicate volumes found",
            "remove_volume_exception": f"Remove existing volumes from storage group {sg_name} failed with error",
            "srdf_more_than_2": f"More than 2 RDF groups exist for the given storage group {sg_name}",
            "missing_cap": "No valid size was specified for the volume",
            "add_vol_unsupport_version": f"Adding new volumes on storage group {sg_name} failed  with error "
            "Add new volumes on SRDF protected storage group is supported from v5978.444.444 onwards",
            "size_conflict": f"Adding new volumes on storage group {sg_name} failed  with error A volume with identifier vol_3 "
            "but different size 2 GB already exists.",
            "add_vol_exception": f"Adding new volumes on storage group {sg_name} failed",
            "add_existing_vol_exception": f"Adding existing volumes to storage group {sg_name} failed",
            "add_vol_duplicated_id": f"One or more volumes to be added are already present in SG {sg_name} with the same name",
            "add_vol_same_id": f"One or more volumes to be added to SG {sg_name} has the same identifier",
            "modify_srp_exception": f"Modify attribute SRP of storage group {sg_name} failed with error",
            "modify_slo_exception": f"Modify attribute SLO of storage group {sg_name} failed with error",
            "modify_compression_exception": f"Modify attribute compression of storage group {sg_name} failed with error",
            "rename_when_create": f"Rename storage group {sg_name} to new name new_name failed because storage group does not exist",
            "rename_exception": f"Rename storage group {sg_name} to new name test_sg_2 failed with error",
            "add_csg_exception": f"Adding child SG child_1 to parent storage group {sg_name} failed with error",
            "remove_csg_exception": f"Removing child storage group child_1 from parent storage group {sg_name} failed with error",
            "add_snapshot_policy_exception": f"Adding snapshot policies to the storage group {sg_name} failed with error",
            "remove_snapshot_policy_exception": f"Removing the snapshot policies from the storage group {sg_name} failed with error",
            "delete_sg_with_linked_snap": f"Cannot delete SG {sg_name} because it has snapshots in linked state. "
            "Unlink the snapshots and and retry",
            "io_limit_required": "Either host_io_limit_mbps or host_io_limit_iops is required along with dynamic_distribution",
            "set_io_limit_exception": "Failed to set host I/O limit. Exception received was",
            "srdf_check_exception": f"Determining SRDF protection for storage group {sg_name} failed with error",
            "get_policy_comp_exception": f"Getting snapshot policy compliance details for the storage group {sg_name} failed with error",
            "iops_check_failed": "IOPS is not in the allowed value range",
            "mbps_check_failed": "MBPS is not in the allowed value range",
        }
        return error_msg[response_type]

    @staticmethod
    def get_exception_response(response_type):
        if response_type == 'get_storage_group':
            return "Failed to get storage group details error:"
