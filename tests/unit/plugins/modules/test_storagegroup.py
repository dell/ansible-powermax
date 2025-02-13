# Copyright: (c) 2022-2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for StorageGroup module on PowerMax"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell import utils
from ansible.module_utils.compat.version import LooseVersion

utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_U4V_connection = MagicMock()
utils.close_connection = MagicMock()
utils.pkg_resources = MagicMock()
utils.pkg_resources.parse_version = LooseVersion
utils.parse_version = LooseVersion
utils.PyU4V = MagicMock()
utils.PyU4V.__version__ = "10.1.0.2"
from ansible.module_utils import basic

basic.AnsibleModule = MagicMock()


from ansible_collections.dellemc.powermax.plugins.modules.storagegroup import (
    StorageGroup,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_storagegroup_api import (
    MockStorageGroupApi,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception import (
    MockApiException,
)
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base import (
    PowerMaxUnitBase,
)


class TestStorageGroup(PowerMaxUnitBase):
    storage_group_args = MockStorageGroupApi.STORAGEGROUP_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return StorageGroup

    def test_storagegroup_init_check_failed(self, powermax_module_mock):
        with patch(
            "ansible_collections.dellemc.powermax.plugins.modules.storagegroup.HAS_PYU4V",
            False,
        ):
            with patch(
                "ansible_collections.dellemc.powermax.plugins.modules.storagegroup.PYU4V_VERSION_CHECK",
                "mock check err",
            ):
                utils.get_U4V_connection = MagicMock(side_effect=MockApiException)
                utils.PyU4V.__version__ = "9.1.0.2"
                powermax_module_mock.show_error_exit = MagicMock()
                powermax_module_mock.__init__()
                assert powermax_module_mock.show_error_exit.call_count == 3

    def test_get_storagegroup_details(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.get_storage_group.assert_called()

    def test_get_storagegroup_details_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            side_effect=MockApiException
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.get_storage_group.assert_called()
        powermax_module_mock.provisioning.create_empty_storage_group.assert_called()

    def test_get_storagegroup_vol_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            side_effect=[[], [], MockApiException]
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("get_vol_list_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_get_storagegroup_vol_details_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("get_vol_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_storagegroup(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=None
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_empty_storage_group.assert_called()

    def test_create_storagegroup_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=None
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_empty_storage_group.assert_not_called()

    def test_create_storagegroup_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=None
        )
        powermax_module_mock.provisioning.create_empty_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("create_sg_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_create_storagegroup_with_snapshots(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "compression": True,
                "service_level": "Diamond",
                "srp": "SRP_1",
                "snapshot_policies": ["10min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=None
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_storage_group.assert_called()

    def test_create_storagegroup_with_snapshots_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "compression": True,
                "service_level": "Diamond",
                "srp": "SRP_1",
                "snapshot_policies": ["10min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=None
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.create_storage_group.assert_not_called()

    def test_get_vol(self, powermax_module_mock):
        powermax_module_mock.module.params = {"vol_id": "1"}
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value={"vol_id": "1"}
        )
        assert powermax_module_mock.get_volume() is not None

    def test_get_vol_name(self, powermax_module_mock):
        powermax_module_mock.module.params = {"vol_id": None, "vol_name": "test_vol"}
        powermax_module_mock.provisioning.find_volume_device_id = MagicMock(
            return_value={"vol_id": "1"}
        )
        assert powermax_module_mock.get_volume() is not None

    def test_get_vol_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = {"vol_id": "test_vol"}
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=MockApiException
        )
        assert powermax_module_mock.get_volume() is None

    def test_add_vol_to_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [
                    {},
                    {"size": 2, "cap_unit": "GB"},
                    {"vol_name": "vol_3", "size": 3},
                ],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            side_effect=[[], ["1"]]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value={"cap_gb": 3}
        )
        powermax_module_mock.perform_module_operation()
        assert (
            powermax_module_mock.provisioning.add_new_volume_to_storage_group.call_count
            == 1
        )

    def test_add_existing_vol_to_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}, {"vol_id": "2"}, {"vol_id": "3"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol_1",
                    "wwn": "33",
                },
                {
                    "effective_wwn": "34",
                    "type": "TDEV",
                    "volumeId": "2",
                    "volume_identifier": "vol_2",
                    "wwn": "34",
                },
                {"effective_wwn": "35", "type": "TDEV", "volumeId": "3", "wwn": "35"},
            ]
        )
        powermax_module_mock.get_volumes_details_storagegroup = MagicMock(
            return_value=[]
        )
        powermax_module_mock.perform_module_operation()
        assert (
            powermax_module_mock.provisioning.add_existing_volume_to_storage_group.call_count
            == 1
        )

    def test_add_existing_vol_to_sg_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value={
                "effective_wwn": "33",
                "type": "TDEV",
                "volumeId": "1",
                "volume_identifier": "vol_1",
                "wwn": "33",
            }
        )
        powermax_module_mock.get_volumes_details_storagegroup = MagicMock(
            return_value=[]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_existing_volume_to_storage_group.assert_not_called()

    def test_add_existing_vol_to_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value={
                "effective_wwn": "33",
                "type": "TDEV",
                "volumeId": "1",
                "volume_identifier": "vol_1",
                "wwn": "33",
            }
        )
        powermax_module_mock.get_volumes_details_storagegroup = MagicMock(
            return_value=[]
        )
        powermax_module_mock.provisioning.add_existing_volume_to_storage_group = (
            MagicMock(side_effect=MockApiException)
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "add_existing_vol_exception", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_protected_existing_vol_to_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value={
                "effective_wwn": "33",
                "type": "TDEV",
                "volumeId": "1",
                "volume_identifier": "vol_1",
                "wwn": "33",
            }
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.get_volumes_details_storagegroup = MagicMock(
            return_value=[]
        )
        powermax_module_mock.provisioning.add_existing_volume_to_storage_group = (
            MagicMock(side_effect=MockApiException)
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "add_existing_vol_exception", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_existing_vol_to_sg_duplicated_id(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}, {"vol_id": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol_1",
                    "wwn": "33",
                },
                {
                    "effective_wwn": "34",
                    "type": "TDEV",
                    "volumeId": "2",
                    "volume_identifier": "vol_1",
                    "wwn": "34",
                },
            ]
        )
        powermax_module_mock.get_volumes_details_storagegroup = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("add_vol_duplicated_id", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_existing_vol_to_sg_same_id(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}, {"vol_id": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol_1",
                    "wwn": "33",
                },
                {
                    "effective_wwn": "34",
                    "type": "TDEV",
                    "volumeId": "2",
                    "volume_identifier": "vol_1",
                    "wwn": "34",
                },
            ]
        )
        powermax_module_mock.get_volumes_details_storagegroup = MagicMock(
            return_value=[]
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("add_vol_same_id", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_vol_to_sg_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"size": 2, "cap_unit": "GB"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_new_volume_to_storage_group.assert_not_called()

    def test_add_vol_to_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"size": 2, "cap_unit": "GB"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.provisioning.add_new_volume_to_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("add_vol_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_vol_to_sg_size_conflict(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [
                    {},
                    {"size": 2, "cap_unit": "GB"},
                    {"vol_name": "vol_3", "size": 3},
                ],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            side_effect=[[], ["1"]]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            return_value={"cap_gb": 2}
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("size_conflict", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_vol_to_sg_no_size(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{}, {"cap_unit": "GB"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("missing_cap"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_vol_to_sg_srdf_wrong_version(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "serial_no": "1",
                "volumes": [{"size": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.common.get_array = MagicMock(
            return_value={"ucode": "5977.444.444"}
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "add_vol_unsupport_version", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_vol_to_sg_srdf_basic(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "serial_no": "1",
                "volumes": [{"size": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[{"remoteSymmetrix": "remote_array_1"}]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_new_volume_to_storage_group.assert_called()

    def test_add_vol_to_sg_srdf_basic_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "serial_no": "1",
                "volumes": [{"size": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[{"remoteSymmetrix": "remote_array_1"}]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_new_volume_to_storage_group.assert_not_called()

    def test_add_vol_to_sg_srdf_multisite(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "serial_no": "1",
                "volumes": [{"size": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0, 1]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[
                {"remoteSymmetrix": "remote_array_1"},
                {"remoteSymmetrix": "remote_array_2"},
            ]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_new_volume_to_storage_group.assert_called()

    def test_add_vol_to_sg_srdf_multisite_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "serial_no": "1",
                "volumes": [{"size": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0, 1]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[
                {"remoteSymmetrix": "remote_array_1"},
                {"remoteSymmetrix": "remote_array_2"},
            ]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_new_volume_to_storage_group.assert_not_called()

    def test_add_vol_to_sg_srdf_3_sites(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "serial_no": "1",
                "volumes": [{"size": "2"}],
                "vol_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(return_value=[])
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0, 1, 2]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[
                {"remoteSymmetrix": "remote_array_1"},
                {"remoteSymmetrix": "remote_array_2"},
                {"remoteSymmetrix": "remote_array_3"},
            ]
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("srdf_more_than_2", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_volumes_from_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [
                    {"vol_id": "1"},
                    {"vol_name": "vol_2"},
                    {"vol_name": "vol_3"},
                    {},
                ],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1", "2"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            side_effect=[["2"], []]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol1_1",
                    "wwn": "33",
                },
                {
                    "effective_wwn": "34",
                    "type": "TDEV",
                    "volumeId": "2",
                    "volume_identifier": "vol_2",
                    "wwn": "34",
                },
            ]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_volume_from_storage_group.assert_called()

    def test_remove_volumes_from_sg_duplicate_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_name": "vol_2"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["2"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["2", "3"]
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("duplicate_volume"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_volumes_from_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol1_1",
                    "wwn": "33",
                }
            ]
        )
        powermax_module_mock.provisioning.remove_volume_from_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("remove_volume_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_volumes_from_sg_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol1_1",
                    "wwn": "33",
                }
            ]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_volume_from_storage_group.assert_not_called()

    def test_remove_volumes_from_sg_srdf_protected(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "absent-in-group",
            }
        )
        res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        res.update({"unprotected": False})
        powermax_module_mock.replication.get_replication_enabled_storage_groups = (
            MagicMock(return_value=["test_sg"])
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=res
        )
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[{"remoteSymmetrix": "remote_array_1"}]
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol1_1",
                    "wwn": "33",
                }
            ]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_volume_from_storage_group.assert_not_called()

    def test_remove_volumes_from_sg_srdf_protected_multisite(
        self, powermax_module_mock
    ):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "absent-in-group",
            }
        )
        res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        res.update({"unprotected": False})
        powermax_module_mock.replication.get_replication_enabled_storage_groups = (
            MagicMock(return_value=["test_sg"])
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=res
        )
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0, 1]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[
                {"remoteSymmetrix": "remote_array_1"},
                {"remoteSymmetrix": "remote_array_2"},
            ]
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol1_1",
                    "wwn": "33",
                }
            ]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_volume_from_storage_group.assert_called()

    def test_remove_volumes_from_sg_srdf_protected_multisite_check_mode(
        self, powermax_module_mock
    ):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "absent-in-group",
            }
        )
        res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        res.update({"unprotected": False})
        powermax_module_mock.replication.get_replication_enabled_storage_groups = (
            MagicMock(return_value=["test_sg"])
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=res
        )
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0, 1]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[
                {"remoteSymmetrix": "remote_array_1"},
                {"remoteSymmetrix": "remote_array_2"},
            ]
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol1_1",
                    "wwn": "33",
                }
            ]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_volume_from_storage_group.assert_not_called()

    def test_remove_volumes_from_sg_srdf_protected_3_sites(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "absent-in-group",
            }
        )
        res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        res.update({"unprotected": False})
        powermax_module_mock.replication.get_replication_enabled_storage_groups = (
            MagicMock(return_value=["test_sg"])
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=res
        )
        powermax_module_mock.replication.get_storage_group_srdf_group_list = MagicMock(
            return_value=[0, 1, 2]
        )
        powermax_module_mock.replication.get_rdf_group = MagicMock(
            side_effect=[
                {"remoteSymmetrix": "remote_array_1"},
                {"remoteSymmetrix": "remote_array_2"},
                {"remoteSymmetrix": "remote_array_3"},
            ]
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["1"]
        )
        powermax_module_mock.provisioning.get_volume = MagicMock(
            side_effect=[
                {
                    "effective_wwn": "33",
                    "type": "TDEV",
                    "volumeId": "1",
                    "volume_identifier": "vol1_1",
                    "wwn": "33",
                }
            ]
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("srdf_more_than_2", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_no_volume_from_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "volumes": [{"vol_id": "1"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["2"]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_volume_from_storage_group.assert_not_called()

    def test_move_volumes_between_sgs(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "target_sg_name": "target_sg",
                "volumes": [{"vol_id": "1"}, {"vol_name": "vol_2"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_volumes_from_storage_group = MagicMock(
            return_value=["1", "2"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["2"]
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["modify_sg"]
        assert powermax_module_mock.module.exit_json.call_args[1]["remove_vols_from_sg"]

    def test_move_volumes_between_sgs_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "target_sg_name": "target_sg",
                "volumes": [{}, {"vol_id": "1"}, {"vol_name": "vol_2"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.get_volumes_storagegroup = MagicMock(
            return_value=["1", "2"]
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["vol2"]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.move_volumes_between_storage_groups.assert_not_called()
        assert powermax_module_mock.module.exit_json.call_args[1]["modify_sg"]
        assert powermax_module_mock.module.exit_json.call_args[1]["remove_vols_from_sg"]

    def test_move_volumes_between_sgs_srdf_check_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "target_sg_name": "target_sg",
                "volumes": [{"vol_id": "123"}],
                "vol_state": "absent-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"unprotected": False})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.get_volumes_to_move = MagicMock(
            return_value=["1", "2", "3"]
        )
        powermax_module_mock.replication.get_replication_enabled_storage_groups = (
            MagicMock(side_effect=MockApiException)
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("srdf_check_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_move_volumes_between_sgs_duplicate_vols(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "state": "present",
                "target_sg_name": "target_sg",
                "volumes": [{"vol_id": "123", "vol_name": "test"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_volume_list = MagicMock(
            return_value=["vol1", "vol2"]
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("duplicate_volume"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_move_volumes_between_srdf_protected_sgs(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "target_sg_name": "target_sg",
                "volumes": [{"vol_id": "123", "vol_name": "test"}],
                "vol_state": "absent-in-group",
            }
        )
        powermax_module_mock.get_volumes_to_move = MagicMock(
            return_value=["1", "2", "3"]
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("move_srdf_vol_no_force"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_move_volumes_between_srdf_protected_sgs_with_force(
        self, powermax_module_mock
    ):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "target_sg_name": "target_sg",
                "volumes": [{"vol_id": "123", "vol_name": "test"}],
                "vol_state": "absent-in-group",
                "force": True,
            }
        )
        powermax_module_mock.get_volumes_to_move = MagicMock(
            return_value=["1", "2", "3"]
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.module.exit_json.call_args[1]["modify_sg"]
        assert powermax_module_mock.module.exit_json.call_args[1]["remove_vols_from_sg"]

    def test_set_host_io_limit(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "host_io_limit": {
                    "dynamic_distribution": "Always",
                    "host_io_limit_mbps": 100,
                    "host_io_limit_iops": 100,
                }
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update(
            {
                "hostIOLimit": {
                    "host_io_limit_mb_sec": "NOLIMIT",
                    "dynamic_distribution": "Never",
                    "host_io_limit_io_sec": "10",
                }
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.provisioning.set_host_io_limit_iops_or_mbps = MagicMock(
            return_value={
                "host_io_limit_mb_sec": "100",
                "host_io_limit_io_sec": "100",
                "dynamicDistribution": "Always",
            }
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.set_host_io_limit_iops_or_mbps.assert_called

    def test_set_host_io_limit_iops_none(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "host_io_limit": {
                    "dynamic_distribution": "Always",
                    "host_io_limit_mbps": 100,
                    "host_io_limit_iops": None,
                }
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update(
            {
                "hostIOLimit": {
                    "host_io_limit_mb_sec": "NOLIMIT",
                    "dynamic_distribution": "Never",
                    "host_io_limit_io_sec": "10",
                }
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.provisioning.set_host_io_limit_iops_or_mbps = MagicMock(
            return_value={
                "host_io_limit_mb_sec": "100",
                "host_io_limit_io_sec": "100",
                "dynamicDistribution": "Always",
            }
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.set_host_io_limit_iops_or_mbps.assert_called

    def test_set_host_io_limit_validate_iops_failed(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "host_io_limit": {
                    "dynamic_distribution": "Always",
                    "host_io_limit_mbps": 100,
                    "host_io_limit_iops": 1,
                }
            }
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("iops_check_failed"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_set_host_io_limit_validate_mbps_failed(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "host_io_limit": {
                    "dynamic_distribution": "Always",
                    "host_io_limit_mbps": -1,
                    "host_io_limit_iops": 100,
                }
            }
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("mbps_check_failed"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_set_host_io_limit_without_io_limit(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "host_io_limit": {
                    "dynamic_distribution": "Always",
                    "host_io_limit_mbps": None,
                    "host_io_limit_iops": None,
                }
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("io_limit_required"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_set_host_io_limit_no_change(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "host_io_limit": {
                    "dynamic_distribution": "Always",
                    "host_io_limit_mbps": 100,
                    "host_io_limit_iops": 100,
                },
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update(
            {
                "hostIOLimit": {
                    "host_io_limit_mb_sec": "100",
                    "dynamicDistribution": "Always",
                    "host_io_limit_io_sec": "100",
                }
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.set_host_io_limit_iops_or_mbps.assert_not_called()

    def test_set_host_io_limit_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "host_io_limit": {
                    "dynamic_distribution": "Always",
                    "host_io_limit_mbps": None,
                    "host_io_limit_iops": 100,
                },
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update(
            {
                "hostIOLimit": {
                    "host_io_limit_mb_sec": "2",
                    "dynamic_distribution": "Never",
                    "host_io_limit_io_sec": "10",
                }
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.provisioning.set_host_io_limit_iops_or_mbps = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("set_io_limit_exception"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_sg_attr(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "new_sg_name": "test_sg_2",
                "srp": "SRP_2",
                "service_level": "Diamond",
                "compression": True,
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.perform_module_operation()
        assert powermax_module_mock.provisioning.modify_storage_group.call_count == 4

    def test_rename_storagegroup_same_name(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"new_sg_name": "test_sg"})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_storage_group.assert_not_called()

    def test_rename_storagegroup_when_create(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"new_sg_name": "new_name"})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=None
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("rename_when_create", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_rename_storagegroup_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"new_sg_name": "test_sg_2"})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.modify_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("rename_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_sg_attr_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "new_sg_name": "test_sg_2",
                "srp": "SRP_2",
                "service_level": "Diamond",
                "compression": True,
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.modify_storage_group.assert_not_called()

    def test_modify_sg_srp_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"srp": "SRP_2"})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.modify_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("modify_srp_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_sg_slo_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"service_level": "Diamond"})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.modify_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("modify_slo_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_modify_sg_compression_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"compression": True})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.modify_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "modify_compression_exception", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_child_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "child_storage_groups": ["child_1", "child_2"],
                "child_sg_state": "present-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            side_effect=[False, True]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_child_storage_group_to_parent_group.assert_called()

    def test_add_child_sg_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {"child_storage_groups": ["child_1"], "child_sg_state": "present-in-group"}
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            return_value=False
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.add_child_storage_group_to_parent_group.assert_not_called()

    def test_add_protected_child_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {"child_storage_groups": ["child_1"], "child_sg_state": "present-in-group"}
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            return_value=False
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("add_csg_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_child_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {"child_storage_groups": ["child_1"], "child_sg_state": "present-in-group"}
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            return_value=False
        )
        powermax_module_mock.provisioning.add_child_storage_group_to_parent_group = (
            MagicMock(side_effect=MockApiException)
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("add_csg_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_child_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "child_storage_groups": ["child_1", "child_2"],
                "child_sg_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            side_effect=[False, True]
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_child_storage_group_from_parent_group.assert_called()

    def test_remove_child_sg_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {"child_storage_groups": ["child_1"], "child_sg_state": "absent-in-group"}
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            return_value=True
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.remove_child_storage_group_from_parent_group.assert_not_called()

    def test_remove_protected_child_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {"child_storage_groups": ["child_1"], "child_sg_state": "absent-in-group"}
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            return_value=True
        )
        powermax_module_mock.if_srdf_protected = MagicMock(return_value=True)
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("remove_csg_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_child_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {"child_storage_groups": ["child_1"], "child_sg_state": "absent-in-group"}
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.is_child_storage_group_in_parent_storage_group = MagicMock(
            return_value=True
        )
        powermax_module_mock.provisioning.remove_child_storage_group_from_parent_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("remove_csg_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_snapshot_pol_to_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy", "30min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.snapshot_policy.associate_to_storage_groups.assert_called()

    def test_add_snapshot_pol_to_sg_unsupported_version(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy", "30min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        utils.PyU4V.__version__ = "9.2.1.2"
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("unsupported_pyu4v_version"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_existing_snapshot_pol_to_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.snapshot_policy.associate_to_storage_groups.assert_not_called()

    def test_add_snapshot_pol_to_sg_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy", "30min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.snapshot_policy.associate_to_storage_groups.assert_not_called()

    def test_add_snapshot_pol_to_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy", "30min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.snapshot_policy.associate_to_storage_groups = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "add_snapshot_policy_exception", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_add_snapshot_pol_to_sg_compliance_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy", "30min_policy"],
                "snapshot_policy_state": "present-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy"]})
        powermax_module_mock.snapshot_policy.get_snapshot_policy_compliance = MagicMock(
            side_effect=MockApiException
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "get_policy_comp_exception", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_remove_snapshot_pol_from_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy"],
                "snapshot_policy_state": "absent-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy", "30min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.snapshot_policy.disassociate_from_storage_groups.assert_called()

    def test_remove_snapshot_pol_from_empty_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy"],
                "snapshot_policy_state": "absent-in-group",
            }
        )
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.snapshot_policy.disassociate_from_storage_groups.assert_not_called()

    def test_remove_no_snapshot_pol_from_sg(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["30min_policy"],
                "snapshot_policy_state": "absent-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.snapshot_policy.disassociate_from_storage_groups.assert_not_called()

    def test_remove_snapshot_pol_from_sg_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy"],
                "snapshot_policy_state": "absent-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy", "30min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.snapshot_policy.disassociate_from_storage_groups.assert_not_called()

    def test_remove_snapshot_pol_from_sg_exception(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update(
            {
                "snapshot_policies": ["10min_policy"],
                "snapshot_policy_state": "absent-in-group",
            }
        )
        sg_res = MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        sg_res.update({"snapshot_policies": ["10min_policy", "30min_policy"]})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=sg_res
        )
        powermax_module_mock.snapshot_policy.disassociate_from_storage_groups = (
            MagicMock(side_effect=MockApiException)
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "remove_snapshot_policy_exception", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_delete_storagegroup(self, powermax_module_mock):
        self.storage_group_args.update({"state": "absent"})
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_storage_group.assert_called()

    def test_delete_storagegroup_linked_snaps(self, powermax_module_mock):
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.replication.get_storage_group_snapshot_list = MagicMock(
            return_value=["snap_1", "snap_2"]
        )
        powermax_module_mock.replication.get_storage_group_snapshot_generation_list = (
            MagicMock(side_effect=[{}, {"isLinked": True}])
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message(
                "delete_sg_with_linked_snap", "test_sg"
            ),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_delete_storagegroup_check_mode(self, powermax_module_mock):
        powermax_module_mock.module.check_mode = True
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.module.params.update({"state": "absent"})
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.provisioning.delete_storage_group.assert_not_called()

    def test_delete_storagegroup_exception(self, powermax_module_mock):
        self.storage_group_args.update({"state": "absent"})
        powermax_module_mock.module.params = self.storage_group_args
        powermax_module_mock.provisioning.get_storage_group = MagicMock(
            return_value=MockStorageGroupApi.STORAGEGROUP_RESPONSE_DETAILS
        )
        powermax_module_mock.provisioning.delete_storage_group = MagicMock(
            side_effect=MockApiException
        )
        self.capture_fail_json_method(
            MockStorageGroupApi.get_error_message("delete_exception", "test_sg"),
            powermax_module_mock,
            "perform_module_operation",
        )

    def test_show_error_exception(self, powermax_module_mock):
        msg = "Error message"
        utils.close_connection = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(msg, powermax_module_mock, "show_error_exit", msg)
