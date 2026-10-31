:description: Using instruction for TNSCM.

#####
Using
#####


``tnscm --help``
================

Check help for **TNSCM** commands using ``tnscm [command] --help``.

.. code-block:: shell

   tnscm --help
   Usage: tnscm [OPTIONS] [COMMAND] [ARGS]...

     TNSCM - manages Tenable Nessus servers from command line

   Options:
     -v, --version       Show the version and exit.
     -u, --update-check  Check if a new version is available and exit.
     --help              Show this message and exit.

   Commands:
     plugin    get Nessus plugin info
     policy    get Nessus policy info
     scan      get Nessus scan details info
     server    get Nessus server info
     settings  get and change Nessus advanced settings
     user      get Nessus user info

All commands need address and port of your Nessus and user name. Examples below use:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username ...

See :ref:`tnscm-global-options` for all connection and output options.

``tnscm plugin``
================

``tnscm plugin --family-list``
------------------------------

Get plugins families list.

.. _tnscm-plugin-details:

``tnscm plugin --plugin-id``
----------------------------

.. versionadded:: v0.1.0

   Plugin details. :ref:`tnscm-upgrade` now!

Get all details of given plugin, together with link to its description on tenable.com.
``--plugin-id`` can be repeated to get details of many plugins at once.

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username --plugin-id 156860

.. code-block:: text
   :caption: Example output (shortened).

   attribute                 value
   ------------------------  -----------------------------------------------------------------
   id                        156860
   name                      Apache Log4j 1.x Multiple Vulnerabilities
   family_name               Misc.
   url                       https://www.tenable.com/plugins/nessus/156860
   risk_factor               High
   cvss3_base_score          9.8
   synopsis                  A logging library running on the remote host has multiple vulnerabilities.
   cve                       CVE-2019-17571, CVE-2020-9488, CVE-2022-23302, CVE-2022-23305, ...
   xref                      CEA-ID:CEA-2021-0004, CEA-ID:CEA-2021-0025, IAVA:2021-A-0573-S

Attributes which occur many times, like ``cve``, ``xref`` or ``dependency``, are joined in table and csv format,
and are lists in json format. Use :ref:`tnscm-filter-option` to compare selected details of many plugins:

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username --plugin-id 156860 --plugin-id 19506 \
     --filter "[].{id: id, name: name, risk_factor: risk_factor, cvss3: cvss3_base_score}"

.. _tnscm-plugin-file:

``tnscm plugin --plugin-file``
------------------------------

.. versionadded:: v0.1.0

   Plugin details by file name. :ref:`tnscm-upgrade` now!

Get details of plugin by its file name, e.g. ``scan_info.nasl``.
Plugin ``dependency`` attribute lists file names, not plugin ids, so you can paste its value
as it is - comma separated list is accepted. ``--plugin-file`` can be repeated and mixed with ``--plugin-id``.

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username \
     --plugin-file "nessus_product_setup.nasl, patches_summary.nbin" \
     --filter "[].{id: id, name: name, fname: fname, family: family_name}"

.. code-block:: text
   :caption: Example output.

         id  name                        fname                      family
   1  83955  Nessus Product Information  nessus_product_setup.nasl  Settings
   2  66334  Patch Report                patches_summary.nbin       General

File name has to be exact, otherwise TNSCM shows ``plugin file NAME not found.`` and exits with code ``2``.

.. _tnscm-plugin-dependencies:

``tnscm plugin --depends-on`` and ``--required-by``
---------------------------------------------------

.. versionadded:: v0.1.0

   Plugin dependency tree. :ref:`tnscm-upgrade` now!

Show tree of plugins on which given plugin depends (``--depends-on``) and plugins which depend on it
(``--required-by``), like file structure. Use with ``--plugin-id`` or ``--plugin-file``,
both options can be used together. Every plugin is shown as ``[plugin id] [plugin name] [plugin file name]``.

- ``--depth INTEGER`` - how many levels of plugins to show. Default is ``1`` - only direct dependencies
  or dependents of given plugin. ``0`` shows all levels.
- ``--max-plugins INTEGER`` - list plugins of one level only if there are at most this many,
  otherwise show only their number. Default is ``100``, ``0`` for no limit.

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username --plugin-id 57399 --required-by

.. code-block:: text
   :caption: Example output.

   [57399] [VMware vSphere Installed Patches] [vmware_installed_patches.nbin] is required by
   └── [97993] [OS Identification and Installed Software Enumeration over SSH v2 (Using New SSH Library)] [ssh_get_info2.nasl] - required by 96541 more, increase --depth INTEGER

Plugin which has more dependencies or dependents than shown gets a note, which option to increase
to see them:

- ``depends on 2 more, increase --depth INTEGER`` or ``required by 96541 more, increase --depth INTEGER`` -
  plugin is on the last level shown,
- ``depends on 3 more, increase --max-plugins INTEGER`` - there are more plugins on the next level than ``--max-plugins``.

When given plugin itself has too many, the note is shown in the first line:

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username --plugin-id 19506 --depends-on --depth 4

.. code-block:: text
   :caption: Example output.

   [19506] [Nessus Scan Information] [scan_info.nasl] depends on
   ├── [83955] [Nessus Product Information] [nessus_product_setup.nasl]
   └── [66334] [Patch Report] [patches_summary.nbin]
      └── [64294] [Patch Management Windows Auditing Conflicts] [patch_management_auditing.nasl]
         ├── [38153] [Microsoft Windows Summary of Missing Patches] [smb_missing_msft_patches.nasl]
         │   ├── [13855] [Microsoft Windows Installed Hotfixes] [smb_hotfixes.nasl] - depends on 2 more, use --depth INTEGER
         │   └── [57033] [Microsoft Patch Bulletin Feasibility Check] [ms_bulletin_checks_possible.nasl] - depends on 8 more, use --depth INTEGER
         └── [67099] [Post-Scan Rules Application] [pluginrules.nbin] 

   verified 8 plugins in 1m 24s, 10.5s per plugin

Plugin which was already shown in the tree is not expanded again, it's marked with
``dependencies listed above`` or ``listed above``.

.. note::

   Nessus API has no direct way to find plugin by its file name, so TNSCM uses plugin search from
   policy editor, which takes a few seconds per lookup. Progress is shown in terminal,
   e.g. ``looking up plugin file patches_summary.nbin > patch_management_auditing.nasl``,
   and summary at the bottom shows how many plugins were verified, how long it took
   and average time per plugin. Use :ref:`tnscm-format-option` ``json`` or ``csv`` to get flat list
   of plugins with ``relation`` and ``level`` columns instead of tree.


``tnscm policy``
================

``tnscm policy --list``
-----------------------

Get scan policy list.

.. note::

   Only policies saved in Nessus **Policies** section are listed.
   Scans created directly from templates don't create a policy.

``tnscm policy --delete``
-------------------------

Delete scan policy.

.. _tnscm-policy-download:

``tnscm policy --download``
---------------------------

.. versionadded:: v0.1.0

   Download (export) policies. :ref:`tnscm-upgrade` now!

Download (export) all policies, or policies given with ``--policy-id`` (can be repeated), as ``*.nessus`` files.

.. code-block:: shell

   tnscm policy -a 127.0.0.1 --port 8834 -u username --download --output-dir ./policies

.. code-block:: text

   saved    My policy (policy 19) - ./policies/127.0.0.1_19_My_policy_20261024-142541.nessus
   saved    Copy of My policy (policy 20) - ./policies/127.0.0.1_20_Copy_of_My_policy_20261024-143949.nessus
   saved    Copy of My policy_01 (policy 22) - ./policies/127.0.0.1_22_Copy_of_My_policy_01_20261024-152319.nessus
   downloaded 3, skipped 0, failed 0

File name contains address, policy id, name and last modification time of the policy,
so changed policy is saved to a new file and unchanged one is skipped.
Use ``--overwrite`` to download it again. Exit code is ``1`` if any download failed.

.. code-block:: shell

   tnscm policy -a 127.0.0.1 --port 8834 -u username --download --policy-id 19 --policy-id 22

.. _tnscm-policy-upload:

``tnscm policy --upload``
-------------------------

.. versionadded:: v0.1.0

   Upload (import) policies. :ref:`tnscm-upgrade` now!

Upload (import) policies from ``*.nessus`` files, e.g. downloaded with ``--download`` from another Nessus,
``--upload`` can be repeated.

.. code-block:: shell

   tnscm policy -a 127.0.0.1 --port 8834 -u username --upload ./policies/127.0.0.1_19_My_policy_20261024-142541.nessus

.. code-block:: text

   imported ./policies/127.0.0.1_19_My_policy_20261024-142541.nessus - policy 26 My policy_01
   imported 1, failed 0

If a policy with the same name exists, Nessus adds a suffix to the name, e.g. ``My policy_01``.
Settings missing in the file get default values of Nessus. Exit code is ``1`` if any upload failed.

.. _tnscm-policy-compare:

``tnscm policy --compare``
--------------------------

.. versionadded:: v0.1.0

   Compare two policies. :ref:`tnscm-upgrade` now!

Compare all settings of two policies, given by ids from ``tnscm policy --list``.
Each row shows values of both policies and result: ``same``, ``different`` or ``only in <policy id>``.
Use ``--diff`` to show only differences.

.. code-block:: shell

   tnscm policy -a 127.0.0.1 --port 8834 -u username --compare 19 22 --diff

.. code-block:: text
   :caption: Example output.

           section                                                                                            setting Policy1 (19)  Policy2 (22)      result
   1   credentials                                                                           Host > SSH > auth_method                   password  only in 22
   2   credentials                                                                Host > SSH > custom_password_prompt                             only in 22
   3   credentials                                                               Host > SSH > elevate_privileges_with                    Nothing  only in 22
   4   credentials                                                                              Host > SSH > password                   ********  only in 22
   5   credentials                                                                  Host > SSH > target_priority_list                             only in 22
   6   credentials                                                                              Host > SSH > username                          x  only in 22
   7      settings                             Discovery > Host Discovery > Ping the remote host > Ping Methods > ARP          yes            no   different
   8      settings                                                                                       Basic > Name      Policy1       Policy2   different
   9      settings                                                   Advanced > General Settings > Enable safe checks          yes            no   different
   10     settings  Discovery > Host Discovery > Ping the remote host > General Settings > Test the local Nessus host          yes            no   different

   247 settings compared: 237 same, 4 different, 6 only in one policy

When some plugins of a family are disabled in a policy, the family is ``mixed`` and its plugins are listed:

.. code-block:: text

       section                                                  setting Policy1 (19)  Policy2 (22)      result
   7   plugins              Amazon Linux Local Security Checks > status      enabled      disabled   different
   8   plugins                         Artificial Intelligence > status      enabled         mixed   different
   9   plugins  Artificial Intelligence > 196906 AI/LLM Software Report      enabled      disabled   different

What is compared:

- **settings** - shown by their location in Nessus UI, e.g.
  ``Discovery > Host Discovery > Ping the remote host > General Settings > Test the local Nessus host``.
  Settings not visible in the UI of given policy template are shown by their id.
- **plugins** - status of each plugin family. If any family is ``mixed`` (some plugins disabled),
  it's followed by status of every plugin of the family, with plugin id and name, in both policies.
- **credentials** - shown by category and type, e.g. ``Host > SSH > username``.
  Credentials of the same type are compared between policies.

.. note::

   Passwords are returned by Nessus as ``********``, so changed password can't be detected.

Show only differences in plugins:

.. code-block:: shell

   tnscm policy -a 127.0.0.1 --port 8834 -u username --compare 19 22 --diff --filter "[?section=='plugins']"


``tnscm scan``
==============

``tnscm scan --list``
---------------------

Get scan list. Use ``--folder`` to list scans of given folder only.

.. _tnscm-scan-list-folders:

``tnscm scan --list-folders``
-----------------------------

.. versionadded:: v0.1.0

Get folder list with ids and names, which you can use with ``--folder`` option.

.. code-block:: text

      id        name    type  unread_count
   1   2       Trash   trash             0
   2   3    My Scans    main             1
   3   4  New folder  custom             0

.. _tnscm-scan-list-history:

``tnscm scan --list-history``
-----------------------------

Get scan list with history, one row per scan run, with folder name, scan id (``id``), ``history_id``,
start (``creation_date``), end (``last_modification_date``) and status of the run.

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --list-history --folder "My Scans" --limit 30d

.. code-block:: text

      folder_id folder_name                    name     owner  id  history_id        creation_date last_modification_date     status
   1          3    My Scans  My Host Discovery Scan  username   6           7  2026-10-24 12:43:50    2026-10-24 12:45:22   canceled
   2          3    My Scans  My Host Discovery Scan  username   9          15  2026-10-24 13:28:06    2026-10-24 13:30:50  completed
   3          4  New folder   My Basic Network Scan  username  12          13  2026-10-24 12:46:13    2026-10-24 12:52:43  completed
   4          4  New folder   My Basic Network Scan  username  12          14  2026-10-24 12:53:18    2026-10-24 12:59:38  completed

.. versionchanged:: v0.1.0

   Folder name column and ``--folder``, ``--limit`` and ``--runs`` options.

Options:

- ``--folder`` - folder id or name, can be repeated,
- ``--limit`` - only runs started in the last given time, see :ref:`tnscm-limit-option`,
- ``--runs latest`` - only the newest run of each scan (newest completed if any),
  the same runs which ``--download --runs latest`` would download.

.. _tnscm-scan-download:

``tnscm scan --download``
-------------------------

.. versionadded:: v0.1.0

   Download scan results. :ref:`tnscm-upgrade` now!

Download scan results (history runs) as ``*.nessus`` or ``*.csv`` files.
Select runs with at least one of ``--limit`` or ``--scan-id``, so nothing is downloaded by accident.

.. important::

   Scan export are not allowed in Nessus Trial versions and Tenable Nessus Essentials.

   Read more in Nessus documentation, in section 
   `Scan Exports and Reports <https://docs.tenable.com/nessus/Content/ScanReportFormats.htm>`_ and
   `Nessus 10.11.0 <https://docs.tenable.com/release-notes/Content/nessus/2025.htm#Tenable-Nessus-10.11.0-(2025-11-20)->`_ release notes.

Download all scan runs from last 7 days in given folder to ``./reports``:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --download --limit 7d --folder "My Scans" --output-dir ./reports

Download only the newest run of each scan from last 7 days:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --download --limit 7d --runs latest

Download the newest completed run of given scan, or all its runs:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --download --scan-id 12
   tnscm scan -a 127.0.0.1 --port 8834 -u username --download --scan-id 12 --runs all

Download exact scan run:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --download --scan-id 12 --history-id 13

Options:

- ``--limit`` - runs started in the last given time, see :ref:`tnscm-limit-option`,
- ``--folder`` - folder id or name, can be repeated,
- ``--scan-id`` - scan id, can be repeated, without ``--limit`` the newest completed run is downloaded,
- ``--history-id`` - exact run of the scan given with ``--scan-id``,
- ``--runs all|latest`` - all runs of each scan or only the newest one,
- ``--output-dir`` - directory for downloaded files, created if missing (default: current directory),
- ``--file-format nessus|csv`` - format of downloaded files (default: ``nessus``),
- ``--overwrite`` - download again files which already exist,
- ``--no-progress`` - one line per run instead of progress bar.

How it works:

- only runs with status ``completed`` or ``imported`` are downloaded, others (e.g. ``running``, ``canceled``)
  are reported as skipped,
- each run is saved in a separate file named
  ``<address>_<scan id>_<history id>_<scan name>_<run start>.nessus``,
- files which already exist are skipped, so you can run the same command e.g. every day in a pipeline,
- in terminal progress bar is shown, in pipelines (or with ``--no-progress``) one line per run is printed:

.. code-block:: text

   saved    My Basic Network Scan (scan 12, history 13) - ./reports/127.0.0.1_12_13_My_Basic_Network_Scan_20261024-124613.nessus
   skipped  My Basic Network Scan (scan 12, history 15) - status is running
   skipped  My Host Discovery Scan (scan 9, history 10) - status is canceled
   downloaded 1, skipped 2, failed 0

Exit code is ``1`` if any download failed, other runs are still downloaded.

.. _tnscm-scan-compare:

``tnscm scan --compare``
------------------------

.. versionadded:: v0.1.0

   Compare findings of two scan runs. :ref:`tnscm-upgrade` now!

Compare findings per host of two scan runs, given as ``SCAN_ID:HISTORY_ID``
(see :ref:`tnscm-scan-list-history`). Runs can belong to the same or different scans,
older run is always treated as first. Each finding (host and plugin) is marked as
``new``, ``fixed``, ``severity changed`` or ``same``. Use ``--diff`` to show only changes.

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --compare 12:13 9:15 --diff

.. code-block:: text
   :caption: Example output (shortened).

   12:13 = My Basic Network Scan, started 2026-10-24 12:46:13, ended 2026-10-24 12:52:43, elapsed 0:06:30, status completed, 68 findings (critical 2, high 4, medium 1, low 0, info 61)
   9:15 = My Host Discovery Scan, started 2026-10-24 13:28:06, ended 2026-10-24 13:30:50, elapsed 0:02:44, status completed, 14 findings (critical 0, high 0, medium 0, low 0, info 14)

               host  plugin_id                                                     plugin_name     12:13  9:15  result
   1    192.168.1.1      10180                                            Ping the remote host            info     new
   2    192.168.1.1      19506                                         Nessus Scan Information            info     new
   9    192.168.1.5     322791    Ubuntu 20.04 LTS / ... : FFmpeg vulnerabilities (USN-8469-1)  critical           fixed

   81 findings compared: 1 same, 13 new, 67 fixed, 0 severity changed

Each run is summarized with start and end time, elapsed time, status and number of plugins per severity.
Findings are listed per host, most severe first.

Show only new critical and high findings:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --compare 12:13 12:14 --diff \
     --filter "[?result=='new' && contains(['critical', 'high'], \"12:14\")]"

Show only selected plugin:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --compare 12:13 9:15 -f '[?plugin_id==`19506`]'

.. note::

   Findings are compared per host and plugin, not per port.

.. versionremoved:: v0.1.0

   ``tnscm scan --delete``, deleting scans via API is not available in Nessus Professional.

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

.. _tnscm-server-health:

``tnscm server --health``
-------------------------

.. versionadded:: v0.1.0

Get scanner health alerts and statistics. Exit code is ``1`` when any alert is critical.

.. code-block:: shell

   tnscm server -a 127.0.0.1 --port 8834 -u username --health

.. code-block:: text
   :caption: Example output (shortened).

   Alerts:
     severity                                 alert                                                                                                       description
   1  warning                       Slow DNS Lookup                                                                             1120 (511%) slow DNS Lookups detected
   5  warning  Minimum memory requirements not met.  Your system does not meet the minimum recommended amount of RAM. Amount recommended: 4 GB. Your system has: 3 GB

   Statistics:
                       attribute              value
   1                  Nessus CPU                1 %
   4               Nessus memory              56 MB
   5                  System RAM            3377 MB
   6              Data disk free  22599 of 49027 MB

.. _tnscm-server-license:

``tnscm server --license``
--------------------------

.. versionadded:: v0.1.0

Get licence and plugin feed status. Exit code is ``1`` when any check has ``warning`` status.

- ``--warn-days N`` - warning when licence expires in N days or less,
- ``--feed-max-age DURATION`` - warning when plugin set is older than given time, e.g. ``2d``, ``12h``.

.. code-block:: shell

   tnscm server -a 127.0.0.1 --port 8834 -u username --license --warn-days 30 --feed-max-age 2d

.. code-block:: text

                       check                                            value   status
   1                    type                              Nessus Professional       ok
   2                 version                                          19.18.6       ok
   3              evaluation                                              yes       ok
   4                     IPs                                     2 used of 32       ok
   5      licence expiration                2026-10-31 11:18:27 (3 days left)  warning
   6              plugin set  202610231756 (2026-10-23 17:56 UTC, 4d 10h old)  warning
   7       loaded plugin set                               same as downloaded       ok
   8             plugin feed            Request to plugins.nessus.org failed.  warning
   9          restart needed                                               no       ok
   10  new version available                                               no       ok

Use it in a monitoring job:

.. code-block:: shell

   tnscm server -a 127.0.0.1 --port 8834 -u username -p "$NESSUS_PASSWORD" --no-keyring \
     --license --warn-days 30 --feed-max-age 2d --hide-banner || echo "check Nessus!"

.. note::

   Only selected licence details are shown, activation code and other secrets are never printed.

.. _tnscm-settings:

``tnscm settings``
==================

``tnscm settings --list``
-------------------------

Get settings list.

.. _tnscm-settings-get:

``tnscm settings --get``
------------------------

.. versionchanged:: v0.1.0

   Get advanced settings. :ref:`tnscm-upgrade` now!

Get value of selected setting, can be repeated.

.. code-block:: shell

   tnscm settings -a 127.0.0.1 --port 8834 -u username --get max_hosts --get max_checks

.. code-block:: text
   :caption: Example output.

            name value
   1   max_hosts   256
   2  max_checks     5


Print value only, e.g. to use it in script:

.. code-block:: shell

   tnscm settings -a 127.0.0.1 --port 8834 -u username --get max_hosts -f "[0].value" --format json --hide-banner --hide-address
   256

.. _tnscm-settings-edit:

``tnscm settings --edit``
-------------------------

.. versionchanged:: v0.1.0

   Edit advanced settings. :ref:`tnscm-upgrade` now!

Change value of existing setting, given as ``NAME=VALUE``, can be repeated.
Planned changes are shown and confirmed before applying, use ``--yes`` to skip confirmation, e.g. in pipelines.

.. code-block:: shell

   tnscm settings -a 127.0.0.1 --port 8834 -u username --edit max_hosts=128 --edit max_checks=4

.. code-block:: text

     action        name current_value new_value
   1   edit   max_hosts           256       128
   2   edit  max_checks             5         4

   Do you want to apply 2 change(s) listed above? [y/N]: y
   Applied 2 change(s). Current values:
            name value
   1   max_hosts   128
   2  max_checks     4

.. _tnscm-settings-add:

``tnscm settings --add``
------------------------

.. versionchanged:: v0.1.0

   Add advanced settings. :ref:`tnscm-upgrade` now!

Add new custom setting, given as ``NAME=VALUE``, can be repeated.

.. code-block:: shell

   tnscm settings -a 127.0.0.1 --port 8834 -u username --add my_custom_setting=value

.. _tnscm-settings-delete:

``tnscm settings --delete``
---------------------------

.. versionchanged:: v0.1.0

   Delete advanced settings. :ref:`tnscm-upgrade` now!

Delete custom setting, or reset built-in setting to its default value, can be repeated.

.. code-block:: shell

   tnscm settings -a 127.0.0.1 --port 8834 -u username --delete my_custom_setting

.. note::

   Nessus hides a built-in setting reset to default from the list, so it can't be changed with ``--edit`` anymore.
   Use ``--add`` to set it again, e.g. ``--add max_hosts=256``.

``tnscm user``
==============

``tnscm user --list``
---------------------

Get user list

.. _tnscm-global-options:

global options
==============

Options available for every command.

``--address``
-------------

``-a, --address TEXT``

address to which you want to login  [default: (127.0.0.1)]

Can be repeated to run the same command on many Nessus servers.

``--port``
----------

``--port TEXT``

port to which you want to login  [default: (443)]

``--username``
--------------

``-u, --username TEXT``

username which you want to use to login  [default: (current user)]

``--password``
--------------

``-p, --password TEXT``

password which you want to use to login

If not given, password is taken from macOS Keychain / Windows Credential Manager,
or you are asked for it and it's saved there.

.. _tnscm-no-keyring-option:

``--no-keyring``
----------------

.. versionadded:: v0.1.0

``--no-keyring``

don't read or save password in OS credential manager (keyring), e.g. in pipelines, use with ``--password``

Pipeline agents usually don't have OS credential manager. Use ``--no-keyring`` with ``--password``,
so keyring is not used at all and you don't need to set ``PYTHON_KEYRING_BACKEND`` variable:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username -p "$NESSUS_PASSWORD" --no-keyring --download --limit 1d --hide-banner

Without ``--password``, ``--no-keyring`` asks for password in terminal, and in pipeline ends with error
``--no-keyring needs --password when not run in a terminal``.

``--insecure``
--------------

``-k, --insecure``

perform insecure SSL connections and transfers

.. _tnscm-ca-cert-option:

``--ca-cert``
-------------

.. versionadded:: v0.1.0

``--ca-cert FILE``

CA certificate (PEM) to verify the Nessus server certificate, e.g. a custom or Nessus CA.

Nessus uses its own certificate authority (CA), which is not trusted by default, so connection fails with
``SSL certificate of <address> can't be verified``. Trust the Nessus CA with ``--ca-cert``
(certificate has to be valid for the address you connect to), or skip verification with ``-k``.

.. code-block:: shell

   curl -sk https://127.0.0.1:8834/getcert -o nessus-ca.pem
   tnscm server -a 127.0.0.1 --port 8834 -u username --status --ca-cert nessus-ca.pem

.. _tnscm-format-option:

``--format``
------------

.. versionchanged:: v0.1.0

   ``-f`` is no longer a short version of ``--format``, it's used for ``--filter``.

``--format TEXT``

data format to display [table,json,csv]  [default: (table)]

.. _tnscm-filter-option:

``--filter``
------------

``-f, --filter TEXT``

filter data with JMESPath. See https://jmespath.org/ for more information and examples.

Examples:

.. code-block:: shell

   # only name and id columns
   --filter "[].{id: id, name: name}"

   # items which name contains "exampl"
   --filter "[? contains(name, 'exampl')].{id: id, name: name}"

   # item with id equal to number 10
   --filter '[?id==`10`]'

.. tip::

   Put text values in single quotes and numbers in backticks.
   In zsh / bash, wrap the whole filter in single quotes when it contains backticks.

Wrong filter is reported before connecting to Nessus:

.. code-block:: text

   Error: Invalid value for '--filter' / '-f': invalid token: Parse error at column 18, token "192" (NUMBER), for expression:
   "[? contains(host, 192.168.1.107)]"
                      ^
   Put text values in single quotes and numbers in backticks, e.g. "[?host=='192.168.1.107']" or '[?plugin_id==`19506`]'. See https://jmespath.org/ for more examples.

.. _tnscm-filter-options-option:

``--filter-options``
--------------------

.. versionadded:: v0.1.0

``--filter-options``

Show all fields of first item which can be used with ``--filter`` (runs ``-f "[0]" --format json``).

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --list-folders --filter-options
   {'unread_count': 0, 'custom': 0, 'default_tag': 0, 'type': 'trash', 'name': 'Trash', 'id': 2}

.. _tnscm-limit-option:

``--limit``
-----------

.. versionadded:: v0.1.0

``--limit DURATION``

Available for ``tnscm scan --list-history`` and ``tnscm scan --download``.
Limit to runs started in the last given time: number with unit
``d`` (days), ``h`` (hours), ``m`` (minutes) or ``s`` (seconds). Units can be combined.

.. code-block:: shell

   --limit 7d       # last 7 days
   --limit 12h      # last 12 hours
   --limit 30m      # last 30 minutes
   --limit 1d6h     # last 30 hours

.. _tnscm-hide-banner:

``--hide-banner``
-----------------

.. versionadded:: v0.1.0

``--hide-banner``

Hide tool name and version printed before results, e.g. to get clean
``csv`` / ``json`` output in pipelines.

.. _tnscm-hide-address:

``--hide-address``
------------------

.. versionadded:: v0.1.0

``--hide-address``

Hide the Nessus address printed before results, e.g. to get clean
``csv`` / ``json`` output in pipelines.

``--verbose``
-------------

``-v, --verbose``

Get more verbose output.
