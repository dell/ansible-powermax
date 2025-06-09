# Copyright: (c) 2022-2025, Dell Technologies

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
from mock.mock import MagicMock, patch
from ansible_collections.dellemc.powermax.plugins.module_utils.storage.dell \
    import utils


utils.get_logger = MagicMock()
utils.has_pyu4v_sdk = MagicMock(return_value=True)
utils.pyu4v_version_check = MagicMock(return_value=None)
utils.get_u4v_unisphere_connection = MagicMock()
utils.close_connection = MagicMock()
from ansible.module_utils import basic
basic.AnsibleModule = MagicMock()

from ansible_collections.dellemc.powermax.plugins.modules.job import Job
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_job_api import MockJobApi
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.mock_api_exception \
    import MockApiException
from ansible_collections.dellemc.powermax.tests.unit.plugins.module_utils.shared_library.powermax_unit_base \
    import PowerMaxUnitBase


class TestJob(PowerMaxUnitBase):
    job_args = MockJobApi.JOB_COMMON_ARGS

    @pytest.fixture
    def module_object(self):
        return Job

    def test_job_init(self, powermax_module_mock):
        with patch('ansible_collections.dellemc.powermax.plugins.modules.job.HAS_PYU4V', False):
            with patch('ansible_collections.dellemc.powermax.plugins.modules.job.PYU4V_VERSION_CHECK', "mock check err"):
                utils.get_u4v_unisphere_connection = MagicMock(side_effect=MockApiException())
                powermax_module_mock.show_error_exit = MagicMock()
                powermax_module_mock.__init__()
                assert powermax_module_mock.show_error_exit.call_count == 3

    def test_get_job_invalid_id(self, powermax_module_mock):
        self.job_args.update(
            {"state": "present",
             "job_id": "invalid_id"})
        powermax_module_mock.module_wo_sensitive_data = self.job_args
        self.capture_fail_json_method(
            MockJobApi.get_error_message(
                'invalid_job_id', job_id='invalid_id'), powermax_module_mock,
            'perform_module_operation')

    def test_get_job(self, powermax_module_mock):
        self.job_args.update(
            {"state": "present",
             "job_id": "100000000"})
        powermax_module_mock.module_wo_sensitive_data = self.job_args
        powermax_module_mock.perform_module_operation()
        powermax_module_mock.common.get_job_by_id.assert_called()
        assert powermax_module_mock.module.exit_json.call_args[1]['changed'] is False

    def test_get_no_job(self, powermax_module_mock):
        self.job_args.update(
            {"state": "present",
             "job_id": "100000000"})
        powermax_module_mock.module_wo_sensitive_data = self.job_args
        powermax_module_mock.common.get_job_by_id = MagicMock(return_value={})
        self.capture_fail_json_method(
            MockJobApi.get_error_message(
                'get_no_job_detail', job_id='100000000'), powermax_module_mock,
            'perform_module_operation')

    def test_get_job_exception(self, powermax_module_mock):
        self.job_args.update(
            {"state": "present",
             "job_id": "100000000"})
        powermax_module_mock.module_wo_sensitive_data = self.job_args
        powermax_module_mock.common.get_job_by_id = MagicMock(side_effect=MockApiException)
        self.capture_fail_json_method(
            MockJobApi.get_error_message(
                'get_job_by_id_exception', job_id='100000000'), powermax_module_mock,
            'perform_module_operation')

    def test_show_error_exception(self, powermax_module_mock):
        msg = "Error message"
        utils.close_connection = MagicMock(
            side_effect=MockApiException)
        self.capture_fail_json_method(msg, powermax_module_mock, 'show_error_exit', msg)
