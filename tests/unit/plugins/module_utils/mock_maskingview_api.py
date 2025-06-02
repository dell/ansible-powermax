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
        "starting_lun_address": None
    }

    CREATE_PAYLOAD = {
        "mv_name": "test_mv",
        "portgroup_name": "test_portgroup",
        "sg_name": "test_sg",
        "state": "present"
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

    MASKING_VIEW_LIST_API_RESPONSE_EXIST = [
        "test_mv",
        "test_mv_rename"
    ]

    MASKING_VIEW_DETAIL_API_RESPONSE = {
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
    def get_delete_mv_payload():
        mv_payload = MockMaskingViewApi.CREATE_PAYLOAD.copy()
        mv_payload['state'] = "absent"
        return mv_payload

    @staticmethod
    def get_rename_mv_payload(payload_new_name):
        mv_payload = MockMaskingViewApi.CREATE_PAYLOAD.copy()
        mv_payload['new_mv_name'] = payload_new_name
        return mv_payload

    @staticmethod
    def get_mv_detail_api_response(payload_key, payload_value):
        mv_response = MockMaskingViewApi.MASKING_VIEW_DETAIL_API_RESPONSE.copy()
        if payload_key:
            mv_response[payload_key] = payload_value
        return mv_response

    @staticmethod
    def get_create_mv_exception_response(response_type):
        if response_type == 'host':
            return "Host test_host_2 does not exist"
        elif response_type == 'hostgroup':
            return "Host Group test_host_gp_1 does not exist"

    @staticmethod
    def get_create_mv_create_exception_response(response_id):
        return ('Create masking view %s failed; error ' % response_id)

    @staticmethod
    def get_create_mv_none_host_hostgroup_exception_response(response_id):
        return ('Failed to create masking view %s, Please '
                'provide SG, PG and host / host group name to '
                'create masking view' % response_id)

    @staticmethod
    def get_create_mv_both_host_hostgroup_exception_response(response_id):
        return ('Failed to create masking view %s,'
                'Please provide either host or hostgroup' % response_id)

    @staticmethod
    def get_change_mv_exception_response(response_id):
        return ('One or more of parameters (PG, SG, '
                'Host/Host Group) provided for the MV '
                '%s differ from the state of the MV on the '
                'array.' % response_id)

    @staticmethod
    def get_delete_mv_exception_response(response_id):
        return ('Delete masking view %s failed with error .' % response_id)

    @staticmethod
    def get_rename_mv_exception_response(response_id):
        return ('Rename masking view %s failed with error .' % response_id)
