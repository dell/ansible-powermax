# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for RDF Group module on PowerMax"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import pytest
from mock.mock import MagicMock
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_rdfgroup_api import MockRDFGroupApi
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
from ansible_collections.dellemc.powermax.plugins.modules.rdfgroup import RDFGroup


class TestInfo():

    get_module_args = MockRDFGroupApi.RDFGROUP_COMMON_ARGS

    @pytest.fixture
    def rdfgroup_module_mock(self, mocker):
        rdfgroup_module_mock = RDFGroup()
        rdfgroup_module_mock.module.check_mode = False
        return rdfgroup_module_mock

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
