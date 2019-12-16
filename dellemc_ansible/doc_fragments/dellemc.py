# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Dell EMC.


class ModuleDocFragment(object):

    DOCUMENTATION = r'''
options:
  - See respective platform section for more details
requirements:
  - See respective platform section for more details
notes:
  - Ansible modules are available for EMC PowerMax Storage Platform

'''

    # Documentation fragment for PowerMax (dellemc_powermax)
    DELLEMC_POWERMAX = r'''
options:
    serial_no:
        description:
            - the serial number of  PowerMax/VMAX array. It is a
              required parameter for all array specific operations 
              except for getting list of arrays in the 
              Gatherfacts module.
        type: str
        required: True
    unispherehost:
        description:
            - IP or FQDN of the Unisphere host
        type: str
        required: True
    universion:
        description:
            - Unisphere version, currently only version '90' is supported.
        type: str
        required: True
    verifycert:
        description:
            - boolean variable to specify whether to validate SSL
              certificate or not.
            - True - indicates that the SSL certificate should be
                     verified.
            - False - indicates that the SSL certificate should not be
                      verified.
        type: bool
        required: True
        choices: [ True, False]        
    user:
        description:
            - username of the Unisphere host.
        type: str
        required: True
    password:
        description:
            - the password of the Unisphere host.
        type: str
        required: True

requirements:
  - A DellEMC PowerMax Storage device.
  - Ansible 2.7.
notes:
  - The modules prefixed with dellemc_powermax are built to support the
    DellEMC PowerMax storage platform.
'''
