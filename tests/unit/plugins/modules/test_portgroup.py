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

from ansible_collections.dellemc.powermax.plugins.modules.portgroup import PortGroup
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_portgroup_api import MockPortGroupApi
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base \
    import PowerMaxUnitBase


class TestPortGroup(PowerMaxUnitBase):
    port_group_args = MockPortGroupApi.PORT_GROUP_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return PortGroup

    def test_portgroup_init_check_failed(self, powermax_module_mock):
        with patch('ansible_collections.dellemc.powermax.plugins.modules.portgroup.HAS_PYU4V', False):
            with patch('ansible_collections.dellemc.powermax.plugins.modules.portgroup.PYU4V_VERSION_CHECK', "mock check err"):
                utils.get_U4V_connection = MagicMock(side_effect=MockApiException())
                powermax_module_mock.show_error_exit = MagicMock()
                powermax_module_mock.__init__()
                assert powermax_module_mock.show_error_exit.call_count == 3

    def test_get_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.get_port_group.assert_called()

    def test_create_port_group_invalid_port_state(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-1D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "absent-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockPortGroupApi.get_error_message('invalid_port_state'), powermax_module_mock,
            'perform_module_operation')

    def test_create_port_group_no_ports_v4(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value={})
        utils.is_array_v4 = MagicMock(return_value=True)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_empty_port_group.assert_called()

    def test_create_port_group_with_ports_v4(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-1D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "present-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value={})
        utils.is_array_v4 = MagicMock(return_value=True)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_new_port_group.assert_called()

    def test_create_port_group_no_ports_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value={})
        utils.is_array_v4 = MagicMock(return_value=True)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_empty_port_group.assert_not_called()

    def test_create_port_group_no_ports_not_v4(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value={})
        utils.is_array_v4 = MagicMock(return_value=False)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_multiport_port_group.assert_called()

    def test_create_port_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-1D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "present-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(side_effect=MockApiException)
        powermax_module_mock.provisioning.create_new_port_group = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockPortGroupApi.get_error_message(
                'create_portgroup_exception', portgroup_name="test_portgroup"), powermax_module_mock,
            'perform_module_operation')

    def test_add_port_to_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-1D", "port_id": "10"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "present-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_called()

    def test_add_port_to_port_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-1D", "port_id": "10"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "present-in-group"})
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_not_called()

    def test_add_existing_port_to_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-2D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "present-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_not_called()

    def test_add_port_to_empty_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-1D", "port_id": "10"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "present-in-group"})
        empty_portgroup_response = MockPortGroupApi.PORT_GROUP_RESPONSE
        empty_portgroup_response.pop("symmetrixPortKey")
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=empty_portgroup_response)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_called()

    def test_add_port_to_port_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-1D", "port_id": "10"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "present-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.provisioning.modify_port_group = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockPortGroupApi.get_error_message(
                'add_port_exception', portgroup_name="test_portgroup"), powermax_module_mock,
            'perform_module_operation')

    def test_remove_port_from_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-2D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "absent-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_called()

    def test_remove_port_from_port_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-2D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "absent-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_not_called()

    def test_remove_non_existing_port_from_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-2D", "port_id": "10"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "absent-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_not_called()

    def test_remove_port_from_empty_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-2D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "absent-in-group"})
        empty_portgroup_response = MockPortGroupApi.PORT_GROUP_RESPONSE
        empty_portgroup_response.pop("symmetrixPortKey")
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=empty_portgroup_response)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_not_called()

    def test_remove_port_from_port_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"ports": [{"director_id": "FA-2D", "port_id": "5"}],
                                                   "port_group_protocol": "iSCSI",
                                                   "port_state": "absent-in-group"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.provisioning.modify_port_group = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockPortGroupApi.get_error_message(
                'remove_port_exception', portgroup_name="test_portgroup"), powermax_module_mock,
            'perform_module_operation')

    def test_rename_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"new_name": "test_portgroup_new"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_called()

    def test_rename_port_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params.update({"new_name": "test_portgroup_new"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_not_called()

    def test_rename_port_group_empty_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"new_name": ""})
        self.capture_fail_json_method(
            "test_portgroup", powermax_module_mock, 'modify_portgroup', "test_portgroup")

    def test_rename_port_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"new_name": "test_portgroup_new"})
        powermax_module_mock.provisioning.modify_port_group = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockPortGroupApi.get_error_message(
                'rename_portgroup_exception', portgroup_name="test_portgroup"), powermax_module_mock,
            'perform_module_operation')

    def test_rename_port_group_original_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"new_name": "test_portgroup"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_port_group.assert_not_called()

    def test_delete_port_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.provisioning.delete_port_group = MagicMock()
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_port_group.assert_called()

    def test_delete_port_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.provisioning.delete_port_group = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockPortGroupApi.get_error_message(
                'delete_portgroup_exception', portgroup_name="test_portgroup"), powermax_module_mock,
            'perform_module_operation')

    def test_delete_port_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.port_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_port_group = MagicMock(return_value=MockPortGroupApi.PORT_GROUP_RESPONSE)
        powermax_module_mock.provisioning.delete_port_group = MagicMock()
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_port_group.assert_not_called()

    def test_show_error_exception(self, powermax_module_mock):
        msg = "Error message"
        utils.close_connection = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(msg, powermax_module_mock, 'show_error_exit', msg)
