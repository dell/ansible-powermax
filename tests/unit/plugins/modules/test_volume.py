# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Volume module on PowerMax"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell import utils
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_unisphere_version = MagicMock(return_value='100')
utils.get_U4V_connection = MagicMock()
utils.close_connection = MagicMock()
from ansible.module_utils import basic

basic.AnsibleModule = MagicMock()


from ansible_collections.dellemc.powermax.plugins.modules.volume import Volume
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils import (
    mock_vol_api as MockVolApi,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestVolume(PowerMaxUnitBase):
    MODULE_PATH = "ansible_collections.dellemc.powermax.plugins.modules.volume.Volume."
    MODULE_UTILS_PATH = (
        "ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell.utils"
    )
    vol_args = {
        "vol_name": None,
        "vol_id": None,
        "state": "present",
        "size": None,
        "sg_name": None,
        "new_sg_name": None,
        "new_name": None,
        "cap_unit": None,
        "vol_wwn": None,
        "serial_no": None,
        "append_vol_id": None,
    }

    @pytest.fixture
    def module_object(self):
        return Volume

    def test_vol_init(self, powermax_module_mock):
        with patch(
            "ansible_collections.dellemc.powermax.plugins.modules.volume.HAS_PYU4V",
            False,
        ):
            with patch(
                "ansible_collections.dellemc.powermax.plugins.modules.volume.PYU4V_VERSION_CHECK",
                "mock check err",
            ):
                utils.get_U4V_connection = MagicMock(side_effect=MockApiException())
                powermax_module_mock.show_error_exit = MagicMock()
                powermax_module_mock.__init__()
                assert powermax_module_mock.show_error_exit.call_count == 3

    def test_create_volume_cap_unit_cyl(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 10,
                "sg_name": "test_sg",
                "cap_unit": "CYL",
                "serial_no": "Test_Serial",
                "append_vol_id": "test_append_vol_id",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.find_volume_device_id = MagicMock(
            return_value="Vol_1"
        )
        powermax_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(
            return_value="test_job"
        )
        powermax_module_mock.common.wait_for_job = MagicMock(
            return_value=MockVolApi.wait_for_job()
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_create_volume_cap_unit_gb(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 10,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
                "append_vol_id": "test_append_vol_id",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.find_volume_device_id = MagicMock(
            return_value="Vol_1"
        )
        powermax_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(
            return_value="test_job"
        )
        powermax_module_mock.common.wait_for_job = MagicMock(side_effect=Exception)
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_create_volume_srdf_1(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "Vol",
                "size": 10,
                "cap_unit": "CYL",
                "sg_name": "test_sg",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_storage_group = MagicMock(
            return_value=MockVolApi.get_storagegroup_details_1()
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=MockVolApi.get_storage_group_srdf_group_list_1()
        )
        powermax_module_mock.provisioning.find_volume_device_id = MagicMock(
            return_value=[1, 2]
        )
        powermax_module_mock.provisioning.is_volume_in_storage_group = MagicMock(
            return_value=True
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_create_volume_srdf_2(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "Vol",
                "size": 10,
                "sg_name": "test_sg",
                "cap_unit": "MB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_storage_group = MagicMock(
            return_value=MockVolApi.get_storagegroup_details_1()
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=MockVolApi.get_storage_group_srdf_group_list_2()
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            return_value=MockVolApi.get_rdf_group()
        )
        powermax_module_mock.provisioning.find_volume_device_id = MagicMock(
            side_effect=MockApiException
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_create_volume_srdf_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "Vol",
                "size": 10,
                "cap_unit": "CYL",
                "sg_name": "test_sg",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_storage_group = MagicMock(
            return_value=MockVolApi.get_storagegroup_details_1()
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=MockVolApi.get_storage_group_srdf_group_list_3()
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("create_vol_srdf_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_volume_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 10,
                "sg_name": "test_sg",
                "cap_unit": "CYL",
                "serial_no": "Test_Serial",
                "append_vol_id": True,
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(
            side_effect=Exception
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("create_vol_exception", vol_name="test_vol"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_volume_without_size_exception_1(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "sg_name": "test_sg",
                "cap_unit": "CYL",
                "serial_no": "Test_Serial",
                "append_vol_id": True,
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(
            side_effect=Exception
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("no_size_exception_1"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_volume_without_size_exception_2(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "sg_name": "test_sg",
                "serial_no": "Test_Serial",
                "append_vol_id": True,
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(
            side_effect=Exception
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("no_size_exception_2"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_volume_without_sg_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 10,
                "cap_unit": "CYL",
                "serial_no": "Test_Serial",
                "append_vol_id": True,
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(
            side_effect=Exception
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("no_sg_name_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_with_new_name_exception(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "present", "vol_id": "test_vol", "new_name": "test_new_name"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.get_volume = MagicMock(side_effect=Exception)
        utils.close_connection = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockVolApi.get_error_message("create_with_new_name_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_without_name_exception(self, powermax_module_mock):
        self.vol_args.update({"state": "present", "size": 0.02})
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        self.capture_fail_json_method(
            MockVolApi.get_error_message("create_without_name_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_volume_srdf_version_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "Vol",
                "size": 10,
                "cap_unit": "CYL",
                "sg_name": "test_sg",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_storage_group = MagicMock(
            return_value=MockVolApi.get_storagegroup_details_1()
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.common.get_array = MagicMock(return_value={"ucode": 1})
        utils.parse_version = MagicMock(side_effect=[1, 2])
        self.capture_fail_json_method(
            MockVolApi.get_error_message("create_vol_srdf_version_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_get_volume_by_name(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "present", "vol_name": "test_vol", "sg_name": "test_sg"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=MockVolApi.get_vol_list()
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.perform_module_operation()
        assert (
            MockVolApi.get_vol_details()
            == powermax_module_mock.module.exit_json.call_args[1]["volume_details"]
        )

    def test_get_volume_by_wwn_exception(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "present", "vol_wwn": "test_vol", "sg_name": "test_sg"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=MockVolApi.get_vol_list()
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("get_vol_by_wwn_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_get_duplicate_vol_exception(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "present", "vol_name": "test_vol", "sg_name": "test_sg"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=[1, 2]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("get_duplicate_vol_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_get_sg_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 10,
                "sg_name": "test_sg",
                "cap_unit": "CYL",
                "serial_no": "Test_Serial",
                "append_vol_id": True,
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            side_effect=Exception
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("get_sg_exception", sg_name="test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_volume_cap_unit_cyl(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "CYL",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_modify_volume_cap_unit_gb(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_modify_volume_srdf_1(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_1()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.replication.get_rdf_group_volume = MagicMock(
            return_value=MockVolApi.get_rdf_group_volume_1()
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_modify_volume_srdf_2(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_2()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.replication.get_rdf_group_volume = MagicMock(
            side_effect=[
                MockVolApi.get_rdf_group_volume_1(),
                MockVolApi.get_rdf_group_volume_2(),
            ]
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_modify_volume_srdf_3(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_2()
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_1()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.replication.get_rdf_group_volume = MagicMock(
            side_effect=[
                MockVolApi.get_rdf_group_volume_2(),
                MockVolApi.get_rdf_group_volume_1(),
            ]
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_modify_volume_srdf_4(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_4()
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_1()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.replication.get_rdf_group_volume = MagicMock(
            MockVolApi.get_rdf_group_volume_1()
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_expand_vol_version_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_2()
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={"ucode": 1})
        utils.parse_version = MagicMock(side_effect=[1, 2])
        self.capture_fail_json_method(
            MockVolApi.get_error_message("expand_vol_srdf_version_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_expand_srdf_vol_version_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_1()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.replication.get_rdf_group_volume = MagicMock(
            return_value=MockVolApi.get_rdf_group_volume_1()
        )
        powermax_module_mock.common.get_array = MagicMock(
            side_effect=[{}, {"ucode": 1}]
        )
        utils.parse_version = MagicMock(side_effect=[1, 2])
        self.capture_fail_json_method(
            MockVolApi.get_error_message("expand_vol_srdf_metro_version_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_volume_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 0.01,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("expand_vol_exception", size=0.01),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_expand_concurrent_config_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_2()
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_2()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.replication.get_rdf_group_volume = MagicMock(
            side_effect=[
                MockVolApi.get_rdf_group_volume_1(),
                MockVolApi.get_rdf_group_volume_2(),
            ]
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockVolApi.get_error_message("expand_volume_exception", size=0.01),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_srdf_vol_expand_exception_1(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_3()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=True
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockVolApi.get_error_message("expand_volume_exception", size=0.01),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_srdf_vol_expand_exception_2(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "size": 200,
                "sg_name": "test_sg",
                "cap_unit": "GB",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_1()
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_2()
        )
        powermax_module_mock.provisioning.provisioning.extend_volume = MagicMock(
            return_value=MockVolApi.get_vol_srdf_details_2()
        )
        powermax_module_mock.common.get_array = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockVolApi.get_error_message("expand_volume_exception", size=0.01),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_rename_volume(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_id": "0072E",
                "new_name": "test_vol_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.get_storage_group = MagicMock(
            return_value=MockVolApi.get_storagegroup_details_1()
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=None)
        powermax_module_mock.provisioning.get_storage_group_from_volume = MagicMock(
            return_value=["test_sg"]
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_rename_volume_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_id": "0072E",
                "new_name": "test_vol_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.get_storage_group_from_volume = MagicMock(
            side_effect=MockApiException()
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("rename_vol_exception", vol_id="0072E"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_rename_volume_with_empty_name_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_id": "0072E",
                "new_name": "",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.get_storage_group_from_volume = MagicMock(
            side_effect=MockApiException()
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("rename_vol_with_empty_name_exeption"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_rename_already_exist_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_id": "0072E",
                "new_name": "test_vol_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.get_storage_group = MagicMock(
            return_value=MockVolApi.get_storagegroup_details_1()
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=MockVolApi.get_vol_list()
        )
        powermax_module_mock.provisioning.get_storage_group_from_volume = MagicMock(
            return_value=["test_sg"]
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("volume_already_exist_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_delete_volume(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "absent", "vol_id": "0072E", "serial_no": "Test_Serial"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.delete_volume = MagicMock(return_value=True)
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_deallocate_volume(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "absent", "vol_id": "0072E", "serial_no": "Test_Serial"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.delete_volume = MagicMock(
            side_effect=[
                MockApiException("A free of all allocations is required"),
                None,
            ]
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_delete_volume_exception(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "absent", "vol_id": "0072E", "serial_no": "Test_Serial"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.delete_volume = MagicMock(
            side_effect=MockApiException()
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("delete_vol_exception", vol_id="0072E"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_deallocate_volume_exception(self, powermax_module_mock):
        self.vol_args.update(
            {"state": "absent", "vol_id": "0072E", "serial_no": "Test_Serial"}
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.delete_volume = MagicMock(
            side_effect=[
                MockApiException("A free of all allocations is required"),
                MockApiException(),
            ]
        )
        self.capture_fail_json_method(
            MockVolApi.get_error_message("delete_vol_exception", vol_id="0072E"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_move_volume_between_sg(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "sg_name": "test_sg",
                "new_sg_name": "test_sg_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            side_effect=[
                MockVolApi.get_storagegroup_details_1(),
                MockVolApi.get_storagegroup_details_2(),
            ]
        )
        powermax_module_mock.replication.get_replication_enabled_storage_groups = (
            MagicMock(return_value=[])
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["changed"] is True

    def test_move_volume_src_srdf_protected_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "sg_name": "test_sg",
                "new_sg_name": "test_sg_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            side_effect=[
                MockVolApi.get_storagegroup_details_1(),
                MockVolApi.get_storagegroup_details_2(),
            ]
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        self.capture_fail_json_method(
            MockVolApi.get_error_message("move_vol_srdf_protected_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_move_volume_dest_srdf_protected_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "sg_name": "test_sg",
                "new_sg_name": "test_sg_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            side_effect=[
                MockVolApi.get_storagegroup_details_1(),
                MockVolApi.get_storagegroup_details_2(),
            ]
        )
        powermax_module_mock.if_srdf_protected = MagicMock(side_effect=[False, True])
        self.capture_fail_json_method(
            MockVolApi.get_error_message("move_vol_srdf_protected_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_move_volume_sdrf_protected_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "sg_name": "test_sg",
                "new_sg_name": "test_sg_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            side_effect=[
                MockVolApi.get_storagegroup_details_1(),
                MockVolApi.get_storagegroup_details_2(),
            ]
        )
        powermax_module_mock.replication.get_replication_enabled_storage_groups = (
            MagicMock(side_effect=MockApiException)
        )
        powermax_module_mock.rename_volume = MagicMock(return_value=True)
        self.capture_fail_json_method(
            MockVolApi.get_error_message(
                "determine_srdf_protected_exception", sg_id="test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_move_volume_already_exit_exception(self, powermax_module_mock):
        self.vol_args.update(
            {
                "state": "present",
                "vol_name": "test_vol",
                "sg_name": "test_sg",
                "new_sg_name": "test_sg_new",
                "serial_no": "Test_Serial",
            }
        )
        powermax_module_mock.module_wo_sensitive_data = self.vol_args
        powermax_module_mock.get_volume = MagicMock(
            return_value=MockVolApi.get_vol_details()
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=MockVolApi.get_vol_list
        )
        powermax_module_mock.rename_volume = MagicMock(return_value=True)
        self.capture_fail_json_method(
            MockVolApi.get_error_message("volume_already_exist_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )
