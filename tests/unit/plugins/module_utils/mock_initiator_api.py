# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Mock Initiator Api for Initiator Test module on PowerMax"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def get_initiator_details():
    return {"alias": "test/host",
            "fabric_name": "1111111111110101111",
            "fcid": "111111",
            "flags_in_effect": "Common_Serial_Number(C)",
            "host": "host_test1",
            "hostGroup": [],
            "initiatorId": "1000000000000001",
            "logged_in": True,
            "maskingview": [],
            "num_of_host_groups": 0,
            "num_of_masking_views": 0,
            "num_of_powerpath_hosts": 0,
            "num_of_vols": 0,
            "on_fabric": True,
            "powerpathhosts": [],
            "symmetrixPortKey": [{
                "directorId": "AA-AA",
                "portId": "01"
            }],
            "type": "Fibre"}


def get_initiator_details_without_alias():
    return {"fabric_name": "1111111111110101111",
            "fcid": "111111",
            "flags_in_effect": "Common_Serial_Number(C)",
            "host": "host_test1",
            "hostGroup": [],
            "initiatorId": "1000000000000001",
            "logged_in": True,
            "maskingview": [],
            "num_of_host_groups": 0,
            "num_of_masking_views": 0,
            "num_of_powerpath_hosts": 0,
            "num_of_vols": 0,
            "on_fabric": True,
            "powerpathhosts": [],
            "symmetrixPortKey": [{
                "directorId": "AA-AA",
                "portId": "01"
            }],
            "type": "Fibre"}


def get_invalid_port_name():
    return "Please specify new_port_name"


def get_invalid_node_name():
    return "Please specify new_node_name"


def get_modify_ex_msg():
    return "Modifying initiator alias failed with error"


def get_initiator_id():
    return "1000000000000001"


def get_invalid_state_msg():
    return "Deletion of initiators is not allowed through Ansible module"
