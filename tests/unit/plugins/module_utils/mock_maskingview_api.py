# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Mock MaskingView Api for MaskingView Test module on PowerMax
"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


class MockMaskingViewApi:
    MASKING_VIEW_COMMON_ARGS = {
        "gateway_host": "**.***.**.***",
        "serial_no": None,
        "mv_name": None,
        "new_mv_name": None,
        "host_name": None,
        "hostgroup_name": None,
        "state": "present"
    }

    CREATE_PAYLOAD = {
        "mv_name": "test_mv",
        "portgroup_name": "test_portgroup",
        "sg_name": "test_sg"
    }

    GET_HOST_LIST_API_RESPONSE = [
        "test_host_1",
        "test_host_2"
    ]

    GET_HOSTGROUP_LIST_API_RESPONSE = [
        "test_host_gp_1",
        "test_host_gp_2"
    ]

    MASKING_VIEW_LIST_API_RESPONSE = [
        "test_mv_2",
        "test_mv_3"
    ]

    CREATE_MV_API_RESP = {
        'maskingViewId': 'test_mv',
        'hostId': 'test_host_2',
        'portGroupId': 'test_portgroup',
        'storageGroupId': 'test_sg'
    }

    @staticmethod
    def get_create_mv_payload(payload_type):
        mv_payload = MockMaskingViewApi.CREATE_PAYLOAD.copy()
        if payload_type == 'host':
            mv_payload['host_name'] = "test_host_2"
        elif payload_type == 'hostgroup':
            mv_payload['hostgroup_name'] = "test_host_gp_1"
        return mv_payload

    @staticmethod
    def get_create_mv_api_response(payload_type):
        mv_response = MockMaskingViewApi.CREATE_MV_API_RESP.copy()
        if payload_type == 'host':
            mv_response['hostId'] = "test_host_2"
        elif payload_type == 'hostgroup':
            mv_response['hostGroupId'] = "test_host_gp_1"
        return mv_response

    @staticmethod
    def get_create_mv_exception_response(response_type):
        if response_type == 'host':
            return "Host test_host_2 does not exist"
        elif response_type == 'hostgroup':
            return "Host Group test_host_gp_1 does not exist"
