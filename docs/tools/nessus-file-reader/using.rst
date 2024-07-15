:description: Using instruction for nessus file reader (nfr).

Using
=====

Check help for **nessus file reader** (``nfr``) commands using ``nfr [command] --help``.

File command
------------

Run ``nfr file --help`` to see options related to nessus file.

File size
.........

Check size of given file:

.. code-block:: shell

   nfr file --size test_files/scan_avrx9t.nessus
   nessus file reader by LimberDuck 0.4.2
   test_files/scan_avrx9t.nessus 2.4 MiB


Check size of more than one file:

.. code-block:: shell

   nfr file --size test_files/scan_avrx9t.nessus test_files/scan_ihc1js.nessus
   nessus file reader by LimberDuck 0.4.2
   test_files/scan_avrx9t.nessus 2.4 MiB
   test_files/scan_ihc1js.nessus 5.0 MiB


Check size of all files in given directory and it's subdirectories:

.. code-block:: shell

   nfr file --size test_files  
   nessus file reader by LimberDuck 0.4.2                                                      
   test_files/scan_avrx9t.nessus 2.4 MiB
   test_files/scan_ihc1js.nessus 5.0 MiB
   test_files/test_subdirectory/scan_ihc1js.nessus 878.3 KiB


File structure
..............

Check structure of given file:

.. code-block:: shell

   nfr file --structure test_files/scan_avrx9t.nessus
   nessus file reader by LimberDuck 0.4.2
   test_files/scan_avrx9t.nessus
   Policy [2/2]
   ├── policyName [3/3]
   ├── Preferences [2/3]
   │   ├── ServerPreferences [1/1]
   │   │   ├── preference [54/54]
   │   │   │   ├── name [1/1]
   │   │   │   └── value [0/1]
   │   │   ├── preference [53/54]
   ...
   │   └── PluginsPreferences [0/1]
   │       ├── item [506/506]
   │       │   ├── pluginName [6/6]
   │       │   ├── pluginId [5/6]
   │       │   ├── fullName [4/6]
   │       │   ├── preferenceName [3/6]
   │       │   ├── preferenceType [2/6]
   │       │   ├── preferenceValues [1/6]
   │       │   └── selectedValue [0/6]
   │       ├── item [505/506]
   ...
   ├── FamilySelection [1/3]
   │   ├── FamilyItem [53/53]
   │   │   ├── FamilyName [1/1]
   │   │   └── Status [0/1]
   │   ├── FamilyItem [52/53]
   │   │   ├── FamilyName [1/1]
   │   │   └── Status [0/1]
   ...
   └── IndividualPluginSelection [0/3]
   │   ├── PluginItem [6/6]
   │   │   ├── PluginId [3/3]
   │   │   ├── PluginName [2/3]
   │   │   ├── Family [1/3]
   │   │   └── Status [0/3]
   ...
   Report [1/2]
   └── ReportHost [0/0]
      ├── HostProperties [409/409]
      │   ├── tag [354/354]
      │   ├── tag [353/354]
   ...
      ├── ReportItem [408/409]
      │   ├── agent [12/12]
      │   ├── description [11/12]
      │   ├── fname [10/12]
      │   ├── plugin_modification_date [9/12]
      │   ├── plugin_name [8/12]
      │   ├── plugin_publication_date [7/12]
      │   ├── plugin_type [6/12]
      │   ├── risk_factor [5/12]
      │   ├── script_version [4/12]
      │   ├── see_also [3/12]
      │   ├── solution [2/12]
      │   ├── synopsis [1/12]
      │   └── plugin_output [0/12]
   ...


.. seealso::

   Check whole example structure `scan_avrx9t_structure.txt <https://github.com/LimberDuck/nessus-file-reader/blob/master/examples/scan_avrx9t_structure.txt>`_.

Scan command
------------

Run ``nfr scan --help`` to see options related to content of nessus file on scan level.

Scan summary
............

See scan summary of given file/-s or all files in given directory and it's subdirectories:

.. code-block:: shell

   nfr scan --scan-summary scan_avrx9t.nessus
   nessus file reader by LimberDuck 0.4.2
   File name           Report name     TH    SH    CC    C    H    M    L    N
   ------------------  ------------  ----  ----  ----  ---  ---  ---  ---  ---
   scan_avrx9t.nessus  test scan        1     1     1   48  182  126   15   38


.. code-block:: shell

   nfr scan --scan-summary-legend                              
   nessus file reader by LimberDuck 0.4.2
   Legend for scan summary:
   File name - nessus file name
   Report name - report name for given nessus file name
   TH - number of target hosts
   SH - number of scanned hosts
   CC - number of hosts scanned with credentials (Credentialed checks yes in Plugin ID 19506)
   C - number of plugins with Critical risk factor for whole scan
   H - number of plugins with High risk factor for whole scan
   M - number of plugins with Medium risk factor for whole scan
   L - number of plugins with Low risk factor for whole scan
   N - number of plugins with None risk factor for whole scan


Policy scan summary
...................

See policy scan summary of given file/-s or all files in given directory and it's subdirectories:

.. code-block:: shell

   nfr scan --policy-summary scan_ihc1js.nessus scan_avrx9t.nessus
   nessus file reader by LimberDuck 0.4.2
   File name           Policy name      Max hosts    Max checks    Checks timeout    Plugins number
   ------------------  -------------  -----------  ------------  ----------------  ----------------
   scan_ihc1js.nessus  Advanced Scan          100             5                 5            103203
   scan_avrx9t.nessus  Test                   100             5                 5            103949



Scan file source
................

See scan file source like Nessus, Tenable.sc, Tenable.io of given file/-s or all files in given directory and it's subdirectories:

.. code-block:: shell

   nfr scan --scan-file-source scan_ihc1js.nessus scan_avrx9t.nessus
   nessus file reader by LimberDuck 0.4.2
   File name           Source
   ------------------  ----------
   scan_ihc1js.nessus  Tenable.sc
   scan_avrx9t.nessus  Nessus
