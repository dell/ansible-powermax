# Copyright: (c) 2021, Dell EMC

# Apache License version 2.0 (see MODULE-LICENSE or http://www.apache.org/licenses/LICENSE-2.0.txt)

""" import powermax sdk"""

from __future__ import (absolute_import, division, print_function)
from decimal import Decimal
import logging
__metaclass__ = type

try:
    import PyU4V
    from PyU4V.utils.exception import ResourceNotFoundException
    HAS_PYU4V = True
except ImportError:
    HAS_PYU4V = False

'''import pkg_resources'''
try:
    from pkg_resources import parse_version
    import pkg_resources
    PKG_RSRC_IMPORTED = True
except ImportError:
    PKG_RSRC_IMPORTED = False

'''
Check required libraries
'''


def has_pyu4v_sdk():
    return HAS_PYU4V


def pyu4v_version_check():
    '''
    Check if required PyU4V version is installed
    '''
    try:
        if not PKG_RSRC_IMPORTED:
            unsupported_version_message = "Unable to import " \
                                          "'pkg_resources', please install" \
                                          " the required package"
            return unsupported_version_message
        min_ver = '9.1.2.0'
        max_ver = '9.3.0.0'
        curr_version = PyU4V.__version__
        unsupported_version_message = "PyU4V {0} is not supported by this " \
                                      "module.Minimum supported version " \
                                      "is : {1} and less than {2} ".format(
                                          curr_version, min_ver, max_ver)
        supported_version = (parse_version(
            min_ver) <= parse_version(curr_version) < parse_version(max_ver)
        )
        if supported_version is False:
            return unsupported_version_message
        return None
    except Exception as e:
        unsupported_version_message = "Unable to get the PyU4V version, " \
                                      "failed with Error {0} ".format(str(e))
        return unsupported_version_message


def universion_check(universion):
    '''
    Check if valid Unisphere Version
    '''
    is_valid_universion = False
    user_message = ""
    curr_version = PyU4V.__version__

    try:
        if curr_version.startswith("9.1") and universion == 91:
            is_valid_universion = True
        elif curr_version.startswith("9.2") and universion == 92:
            is_valid_universion = True
        else:
            user_message = "Unsupported unisphere version for current PyU4V"

        universion_details = {"is_valid_universion": is_valid_universion,
                              "user_message": user_message}
        return universion_details

    except Exception as e:
        is_valid_universion = False
        user_message = "Failed to validate the Unisphere version " \
                       "with error {0}".format(str(e))

        universion_details = {"is_valid_universion": is_valid_universion,
                              "user_message": user_message}
        return universion_details


'''
This method provides common access parameters required for the ansible modules
 on PowerMax
options:
  unispherehost:
    description:
    - IP/FQDN of unisphere host.
    required: true
  universion:
    description:
    - Version of univmax SDK.
  verifycert:
    description:
    - Boolean value to inform system whether to verify client certificate or
    not.
  user:
    description:
    - User name to access on to unispherehost
  password:
    description:
    - password to access on to unispherehost
  serial_no:
    description:
    - Serial number of Powermax system

'''


def get_powermax_management_host_parameters():
    return dict(
        unispherehost=dict(type='str', required=True, no_log=True),
        universion=dict(type='int', required=False, choices=[91, 92]),
        verifycert=dict(type='bool', required=True, choices=[True, False]),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        serial_no=dict(type='str', required=True)
    )


'''
This method provides common access parameters required for the ansible modules
 on PowerMax Unisphere
options:
  unispherehost:
    description:
    - IP/FQDN of unisphere host.
    required: true
  universion:
    description:
    - Version of univmax SDK.
  verifycert:
    description:
    - Boolean value to inform system whether to verify client certificate or
    not.
  user:
    description:
    - User name to access on to unispherehost
  password:
    description:
    - password to access on to unispherehost
'''


def get_u4v_unisphere_connection_parameters():
    return dict(
        unispherehost=dict(type='str', required=True, no_log=True),
        universion=dict(type='int', required=False, choices=[91, 92]),
        verifycert=dict(type='bool', required=True, choices=[True, False]),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True)
    )


'''
This method is to establish connection to PowerMax
using PyU4v SDK.
parameters:
  module_params - Ansible module parameters which contain below unisphere
   details to establish connection on to Unisphere
     - unispherehost: IP/FQDN of unisphere host.
     - universion:Version of univmax SDK.
     - verifycert: Boolean value to inform system whether to verify client
      certificate or not.
     - user:  User name to access on to unispherehost
     - password: Password to access on to unispherehost
     - serial_no: Serial number of Powermax system
returns connection object to access provisioning and protection sdks
'''


def get_U4V_connection(module_params, application_type=None):
    if HAS_PYU4V:
        conn = PyU4V.U4VConn(server_ip=module_params['unispherehost'],
                             port=8443,
                             array_id=module_params['serial_no'],
                             verify=module_params['verifycert'],
                             username=module_params['user'],
                             password=module_params['password'],
                             application_type=application_type)
        return conn


'''
This method is to establish connection to PowerMax Unisphere
using PyU4v SDK.
parameters:
  module_params - Ansible module parameters which contain below unisphere
                  details to establish connection on to Unisphere
     - unispherehost: IP/FQDN of unisphere host.
     - universion:Version of univmax SDK.
     - verifycert: Boolean value to inform system whether to verify client
                   certificate or not.
     - user:  User name to access on to unispherehost
     - password: Password to access on to unispherehost
returns connection object to access U4V Unisphere Common sdks
'''


def get_u4v_unisphere_connection(module_params, application_type=None):
    if HAS_PYU4V:
        conn = PyU4V.U4VConn(server_ip=module_params['unispherehost'],
                             port=8443,
                             verify=module_params['verifycert'],
                             username=module_params['user'],
                             password=module_params['password'],
                             application_type=application_type)
        return conn


'''
This method is to initialize logger and return the logger object
parameters:
     - module_name: Name of module to be part of log message.
     - log_file_name: name of the file in which the log meessages get
      appended.
     - log_devel: log level.
returns logger object
'''


def get_logger(module_name, log_file_name='dellemc_ansible_provisioning.log',
               log_devel=logging.INFO):
    FORMAT = '%(asctime)-15s %(filename)s %(levelname)s : %(message)s'
    logging.basicConfig(filename=log_file_name, format=FORMAT)
    LOG = logging.getLogger(module_name)
    LOG.setLevel(log_devel)
    return LOG


'''
Convert the given size to bytes
'''
KB_IN_BYTES = 1024
MB_IN_BYTES = 1024 * 1024
GB_IN_BYTES = 1024 * 1024 * 1024
TB_IN_BYTES = 1024 * 1024 * 1024 * 1024


def get_size_bytes(size, cap_units):
    if size is not None and size > 0:
        if cap_units in ('kb', 'KB'):
            return size * KB_IN_BYTES
        elif cap_units in ('mb', 'MB'):
            return size * MB_IN_BYTES
        elif cap_units in ('gb', 'GB'):
            return size * GB_IN_BYTES
        elif cap_units in ('tb', 'TB'):
            return size * TB_IN_BYTES
        else:
            return size
    else:
        return 0


'''
Convert the given size to size in GB, size is restricted to 2 decimal places
'''


def get_size_in_gb(size, cap_units):
    size_in_bytes = get_size_bytes(size, cap_units)
    size = Decimal(size_in_bytes / GB_IN_BYTES)
    size_in_gb = round(size, 2)
    return size_in_gb


'''
Close unisphere connection
'''


def close_connection(module_obj):
    module_obj.close_session()
