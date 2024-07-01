# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Volume module on PowerMax"""

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


from ansible_collections.dellemc.powermax.plugins.modules.volume import Volume
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils \
    import mock_vol_api as MockVolApi


class TestVolume():
    MODULE_PATH = 'ansible_collections.dellemc.powermax.plugins.modules.volume.Volume.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell.utils'
    vol_args = {'vol_name': None, 'vol_id': None, 'state': 'present',
                'size': None, 'sg_name': None, 'new_sg_name': None, 'new_name': None,
                'cap_unit': None, 'vol_wwn': None, 'serial_no': None, 'append_vol_id': None}

    @pytest.fixture
    def vol_module_mock(self, mocker):
        vol_module_mock = Volume()
        vol_module_mock.module = MagicMock()
        vol_module_mock.provisioning = MagicMock()
        vol_module_mock.module.check_mode = False
        vol_module_mock.u4v_conn = MagicMock()
        return vol_module_mock

    def test_create_volume_cap_unit_cyl(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'test_vol', 'size': 10, 'sg_name': 'test_sg',
                              'cap_unit': 'CYL', 'serial_no': 'Test_Serial'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.get_volume = MagicMock(return_value=None)
        vol_module_mock.get_storage_group = MagicMock(return_value=None)
        vol_module_mock.provisioning.find_volume_device_id = (MagicMock(return_value="Vol_1"))
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert vol_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_get_volume_by_id(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_id': 'test_vol'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.provisioning.get_volume = MagicMock(return_value=MockVolApi.get_vol_details())
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert (MockVolApi.get_vol_details()
                == vol_module_mock.module.exit_json.call_args[1]["volume_details"])

    def test_get_volume_by_name(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'test_vol', 'sg_name': 'test_sg'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.provisioning.get_volume_list = MagicMock(return_value=MockVolApi.get_vol_list())
        vol_module_mock.provisioning.get_volume = MagicMock(return_value=MockVolApi.get_vol_details())
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert (MockVolApi.get_vol_details()
                == vol_module_mock.module.exit_json.call_args[1]["volume_details"])

    def test_create_volume_cap_unit_gb(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'test_vol', 'size': 10, 'sg_name': 'test_sg',
                              'cap_unit': 'GB', 'serial_no': 'Test_Serial'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.get_volume = MagicMock(return_value=None)
        vol_module_mock.get_storage_group = MagicMock(return_value=None)
        vol_module_mock.provisioning.find_volume_device_id = (MagicMock(return_value="Vol_1"))
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert vol_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_get_volume_by_wwn(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_wwn': 'test_vol', 'sg_name': 'test_sg'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.provisioning.get_volume_list = MagicMock(return_value=MockVolApi.get_vol_list())
        vol_module_mock.provisioning.get_volume = MagicMock(return_value=MockVolApi.get_vol_details())
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert (MockVolApi.get_vol_details()
                == vol_module_mock.module.exit_json.call_args[1]["volume_details"])

    def test_create_volume_append_vol_id(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'Vol', 'size': 10, 'sg_name': 'test_sg',
                              'cap_unit': 'MB', 'serial_no': 'Test_Serial', 'append_vol_id': True})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.get_volume = MagicMock(return_value=None)
        vol_module_mock.get_storage_group = MagicMock(return_value=None)
        vol_module_mock.provisioning.find_volume_device_id = (MagicMock(return_value="Vol0001"))
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert vol_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_volume_exception(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'test_vol', 'size': 10, 'sg_name': 'test_sg',
                              'cap_unit': 'CYL', 'serial_no': 'Test_Serial', 'append_vol_id': True})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.get_volume = MagicMock(return_value=None)
        vol_module_mock.get_storage_group = MagicMock(return_value=None)
        vol_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(side_effect=Exception)
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert MockVolApi.create_vol_exception(vol_module_mock.module.params['vol_name']) in vol_module_mock.module.fail_json.call_args[1]['msg']

    def test_modify_volume_cap_unit_cyl(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'test_vol', 'size': 200, 'sg_name': 'test_sg',
                              'cap_unit': 'CYL', 'serial_no': 'Test_Serial'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.get_volume = MagicMock(return_value=MockVolApi.get_vol_details())
        vol_module_mock.get_storage_group = MagicMock(return_value=None)
        vol_module_mock.provisioning.provisioning.extend_volume = (MagicMock(return_value=True))
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert vol_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_volume_cap_unit_gb(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'test_vol', 'size': 200, 'sg_name': 'test_sg',
                              'cap_unit': 'GB', 'serial_no': 'Test_Serial'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.get_volume = MagicMock(return_value=MockVolApi.get_vol_details())
        vol_module_mock.get_storage_group = MagicMock(return_value=None)
        vol_module_mock.provisioning.provisioning.extend_volume = (MagicMock(return_value=True))
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert vol_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_modify_volume_exception(self, vol_module_mock):
        self.vol_args.update({'state': 'present', 'vol_name': 'test_vol', 'size': 0.01, 'sg_name': 'test_sg',
                              'cap_unit': 'GB', 'serial_no': 'Test_Serial'})
        vol_module_mock.module.params = self.vol_args
        vol_module_mock.get_volume = MagicMock(return_value=MockVolApi.get_vol_details())
        vol_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        vol_module_mock.perform_module_operation()
        assert MockVolApi.expand_vol_exception(str(vol_module_mock.module.params['size'])) in vol_module_mock.module.fail_json.call_args[1]['msg']
