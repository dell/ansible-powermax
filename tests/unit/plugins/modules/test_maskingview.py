# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for MaskingView module on PowerMax"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_maskingview_api import MockMaskingViewApi
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.universion_check = MagicMock(return_value={"is_valid_universion": True})
utils.get_U4V_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powermax.plugins.modules.maskingview import MaskingView


class TestMaskingView():

    get_module_args = MockMaskingViewApi.MASKING_VIEW_COMMON_ARGS

    @pytest.fixture
    def maskingview_module_mock(self, mocker):
        maskingview_module_mock = MaskingView()
        maskingview_module_mock.module.check_mode = False
        return maskingview_module_mock

    def mock_host_list(self, maskingview_module_mock, call_exception):
        if not call_exception:
            maskingview_module_mock.provisioning.get_host_list = \
                MagicMock(return_value=MockMaskingViewApi.GET_HOST_LIST_API_RESPONSE)
        else:
            maskingview_module_mock.provisioning.get_host_list = \
                MagicMock(side_effect=Exception)

    def mock_hostgroup_list(self, maskingview_module_mock, call_exception):
        if not call_exception:
            maskingview_module_mock.provisioning.get_host_group_list = \
                MagicMock(return_value=MockMaskingViewApi.GET_HOSTGROUP_LIST_API_RESPONSE)
        else:
            maskingview_module_mock.provisioning.get_host_list = \
                MagicMock(side_effect=Exception)

    def mock_get_masking_view_list(self, maskingview_module_mock):
        maskingview_module_mock.provisioning.get_masking_view_list = \
            MagicMock(return_value=MockMaskingViewApi.MASKING_VIEW_LIST_API_RESPONSE)

    def mock_create_mv_exist_comp(self, maskingview_module_mock, type):
        maskingview_module_mock.provisioning.create_masking_view_existing_components = \
            MagicMock(return_value=MockMaskingViewApi.get_create_mv_payload(type))

    def create_mv_host(self, maskingview_module_mock, type, call_exception=False):
        if type == 'host':
            self.mock_host_list(maskingview_module_mock, call_exception)
        elif type == 'hostgroup':
            self.mock_hostgroup_list(maskingview_module_mock, call_exception)
        self.mock_get_masking_view_list(maskingview_module_mock)
        self.mock_create_mv_exist_comp(maskingview_module_mock, type)
        maskingview_module_mock.perform_module_operation()

    def test_create_maskingview_with_host(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('host'))
        maskingview_module_mock.module.params = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'host')
        maskingview_module_mock.provisioning.create_masking_view_existing_components.assert_called()

    def test_create_maskingview_with_host_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('host'))
        maskingview_module_mock.module.params = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'host', True)
        assert MockMaskingViewApi.get_create_mv_exception_response('host') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_maskingview_with_hostgroup(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('hostgroup'))
        maskingview_module_mock.module.params = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'hostgroup')
        maskingview_module_mock.provisioning.create_masking_view_existing_components.assert_called()

    def test_create_maskingview_with_hostgroup_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('hostgroup'))
        maskingview_module_mock.module.params = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'hostgroup', True)
        assert MockMaskingViewApi.get_create_mv_exception_response('hostgroup') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']
