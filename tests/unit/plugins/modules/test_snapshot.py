# Copyright: (c) 2024, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Unit Tests for Snapshot module on PowerMax"""

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


from ansible_collections.dellemc.powermax.plugins.modules.snapshot import Snapshot, SnapshotHandler
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_snapshot_api import MockSnapshotApi
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base \
    import PowerMaxUnitBase


class TestSnapshot(PowerMaxUnitBase):
    MODULE_PATH = 'ansible_collections.dellemc.powermax.plugins.modules.snapshot.Snapshot.'
    MODULE_UTILS_PATH = 'ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell.utils'
    snapshot_args = MockSnapshotApi.SNAPSHOT_COMMON_ARGS

    @pytest.fixture
    def snapshot_module_mock(self, mocker):
        snapshot_module_mock = Snapshot()
        snapshot_module_mock.module = MagicMock()
        snapshot_module_mock.replication = MagicMock()
        snapshot_module_mock.module.check_mode = False
        snapshot_module_mock.u4v_conn = MagicMock()
        return snapshot_module_mock

    def test_create_snapshot_ttl_unit_days(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'ttl': "2",
             'ttl_unit': "days"})
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.create_storage_group_snapshot.assert_called()
        assert snapshot_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_snapshot_ttl_unit_hours(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'ttl': "2",
             'ttl_unit': "hours"})
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.create_storage_group_snapshot.assert_called()
        assert snapshot_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_create_snapshot_ttl_none(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'ttl': "None",
             'ttl_unit': "days"})
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.create_storage_group_snapshot.assert_called()
        assert snapshot_module_mock.module.exit_json.call_args[1]['changed'] is True

    def test_get_snapshot_by_generation(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.get_snapshot_generation_details.assert_called()

    def test_get_snapshot_by_id(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.get_snapshot_snap_id_details.assert_called()

    def test_get_snapshot_by_name(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_storage_group_snapshot_generation_list = MagicMock(
            return_value=MockSnapshotApi.GENERATION_LIST)
        snapshot_module_mock.is_snap_id_supported = MagicMock(return_value=True)
        snapshot_module_mock.replication.get_storage_group_snapshot_snap_id_list = MagicMock(
            return_value=MockSnapshotApi.SNAP_ID_LIST)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.get_storage_group_snapshot_generation_list.assert_called()

    def test_get_snapshot_by_generation_no_snap_id(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_storage_group_snapshot_generation_list = MagicMock(
            return_value=MockSnapshotApi.GENERATION_LIST)
        snapshot_module_mock.is_snap_id_supported = MagicMock(return_value=False)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.get_storage_group_snapshot_generation_list.assert_called()

    def test_rename_snapshot_by_id(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'new_snapshot_name': "new_test_snapshot_name"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot_by_snap_id.assert_called()

    def test_rename_snapshot_by_generation(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0,
             'new_snapshot_name': "new_test_snapshot_name"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot.assert_called()

    def test_rename_snapshot_with_existing_name_idempotency(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0,
             'new_snapshot_name': MockSnapshotApi.SNAPSHOT_NAME
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)

    def test_link_snapshot_by_id(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'link_status': "linked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot_by_snap_id.assert_called()

    def test_link_linked_snapshot_by_id_idempotency(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'link_status': "linked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_LINKED_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)

    def test_link_snapshot_by_generation(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0,
             'link_status': "linked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot.assert_called()

    def test_link_linked_snapshot_by_generation_idempotency(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0,
             'link_status': "linked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_LINKED_2)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)

    def test_unlink_snapshot_by_id(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'link_status': "unlinked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_LINKED_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot_by_snap_id.assert_called()

    def test_unlink_unlinked_snapshot_by_id_idempotency(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'link_status': "unlinked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_1)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)

    def test_unlink_snapshot_by_generation(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0,
             'link_status': "unlinked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_LINKED_2)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot.assert_called()

    def test_unlink_unlinked_snapshot_by_generation_idempotency(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0,
             'link_status': "unlinked",
             'target_sg_name': "ansible-snap-sg-target"
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_2)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)

    def test_restore_snapshot_by_id(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID,
             'restore': True
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_2)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot_by_snap_id.assert_called()

    def test_restore_snapshot_by_generation(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'present',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0,
             'restore': True
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_2)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.modify_storage_group_snapshot.assert_called()

    def test_delete_snapshot_by_id(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'absent',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_2)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.delete_storage_group_snapshot_by_snap_id.assert_called()

    def test_delete_snapshot_by_generation(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'absent',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'generation': 0
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_generation_details = MagicMock(return_value=MockSnapshotApi.SNAPSHOT_DETAILS_2)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)
        snapshot_module_mock.replication.delete_storage_group_snapshot.assert_called()

    def test_delete_non_existing_snapshot_by_id_idempotency(self, snapshot_module_mock):
        self.snapshot_args.update(
            {'state': 'absent',
             'sg_name': MockSnapshotApi.SG_NAME,
             'snapshot_name': MockSnapshotApi.SNAPSHOT_NAME,
             'snapshot_id': MockSnapshotApi.SNAPSHOT_ID
             })
        snapshot_module_mock.module.params = self.snapshot_args
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(side_effect=MockApiException)
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        SnapshotHandler().handle(snapshot_module_mock, snapshot_module_mock.module.params)

    def test_get_snapshot_by_id_exception(self, snapshot_module_mock):
        sg_id = MockSnapshotApi.SG_NAME
        snapshot_name = MockSnapshotApi.SNAPSHOT_NAME
        snap_id = MockSnapshotApi.SNAPSHOT_ID
        generation = None
        snapshot_module_mock.u4v_conn.set_array_id = MagicMock(return_value=None)
        snapshot_module_mock.replication.get_snapshot_snap_id_details = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'get_details_exception'), snapshot_module_mock,
            'get_snapshot', sg_id, snapshot_name, generation, snap_id)

    def test_rename_snapshot_by_id_exception(self, snapshot_module_mock):
        sg_id = MockSnapshotApi.SG_NAME
        snap_name = MockSnapshotApi.SNAPSHOT_NAME
        new_snap_name = "new_test_snapshot_name"
        generation = 0
        snap_id = MockSnapshotApi.SNAPSHOT_ID
        snapshot_module_mock.replication.modify_storage_group_snapshot = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'rename_exception'), snapshot_module_mock,
            'rename_sg_snapshot', sg_id, snap_name, new_snap_name, generation, snap_id)

    def test_create_snapshot_exception(self, snapshot_module_mock):
        sg_id = MockSnapshotApi.SG_NAME
        snap_name = MockSnapshotApi.SNAPSHOT_NAME
        ttl = "2"
        ttl_unit = "days"
        snapshot_module_mock.replication.create_storage_group_snapshot = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'create_exception'), snapshot_module_mock,
            'create_sg_snapshot', sg_id, snap_name, ttl, ttl_unit)

    def test_delete_snapshot_by_id_exception(self, snapshot_module_mock):
        sg_id = MockSnapshotApi.SG_NAME
        snap_name = MockSnapshotApi.SNAPSHOT_NAME
        generation = None
        snap_id = MockSnapshotApi.SNAPSHOT_ID
        snapshot_module_mock.replication.delete_storage_group_snapshot_by_snap_id = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'delete_exception'), snapshot_module_mock,
            'delete_sg_snapshot', sg_id, snap_name, generation, snap_id)

    def test_restore_snapshot_by_id_exception(self, snapshot_module_mock):
        sg_id = MockSnapshotApi.SG_NAME
        snap_name = MockSnapshotApi.SNAPSHOT_NAME
        snap_id = MockSnapshotApi.SNAPSHOT_ID
        snapshot_module_mock.replication.modify_storage_group_snapshot_by_snap_id = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'restore_exception'), snapshot_module_mock,
            'restore_snapshot', sg_id, snap_name, snap_id)

    def test_link_snapshot_by_id_exception(self, snapshot_module_mock):
        sg_id = MockSnapshotApi.SG_NAME
        snap_name = MockSnapshotApi.SNAPSHOT_NAME
        snap_id = MockSnapshotApi.SNAPSHOT_ID
        target_sg = "ansible-snap-sg-target"
        link = "linked"
        unlink = None
        generation = None
        snapshot_module_mock.replication.modify_storage_group_snapshot_by_snap_id = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'link_exception'), snapshot_module_mock,
            'modify_snapshot', sg_id, target_sg, snap_name, link, unlink, snap_id, generation)

    def test_show_error_exception(self, snapshot_module_mock):
        msg = "random error message"
        utils.close_connection = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'exit_exception'), snapshot_module_mock,
            'show_error_exit', msg)

    def test_rename_snapshot_wo_snapshot_id_or_generation_exception(self, snapshot_module_mock):
        generation = None
        snap_id = None
        self.capture_fail_json_method(
            MockSnapshotApi.get_error_message(
                'no_id_exception'), snapshot_module_mock,
            'is_valid_generation_or_id', generation, snap_id)
