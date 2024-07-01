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

    def mock_get_host(self, host_module_mock):
        host_module_mock.provisioning.get_host = MagicMock(return_value=MockHostApi.GET_HOST_API_RESPONSE)

    def mock_modify_host(self, host_module_mock, call_exception=False):
        if not call_exception:
            host_module_mock.provisioning.get_host = MagicMock(return_value=MockHostApi.GET_HOST_API_RESPONSE)
        else:
            host_module_mock.provisioning.modify_host = MagicMock(side_effect=Exception)

    def update_initiators(self, host_module_mock, call_exception=False):
        self.mock_get_host(host_module_mock)
        self.mock_modify_host(host_module_mock, call_exception)
        host_module_mock.perform_module_operation()

    def test_add_initiators_to_host(self, host_module_mock):
        self.get_module_args.update(MockHostApi.ADD_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        self.update_initiators(host_module_mock)
        host_module_mock.provisioning.modify_host.assert_called()

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

    def test_remove_initiators_from_host_exception(self, host_module_mock):
        self.get_module_args.update(MockHostApi.REMOVE_INITIATOR_PAYLOAD)
        host_module_mock.module.params = self.get_module_args
        self.update_initiators(host_module_mock, True)
        assert MockHostApi.get_initiator_exception_response('remove_initiators_from_host') == \
            host_module_mock.module.fail_json.call_args[1]['msg']
