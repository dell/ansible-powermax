# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils


utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_U4V_connection = MagicMock()
utils.close_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.powermax.plugins.modules.port import Port
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_port_api import MockPortApi
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base \
    import PowerMaxUnitBase


class TestPort(PowerMaxUnitBase):
    port_args = MockPortApi.PORT_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return Port

    def test_port_init_check_failed(self, powermax_module_mock):
        with patch('ansible_collections.dellemc.powermax.plugins.modules.port.HAS_PYU4V', False):
            with patch('ansible_collections.dellemc.powermax.plugins.modules.port.PYU4V_VERSION_CHECK', "mock check err"):
                utils.get_U4V_connection = MagicMock(side_effect=MockApiException())
                powermax_module_mock.show_error_exit = MagicMock()
                powermax_module_mock.__init__()
                assert powermax_module_mock.show_error_exit.call_count == 3

    def test_get_port(self, powermax_module_mock):
        self.port_args.update(
            {"ports": [{"director_id": "FA-1D", "port_id": "5"}]})
        powermax_module_mock.module.params = self.port_args
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.get_director_port.assert_called()
        assert powermax_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_get_port_no_director(self, powermax_module_mock):
        self.port_args.update(
            {"ports": [{"director_id": "FA-1D", "port_id": "5"}, {"director_id": "FA-2D", "port_id": ""}]})
        powermax_module_mock.module.params = self.port_args
        powermax_module_mock.provisioning.get_director_port = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockPortApi.get_error_message(
                'missing_mandatory_args'), powermax_module_mock,
            'perform_module_operation')

    def test_get_port_exception(self, powermax_module_mock):
        self.port_args.update(
            {"ports": [{"director_id": "FA-1D", "port_id": "5"}]})
        powermax_module_mock.module.params = self.port_args
        powermax_module_mock.provisioning.get_director_port = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockPortApi.get_error_message(
                'get_port_exception', director_id="FA-1D", port_id="5"), powermax_module_mock,
            'perform_module_operation')

    def test_show_error_exception(self, powermax_module_mock):
        msg = "Error message"
        utils.close_connection = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(msg, powermax_module_mock, 'show_error_exit', msg)
