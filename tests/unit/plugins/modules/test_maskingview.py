# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for MaskingView module on PowerMax"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_maskingview_api import MockMaskingViewApi
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
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

    def mock_get_masking_view_list(self, maskingview_module_mock, call_exception):
        if not call_exception:
            maskingview_module_mock.provisioning.get_masking_view_list = \
                MagicMock(return_value=MockMaskingViewApi.MASKING_VIEW_LIST_API_RESPONSE)
        else:
            maskingview_module_mock.provisioning.get_masking_view_list = \
                MagicMock(side_effect=Exception)

    def mock_get_masking_view_list_exist(self, maskingview_module_mock):
        maskingview_module_mock.provisioning.get_masking_view_list = \
            MagicMock(return_value=MockMaskingViewApi.MASKING_VIEW_LIST_API_RESPONSE_EXIST)

    def mock_get_masking_view_detail(self, maskingview_module_mock, key, value):
        maskingview_module_mock.provisioning.get_masking_view = \
            MagicMock(return_value=MockMaskingViewApi.get_mv_detail_api_response(key, value))

    def mock_create_mv_exist_comp(self, maskingview_module_mock, type, call_exception):
        if not call_exception:
            maskingview_module_mock.provisioning.create_masking_view_existing_components = \
                MagicMock(return_value=MockMaskingViewApi.get_create_mv_payload(type))
        else:
            maskingview_module_mock.provisioning.create_masking_view_existing_components = \
                MagicMock(side_effect=Exception)

    def mock_delete_masking_view(self, maskingview_module_mock, call_exception):
        if not call_exception:
            maskingview_module_mock.provisioning.delete_masking_view = \
                MagicMock(return_value=True)
        else:
            maskingview_module_mock.provisioning.delete_masking_view = \
                MagicMock(side_effect=Exception)

    def mock_rename_masking_view(self, maskingview_module_mock, call_exception):
        if not call_exception:
            maskingview_module_mock.provisioning.rename_masking_view = \
                MagicMock(return_value=True)
        else:
            maskingview_module_mock.provisioning.rename_masking_view = \
                MagicMock(side_effect=Exception)

    def create_mv_host(self, maskingview_module_mock, type, call_list_exception=False, call_create_exception=False):
        if type == 'host':
            self.mock_host_list(maskingview_module_mock, call_list_exception)
        elif type == 'hostgroup':
            self.mock_hostgroup_list(maskingview_module_mock, call_list_exception)
        self.mock_get_masking_view_list(maskingview_module_mock, call_list_exception)
        self.mock_create_mv_exist_comp(maskingview_module_mock, type, call_create_exception)
        maskingview_module_mock.perform_module_operation()

    def change_mv_host(self, maskingview_module_mock, key, value, call_exception=False):
        self.mock_host_list(maskingview_module_mock, call_exception)
        self.mock_get_masking_view_list_exist(maskingview_module_mock)
        self.mock_get_masking_view_detail(maskingview_module_mock, key, value)
        maskingview_module_mock.perform_module_operation()

    def delete_mv_host(self, maskingview_module_mock, call_exception=False):
        self.mock_host_list(maskingview_module_mock, call_exception)
        self.mock_get_masking_view_list_exist(maskingview_module_mock)
        self.mock_get_masking_view_detail(maskingview_module_mock, '', '')
        self.mock_delete_masking_view(maskingview_module_mock, call_exception)
        maskingview_module_mock.perform_module_operation()

    def rename_mv_host(self, maskingview_module_mock, call_exception=False):
        self.mock_host_list(maskingview_module_mock, False)
        self.mock_get_masking_view_list_exist(maskingview_module_mock)
        self.mock_get_masking_view_detail(maskingview_module_mock, '', '')
        self.mock_rename_masking_view(maskingview_module_mock, call_exception)
        maskingview_module_mock.perform_module_operation()

    def test_create_maskingview_with_host(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('host'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'host')
        maskingview_module_mock.provisioning.create_masking_view_existing_components.assert_called()

    def test_create_maskingview_with_host_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('host'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'host', True)
        assert MockMaskingViewApi.get_create_mv_exception_response('host') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_maskingview_with_hostgroup(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('hostgroup'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'hostgroup')
        maskingview_module_mock.provisioning.create_masking_view_existing_components.assert_called()

    def test_create_maskingview_with_hostgroup_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('hostgroup'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'hostgroup', True)
        assert MockMaskingViewApi.get_create_mv_exception_response('hostgroup') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_maskingview_with_hostgroup_create_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('hostgroup'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'hostgroup', False, True)
        assert MockMaskingViewApi.get_create_mv_create_exception_response('test_mv') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_maskingview_with_both_hostgroup_host_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('hostgroup'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('host'))
        maskingview_module_mock.module_wo_sensitive_data.update(self.get_module_args)
        self.create_mv_host(maskingview_module_mock, 'hostgroup')
        assert MockMaskingViewApi.get_create_mv_both_host_hostgroup_exception_response('test_mv') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_maskingview_with_none_hostgroup_host_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload(''))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.create_mv_host(maskingview_module_mock, 'hostgroup')
        assert MockMaskingViewApi.get_create_mv_none_host_hostgroup_exception_response('test_mv') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_change_maskingview_with_unsupported_exception(self, maskingview_module_mock):
        unsupported_params = ['portGroupId', 'storageGroupId', 'hostId', 'hostGroupId', 'hostId_hostgroup_name', 'hostGroupId_host_name']
        for param_key in unsupported_params:
            self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('host'))
            if param_key == 'hostId_hostgroup_name':
                self.get_module_args.update(MockMaskingViewApi.get_create_mv_payload('hostgroup'))
            maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
            if param_key != 'hostId_hostgroup_name' and param_key != 'hostId_hostgroup_name' :
                self.change_mv_host(maskingview_module_mock, param_key, ('%s_change' % param_key))
            assert MockMaskingViewApi.get_change_mv_exception_response('test_mv') == \
                maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_delete_maskingview(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_delete_mv_payload())
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.delete_mv_host(maskingview_module_mock)
        maskingview_module_mock.provisioning.delete_masking_view.assert_called()

    def test_delete_maskingview_with_check_mode(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_delete_mv_payload())
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        maskingview_module_mock.module.check_mode = True
        self.delete_mv_host(maskingview_module_mock)
        maskingview_module_mock.provisioning.delete_masking_view.assert_not_called()

    def test_delete_maskingview_with_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_delete_mv_payload())
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.delete_mv_host(maskingview_module_mock, True)
        assert MockMaskingViewApi.get_delete_mv_exception_response('test_mv') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_rename_maskingview(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_rename_mv_payload('test_mv_rename'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.rename_mv_host(maskingview_module_mock)
        maskingview_module_mock.provisioning.rename_masking_view.assert_called()

    def test_rename_maskingview_with_check_mode(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_rename_mv_payload('test_mv_rename'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        maskingview_module_mock.module.check_mode = True
        self.rename_mv_host(maskingview_module_mock)
        maskingview_module_mock.provisioning.rename_masking_view.assert_not_called()

    def test_rename_maskingview_with_same_name(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_rename_mv_payload('test_mv'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.rename_mv_host(maskingview_module_mock)
        maskingview_module_mock.provisioning.rename_masking_view.assert_not_called()

    def test_rename_maskingview_with_exception(self, maskingview_module_mock):
        self.get_module_args.update(MockMaskingViewApi.get_rename_mv_payload('test_mv_rename'))
        maskingview_module_mock.module_wo_sensitive_data = self.get_module_args
        self.rename_mv_host(maskingview_module_mock, True)
        assert MockMaskingViewApi.get_rename_mv_exception_response('test_mv') == \
            maskingview_module_mock.module.fail_json.call_args[1]['msg']

    def test_maskingview_init_check_failed(self, maskingview_module_mock):
        with patch('ansible_collections.dellemc.powermax.plugins.modules.maskingview.HAS_PYU4V', False):
            with patch('ansible_collections.dellemc.powermax.plugins.modules.maskingview.PYU4V_VERSION_CHECK', "mock check err"):
                utils.get_U4V_connection = MagicMock(side_effect=Exception)
                maskingview_module_mock.show_error_exit = MagicMock()
                maskingview_module_mock.__init__()
                assert maskingview_module_mock.show_error_exit.call_count == 3
