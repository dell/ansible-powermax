# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock Port Api for Port Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockPortApi:
    PORT_COMMON_ARGS = {
        "gateway_host": "**.***.**.***",
        "serial_no": None,
    }

    @staticmethod
    def get_error_message(response_type, director_id=None, port_id=None):
        error_msg = {"get_port_exception": f"Failed to get details of port {director_id}:{port_id} with error",
                     "missing_mandatory_args": "Director ID and Port ID is mandatory for listing port information"}
        return error_msg[response_type]
