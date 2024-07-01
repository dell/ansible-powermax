# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Info module on PowerMax"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_info_api import MockInfoApi
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
from ansible_collections.dellemc.powermax.plugins.modules.info import Info


class TestInfo():

    get_module_args = MockInfoApi.INFO_COMMON_ARGS

    @pytest.fixture
    def info_module_mock(self, mocker):
        info_module_mock = Info()
        info_module_mock.module.check_mode = False
        return info_module_mock

    def test_get_mv_connections(self, info_module_mock):
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "logged_in",
                    "filter_operator": "equal",
                    "filter_value": "True"
                },
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "equal",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['mv_connections']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.get_masking_view_list = MagicMock(
            return_value=MockInfoApi.MASKING_VIEW_LIST
        )
        info_module_mock.provisioning.get_masking_view_connections = MagicMock(
            return_value=MockInfoApi.MASKING_VIEW_CONNECTIONS_LIST
        )
        info_module_mock.perform_module_operation()
        info_module_mock.get_masking_view_list.assert_called()
        info_module_mock.provisioning.get_masking_view_connections.assert_called()

    def test_get_mv_connections_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "logged_in",
                    "filter_operator": "equal",
                    "filter_value": "True"
                },
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "equal",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['mv_connections']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.get_masking_view_list = MagicMock(
            return_value=MockInfoApi.MASKING_VIEW_LIST
        )
        info_module_mock.provisioning.get_masking_view_connections = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_details_mv_connections') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_volume_details(self, info_module_mock):
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "equal",
                    "filter_value": "10"
                }
            ],
            'gather_subset': ['vol']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.get_volume_list = MagicMock(
            return_value=MockInfoApi.VOLUME_LIST
        )
        info_module_mock.provisioning.get_volume = MagicMock(return_value=MockInfoApi.VOLUME_DETAILS_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.get_volume_list.assert_called()

    def test_get_volume_details_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "equal",
                    "filter_value": "10"
                }
            ],
            'gather_subset': ['vol']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_volume_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.provisioning.get_volume = MagicMock(return_value=MockInfoApi.VOLUME_DETAILS_LIST)
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_volume_details') in info_module_mock.module.fail_json.call_args[1]['msg']
