# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Host Group Api for Host Group Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockHostGroupApi:
    HOST_GROUP_COMMON_ARGS = {
        "state": "present",
        "host_state": None,
        "hostgroup_name": "test_hostgroup",
        "hosts": None,
        "host_flags": None,
        "host_type": None,
        "new_name": None
    }

    HOST_GROUP_RESPONSE = {
        "num_of_hosts": 1,
        "num_of_initiators": 1,
        "enabled_flags": "",
        "num_of_masking_views": 0,
        "disabled_flags": "",
        "host": [
            {
                "initiator": [
                    "1000000000000001"
                ],
                "hostId": "test_hg_host"
            }
        ],
        "port_flags_override": False,
        "type": "Fibre",
        "consistent_lun": False,
        "hostGroupId": "test_hostgroup"
    }

    @staticmethod
    def get_error_message(response_type, hostgroup_name=None):
        error_msg = {"empty_hostgroup_name": "hostgroup_name is mandatory parameter. Please provide valid host group name.",
                     "get_hostgroup_exception": f"Got error while getting details of host group {hostgroup_name}",
                     "create_host_exception": f"Create host group {hostgroup_name} failed with error",
                     "get_host_exception_while_creation": f"Create host group {hostgroup_name} failed as the host ansible_test_host does not exist",
                     "add_host_exception": f"Adding host ['ansible_test_host'] to host group {hostgroup_name} failed with error",
                     "remove_host_exception": f"Removing host ['test_hg_host'] from host group {hostgroup_name} failed with error",
                     "invalid_new_name_arg": "Invalid argument 'new_name' while creating a host",
                     "rename_exception": f"Renaming of host group {hostgroup_name} failed with error",
                     "delete_hostgroup_exception": f"Delete host group {hostgroup_name} failed with error",
                     "remove_host_during_creation": "Incorrect host_state specified for Create hostgroup functionality",
                     "rename_same_name": "Please provide valid hostgroup name",
                     "modify_host_flag_exception": f"Modify host group {hostgroup_name} failed with error"}
        return error_msg[response_type]
