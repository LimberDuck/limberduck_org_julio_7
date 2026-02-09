:description: Using instruction for TSCCM.

#####
Using
#####

``tsccm --help``
==============

Check help for **TSCCM** commands using ``tsccm [command] --help``.


``tsccm audit-file``
====================

``tsccm audit-file --list``
---------------------------

Get audit files list.

``tsccm credential``
====================

``tsccm credential --list``
---------------------------

Get credentials list from Tenable Security Center.


.. code-block:: shell

   tsccm credential -a console_address -u user_name --list
   tsccm v.0.0.7

             id          name        type     authType   ownerUsername          createdTime        modifiedTime
   1    1000002   cred_name_1    database     password           user1  2025-01-28 16:14:01 2025-05-16 11:31:33
   2    1000003   cred_name_2         ssh    publicKey           user2  2025-02-22 12:53:40 2025-03-21 11:21:52
   3    1000004   cred_name_3     windows     password           user3  2025-02-23 11:11:35 2025-03-21 11:22:06
   .. more rows ...

.. tip::

   Use :ref:`tsccm-format-option` option to change the output format. For example, use ``--format csv`` 
   to get the output in |CSV| format, or ``--format json`` to get the output in |JSON| format.

.. tip::

   To convert |CSV| files to Excel in bulk use :doc:`../converter-csv/index`.

.. tip::
   If you use self signed certificate for your Tenable Security Center, 
   use :ref:`tsccm-insecure-option` / ``-k`` option to perform insecure |SSL| connection.

   .. warning::
    
    It's strongly recommended to configure your Tenable Security Center to use a valid certificate.

``tsccm group``
===============

``tsccm group --list``
----------------------

Get groups list.

``tsccm policy``
================

``tsccm policy --list``
----------------------

Get scan policies list.

``tsccm role``
==============

``tsccm role --list``
----------------------

Get roles list

``tsccm scan``
==============

``tsccm scan --list``
----------------------

Get active scans list.

``tsccm scan-result``
====================

``tsccm scan-result --list``
----------------------------

Get scans results list.

``tsccm server``
================

``tsccm server --status``
-------------------------

Get server status.

``tsccm server --ips``
-----------------------

Get the number of licensed IPs, active IPs and left IPs

``tsccm server --version``
--------------------------

Get server version.

global options
==============

``--address``
-------------

-a, --address TEXT

address to which you want to login  [default: (127.0.0.1)]

``--port``
----------

--port TEXT

port to which you want to login  [default: (443)]

``--username``
--------------

-u, --username TEXT 
username which you want to use to login  [default: (current user)]

``--password``
--------------

-p, --password TEXT

password which you want to use to login

.. _tsccm-insecure-option:

``--insecure``
--------------

-k, --insecure

perform insecure SSL connections and transfers

.. _tsccm-format-option:

``--format``
------------

-f, --format TEXT

data format to display [table,json,csv]  [default: (table)]

``--filter``
------------

-f, --filter TEXT

filter data with JMESPath. See https://jmespath.org/ for more information and examples.

``--verbose``
-------------

-v, --verbose

Get more verbose output.