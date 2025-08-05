# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for MetroDR module on PowerMax"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_storagegroup_api import MockStorageGroupApi
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_metrodr_api import MockMetroDRApi
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_U4V_connection = MagicMock()
utils.close_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.powermax.plugins.modules.metrodr import MetroDR
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestMetroDR(PowerMaxUnitBase):
    MODULE_PATH = 'ansible_collections.dellemc.powermax.plugins.modules.metrodr.MetroDR.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell.utils'
    metro_args = {'sg_name': 'test_sg', 'env_name': 'None', 'state': 'present',
                  'metro_r1_array_id': None, 'metro_r2_array_id': None, 'dr_array_id': None, 'replication_mode': None,
                  'wait_for_completion': None, 'new_rdf_group_r1': None, 'new_rdf_group_r2': None, 'remove_r1_dr_rdfg': None,
                  'srdf_param': None}

    @pytest.fixture
    def metro_module_mock(self, mocker):
        metro_module_mock = MetroDR()
        metro_module_mock.module = MagicMock()
        metro_module_mock.module.check_mode = False
        metro_module_mock.provisioning = MagicMock()
        metro_module_mock.metro = MagicMock()
        return metro_module_mock

    @pytest.fixture
    def module_object(self):
        return MetroDR

    def test_init_check_failed(self, powermax_module_mock):
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
                assert powermax_module_mock.show_error_exit.call_count == 1

    def test_get_storage_group_details(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3', 'sg_name': 'test_sg'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.provisioning.get_storage_group = MagicMock(return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS)
        metro_module_mock.get_storage_group_details()
        metro_module_mock.provisioning.get_storage_group.assert_called()

        # Exception testing
        metro_module_mock.provisioning.get_storage_group = MagicMock(
            side_effect=Exception
        )
        metro_module_mock.get_storage_group_details()
        assert MockStorageGroupApi.get_exception_response('get_storage_group') in metro_module_mock.module.fail_json.call_args[1]['msg']

        # No storage group name testing
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.get_storage_group_details()
        assert MockStorageGroupApi.get_exception_response('get_storage_group') in metro_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_storage_group_srdf_group_list(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3', 'sg_name': 'test_sg'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_DETAILS)
        metro_module_mock.get_storage_group_srdf_group_list()
        metro_module_mock.replication.get_storage_group_srdf_group_list.assert_called()

        # Exception testing
        metro_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            side_effect=Exception
        )
        metro_module_mock.get_storage_group_srdf_group_list()
        assert MockMetroDRApi.get_exception_response('get_storage_group_srdf_group_list') in metro_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_storage_group_srdf_details(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3', 'sg_name': 'test_sg'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.replication.get_storage_group_srdf_details = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_DETAILS)
        metro_module_mock.get_storage_group_srdf_details('test_srdf_gr')
        metro_module_mock.replication.get_storage_group_srdf_details.assert_called()

        # Exception testing
        metro_module_mock.replication.get_storage_group_srdf_details = MagicMock(
            side_effect=Exception
        )
        metro_module_mock.get_storage_group_srdf_details('test_srdf_gr')
        assert MockMetroDRApi.get_exception_response('get_storage_group_srdf_details') in metro_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_rdf_group(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3', 'sg_name': 'test_sg'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.replication.get_rdf_group = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_DETAILS)
        metro_module_mock.get_rdf_group('test_gr')
        metro_module_mock.replication.get_rdf_group.assert_called()

        # Exception testing
        metro_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=Exception
        )
        metro_module_mock.get_rdf_group('test_gr')
        assert MockMetroDRApi.get_exception_response('get_rdf_group') in metro_module_mock.module.fail_json.call_args[1]['msg']

    def test_metrodr_delete_env(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '1.1.1.1', 'metro_r2_array_id': '2.2.2.2',
                                'dr_array_id': '3.3.3.3', 'sg_name': 'test_sg', 'state': 'absent'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.metro.delete_metrodr_environment = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_DETAILS)
        metro_module_mock.perform_module_operation()
        metro_module_mock.metro.delete_metrodr_environment.assert_called()

        # Exception testing
        metro_module_mock.metro.delete_metrodr_environment = MagicMock(
            side_effect=Exception
        )
        metro_module_mock.perform_module_operation()
        assert MockMetroDRApi.get_exception_response('delete_metrodr_env') in metro_module_mock.module.fail_json.call_args[1]['msg']

    def test_pre_checks(self, metro_module_mock):
        # Exception testing: SG should protected with srdf
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'sg_name': 'test_sg'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.get_storage_group_srdf_group_list = MagicMock(return_value=None)
        metro_module_mock.pre_checks_for_convert()
        assert MockMetroDRApi.get_exception_response('pre_check_srdf_group') in metro_module_mock.module.fail_json.call_args[1]['msg']

        # Run with Async mode
        metro_module_mock.get_storage_group_srdf_group_list = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_LIST)
        metro_module_mock.get_storage_group_srdf_details = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_DETAILS)
        metro_module_mock.get_rdf_group = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_DETAILS)

        metro_module_mock.pre_checks_for_convert()
        metro_module_mock.get_storage_group_srdf_group_list()
        metro_module_mock.get_storage_group_srdf_details()
        metro_module_mock.get_rdf_group()

        metro_module_mock.get_storage_group_srdf_details = MagicMock(return_value=MockMetroDRApi.STORAGE_GROUP_RDF_GROUP_VOLUME_ACTIVE_DETAILS)

        metro_module_mock.pre_checks_for_convert()
        metro_module_mock.get_storage_group_srdf_details()

    def test_convert_to_metrodr_env(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'sg_name': 'test_sg'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.metro.convert_to_metrodr_environment = MagicMock(return_value=None)
        metro_module_mock.pre_checks_for_convert = MagicMock(return_value=None)

        metro_module_mock.convert_to_metrodr_env()
        metro_module_mock.metro.convert_to_metrodr_environment.assert_called()
        # Exception testing

        metro_module_mock.metro.convert_to_metrodr_environment = MagicMock(side_effect=Exception)
        metro_module_mock.convert_to_metrodr_env()
        assert MockMetroDRApi.get_exception_response('convert_to_metrodr_env') in metro_module_mock.module.fail_json.call_args[1]['msg']

    def test_pre_checks_for_modify(self, metro_module_mock):
        # Exception testing SetMode
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async', 'srdf_param': {'srdf_state': 'Split', 'keep_r2': None}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.pre_checks_for_modify()
        assert MockMetroDRApi.get_exception_response('pre_checks_for_modify_split_mode') in metro_module_mock.module.fail_json.call_args[1]['msg']

        # Exception testing keep_r2
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async', 'srdf_param': {'srdf_state': 'Split', 'keep_r2': 'true'}})
        metro_module_mock.pre_checks_for_modify()
        assert MockMetroDRApi.get_exception_response('pre_checks_for_modify_keep_r2') in metro_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_metrodr_env_get_only_case(self, metro_module_mock):
        # Get should fail before pre_check as get operation
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async'})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.pre_checks_for_modify = MagicMock(return_value=None)
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS)
        metro_module_mock.pre_checks_for_modify.assert_not_called()

    def test_modify_metrodr_env_itempotency(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async',
                                'srdf_param': {'srdf_state': 'Split', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        # Itempotency test should return and not attempt modify
        metro_module_mock.get_modify_dict = MagicMock(return_value=None)
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.metro.modify_metrodr_environment = MagicMock(return_value=None)
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS)
        metro_module_mock.metro.modify_metrodr_environment.assert_not_called()

    def test_modify_metrodr(self, metro_module_mock):
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async',
                                'srdf_param': {'srdf_state': 'Split', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.pre_checks_for_modify = MagicMock(return_value=None)
        metro_module_mock.get_metrodr_env = MagicMock(return_value=None)
        metro_module_mock.metro.modify_metrodr_environment = MagicMock(return_value=None)
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS)
        metro_module_mock.pre_checks_for_modify.assert_called()
        metro_module_mock.get_metrodr_env.assert_called()
        metro_module_mock.metro.modify_metrodr_environment.assert_called()

        # Sync Failover
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async',
                                'srdf_param': {'srdf_state': 'Failover', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS_FORCE_SYNC)
        metro_module_mock.metro.modify_metrodr_environment.assert_called()

        # Sync Split
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async',
                                'srdf_param': {'srdf_state': 'Split', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS_FORCE_SYNC)
        metro_module_mock.metro.modify_metrodr_environment.assert_called()

        # Suspended Failover
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async',
                                'srdf_param': {'srdf_state': 'Failover', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS)
        metro_module_mock.metro.modify_metrodr_environment.assert_called()

        # Split Failover
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async',
                                'srdf_param': {'srdf_state': 'Failover', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS_FORCE_SPLIT)
        metro_module_mock.metro.modify_metrodr_environment.assert_called()

        # Split Restore
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'async',
                                'srdf_param': {'srdf_state': 'Restore', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS_FORCE_SPLIT)
        metro_module_mock.metro.modify_metrodr_environment.assert_called()

        # SetMode Itempotency
        self.metro_args.update({'env_name': 'metro_env', 'metro_r1_array_id': '000297900330', 'metro_r2_array_id': '000297900330',
                                'dr_array_id': '3.3.3.3', 'replication_mode': 'Adaptive Copy',
                                'srdf_param': {'srdf_state': 'SetMode', 'keep_r2': None, 'metro': 'true', 'dr': 'true'}})
        metro_module_mock.module.params = self.metro_args
        metro_module_mock.modify_metrodr_env(MockMetroDRApi.METRO_DR_ENV_DETAILS_FORCE_SPLIT)

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
