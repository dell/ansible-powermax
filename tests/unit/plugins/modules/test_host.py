# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Host module on PowerMax"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_host_api import (
    MockHostApi,
)
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell import utils
from ansible.module_utils import basic


utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_U4V_connection = MagicMock()
basic.AnsibleModule = MagicMock()


from ansible_collections.dellemc.powermax.plugins.modules.host import Host
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestHost(PowerMaxUnitBase):
    host_args = MockHostApi.HOST_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return Host

    def test_host_init_check_failed(self, powermax_module_mock):
        with patch(
            "ansible_collections.dellemc.powermax.plugins.modules.host.HAS_PYU4V",
            False,
        ):
            with patch(
                "ansible_collections.dellemc.powermax.plugins.modules.host.PYU4V_VERSION_CHECK",
                "mock check err",
            ):
                utils.get_U4V_connection = MagicMock(side_effect=MockApiException())
                powermax_module_mock.show_error_exit = MagicMock()
                powermax_module_mock.__init__()
                assert powermax_module_mock.show_error_exit.call_count == 3

    def test_get_host_exception(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update({"host_name": "test_host"})
        powermax_module_mock.provisioning.get_host = MagicMock(
            side_effect=MockApiException
        )
        powermax_module_mock.perform_module_operation()

    def test_create_host(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "volume_set_addressing": "unset",
                    "disable_q_reset_on_ua": False,
                    "consistent_lun": True,
                },
            }
        )
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host.assert_called()

    def test_create_host_check_mode_disabe_consistent_lun(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "volume_set_addressing": "unset",
                    "disable_q_reset_on_ua": False,
                    "consistent_lun": False,
                },
            }
        )
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host.assert_not_called()

    def test_create_host_no_name(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("create_host_empty_name"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_host_with_type(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "host_type": "default"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host.assert_called()

    def test_create_host_new_name(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "new_name": "test_host_new_name"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("create_host_new_name"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_host_init_absent(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "initiator_state": "absent-in-host"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("create_host_init_absent"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_host_check_mode(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update({"host_name": "test_host"})
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_host.assert_not_called()

    def test_create_host_exception(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update({"host_name": "test_host"})
        powermax_module_mock.provisioning.get_host = MagicMock(return_value={})
        powermax_module_mock.provisioning.create_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("create_host"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_rename_host(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "new_name": "test_host_new", "host_type": "hpux"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_rename_host_exception(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "new_name": "test_host_new"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.provisioning.modify_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("rename_host"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_rename_host_check_mode(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "new_name": "test_host_new", "host_type": "hpux"}
        )
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_not_called()

    def test_rename_host_same_name(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "new_name": "test_host"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_not_called()

    def test_rename_host_empty_name(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "new_name": ""}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("rename_host_empty_name"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_host_host_flags(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "volume_set_addressing": "unset",
                    "disable_q_reset_on_ua": False,
                },
            }
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_exception(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "new_name": "test_host_new", "host_type": "hpux"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.provisioning.modify_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("modify_host"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_invalid_initiators_to_host(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {
                "host_name": "test_host",
                "initiators": ["invalid_initiator"],
                "initiator_state": "present-in-host",
            }
        )
        self.capture_fail_json_method(
            MockHostApi.get_initiator_exception_response("invalid_initiator"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_host_flags_no_change(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update(
            {
                "enabled_flags": "spc2_protocol_version",
                "disabled_flags": "disable_q_reset_on_ua",
            }
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=host_response
        )
        powermax_module_mock.module_wo_sensitive_data.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "disable_q_reset_on_ua": False,
                    "consistent_lun": False,
                },
            }
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_not_called()

    def test_modify_host_flags_enable_consistent_lun(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "host_flags": {"consistent_lun": True}}
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_flags_disable_consistent_lun(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update({"consistent_lun": True})
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=host_response
        )
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "host_flags": {"consistent_lun": False}}
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_flags(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update(
            {
                "enabled_flags": "spc2_protocol_version",
                "disabled_flags": "disable_q_reset_on_ua",
            }
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=host_response
        )
        powermax_module_mock.module_wo_sensitive_data.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": False,
                    "disable_q_reset_on_ua": True,
                },
            }
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_flags_check_mode(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module.check_mode = True
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update(
            {
                "enabled_flags": "spc2_protocol_version",
                "disabled_flags": "disable_q_reset_on_ua",
            }
        )
        powermax_module_mock.module_wo_sensitive_data.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": False,
                    "disable_q_reset_on_ua": True,
                },
            }
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=host_response
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_not_called()

    def test_delete_host(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "state": "absent"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_host.assert_called()

    def test_delete_host_check_mode(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module_wo_sensitive_data.update(
            {"host_name": "test_host", "state": "absent"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_host.assert_not_called()

    def test_delete_host_exception(self, powermax_module_mock):
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"state": "absent", "host_name": "test_host"}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.provisioning.delete_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostApi.get_host_exception_response("delete_host"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_show_error_exception(self, powermax_module_mock):
        msg = "Error message"
        utils.close_connection = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            "Error message",
            powermax_module_mock,
            "show_error_exit",
            msg,
        )

    def test_add_initiators_to_host_split(self, powermax_module_mock):
        self.host_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"initiators": ["100xx000xxxxxxxx/200xx000xxxxxxxx"]}
        )
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_get_initiators_exception(self, powermax_module_mock):
        self.host_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update(
            {"initiators": ["100xx000xxxxxxxx/200xx000xxxxxxxx"]}
        )
        powermax_module_mock.provisioning.get_initiator_list = MagicMock(
            return_value={}
        )
        self.capture_fail_json_method(
            MockHostApi.get_initiator_exception_response("get_initiators_alias"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_initiators_to_host(self, powermax_module_mock):
        self.host_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_add_initiators_to_host_check_mode(self, powermax_module_mock):
        self.host_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_not_called()

    def test_add_initiators_to_host_existing(self, powermax_module_mock):
        self.host_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module_wo_sensitive_data.update({"initiators": ["100xx000xxxxxxxx"]})
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_not_called()

    def test_add_empty_initiator_list_to_host(self, powermax_module_mock):
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        assert powermax_module_mock.add_host_initiators("test_host", []) is False

    def test_add_initiators_to_host_exception(self, powermax_module_mock):
        self.host_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.provisioning.modify_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostApi.get_initiator_exception_response("add_initiators_to_host"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_initiators_from_host(self, powermax_module_mock):
        self.host_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_called()

    def test_remove_initiators_from_host_check_mode(self, powermax_module_mock):
        self.host_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_host.assert_not_called()

    def test_remove_empty_initiator_list_from_host(self, powermax_module_mock):
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        assert powermax_module_mock.remove_host_initiators("test_host", []) is False

    def test_remove_initiator_from_empty_host(self, powermax_module_mock):
        self.host_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update({"initiators": []})
        powermax_module_mock.module.provisioning.get_host = MagicMock(
            return_value=host_response
        )
        assert powermax_module_mock.remove_host_initiators("test_host", []) is False

    def test_remove_initiators_from_host_exception(self, powermax_module_mock):
        self.host_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        powermax_module_mock.module_wo_sensitive_data = self.host_args
        powermax_module_mock.provisioning.get_host = MagicMock(
            return_value=MockHostApi.GET_HOST_API_RESPONSE
        )
        powermax_module_mock.provisioning.modify_host = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockHostApi.get_initiator_exception_response("remove_initiators_from_host"),
            powermax_module_mock,
            "perform_module_operation",
        )
