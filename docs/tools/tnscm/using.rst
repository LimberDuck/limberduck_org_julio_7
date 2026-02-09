:description: Using instruction for TNSCM.

#####
Using
#####


``tnscm --help``
==============

Check help for **TNSCM** commands using ``tnscm [command] --help``.

``tnscm plugin``
================

``tnscm plugin --family-list``
------------------------------

Get plugins families list.


``tnscm policy``
================

``tnscm policy --list``
-----------------------

Get scan policy list.

``tnscm policy --delete``
-------------------------

Delete scan policy.

``tnscm scan``
==============

``tnscm scan --list``
---------------------

Get scan list.

``tnscm scan --delete``
-----------------------

Delete scan with whole history.

``tnscm server``
================

``tnscm server --status``
-------------------------

Get server status.

``tnscm server --ips``
-----------------------

Get the number of licensed IPs, active IPs and left IPs.

``tnscm server --version``
--------------------------

Get server version.

``tnscm settings``
================

``tnscm settings --list``
-------------------------

Get settings list.

``tnscm user``
==============

``tnscm user --list``
---------------------

Get user list

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

``--insecure``
--------------

-k, --insecure

perform insecure SSL connections and transfers

.. _tnscm-format-option:

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