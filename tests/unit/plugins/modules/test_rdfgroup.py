# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for RDF Group module on PowerMax"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_rdfgroup_api import MockRDFGroupApi
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
from ansible_collections.dellemc.powermax.plugins.modules.rdfgroup import RDFGroup
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestInfo(PowerMaxUnitBase):

    get_module_args = MockRDFGroupApi.RDFGROUP_COMMON_ARGS

    @pytest.fixture
    def rdfgroup_module_mock(self, mocker):
        rdfgroup_module_mock = RDFGroup()
        rdfgroup_module_mock.module.check_mode = False
        return rdfgroup_module_mock

    @pytest.fixture
    def module_object(self):
        return RDFGroup

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

    def test_get_rdfgroup_volume_details(self, rdfgroup_module_mock):
        self.get_module_args.update({
            "rdfgroup_number": 1,
            "vol_name": "test_vol"
        })
        rdfgroup_module_mock.module.params = self.get_module_args
        rdfgroup_module_mock.replication.get_rdf_group_volume_list = MagicMock(
            return_value=MockRDFGroupApi.RDF_GROUP_VOLUME_LIST
        )
        rdfgroup_module_mock.replication.get_rdf_group_volume = MagicMock(
            return_value=MockRDFGroupApi.RDF_GROUP_VOLUME_DETAILS
        )
        rdfgroup_module_mock.perform_module_operation()
        rdfgroup_module_mock.replication.get_rdf_group_volume_list.assert_called()
        rdfgroup_module_mock.replication.get_rdf_group_volume.assert_called()

    def test_get_rdfgroup_volume_details_with_exception(self, rdfgroup_module_mock):
        self.get_module_args.update({
            "rdfgroup_number": 1,
            "vol_name": "test_vol"
        })
        rdfgroup_module_mock.module.params = self.get_module_args
        rdfgroup_module_mock.replication.get_rdf_group_volume_list = MagicMock(
            return_value=MockRDFGroupApi.RDF_GROUP_VOLUME_LIST
        )
        rdfgroup_module_mock.replication.get_rdf_group_volume = MagicMock(
            side_effect=Exception
        )
        rdfgroup_module_mock.perform_module_operation()
        assert MockRDFGroupApi.get_exception_response('get_rdfgroup_volume_details') in rdfgroup_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_rdf_group_volumes(self, rdfgroup_module_mock):
        self.get_module_args.update({
            "rdfgroup_number": 1,
            "vol_name": "test_vol"
        })
        rdfgroup_module_mock.module.params = self.get_module_args
        rdfgroup_module_mock.replication.get_rdf_group_volume_list = MagicMock(return_value=MockRDFGroupApi.RDF_GROUP_VOLUME_LIST)
        rdfgroup_module_mock.get_rdf_group_volumes(1)
        rdfgroup_module_mock.replication.get_rdf_group_volume_list.assert_called()

        # Exception testing
        rdfgroup_module_mock.replication.get_rdf_group_volume_list = MagicMock(
            side_effect=Exception
        )
        rdfgroup_module_mock.get_rdf_group_volumes(1)
        assert MockRDFGroupApi.get_exception_response('get_rdf_volume_list') in rdfgroup_module_mock.module.fail_json.call_args[1]['msg']

    def test_get_rdf_group_details(self, rdfgroup_module_mock):
        self.get_module_args.update({
            "rdfgroup_number": 1,
            "vol_name": "test_vol"
        })
        rdfgroup_module_mock.module.params = self.get_module_args
        rdfgroup_module_mock.replication.get_rdf_group = MagicMock(return_value=MockRDFGroupApi.RDF_GROUP_DETAILS)
        rdfgroup_module_mock.get_rdf_group_details(1)
        rdfgroup_module_mock.replication.get_rdf_group.assert_called()

        # Exception testing
        rdfgroup_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=Exception
        )
        rdfgroup_module_mock.get_rdf_group_details(1)
        assert MockRDFGroupApi.get_exception_response('get_rdf_group_details') in rdfgroup_module_mock.module.fail_json.call_args[1]['msg']
