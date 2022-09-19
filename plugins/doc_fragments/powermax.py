# -*- coding: utf-8 -*-
# Copyright: (c) 2019-2021, Dell Technologies.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r'''
options:
    unispherehost:
        description:
            - IP or FQDN of the Unisphere host
        type: str
        required: True
    universion:
        description:
            - Unisphere version, currently '91', '92' and '100' versions are
              supported.
        type: int
        required: False
        choices: [91, 92, 100]
    verifycert:
        description:
            - Specifies system whether to validate SSL certificate or not, Values can be True or
              False or a custom file path for SSL certificate with .pem extension or .cer with base 64 encoding.
        type: str
        required: True
    user:
        description:
            - The username of the Unisphere host.
        type: str
        required: True
    password:
        description:
            - The password of the Unisphere host.
        type: str
        required: True

requirements:
  - A Dell PowerMax storage system.
  - Ansible 2.11, 2.12, 2.13.
notes:
  - The modules present in this collection named as 'dellemc.powermax'
    are built to support the Dell PowerMax storage platform.
'''

    # Documentation fragment for PowerMax with serial_no (powermax_serial_no)
    POWERMAX_SERIAL_NO = r'''
options:
    serial_no:
        description:
            - The serial number of the PowerMax/VMAX array. It is a
              required parameter for all array-specific operations
              except for getting a list of arrays in the
              Gatherfacts module.
        type: str
        required: True
'''
