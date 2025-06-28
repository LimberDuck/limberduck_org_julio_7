:description: Programming instruction for nessus file reader (nfr).

Programming
===========

If command-line tool interface is not enough for you or you want to build 
your own solution you can use **nessus file reader (NFR)** as a python module:

Import `nessus-file-reader` module.
   
.. code-block:: python
   
   import nessus_file_reader as nfr

File functions
--------------

Use `file` functions to get details about provided file, e.g., root, file name, file size.
   
.. code-block:: python
   :linenos:
   :emphasize-lines: 5,7,8

   import nessus_file_reader as nfr

   nessus_scan_file = './your_nessus_file.nessus'

   root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

   file_name = nfr.file.nessus_scan_file_name_with_path(nessus_scan_file)
   file_size = nfr.file.nessus_scan_file_size_human(nessus_scan_file)

   print(f'File name: {file_name}')
   print(f'File size: {file_size}')

Scan functions
--------------

Use `scan` functions to get details about provided scan, e.g., report name, number of target/scanned/credentialed hosts, scan time start/end/elapsed and more.

.. code-block:: python
   :linenos:
   :emphasize-lines: 7-13

   import nessus_file_reader as nfr

   nessus_scan_file = './your_nessus_file.nessus'

   root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

   report_name = nfr.scan.report_name(root)
   number_of_target_hosts = nfr.scan.number_of_target_hosts(root)
   number_of_scanned_hosts = nfr.scan.number_of_scanned_hosts(root)
   number_of_scanned_hosts_with_credentialed_checks_yes = nfr.scan.number_of_scanned_hosts_with_credentialed_checks_yes(root)
   scan_time_start = nfr.scan.scan_time_start(root)
   scan_time_end = nfr.scan.scan_time_end(root)
   scan_time_elapsed = nfr.scan.scan_time_elapsed(root)

   print(f' Report name: {report_name}')
   print(f' Number of target/scanned/credentialed hosts: {number_of_target_hosts}/{number_of_scanned_hosts}/{number_of_scanned_hosts_with_credentialed_checks_yes}')
   print(f' Scan time START - END (ELAPSED): {scan_time_start} - {scan_time_end} ({scan_time_elapsed})')

Host functions
--------------

Use `host` functions to get details about hosts from provided scan, e.g., report hosts names, operating system, hosts scan time start/end/elapsed, number of Critical/High/Medium/Low/None findings and more.

.. code-block:: python
   :linenos:
   :emphasize-lines: 8-17

   import nessus_file_reader as nfr

   nessus_scan_file = './your_nessus_file.nessus'

   root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

   for report_host in nfr.scan.report_hosts(root):
      report_host_name = nfr.host.report_host_name(report_host)
      report_host_os = nfr.host.detected_os(report_host)
      report_host_scan_time_start = nfr.host.host_time_start(report_host)
      report_host_scan_time_end = nfr.host.host_time_end(report_host)
      report_host_scan_time_elapsed = nfr.host.host_time_elapsed(report_host)
      report_host_critical = nfr.host.number_of_plugins_per_risk_factor(report_host, 'Critical')
      report_host_high = nfr.host.number_of_plugins_per_risk_factor(report_host, 'High')
      report_host_medium = nfr.host.number_of_plugins_per_risk_factor(report_host, 'Medium')
      report_host_low = nfr.host.number_of_plugins_per_risk_factor(report_host, 'Low')
      report_host_none = nfr.host.number_of_plugins_per_risk_factor(report_host, 'None')

      print(f'  Report host name: {report_host_name}')
      print(f'  Report host OS: {report_host_os}')
      print(f'  Host scan time START - END (ELAPSED): {report_host_scan_time_start} - {report_host_scan_time_end} ({report_host_scan_time_elapsed})')
      print(f'  Critical/High/Medium/Low/None findings: {report_host_critical}/{report_host_high}/{report_host_medium}/{report_host_low}/{report_host_none}')

Plugin functions
----------------

Use `plugin` functions to get details about plugins reported in provided scan, e.g., plugins ID, plugins risk factor, plugins name.

.. code-block:: python
   :linenos:
   :emphasize-lines: 10-12

   import nessus_file_reader as nfr

   nessus_scan_file = './your_nessus_file.nessus'

   root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

   for report_host in nfr.scan.report_hosts(root):
      report_items_per_host = nfr.host.report_items(report_host)
      for report_item in report_items_per_host:
         plugin_id = int(nfr.plugin.report_item_value(report_item, 'pluginID'))
         risk_factor = nfr.plugin.report_item_value(report_item, 'risk_factor')
         plugin_name = nfr.plugin.report_item_value(report_item, 'pluginName')

         print('\t', plugin_id, '  \t\t\t', risk_factor, '  \t\t\t', plugin_name)


If you want to get output for interesting you plugin, e.g., "Nessus Scan Information" use below function

.. code-block:: python
   :linenos:
   :emphasize-lines: 8

   import nessus_file_reader as nfr

   nessus_scan_file = './your_nessus_file.nessus'

   root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

   for report_host in nfr.scan.report_hosts(root):
      pido_19506 = nfr.plugin.plugin_output(root, report_host, '19506')

      print(f'Nessus Scan Information Plugin Output:\n{pido_19506}')


If you know that interesting you plugin occurs more than ones for particular host, e.g., "Netstat Portscanner (SSH)" use below function

.. code-block:: python
   :linenos:
   :emphasize-lines: 8

   import nessus_file_reader as nfr

   nessus_scan_file = './your_nessus_file.nessus'

   root = nfr.file.nessus_scan_file_root_element(nessus_scan_file)

   for report_host in nfr.scan.report_hosts(root):
      pidos_14272 = nfr.plugin.plugin_outputs(root, report_host, '14272')

      print(f'All findings for Netstat Portscanner (SSH): \n{pidos_14272}')
