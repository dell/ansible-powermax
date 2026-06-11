# Copyright: (c) 2024-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for SRDF module on PowerMax"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell import utils
from ansible.module_utils.compat.version import LooseVersion

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_U4V_connection = MagicMock()
utils.close_connection = MagicMock()
utils.parse_version = LooseVersion
utils.PyU4V = MagicMock()
utils.PyU4V.__version__ = "10.1.0.2"
from ansible.module_utils import basic

basic.AnsibleModule = MagicMock()


from ansible_collections.dellemc.powermax.plugins.modules.srdf import (
    SRDF,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_srdf_api import (
    MockSRDFApi,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestSRDF(PowerMaxUnitBase):
    srdf_args = MockSRDFApi.SRDF_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return SRDF

    def test_get_srdf_link(self, powermax_module_mock):
        """U-020: get_srdf_link returns SRDF details"""
        powermax_module_mock.module.params = self.srdf_args
        powermax_module_mock.replication.get_storage_group_srdf_details = MagicMock(
            return_value=MockSRDFApi.SRDF_LINK_DETAILS
        )
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[1]
        )
        result = powermax_module_mock.get_srdf_link("test_sg")
        assert result is not None
        assert len(result) == 1
        assert result[0]["storageGroupName"] == "test_sg"
        powermax_module_mock.replication.get_storage_group_srdf_details.assert_called()

    def test_get_srdf_link_exception(self, powermax_module_mock):
        """U-020 error path: get_srdf_link handles exception"""
        powermax_module_mock.module.params = self.srdf_args
        powermax_module_mock.replication.get_storage_group_srdf_details = MagicMock(
            side_effect=MockApiException
        )
        result = powermax_module_mock.get_srdf_link("test_sg")
        assert result is None

    def test_create_srdf_link_backward_compat(self, powermax_module_mock):
        """U-019: create_srdf_link without rdf_target_sg_name uses default"""
        args = dict(self.srdf_args)
        args["rdf_target_sg_name"] = None
        powermax_module_mock.module.params = args
        powermax_module_mock.module.check_mode = False
        powermax_module_mock.replication.create_storage_group_srdf_pairings = MagicMock(
            return_value=MockSRDFApi.JOB_DETAILS
        )
        result = powermax_module_mock.create_srdf_link()
        assert result is True
        powermax_module_mock.replication.create_storage_group_srdf_pairings.assert_called_once()
        call_kwargs = powermax_module_mock.replication.create_storage_group_srdf_pairings.call_args
        assert call_kwargs[1]["storage_group_id"] == "test_sg"

    def test_create_srdf_link_with_rdf_target_sg_name(self, powermax_module_mock):
        """U-018: create_srdf_link passes rdf_target_sg_name to SDK"""
        args = dict(self.srdf_args)
        args["rdf_target_sg_name"] = "DR_test_sg"
        powermax_module_mock.module.params = args
        powermax_module_mock.module.check_mode = False
        powermax_module_mock.replication.create_storage_group_srdf_pairings = MagicMock(
            return_value=MockSRDFApi.JOB_DETAILS
        )
        result = powermax_module_mock.create_srdf_link()
        assert result is True
        powermax_module_mock.replication.create_storage_group_srdf_pairings.assert_called_once()

    def test_create_srdf_link_empty_rdf_target(self, powermax_module_mock):
        """U-E10: empty rdf_target_sg_name treated as None"""
        args = dict(self.srdf_args)
        args["rdf_target_sg_name"] = ""
        powermax_module_mock.module.params = args
        powermax_module_mock.module.check_mode = False
        powermax_module_mock.replication.create_storage_group_srdf_pairings = MagicMock(
            return_value=MockSRDFApi.JOB_DETAILS
        )
        result = powermax_module_mock.create_srdf_link()
        assert result is True

    def test_create_srdf_link_exception(self, powermax_module_mock):
        """U-E12: Exception in create_srdf_link handled"""
        args = dict(self.srdf_args)
        args["rdf_target_sg_name"] = None
        powermax_module_mock.module.params = args
        powermax_module_mock.module.check_mode = False
        powermax_module_mock.replication.create_storage_group_srdf_pairings = MagicMock(
            side_effect=Exception("API error")
        )
        powermax_module_mock.show_error_exit = MagicMock()
        powermax_module_mock.create_srdf_link()
        powermax_module_mock.show_error_exit.assert_called_once()

    def test_create_srdf_link_missing_params(self, powermax_module_mock):
        """Baseline: create_srdf_link fails with missing mandatory params"""
        args = dict(self.srdf_args)
        args["remote_serial_no"] = None
        args["srdf_mode"] = None
        args["rdf_target_sg_name"] = None
        powermax_module_mock.module.params = args
        powermax_module_mock.show_error_exit = MagicMock()
        powermax_module_mock.create_srdf_link()
        assert powermax_module_mock.show_error_exit.called
        # Check the first call (mandatory params check)
        first_call_args = powermax_module_mock.show_error_exit.call_args_list[0]
        assert "Mandatory parameters" in first_call_args[1]["msg"]
