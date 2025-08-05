# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Info module on PowerMax"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_info_api import MockInfoApi
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_U4V_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()
from ansible_collections.dellemc.powermax.plugins.modules.info import Info

from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestInfo(PowerMaxUnitBase):
    get_module_args = MockInfoApi.INFO_COMMON_ARGS

    @pytest.fixture
    def info_module_mock(self, mocker):
        info_module_mock = Info()
        info_module_mock.module.check_mode = False
        return info_module_mock

    @pytest.fixture
    def module_object(self):
        return Info

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
        # Run tests with name filter
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
            "gather_subset": ['mv_connections'],
            "masking_view_name": 'EMBEDDED_NAS_DM_MV'
        })
        info_module_mock.provisioning.get_masking_view = MagicMock(
            return_value=MockInfoApi.MASKING_VIEW_LIST
        )
        info_module_mock.perform_module_operation()

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
                    "filter_operator": "like",
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
                    "filter_operator": "lesser",
                    "filter_value": "10"
                }
            ],
            'gather_subset': ['vol']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=MockInfoApi.VOLUME_LIST
        )
        info_module_mock.provisioning.get_volume = MagicMock(return_value=MockInfoApi.VOLUME_DETAILS_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_volume_list.assert_called()

        info_module_mock.provisioning.get_volume = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_volume_details') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_volume_details_with_exception(self, info_module_mock):
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
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

    def test_storage_group_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['sg']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_storage_group_list = MagicMock(return_value=MockInfoApi.SG_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_storage_group_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['sg']
        })
        info_module_mock.provisioning.get_storage_group_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_storage_group') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_srp_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['srp']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_srp_list = MagicMock(return_value=MockInfoApi.SRP_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_srp_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['srp']
        })
        info_module_mock.provisioning.get_srp_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_srp') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_portgroup_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['pg']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_port_group_list = MagicMock(return_value=MockInfoApi.PORT_GROUP_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_port_group_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['pg']
        })
        info_module_mock.provisioning.get_port_group_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_port_group') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_host_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['host']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_host_list = MagicMock(return_value=MockInfoApi.HOST_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_host_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['host']
        })
        info_module_mock.provisioning.get_host_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_host_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_hostgroup_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['hg']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_host_group_list = MagicMock(return_value=MockInfoApi.HOST_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_host_group_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['hg']
        })
        info_module_mock.provisioning.get_host_group_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_host_group_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_port_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['port']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_port_list = MagicMock(return_value=MockInfoApi.PORT_GROUP_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_port_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['port']
        })
        info_module_mock.provisioning.get_port_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_port_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_rdfgroup_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['rdf']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.replication.get_rdf_group_list = MagicMock(return_value=MockInfoApi.SRDF_GROUP_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.replication.get_rdf_group_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['rdf']
        })
        info_module_mock.replication.get_rdf_group_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_rdf_group_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_metro_dr_env_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['metro_dr_env']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.u4v_conn.metro_dr.get_metrodr_environment_list = MagicMock(return_value=MockInfoApi.METRO_DR_ENV_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.u4v_conn.metro_dr.get_metrodr_environment_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['metro_dr_env']
        })
        info_module_mock.u4v_conn.metro_dr.get_metrodr_environment_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_metrodr_environment_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_snapshot_policies_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['snapshot_policies']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.u4v_conn.snapshot_policy.get_snapshot_policy_list = MagicMock(return_value=MockInfoApi.SNAPSHOT_POLICY_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.u4v_conn.snapshot_policy.get_snapshot_policy_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['snapshot_policies']
        })
        info_module_mock.u4v_conn.snapshot_policy.get_snapshot_policy_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_snapshot_policy_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_initiators_list(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['initiators']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_initiator_list = MagicMock(return_value=MockInfoApi.INITIATOR_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_initiator_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['initiators']
        })
        info_module_mock.provisioning.get_initiator_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_initiator_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_alerts(self, info_module_mock):
        self.get_module_args.update({
            "filters": [
                {
                    "object": "test_obj",
                    "type": "test_type",
                    "description": "test_description"
                },
            ],
            "gather_subset": ['alert']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.u4v_conn.system.get_alert_ids = MagicMock(return_value=MockInfoApi.ALERT_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.u4v_conn.system.get_alert_ids.assert_called()

    def test_get_health(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['health']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.u4v_conn.system.get_system_health = MagicMock(return_value=MockInfoApi.HEALTH_CHECK)
        info_module_mock.perform_module_operation()
        info_module_mock.u4v_conn.system.get_system_health.assert_called()

    def test_get_masking_views(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": ['mv']
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.provisioning.get_masking_view_list = MagicMock(return_value=MockInfoApi.MASKING_VIEW_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.provisioning.get_masking_view_list.assert_called()

        # Exception testing
        self.get_module_args.update({
            "filters": [
                {
                    "filter_key": "cap_gb",
                    "filter_operator": "greater",
                    "filter_value": "10"
                }
            ],
            "gather_subset": ['mv']
        })
        info_module_mock.provisioning.get_masking_view_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_masking_view_list') in info_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_array(self, info_module_mock):
        self.get_module_args.update({
            "filters": [],
            "gather_subset": []
        })
        info_module_mock.module.params = self.get_module_args
        info_module_mock.module.params['serial_no'] = ''
        info_module_mock.__init__()
        info_module_mock.u4v_unisphere_con.common.get_array_list = MagicMock(return_value=MockInfoApi.MASKING_VIEW_LIST)
        info_module_mock.perform_module_operation()
        info_module_mock.u4v_unisphere_con.common.get_array_list.assert_called()

        # Exception testing
        info_module_mock.u4v_unisphere_con.common.get_array_list = MagicMock(
            side_effect=Exception
        )
        info_module_mock.perform_module_operation()
        assert MockInfoApi.get_exception_response('get_array_list') in info_module_mock.module.fail_json.call_args[1]['msg']
