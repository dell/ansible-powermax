.. _job_module:


job -- Gets the detail information about a Job of a PowerMax/VMAX storage system
================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Gets details of a Job from a specified PowerMax/VMAX storage system.

The details listed are of an asynchronous task.



Requirements
------------
The below requirements are needed on the host that executes this module.

- A Dell PowerMax storage system.
- Ansible-core 2.15 or later.
- Python 3.10, 3.11 or 3.12.



Parameters
----------

  job_id (True, str, None)
    Job ID of an asynchronous task, used for getting details of a job.


  unispherehost (True, str, None)
    IP or FQDN of the Unisphere host


  universion (False, int, None)
    Unisphere version, currently '91', '92', '100' and '101' versions are supported.


  verifycert (True, str, None)
    Specifies system whether to validate SSL certificate or not, Values can be True or False or a custom file path for SSL certificate with .pem extension or .cer with base 64 encoding.


  user (True, str, None)
    The username of the Unisphere host.


  password (True, str, None)
    The password of the Unisphere host.


  timeout (optional, int, 120)
    Time after which the connection will get terminated.

    It is to be mentioned in seconds.


  port (optional, int, 8443)
    The port of the Unisphere host.





Notes
-----

.. note::
   - The modules present in this collection named as 'dellemc.powermax' are built to support the Dell PowerMax storage platform.




Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get the details of a Job.
      dellemc.powermax.job:
        unispherehost: "{{unispherehost}}"
        universion: "{{universion}}"
        verifycert: "{{verifycert}}"
        user: "{{user}}"
        password: "{{password}}"
        job_id: "1570622921504"



Return Values
-------------

changed (always, bool, )
  Whether or not the resource has changed.


Job_details (When job exist., dict, )
  Details of the job.


  completed_date_milliseconds (, int, )
    Date of job completion in milliseconds.


  jobId (, str, )
    Unique identifier of the job.


  last_modified_date (, str, )
    Last modified date of job.


  last_modified_date_milliseconds (, int, )
    Last modified date of job in milliseconds.


  name (, str, )
    Name of the job.


  resourceLink (, str, )
    Resource link w.r.t Unisphere.


  result (, str, )
    Job description


  status (, str, )
    Status of the job.


  task (, list, )
    Details about the job.


  username (, str, )
    Unisphere username.






Status
------





Authors
~~~~~~~

- Rajshree Khare (@khareRajshree) <ansible.team@dell.com>

