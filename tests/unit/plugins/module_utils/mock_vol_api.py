# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Volume Api for Volume Test module on PowerMax"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


def get_vol_details():
    return {
        "allocated_percent": 0,
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
        "storage_groups": [{"storage_group_name": "test_sg", "portId": "01"}],
        "storageGroupId": ["test_sg"],
        "ssid": "FFFFFFFF",
        "status": "Ready",
        "type": "TDEV",
        "unreducible_data_gb": 0.0,
        "volumeId": "0072E",
        "volume_identifier": "test_vol",
        "wwn": "60000970000197902573533030373245",
    }


def get_vol_srdf_details_1():
    return {
        "allocated_percent": 0,
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
        "storage_groups": [{"storage_group_name": "test_sg", "portId": "01"}],
        "storageGroupId": ["test_sg"],
        "ssid": "FFFFFFFF",
        "status": "Ready",
        "type": "RDF1+TDEV",
        "rdfGroupId": [{"rdf_group_number": 1}],
        "unreducible_data_gb": 0.0,
        "volumeId": "0072E",
        "volume_identifier": "test_vol",
        "wwn": "60000970000197902573533030373245",
    }


def get_vol_srdf_details_2():
    return {
        "allocated_percent": 0,
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
        "storage_groups": [{"storage_group_name": "test_sg", "portId": "01"}],
        "storageGroupId": ["test_sg"],
        "ssid": "FFFFFFFF",
        "status": "Ready",
        "type": "RDF1+TDEV",
        "rdfGroupId": [{"rdf_group_number": 1}, {"rdf_group_number": 1}],
        "unreducible_data_gb": 0.0,
        "volumeId": "0072E",
        "volume_identifier": "test_vol",
        "wwn": "60000970000197902573533030373245",
    }


def get_vol_srdf_details_3():
    return {
        "allocated_percent": 0,
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
        "storage_groups": [{"storage_group_name": "test_sg", "portId": "01"}],
        "storageGroupId": ["test_sg"],
        "ssid": "FFFFFFFF",
        "status": "Ready",
        "type": "RDF2+TDEV",
        "rdfGroupId": [{"rdf_group_number": 1}, {"rdf_group_number": 1}],
        "unreducible_data_gb": 0.0,
        "volumeId": "0072E",
        "volume_identifier": "test_vol",
        "wwn": "60000970000197902573533030373245",
    }


def get_vol_srdf_details_4():
    return {
        "allocated_percent": 0,
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
        "storage_groups": [{"storage_group_name": "test_sg", "portId": "01"}],
        "storageGroupId": ["test_sg"],
        "ssid": "FFFFFFFF",
        "status": "Ready",
        "type": "RDF2+TDEV",
        "rdfGroupId": [{"rdf_group_number": 1}],
        "unreducible_data_gb": 0.0,
        "volumeId": "0072E",
        "volume_identifier": "test_vol",
        "wwn": "60000970000197902573533030373245",
    }


def get_vol_list():
    return [
        {
            "allocated_percent": 0,
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
            "storage_groups": [{"storage_group_name": "test_sg", "portId": "01"}],
            "storageGroupId": ["test_sg"],
            "ssid": "FFFFFFFF",
            "status": "Ready",
            "type": "TDEV",
            "unreducible_data_gb": 0.0,
            "volumeId": "0072E",
            "volume_identifier": "test_vol",
            "wwn": "60000970000197902573533030373245",
        }
    ]


def get_storagegroup_details_1():
    return {
        "storageGroupId": "test_sg",
        "slo": "Diamond",
        "service_level": "Diamond",
        "base_slo_name": "Diamond",
        "srp": "SRP_1",
        "slo_compliance": "STABLE",
        "num_of_vols": 0,
        "num_of_child_sgs": 0,
        "num_of_parent_sgs": 0,
        "num_of_masking_views": 0,
        "num_of_snapshots": 0,
        "cap_gb": 0.0,
        "type": "Standalone",
        "unprotected": False,
        "hostIOLimit": {
            "host_io_limit_mb_sec": "100",
            "host_io_limit_io_sec": "100",
            "dynamicDistribution": "Always",
        },
        "compression": True,
        "compression_ratio_to_one": 0.0,
        "unreducible_data_gb": 0.0,
    }


def get_storagegroup_details_2():
    return {
        "storageGroupId": "test_sg_new",
        "slo": "Diamond",
        "service_level": "Diamond",
        "base_slo_name": "Diamond",
        "srp": "SRP_1",
        "slo_compliance": "STABLE",
        "num_of_vols": 0,
        "num_of_child_sgs": 0,
        "num_of_parent_sgs": 0,
        "num_of_masking_views": 0,
        "num_of_snapshots": 0,
        "cap_gb": 0.0,
        "type": "Standalone",
        "unprotected": False,
        "hostIOLimit": {
            "host_io_limit_mb_sec": "100",
            "host_io_limit_io_sec": "100",
            "dynamicDistribution": "Always",
        },
        "compression": True,
        "compression_ratio_to_one": 0.0,
        "unreducible_data_gb": 0.0,
    }


def wait_for_job():
    return [{"description": "Creating new Volumes (vol-123)"}]


def get_rdf_group_volume_1():
    return {
        "rdfMode": "Active",
        "remoteVolumeName": "test_remote_volume_name",
        "remoteSymmetrixId": "test_remote_symmetrix_id",
        "localSymmetrixId": "test_local_symmetrix_id",
        "localRdfGroupNumber": "test_local_rdf_group_number",
    }


def get_rdf_group_volume_2():
    return {
        "rdfMode": "Inactive",
        "remoteVolumeName": "test_remote_volume_name",
        "remoteSymmetrixId": "test_remote_symmetrix_id",
        "localSymmetrixId": "test_local_symmetrix_id",
    }


def get_rdf_group_volume_3():
    return {
        "rdfMode": "Active",
        "remoteVolumeName": "test_remote_volume_name",
        "remoteSymmetrixId": "test_remote_symmetrix_id",
        "localSymmetrixId": "test_local_symmetrix_id",
        "localRdfGroupNumber": "test_local_rdf_group_number",
    }


def get_rdf_group():
    return {"remoteSymmetrix": "test_remote_sysmmetrix"}


def get_storage_group_srdf_group_list_1():
    return [
        {
            "rdfMode": "Active",
            "remoteVolumeName": "test_remote_volume_name",
            "remoteSymmetrixId": "test_remote_symmetrix_id",
            "localSymmetrixId": "test_local_symmetrix_id",
            "localRdfGroupNumber": "test_local_rdf_group_number",
        },
        {
            "rdfMode": "Inactive",
            "remoteVolumeName": "test_remote_volume_name",
            "remoteSymmetrixId": "test_remote_symmetrix_id",
            "localSymmetrixId": "test_local_symmetrix_id",
        },
    ]


def get_storage_group_srdf_group_list_2():
    return [
        {
            "rdfMode": "Active",
            "remoteVolumeName": "test_remote_volume_name",
            "remoteSymmetrixId": "test_remote_symmetrix_id",
            "localSymmetrixId": "test_local_symmetrix_id",
            "localRdfGroupNumber": "test_local_rdf_group_number",
        }
    ]


def get_storage_group_srdf_group_list_3():
    return [
        {
            "rdfMode": "Active",
            "remoteVolumeName": "test_remote_volume_name",
            "remoteSymmetrixId": "test_remote_symmetrix_id",
            "localSymmetrixId": "test_local_symmetrix_id",
            "localRdfGroupNumber": "test_local_rdf_group_number",
        },
        {
            "rdfMode": "Active",
            "remoteVolumeName": "test_remote_volume_name",
            "remoteSymmetrixId": "test_remote_symmetrix_id",
            "localSymmetrixId": "test_local_symmetrix_id",
        },
        {
            "rdfMode": "Active",
            "remoteVolumeName": "test_remote_volume_name",
            "remoteSymmetrixId": "test_remote_symmetrix_id",
            "localSymmetrixId": "test_local_symmetrix_id",
        },
    ]


def get_error_message(
    response_type, vol_name=None, vol_id=None, sg_name=None, sg_id=None, size=None
):
    error_msg = {
        "create_vol_exception": f"Create volume {vol_name} failed with error",
        "expand_vol_exception": f"Current volume size 0.02 GB is greater than {size} GB specified.",
        "delete_vol_exception": f"Delete volume {vol_id} failed with error",
        "rename_vol_exception": f"Rename volume {vol_id} failed with error",
        "rename_vol_with_empty_name_exeption": "Please provide valid volume name",
        "no_size_exception_1": "Parameters size and cap_unit are required together",
        "no_size_exception_2": "Size is required to create volume",
        "no_sg_name_exception": "Specify Storage group name along with volume name",
        "get_sg_exception": f"Get storage group {sg_name} failed with error",
        "get_vol_by_id_exception": f"Got error {None} while getting details of volume {vol_id}",
        "get_duplicate_vol_exception": "Duplicate volumes found",
        "create_with_new_name_exception": "Invalid argument new_name",
        "get_vol_by_wwn_exception": "It is recommended that the user retries the operation with Volume name or ID",
        "expand_volume_exception": "Expansion of volume in Cascaded / Metro DR configurations is not supported",
        "volume_already_exist_exception": "Volume already exists",
        "determine_srdf_protected_exception": f"Failed to determine if storage group {sg_id} is srdf protected",
        "move_vol_srdf_protected_exception": "not supported from Ansible module as this operation for an SRDF protected",
        "create_without_name_exception": "vol_name is required during volume creation",
        "create_vol_srdf_exception": "More than 2 rdf groups exists for the given storage group",
        "create_vol_srdf_version_exception": "Creating new volumes on SRDF protected storage groups is supported from v5978.444.444 onward",
        "expand_vol_srdf_version_exception": "Expansion of SRDF protected volume is supported from v5978.444.444 onward",
        "expand_vol_srdf_metro_version_exception": "Expansion of SRDF/Metro protected volumes is supported from v5978.444.444 onward",
    }
    return error_msg[response_type]
