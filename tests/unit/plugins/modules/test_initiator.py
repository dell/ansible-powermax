# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Initiator module on PowerMax"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.universion_check = MagicMock(return_value={"is_valid_universion": True})
utils.get_U4V_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()


from ansible_collections.dellemc.powermax.plugins.modules.initiator import Initiator
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils \
    import mock_initiator_api as MockInitiatorApi


class TestPowerMaxInitiator():
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell.utils'
    initiator_args = {'universion': None, 'initiator_id': '1000000000000001', 'state': 'present',
                      'alias': None, 'new_alias': None}

    @pytest.fixture
    def initiator_module_mock(self):
        initiator_module_mock = Initiator()
        initiator_module_mock.provisioning.get_initiator_list \
            = MagicMock(return_value=MockInitiatorApi.get_initiator_id())
        initiator_module_mock.provisioning.get_initiator \
            = MagicMock(return_value=MockInitiatorApi.get_initiator_details())
        return initiator_module_mock

    def test_get_initiator_details(self, initiator_module_mock):
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.perform_module_operation()
        assert (MockInitiatorApi.get_initiator_details()
                == initiator_module_mock.module.exit_json.call_args[1]["initiator_details"])
        assert initiator_module_mock.module.exit_json.call_args[1]["changed"] is False

    def test_rename_initiator_alias(self, initiator_module_mock):
        self.initiator_args.update({'new_alias': {'new_node_name': 'None', 'new_port_name': 'hostHBA'}})
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.provisioning.modify_initiator \
            = MagicMock(return_value=True)
        initiator_module_mock.perform_module_operation()
        assert initiator_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_set_initiator_alias(self, initiator_module_mock):
        self.initiator_args.update({'new_alias': {'new_node_name': 'testHBA', 'new_port_name': 'hostHBA'}})
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.provisioning.get_initiator \
            = MagicMock(return_value=MockInitiatorApi.get_initiator_details_without_alias())
        initiator_module_mock.provisioning.modify_initiator \
            = MagicMock(return_value=True)
        initiator_module_mock.perform_module_operation()
        assert initiator_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_invalid_initiator_alias(self, initiator_module_mock):
        self.initiator_args.update({'new_alias': {'new_node_name': 'testHBA', 'new_port_name': ''}})
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.perform_module_operation()
        assert initiator_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInitiatorApi.get_invalid_port_name()

    def test_invalid_initiator_alias_port_name(self, initiator_module_mock):
        self.initiator_args.update({'new_alias': {'new_node_name': 'testHBA', 'new_port_name': None}})
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.provisioning.get_initiator \
            = MagicMock(return_value=MockInitiatorApi.get_initiator_details_without_alias())
        initiator_module_mock.perform_module_operation()
        assert initiator_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInitiatorApi.get_invalid_port_name()

    def test_invalid_initiator_alias_node_name(self, initiator_module_mock):
        self.initiator_args.update({'new_alias': {'new_node_name': None, 'new_port_name': 'testHBA'}})
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.provisioning.get_initiator \
            = MagicMock(return_value=MockInitiatorApi.get_initiator_details_without_alias())
        initiator_module_mock.perform_module_operation()
        assert initiator_module_mock.module.fail_json.call_args[1]['msg'] == \
            MockInitiatorApi.get_invalid_node_name()

    def test_modify_initiator_exception(self, initiator_module_mock):
        self.initiator_args.update({'new_alias': {'new_node_name': 'testHBA', 'new_port_name': ''}})
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.provisioning.modify_initiator \
            = MagicMock(side_effect=Exception)
        initiator_module_mock.perform_module_operation()
        assert MockInitiatorApi.get_modify_ex_msg() in \
            initiator_module_mock.module.fail_json.call_args[1]['msg']

    def test_invalid_initiator_state(self, initiator_module_mock):
        self.initiator_args.update({'state': 'absent'})
        initiator_module_mock.module.params = self.initiator_args
        initiator_module_mock.perform_module_operation()
        assert MockInitiatorApi.get_invalid_state_msg() in \
            initiator_module_mock.module.fail_json.call_args[1]['msg']
