# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Port Group Api for Port Group Test module on PowerMax
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MockPortGroupApi:
    PORT_GROUP_COMMON_ARGS = {
        "state": "present",
        "portgroup_name": "test_portgroup",
        "new_name": None,
        "port_state": None,
        "ports": None,
        "port_group_protocol": None,
    }

    PORT_GROUP_RESPONSE = {
        "portGroupId": "test_portgroup",
        "symmetrixPortKey": [
            {"directorId": "FA-2D", "portId": "5"},
            {"directorId": "FA-2D", "portId": "7"},
        ],
        "num_of_masking_views": 0,
        "type": "Fibre",
        "num_of_ports": 2,
    }

    @staticmethod
    def get_error_message(response_type, portgroup_name=None):
        error_msg = {
            "invalid_port_state": "Create port group test_portgroup failed; "
            "error Invalid port_state: Ports can only be added while creating portgroup",
            "create_portgroup_exception": f"Create port group {portgroup_name} failed; error",
            "portgroup_empty_new_name": "Please provide new name for the port group",
            "delete_portgroup_exception": f"Delete port group {portgroup_name} failed.",
            "rename_portgroup_exception": f"Modify port group {portgroup_name} failed with error .",
            "add_port_exception": "Add port {'director_id': 'FA-1D', 'port_id': '10'} to port group test_portgroup failed with error .",
            "remove_port_exception": "Remove port {'director_id': 'FA-2D', 'port_id': '5'} "
            "from port group test_portgroup failed with error .",
        }
        return error_msg[response_type]
