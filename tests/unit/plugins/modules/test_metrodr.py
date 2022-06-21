# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for MetroDR module on PowerMax"""

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
utils.close_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()


from ansible_collections.dellemc.powermax.plugins.modules.metrodr import MetroDR


class TestMetroDR():
    MODULE_PATH = 'ansible_collections.dellemc.powermax.plugins.modules.metrodr.MetroDR.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell.utils'
    metro_args = {'sg_name': 'test_sg', 'env_name': 'None', 'state': 'present',
                  'metro_r1_array_id': None, 'metro_r2_array_id': None, 'dr_array_id': None, 'replication_mode': None,
                  'wait_for_completion': None, 'new_rdf_group_r1': None, 'new_rdf_group_r2': None, 'remove_r1_dr_rdfg': None,
                  'srdf_param': None}

    @pytest.fixture
    def metro_module_mock(self, mocker):
        mocker.patch(self.MODULE_PATH + '__init__', return_value=None)
        metro_module_mock = MetroDR()
        metro_module_mock.module = MagicMock()
        metro_module_mock.module.check_mode = False
        metro_module_mock.provisioning = MagicMock()
        metro_module_mock.metro = MagicMock()
        return metro_module_mock

    def test_get_metro_session(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.perform_module_operation()
        assert metro_module_mock.module.exit_json.call_args[1]["changed"] is False

    def test_create_metro_session(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'Asynchronous'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.get_metrodr_env = MagicMock(return_value=None)
        metro_module_mock.get_storage_group_details = MagicMock(return_value={"unprotected": True, "sg_name": "Test"})
        metro_module_mock.perform_module_operation()
        assert metro_module_mock.module.exit_json.call_args[1]["changed"]

    def test_invalid_create_metro_session(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.get_metrodr_env = MagicMock(return_value=None)
        metro_module_mock.get_storage_group_details = MagicMock(return_value={"unprotected": True, "sg_name": "Test"})
        metro_module_mock.perform_module_operation()
        assert "Please provide value for: 'replication_mode'" in metro_module_mock.module.fail_json.call_args[1]['msg']
