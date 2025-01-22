# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell import utils


utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.universion_check = MagicMock(return_value={"is_valid_universion": True})
utils.get_U4V_connection = MagicMock()
utils.close_connection = MagicMock()
from ansible.module_utils import basic

basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.powermax.plugins.modules.hostgroup import HostGroup
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_hostgroup_api import (
    MockHostGroupApi,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestHostGroup(PowerMaxUnitBase):
    host_group_args = MockHostGroupApi.HOST_GROUP_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return HostGroup

    def test_hostgroup_init_check_failed(self, powermax_module_mock):
        with patch('ansible_collections.dellemc.powermax.plugins.modules.hostgroup.HAS_PYU4V', False):
            with patch('ansible_collections.dellemc.powermax.plugins.modules.hostgroup.PYU4V_VERSION_CHECK', "mock check err"):
                utils.universion_check = MagicMock(return_value={
                    "is_valid_universion": False, "user_message": "mock user msg"})
                utils.get_U4V_connection = MagicMock(side_effect=MockApiException())
                powermax_module_mock.show_error_exit = MagicMock()
                powermax_module_mock.__init__()
                assert powermax_module_mock.show_error_exit.call_count == 4

    def test_get_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.get_host_group.assert_called()

    def test_get_host_group_empty_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"hostgroup_name": ""})
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message("empty_hostgroup_name"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_get_host_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message("get_hostgroup_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_empty_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host.assert_called()

    def test_create_empty_host_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "consistent_lun": True,
                    "volume_set_addressing": "unset",
                    "disable_q_reset_on_ua": False,
                    "openvms": "unset",
                },
            }
        )
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host.assert_not_called()

    def test_create_host_group_with_new_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"new_name": "test_hostgroup_new"})
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message("invalid_new_name_arg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_host_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        powermax_module_mock.provisioning.create_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message(
                "create_host_exception", "test_hostgroup"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "consistent_lun": True,
                    "volume_set_addressing": "unset",
                    "disable_q_reset_on_ua": False,
                    "openvms": "unset",
                },
            }
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host_group.assert_called()

    def test_create_host_group_removing_hosts(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"hosts": ["ansible_test_host"], "host_state": "absent-in-group"}
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message(
                "remove_host_during_creation", "test_hostgroup"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_host_group_get_host_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "consistent_lun": True,
                    "volume_set_addressing": "unset",
                    "disable_q_reset_on_ua": False,
                    "openvms": "unset",
                },
            }
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        powermax_module_mock.provisioning.get_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message(
                "get_host_exception_while_creation", "test_hostgroup"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_host_group_different_flags(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_flags": {
                    "consistent_lun": False,
                },
            }
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host_group.assert_called()

    def test_create_host_group_with_host_type(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_type": "default",
            }
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(return_value=None)
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host_group.assert_called()

    def test_rename_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"new_name": "test_hostgroup_new"})
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_rename_host_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"new_name": "test_hostgroup_new"})
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_rename_host_group_same_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"new_name": "test_hostgroup"})
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_rename_host_group_empty_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"new_name": ""})
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message("rename_same_name", "test_hostgroup"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_rename_host_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"new_name": "test_hostgroup_new"})
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.provisioning.modify_host_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message("rename_exception", "test_hostgroup"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_host_to_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_type": "hpux",
            }
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_add_host_to_host_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_type": "hpux",
            }
        )
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_add_host_to_host_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_type": "hpux",
            }
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.provisioning.modify_host_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message("add_host_exception", "test_hostgroup"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_host_to_empty_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "present-in-group",
                "host_type": "hpux",
            }
        )
        host_group_response = MockHostGroupApi.HOST_GROUP_RESPONSE
        host_group_response.pop("host")
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=host_group_response
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_add_existing_host_to_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"hosts": ["test_hg_host"], "host_state": "present-in-group"}
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_add_none_host_to_host_group(self, powermax_module_mock):
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        assert (
            powermax_module_mock.add_hosts_to_hostgroup("test_hostgroup", []) is False
        )
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_remove_host_from_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"hosts": ["test_hg_host"], "host_state": "absent-in-group"}
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_remove_host_from_host_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"hosts": ["test_hg_host"], "host_state": "absent-in-group"}
        )
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_remove_host_from_host_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"hosts": ["test_hg_host"], "host_state": "absent-in-group"}
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.provisioning.modify_host_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            "test_hostgroup", powermax_module_mock, "perform_module_operation"
        )

    def test_remove_host_from_empty_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "hosts": ["ansible_test_host"],
                "host_state": "absent-in-group",
                "host_type": "hpux",
            }
        )
        host_group_response = MockHostGroupApi.HOST_GROUP_RESPONSE
        host_group_response.pop("host")
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=host_group_response
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_remove_no_host_from_host_group(self, powermax_module_mock):
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        assert (
            powermax_module_mock.remove_hosts_from_hostgroup("test_hostgroup", [])
            is False
        )
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_modify_host_group_flags(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {
                "host_flags": {
                    "spc2_protocol_version": True,
                    "consistent_lun": True,
                    "volume_set_addressing": "unset",
                    "disable_q_reset_on_ua": False,
                    "openvms": True,
                }
            }
        )
        host_group_response = MockHostGroupApi.HOST_GROUP_RESPONSE
        host_group_response.update(
            {
                "enabled_flags": "openvms,disable_q_reset_on_ua",
                "disabled_flags": "spc2_protocol_version",
            }
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=host_group_response
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_modify_host_group_flags_inital_set(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"host_flags": {"spc2_protocol_version": True}}
        )
        host_group_response = MockHostGroupApi.HOST_GROUP_RESPONSE
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=host_group_response
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_modify_host_group_flags_disable_consistent_lun(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"host_flags": {"consistent_lun": False}}
        )
        host_group_response = MockHostGroupApi.HOST_GROUP_RESPONSE
        host_group_response.update({"consistent_lun": True})
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=host_group_response
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_called()

    def test_modify_host_group_flags_no_change(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update(
            {"host_flags": {"openvms": True, "spc2_protocol_version": False}}
        )
        host_group_response = MockHostGroupApi.HOST_GROUP_RESPONSE
        host_group_response.update(
            {"enabled_flags": "openvms", "disabled_flags": "spc2_protocol_version"}
        )
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=host_group_response
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_modify_host_group_flags_no_type_no_flags(self, powermax_module_mock):
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        assert powermax_module_mock.modify_host_flags("test_hostgroup") is False
        powermax_module_mock.provisioning.modify_host_group.assert_not_called()

    def test_delete_host_group(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_host_group.assert_called()

    def test_delete_host_group_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_host_group.assert_not_called()

    def test_delete_host_group_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.host_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.provisioning.get_host_group = MagicMock(
            return_value=MockHostGroupApi.HOST_GROUP_RESPONSE
        )
        powermax_module_mock.provisioning.delete_host_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostGroupApi.get_error_message(
                "delete_hostgroup_exception", "test_hostgroup"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_show_error_exception(self, powermax_module_mock):
        msg = "Error message"
        utils.close_connection = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(msg, powermax_module_mock, "show_error_exit", msg)
