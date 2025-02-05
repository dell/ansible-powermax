# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Host module on PowerMax"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_host_api import MockHostApi
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
from ansible_collections.dellemc.powermax.plugins.modules.host import Host


class TestHost():

    get_module_args = MockHostApi.HOST_COMMON_ARGS

    @pytest.fixture
    def host_module_mock(self, mocker):
        host_module_mock = Host()
        host_module_mock.module.check_mode = False
        return host_module_mock

    def mock_get_host(self, host_module_mock, call_exception=False):
        if not call_exception:
            host_module_mock.provisioning.get_host = MagicMock(return_value=MockHostApi.GET_HOST_API_RESPONSE)
        else:
            host_module_mock.provisioning.get_host = MagicMock(side_effect=Exception)

    def mock_modify_host(self, host_module_mock, call_exception=False):
        if not call_exception:
            host_module_mock.provisioning.get_host = MagicMock(return_value=MockHostApi.GET_HOST_API_RESPONSE)
        else:
            host_module_mock.provisioning.modify_host = MagicMock(side_effect=Exception)

    def update_initiators(self, host_module_mock, call_exception=False):
        self.mock_get_host(host_module_mock)
        self.mock_modify_host(host_module_mock, call_exception)
        host_module_mock.perform_module_operation()

    def test_get_host_exception(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"host_name": "test_host"})
        host_module_mock.provisioning.get_host = MagicMock(side_effect=Exception)
        host_module_mock.perform_module_operation()

    def test_create_host(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_flags": {
                "spc2_protocol_version": True,
                "volume_set_addressing": "unset",
                "disable_q_reset_on_ua": False,
                "consistent_lun": True
            }})
        host_module_mock.provisioning.get_host = MagicMock(return_value={})
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.create_host.assert_called()

    def test_create_host_check_mode_disabe_consistent_lun(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_flags": {
                "spc2_protocol_version": True,
                "volume_set_addressing": "unset",
                "disable_q_reset_on_ua": False,
                "consistent_lun": False
            }})
        host_module_mock.module.check_mode = True
        host_module_mock.provisioning.get_host = MagicMock(return_value={})
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.create_host.assert_not_called()

    def test_create_host_with_type(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"host_type": "default"})
        host_module_mock.provisioning.get_host = MagicMock(return_value={})
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.create_host.assert_called()

    def test_create_host_new_name(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "new_name": "test_host_new_name"
        })
        host_module_mock.provisioning.get_host = MagicMock(return_value={})
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_exception_response('create_host_new_name') == \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_host_init_absent(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "initiator_state": "absent-in-host"
        })
        host_module_mock.provisioning.get_host = MagicMock(return_value={})
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_exception_response('create_host_init_absent') == \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_create_host_check_mode(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.check_mode = True
        host_module_mock.provisioning.get_host = MagicMock(return_value={})
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.create_host.assert_not_called()

    def test_create_host_exception(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"host_name": "test_host"})
        host_module_mock.provisioning.get_host = MagicMock(return_value={})
        host_module_mock.provisioning.create_host = MagicMock(side_effect=Exception)
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_exception_response('create_host') == \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_rename_host(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_name": "test_host",
            "new_name": "test_host_new",
            "host_type": "hpux"})
        self.mock_get_host(host_module_mock)
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_called()

    def test_rename_host_check_mode(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_name": "test_host",
            "new_name": "test_host_new",
            "host_type": "hpux"})
        host_module_mock.module.check_mode = True
        self.mock_get_host(host_module_mock)
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_not_called()

    def test_rename_host_same_name(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_name": "test_host",
            "new_name": "test_host"})
        self.mock_get_host(host_module_mock)
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_not_called()

    def test_rename_host_empty_name(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_name": "test_host",
            "new_name": ""})
        self.mock_get_host(host_module_mock)
        host_module_mock.perform_module_operation()
        assert MockHostApi.get_host_exception_response('rename_host_empty_name') == \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_host_host_flags(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_name": "test_host",
            "host_flags": {
                "spc2_protocol_version": True,
                "volume_set_addressing": "unset",
                "disable_q_reset_on_ua": False,
            }})
        self.mock_get_host(host_module_mock)
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_exception(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({
            "host_name": "test_host",
            "new_name": "test_host_new",
            "host_type": "hpux"})
        self.mock_get_host(host_module_mock)
        host_module_mock.provisioning.modify_host = MagicMock(side_effect=Exception)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.fail_json.call_args[1].get('msg') == \
            MockHostApi.get_host_exception_response('modify_host')

    def test_add_invalid_initiators_to_host(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"initiators": ["invalid_initiator"],
                                               "initiator_state": "present-in-host"})
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.fail_json.call_args[1].get('msg') == \
            MockHostApi.get_initiator_exception_response('invalid_initiator')

    def test_modify_host_flags_no_change(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update({"enabled_flags": "spc2_protocol_version", "disabled_flags": "disable_q_reset_on_ua"})
        host_module_mock.provisioning.get_host = MagicMock(return_value=host_response)
        host_module_mock.module.params.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": True,
                    "disable_q_reset_on_ua": False,
                    "consistent_lun": False,
                },
            }
        )
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_not_called()

    def test_modify_host_flags_enable_consistent_lun(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.provisioning.get_host = MagicMock(return_value=MockHostApi.GET_HOST_API_RESPONSE)
        host_module_mock.module.params.update({"host_name": "test_host",
                                               "host_flags": {"consistent_lun": True}})
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_flags_disable_consistent_lun(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update({"consistent_lun": True})
        host_module_mock.provisioning.get_host = MagicMock(return_value=host_response)
        host_module_mock.module.params.update({"host_name": "test_host",
                                               "host_flags": {"consistent_lun": False}})
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_flags(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update({"enabled_flags": "spc2_protocol_version", "disabled_flags": "disable_q_reset_on_ua"})
        host_module_mock.provisioning.get_host = MagicMock(return_value=host_response)
        host_module_mock.module.params.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": False,
                    "disable_q_reset_on_ua": True,
                },
            }
        )
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_called()

    def test_modify_host_flags_check_mode(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.check_mode = True
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update({"enabled_flags": "spc2_protocol_version", "disabled_flags": "disable_q_reset_on_ua"})
        host_module_mock.provisioning.get_host = MagicMock(return_value=host_response)
        host_module_mock.module.params.update(
            {
                "host_name": "test_host",
                "host_flags": {
                    "spc2_protocol_version": False,
                    "disable_q_reset_on_ua": True,
                },
            }
        )
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.modify_host.assert_not_called()

    def test_delete_host(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"state": "absent"})
        self.mock_get_host(host_module_mock)
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.delete_host.assert_called()

    def test_delete_host_check_mode(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.check_mode = True
        host_module_mock.module.params.update({"state": "absent"})
        self.mock_get_host(host_module_mock)
        host_module_mock.perform_module_operation()
        host_module_mock.provisioning.delete_host.assert_not_called()

    def test_delete_host_exception(self, host_module_mock):
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"state": "absent", "host_name": "test_host"})
        self.mock_get_host(host_module_mock)
        host_module_mock.provisioning.delete_host = MagicMock(side_effect=Exception)
        host_module_mock.perform_module_operation()
        assert host_module_mock.module.fail_json.call_args[1].get('msg') is not None

    def test_show_error_exception(self, host_module_mock):
        msg = "Error message"
        utils.close_connection = MagicMock(
            side_effect=Exception)
        host_module_mock.show_error_exit(msg)
        assert host_module_mock.module.fail_json.call_args[1].get('msg') == msg

    def test_add_initiators_to_host_split(self, host_module_mock):
        self.get_module_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"initiators": ["100xx000xxxxxxxx/200xx000xxxxxxxx"]})
        self.update_initiators(host_module_mock)
        host_module_mock.provisioning.modify_host.assert_called()

    def test_get_initiators_exception(self, host_module_mock):
        self.get_module_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"initiators": ["100xx000xxxxxxxx/200xx000xxxxxxxx"]})
        host_module_mock.provisioning.get_initiator_list = MagicMock(return_value={})
        self.update_initiators(host_module_mock)
        assert host_module_mock.module.fail_json.call_args[1].get('msg') == \
            MockHostApi.get_initiator_exception_response('get_initiators_alias')

    def test_add_initiators_to_host(self, host_module_mock):
        self.get_module_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        self.update_initiators(host_module_mock)
        host_module_mock.provisioning.modify_host.assert_called()

    def test_add_initiators_to_host_check_mode(self, host_module_mock):
        self.get_module_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.check_mode = True
        self.update_initiators(host_module_mock)
        host_module_mock.provisioning.modify_host.assert_not_called()

    def test_add_initiators_to_host_existing(self, host_module_mock):
        self.get_module_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.params.update({"initiators": ["100xx000xxxxxxxx"]})
        self.update_initiators(host_module_mock)
        host_module_mock.provisioning.modify_host.assert_not_called()

    def test_add_empty_initiator_list_to_host(self, host_module_mock):
        self.mock_get_host(host_module_mock)
        assert host_module_mock.add_host_initiators("test_host", []) is False

    def test_add_initiators_to_host_exception(self, host_module_mock):
        self.get_module_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        self.update_initiators(host_module_mock, True)
        assert MockHostApi.get_initiator_exception_response('add_initiators_to_host') == \
            host_module_mock.module.fail_json.call_args[1]['msg']

    def test_remove_initiators_from_host(self, host_module_mock):
        self.get_module_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        self.update_initiators(host_module_mock)
        host_module_mock.provisioning.modify_host.assert_called()

    def test_remove_initiators_from_host_check_mode(self, host_module_mock):
        self.get_module_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        host_module_mock.module.check_mode = True
        self.update_initiators(host_module_mock)
        host_module_mock.provisioning.modify_host.assert_not_called()

    def test_remove_empty_initiator_list_from_host(self, host_module_mock):
        self.mock_get_host(host_module_mock)
        assert host_module_mock.remove_host_initiators("test_host", []) is False

    def test_remove_initiator_from_empty_host(self, host_module_mock):
        self.get_module_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        host_response = MockHostApi.GET_HOST_API_RESPONSE
        host_response.update({"initiators": []})
        host_module_mock.module.provisioning.get_host = MagicMock(return_value=host_response)
        assert host_module_mock.remove_host_initiators("test_host", []) is False

    def test_remove_initiators_from_host_exception(self, host_module_mock):
        self.get_module_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        self.update_initiators(host_module_mock, True)
        assert MockHostApi.get_initiator_exception_response('remove_initiators_from_host') == \
            host_module_mock.module.fail_json.call_args[1]['msg']
