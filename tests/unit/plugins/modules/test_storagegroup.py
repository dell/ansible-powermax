# Copyright: (c) 2022, Dell Technologies

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

"""Unit Tests for StorageGroup module on PowerMax"""

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


from ansible_collections.dellemc.powermax.plugins.modules.storagegroup import StorageGroup


class TestStorageGroup():
    MODULE_PATH = 'ansible_collections.dellemc.powermax.plugins.modules.storagegroup.StorageGroup.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell.utils'
    sg_args = {'sg_name': 'test_sg', 'service_level': 'None', 'state': 'present',
               'srp': None, 'compression': None, 'volumes': None, 'vol_state': None,
               'child_storage_groups': None, 'child_sg_state': None, 'new_sg_name': None, 'snapshot_policies': None,
               'snapshot_policy_state': None, 'target_sg_name': None, 'force': None}

    @pytest.fixture
    def sg_module_mock(self, mocker):
        mocker.patch(self.MODULE_PATH + '__init__', return_value=None)
        sg_module_mock = StorageGroup()
        sg_module_mock.module = MagicMock()
        sg_module_mock.provisioning = MagicMock()
        return sg_module_mock

    def test_move_volumes_between_sgs(self, sg_module_mock):
        self.sg_args.update({'state': 'present', 'target_sg_name': 'target_sg', 'volumes': [{'vol_id': '123'}],
                             'vol_state': 'absent-in-group'})
        sg_module_mock.module.params = self.sg_args
        sg_module_mock.get_volumes_to_move = MagicMock(return_value=['1', '2', '3'])
        sg_module_mock.perform_module_operation()
        assert sg_module_mock.module.exit_json.call_args[1]["modify_sg"]
        assert sg_module_mock.module.exit_json.call_args[1]["remove_vols_from_sg"]

    def test_move_volumes_between_sgs_duplicate_vols(self, sg_module_mock):
        self.sg_args.update({'state': 'present', 'target_sg_name': 'target_sg', 'volumes': [{'vol_id': '123', 'vol_name': 'test'}],
                             'vol_state': 'absent-in-group'})
        sg_module_mock.module.params = self.sg_args
        sg_module_mock.provisioning.get_volume_list = MagicMock(return_value=['vol1', 'vol2'])
        sg_module_mock.perform_module_operation()
        assert "Duplicate volumes found" in sg_module_mock.module.fail_json.call_args[1]['msg']
