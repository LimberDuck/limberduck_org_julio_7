:blogpost: true

TNSCM v0.1.0: Download and compare scans and policies!
======================================================

.. post:: 2026-10-31 09:45:00
   :tags: TNSCM
   :category: Tools, News
   :author: Damian

The latest release of LimberDuck **TNSCM** ``v0.1.0`` brings the biggest update so far. Now you can download
scan results, compare findings of two scan runs, back up and compare policies, monitor scanner health
and license, check plugin details and manage advanced settings - all from command line,
also in CI/CD pipeline or scheduled job.

.. admonition:: What's new?
   :class: hint

   - ``tnscm scan --download`` - download scan results from given time, folder or exact scan run,
   - ``tnscm scan --compare`` - see ``new``, ``fixed`` and changed findings per host between two scan runs,
   - ``tnscm policy --compare`` - compare all settings, plugins and credentials of two policies,
   - ``tnscm policy --download`` and ``--upload`` - export and import policies,
   - ``tnscm server --health`` and ``--license`` - scanner health alerts, license expiration and plugin feed status,
   - ``tnscm plugin --plugin-id`` and ``--plugin-file`` - plugin details by id or file name with link to its description on tenable.com,
   - ``tnscm plugin --depends-on`` and ``--required-by`` - tree of plugins on which given plugin depends and plugins which depend on it,
   - ``tnscm settings`` - get, edit, add and delete advanced settings,
   - ``--ca-cert`` to verify Nessus certificate, ``--no-keyring`` for pipelines, ``--filter-options``,
     ``--hide-banner`` and ``--hide-address`` for every command,
   - clear error messages and exit codes instead of tracebacks.

Download scan results
---------------------

Download all scan runs from last 7 days in given folder:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --download --limit 7d --folder "My Scans" --output-dir ./reports

Use ``--limit`` with ``d`` (days), ``h`` (hours), ``m`` (minutes) or ``s`` (seconds) units, e.g. ``12h`` or ``1d6h``. 
Each run is saved in a separate file, files already downloaded are skipped, so you can run the same command every day.

Check what will be downloaded before with ``--list-history``:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username --list-history --limit 7d --runs latest

Compare two scan runs
---------------------

What changed since the last scan? Give two runs as ``SCAN_ID:HISTORY_ID`` and see only changes:

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

Runs can belong to the same or different scans, each finding is marked as ``new``, ``fixed``,
``severity changed`` or ``same``.

Compare two policies
--------------------

Find out why two scans give different results:

.. code-block:: shell

   tnscm policy -a 127.0.0.1 --port 8834 -u username --compare 19 22 --diff

.. code-block:: text
   :caption: Example output (shortened).

           section                                                                   setting Policy1 (19) Policy2 (22)      result
   6   credentials                                                     Host > SSH > username                         x  only in 22
   7      settings    Discovery > Host Discovery > Ping the remote host > Ping Methods > ARP          yes           no   different
   9      settings                          Advanced > General Settings > Enable safe checks          yes           no   different

Settings are shown by their location in Nessus UI, credentials by their type, and when some plugins of
a family are disabled, every plugin of the family is listed.

Back up and restore policies
----------------------------

Download all policies as ``.nessus`` files, e.g. every day to keep their history, and upload them
to the same or another Nessus:

.. code-block:: shell

   tnscm policy -a 127.0.0.1 --port 8834 -u username --download --output-dir ./policies
   tnscm policy -a 127.0.0.2 --port 8834 -u username --upload ./policies/127.0.0.1_19_My_policy_20261024-142541.nessus

File name contains last modification time of the policy, so only changed policies are downloaded again.

Monitor your scanner
--------------------

Check scanner health alerts and statistics, license expiration and plugin feed:

.. code-block:: shell

   tnscm server -a 127.0.0.1 --port 8834 -u username --license --warn-days 30 --feed-max-age 2d

.. code-block:: text

                       check                                            value   status
   5      license expiration                2026-10-31 11:18:27 (3 days left)  warning
   6              plugin set  202610231756 (2026-10-23 17:56 UTC, 4d 10h old)  warning
   8             plugin feed            Request to plugins.nessus.org failed.  warning

Any ``warning`` gives exit code ``1``, so it's ready for a monitoring job.
``tnscm server --health`` shows alerts like slow DNS lookups or not enough memory, and CPU, memory and disk usage.

Run in pipelines
----------------

Pipeline agents usually don't have OS credential manager. Use ``--no-keyring`` with ``--password``
and ``--hide-banner`` to get clean output:

.. code-block:: shell

   tnscm scan -a 127.0.0.1 --port 8834 -u username -p "$NESSUS_PASSWORD" --no-keyring \
     --download --limit 1d --output-dir ./reports --hide-banner

Advanced settings
-----------------

Change advanced settings with confirmation, or without it in pipelines with ``--yes``:

.. code-block:: shell

   tnscm settings -a 127.0.0.1 --port 8834 -u username --edit max_hosts=128 --edit max_checks=4

Plugin details
--------------

Get plugin details with link to its description on tenable.com:

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username --plugin-id 19506

Plugin ``dependency`` attribute lists file names - paste them as they are to get these plugins too:

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username --plugin-file "nessus_product_setup.nasl, patches_summary.nbin"

See which plugins depend on given plugin - or on which plugins it depends with ``--depends-on``.
Only direct ones are shown by default, increase ``--depth`` to see more levels:

.. code-block:: shell

   tnscm plugin -a 127.0.0.1 --port 8834 -u username --plugin-id 57399 --required-by

.. code-block:: text

   [57399] [VMware vSphere Installed Patches] [vmware_installed_patches.nbin] is required by
   └── [97993] [OS Identification and Installed Software Enumeration over SSH v2 (Using New SSH Library)] [ssh_get_info2.nasl] - required by 96541 more, increase --depth INTEGER

.. important::

   **TNSCM** v0.1.0 requires Python 3.11 or newer.
   ``tnscm scan --delete`` was removed, as deleting scans via API is not available in Nessus Professional.

.. seealso::

   For detailed usage guides, check out:
      - :ref:`tnscm-plugin-details`
      - :ref:`tnscm-plugin-file`
      - :ref:`tnscm-plugin-dependencies`
      - :ref:`tnscm-policy-download`
      - :ref:`tnscm-policy-upload`
      - :ref:`tnscm-policy-compare`
      - :ref:`tnscm-scan-list-folders`
      - :ref:`tnscm-scan-list-history`
      - :ref:`tnscm-scan-download`
      - :ref:`tnscm-scan-compare`
      - :ref:`tnscm-server-health`
      - :ref:`tnscm-server-license`
      - :ref:`tnscm-settings-get`
      - :ref:`tnscm-settings-edit`
      - :ref:`tnscm-settings-add`
      - :ref:`tnscm-settings-delete`
      - :ref:`tnscm-no-keyring-option`
      - :ref:`tnscm-ca-cert-option`
      - :ref:`tnscm-filter-options-option`
      - :ref:`tnscm-limit-option`
      - :ref:`tnscm-limit-option`
      - :ref:`tnscm-hide-banner`
      - :ref:`tnscm-hide-address`

.. hint::
   You can download the latest version of **TNSCM** from |PyPI| using ``pip``.
   Read more on :ref:`tnscm-upgrade` page.
