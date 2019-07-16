
try:
    import PyU4V
    HAS_PYU4V = True
except ImportError:
    HAS_PYU4V = False

import logging

from decimal import Decimal

'''
Check required libraries
'''

def has_pyu4v_sdk():
    return HAS_PYU4V


'''
Check if required PyU4V version installed
'''


def pyu4v_version_check():
    try:
        from pkg_resources import parse_version
        supported_version = False
        min_ver = '3.0.0.14'
        curr_version = PyU4V.__version__
        unsupported_version_message = "PyU4V {0} is not supported by this module.Minimum supported version is : " \
                                      "{1} ".format(curr_version, min_ver)
        supported_version = parse_version(curr_version) >= parse_version(min_ver)
        if supported_version is False:
            return unsupported_version_message
        else:
            return None
    except Exception as e:
        unsupported_version_message = "Unable to get the PyU4V version, failed with Error {0} ".format(
            str(e))
        return unsupported_version_message



'''
This method provide parameter required for the ansible modules on PowerMax
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
    - Boolean value to inform system whether to verify client certificate or not.
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
        unispherehost=dict(type='str', required=True),
        universion=dict(type='int', required=True),
        verifycert=dict(type='bool', required=True),
        user=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
        serial_no=dict(type='str', required=True)
    )


'''
This method is to establish connection to PowerMax
using PyU4v SDK.

parameters:
  module_params - Ansible module parameters which contain below unisphere details
                 to establish connection on to Unisphere
     - unispherehost: IP/FQDN of unisphere host.
     - universion:Version of univmax SDK.
     - verifycert: Boolean value to inform system whether to verify client certificate or not.
     - user:  User name to access on to unispherehost
     - password: Password to access on to unispherehost
     - serial_no: Serial number of Powermax system
returns connection object to access provisioning and protection sdks
'''


def get_U4V_connection(module_params):
    if HAS_PYU4V:
        conn = PyU4V.U4VConn(server_ip=module_params['unispherehost'],
                             port=8443,
                             array_id=module_params['serial_no'],
                             verify=module_params['verifycert'],
                             username=module_params['user'],
                             password=module_params['password'],
                             u4v_version=module_params['universion'])
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


def get_u4v_unisphere_connection(module_params):
    if HAS_PYU4V:
        conn = PyU4V.U4VConn(server_ip=module_params['unispherehost'], port=8443,
                             verify=module_params['verifycert'],
                             username=module_params['user'],
                             password=module_params['password'],
                             u4v_version=module_params['universion'])
        return conn


'''
This method is to initialize logger and return the logger object 

parameters:
     - module_name: Name of module to be part of log message.
     - log_file_name: name of the file in which the log meessages get appended.
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
MB_IN_BYTES = 1024*1024
GB_IN_BYTES = 1024*1024*1024
TB_IN_BYTES = 1024*1024*1024*1024


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
