# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Host Api for Host Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockHostApi:
    HOST_COMMON_ARGS = {
        "gateway_host": "**.***.**.***",
        "serial_no": None,
        "host_name": None,
        "initiators": [],
        "initiator_state": None,
        "new_name": None,
        "host_flags": {},
        "host_type": None,
        "state": "present"
    }

    GET_HOST_API_RESPONSE = {
        'hostId': 'test_host',
        'num_of_masking_views': 0,
        'num_of_initiators': 2,
        'num_of_host_groups': 0,
        'port_flags_override': False,
        'consistent_lun': False,
        'enabled_flags': '',
        'disabled_flags': '',
        'type': 'Fibre',
        'initiator': [
            '100xx000xxxxxxxx',
        ],
        'num_of_powerpath_hosts': 0,
        'bw_limit': 0
    }

    ADD_INITIATOR_PAYLOAD = {
        "host_name": "test_host",
        "initiators": [
            "100xx111xxxxxxxx"
        ],
        "initiator_state": 'present-in-host'
    }

    REMOVE_INITIATOR_PAYLOAD = {
        "host_name": "test_host",
        "initiators": [
            "100xx000xxxxxxxx"
        ],
        "initiator_state": 'absent-in-host'
    }

    @staticmethod
    def get_initiator_exception_response(response_type):
        if response_type == 'add_initiators_to_host':
            return "Adding initiators ['100xx111xxxxxxxx'] to host test_host failed with error "
        elif response_type == 'remove_initiators_from_host':
            return "Removing initiators ['100xx000xxxxxxxx'] from host test_host failed with error "
