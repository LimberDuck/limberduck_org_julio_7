#######################
Vulnerabilities section
#######################

Here you will find all details about data visible in target file in *Vulnerabilities* section.

.. list-table:: Column details explanation
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Column name in the target |xlsx| file.

    * - Description
      - Short description of particular data.

    * - Source
      - Information about the exact source from where |NFA| takes data.

    * - Post-processing
      - Information on how the gathered data is processed, if it's processed at all.

    * - Column type
      - 
        ``default`` - column always appears in the report.
            
        ``debug`` - column appears in the report only if the ``add debug data`` option has been enabled.

.. note::
    Some of the columns are visible only if you use ``add debug data`` option for analysis (see :doc:`../settings` to adhere more information about this option). 
    For all of these columns you will find below information **Column type** : ``debug``.


*****************
Nessus scanner IP
*****************

.. list-table:: Nessus scanner IP - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Nessus scanner IP

    * - Description
      - Scanner IP used during scan of reported host based on Plugin ID 19506 output.

    * - Source
      - nessus file > ``ReportHost/ReportItem/[pluginID="19506"]/plugin_output``

    * - Post-processing
      - 
        1. If Plugin ID 19506 output exist extract Scanner IP from output line with ``Scanner IP :``
        2. If Plugin ID 19506 output does not exist return:
            - ``No output recorded.`` - if plugin appeared in the report but does not return any output,
            - ``Check Audit Trail.`` - if plugin does not appeared in the report but used during scan,
            - ``{plugin_id} not enabled.`` - if plugin has not been enabled in policy used during scan.

    * - Column type
      - ``debug``

.. seealso::
    Read more about plugin which source for this column on Tenable website https://www.tenable.com/plugins/nessus/19506

****************
Nessus scan name
****************

.. list-table:: Nessus scan name - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Nessus scan name

    * - Description
      - Scan name given by user during scan setting up.

    * - Source
      - nessus file > ``Report/name``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

****************
Nessus file name
****************

.. list-table:: Nessus file name - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Nessus file name

    * - Description
      - Nessus file name assigned during the file downloading.

    * - Source
      - nessus file

    * - Post-processing
      - Absolute path of the given file.

    * - Column type
      - ``debug``

******
Target
******

.. list-table:: Target - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Target

    * - Description
      - Name of reported host. This can be either |IP| or |FQDN|, depending on this what has been given as target.

    * - Source
      - nessus file > ``ReportHost/[@name='name']``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

********
Hostname
********

.. list-table:: Hostname - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Hostname

    * - Description
      - Hostname of reported host.

    * - Source
      - nessus file > ``ReportHost/HostProperties/tag/[@name='hostname']``

    * - Post-processing
      - 
        1. Value changed to lowercase.
        2. If hostname field contains |FQDN| only hostname will be returned.

    * - Column type
      - ``debug``, ``default``

****
FQDN
****

.. list-table:: FQDN - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - FQDN

    * - Description
      - |FQDN| of reported host.

    * - Source
      - nessus file > ``ReportHost/HostProperties/tag/[@name='host-fqdn']``

    * - Post-processing
      - Value changed to lowercase.

    * - Column type
      - ``debug``, ``default``

**
IP
**

.. list-table:: IP - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - IP

    * - Description
      - |IP| of reported host.

    * - Source
      - nessus file > ``ReportHost/HostProperties/tag/[@name='host-ip']``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

*******
Scanned
*******

.. list-table:: Scanned - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Scanned

    * - Description
      - Information if target host has been scanned.
        
        - ``yes`` if target host is on the list of reported hosts.
        
        - ``no`` if target host is not on the list of reported hosts.

    * - Source
      - 
        nessus file > ``Preferences/ServerPreferences/preference/[name='TARGET']/value``

        nessus file > ``ReportHost/[@name='name']``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

*******************
Credentialed checks
*******************

.. list-table:: Credentialed checks - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Credentialed checks

    * - Description
      - Information if reported host has been scanned with credentialed checks.
        
    * - Source
      - nessus file > ``ReportHost/ReportItem/[pluginID="19506"]/plugin_output``

    * - Post-processing
      -
            1. If Plugin ID 19506 output exist extract ``yes`` or ``no`` from output line with ``Credentialed checks :``.
      
            2. If Plugin ID 19506 output does not exist return ``no``.

    * - Column type
      - ``debug``, ``default``

.. seealso::
    Read more about this plugin on Tenable website https://www.tenable.com/plugins/nessus/19506

***********
Policy name
***********

.. list-table:: Policy name - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Policy name

    * - Description
      - Policy name selected by user during scan setting up.

    * - Source
      - nessus file > ``Policy/policyName``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

********
Protocol
********

.. list-table:: Protocol - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Protocol

    * - Description
      - Exact protocol type returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/[@protocol]``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

************
Service Name
************

.. list-table:: Service Name - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Service Name

    * - Description
      - Exact service name returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/[@svc_name]``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

****
Port
****

.. list-table:: Port - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Port

    * - Description
      - Exact port returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/[@port]``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

*********
Plugin ID
*********

.. list-table:: Plugin ID - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin ID

    * - Description
      - Exact Plugin ID returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/[@pluginID]``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

***********
Plugin name
***********

.. list-table:: Plugin name - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin name

    * - Description
      - Exact Plugin Name returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/[@pluginName]``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

***********
Plugin type
***********

.. list-table:: Plugin type - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin type

    * - Description
      - Exact Plugin type returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/plugin_type``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

***************
Severity Number
***************

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!


.. list-table:: Severity Number - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Severity Number

    * - Description
      - Exact Plugin Severity Number returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/severity``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

********
Severity
********

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: Severity - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Severity

    * - Description
      - Exact Plugin Severity returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/severity``

    * - Post-processing
      - Severity is returned in human readable format, e.g. 
        ``Critical``, ``High``, ``Medium``, ``Low``, ``Info`` 
        using **nessus file reader (NFR)**'s function 
        ``severity_number_to_label(severity_number)``

    * - Column type
      - ``debug``, ``default``

***********
Risk Factor
***********

.. list-table:: Risk Factor - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Risk Factor

    * - Description
      - Exact Plugin Risk Factor returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/risk_factor``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

*****************
CVSSv2 Base Score
*****************

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: CVSSv2 Base Score - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVSSv2 Base Score

    * - Description
      - Exact Plugin |CVSSv2| base score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cvss2_base_score``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

******
CVSSv2
******

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: CVSSv2 - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVSSv2

    * - Description
      - Exact Plugin CVSSv2 label based on |CVSSv2| base score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cvss2_base_score``

    * - Post-processing
      - Severity is returned in human readable format, e.g. 
        ``Critical``, ``High``, ``Medium``, ``Low``, ``None`` 
        using **nessus file reader (NFR)**'s function 
        ``cvssv2_score_to_severity(cvss_score)``

    * - Column type
      - ``debug``, ``default``

*****************
CVSSv3 Base Score
*****************

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: CVSSv3 Base Score - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVSSv3 Base Score

    * - Description
      - Exact Plugin |CVSSv3| base score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cvss3_base_score``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

******
CVSSv3
******

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: CVSSv3 - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVSSv3

    * - Description
      - Exact Plugin CVSSv3 label based on |CVSSv3| base score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cvss3_base_score``

    * - Post-processing
      - Severity is returned in human readable format, e.g. 
        ``Critical``, ``High``, ``Medium``, ``Low``, ``None`` 
        using **nessus file reader (NFR)**'s function 
        ``cvssv3_score_to_severity(cvss_score)``

    * - Column type
      - ``debug``, ``default``

*****************
CVSSv4 Base Score
*****************

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: CVSSv4 Base Score - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVSSv4 Base Score

    * - Description
      - Exact Plugin |CVSSv4| base score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cvss4_base_score``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

******
CVSSv4
******

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: CVSSv4 - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVSSv4

    * - Description
      - Exact Plugin CVSSv4 label based on |CVSSv4| base score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cvss4_base_score``

    * - Post-processing
      - Severity is returned in human readable format, e.g. 
        ``Critical``, ``High``, ``Medium``, ``Low``, ``None`` 
        using **nessus file reader (NFR)**'s function 
        ``cvssv4_score_to_severity(cvss_score)``

    * - Column type
      - ``debug``, ``default``

*********
VPR Score
*********

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: VPR Score - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - VPR Score

    * - Description
      - Exact Plugin |VPR| score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/vpr_score``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

***
VPR
***

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: VPR - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - VPR

    * - Description
      - Exact Plugin |VPR| label based on |VPR| score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/vpr_score``

    * - Post-processing
      - Severity is returned in human readable format, e.g. 
        ``Critical``, ``High``, ``Medium``, ``Low``, ``None`` 
        using **nessus file reader (NFR)**'s function 
        ``vpr_score_to_severity(vpr_score)``

    * - Column type
      - ``debug``, ``default``

****
EPSS
****

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: EPSS - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - EPSS

    * - Description
      - Exact Plugin |EPSS| score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/epss_score``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

******
EPSS %
******

.. versionadded:: v0.8.0

   :ref:`nfr-upgrade` now!

.. list-table:: EPSS % - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - EPSS %

    * - Description
      - Exact Plugin |EPSS| percentage based on |EPSS| score returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/epss_score``

    * - Post-processing
      - Score saved with ``%`` format using XlsxWriter.

    * - Column type
      - ``debug``, ``default``

*************
Plugin family
*************

.. list-table:: Plugin family - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin family

    * - Description
      - Exact Plugin Family returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/[@pluginFamily]``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

****************
Plugin file name
****************

.. list-table:: Plugin file name - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin file name

    * - Description
      - Exact Plugin file name returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/fname``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``

**************
Plugin version
**************

.. list-table:: Plugin version - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin version

    * - Description
      - Exact Plugin version returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/script_version``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

***********************
Plugin publication date
***********************

.. list-table:: Plugin publication date - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin publication date

    * - Description
      - Exact Plugin publication date returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/plugin_publication_date``

    * - Post-processing
      - Return in format ``yyyy-mm-dd``.

    * - Column type
      - ``debug``, ``default``

************************
Plugin modification date
************************

.. list-table:: Plugin modification date - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin modification date

    * - Description
      - Exact Plugin modification date returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/plugin_modification_date``

    * - Post-processing
      - Return in format ``yyyy-mm-dd``.

    * - Column type
      - ``debug``, ``default``

******************
Plugin description
******************

.. list-table:: Plugin description - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin description

    * - Description
      - Exact Plugin description returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/description``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

********
Solution
********

.. list-table:: Solution - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Solution

    * - Description
      - Exact Plugin solution returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/solution``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

*************
Plugin output
*************

.. list-table:: Plugin output - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Plugin output

    * - Description
      - Exact Plugin output returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/plugin_output``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

***********
CVE counter
***********

.. list-table:: CVE counter - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVE counter

    * - Description
      - Number of |CVE| assigned to particular Plugin returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cve``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

**********
CVE number
**********

.. list-table:: CVE number - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - CVE number

    * - Description
      - List of |CVE| assigned to particular Plugin returned by Nessus.

    * - Source
      - nessus file > ``ReportHost/ReportItem/cve``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

*****************
Exploit available
*****************

.. list-table:: Exploit available - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Exploit available

    * - Description
      - Information if Exploit is available.

    * - Source
      - nessus file > ``ReportHost/ReportItem/exploit_available``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

*********************
Exploit code maturity
*********************

.. list-table:: Exploit code maturity - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Exploit code maturity

    * - Description
      - Information about Exploit code maturity.

    * - Source
      - nessus file > ``ReportHost/ReportItem/exploit_code_maturity``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``

****************************
Exploit framework metasploit
****************************

.. list-table:: Exploit framework metasploit - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Exploit framework metasploit

    * - Description
      - Information about Exploit framework metasploit.

    * - Source
      - nessus file > ``ReportHost/ReportItem/exploit_framework_metasploit``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``


*******************
Exploitability ease
*******************

.. list-table:: Exploitability ease - column details
    :widths: 20 80
    :stub-columns: 1

    * - Header name
      - Exploitability ease

    * - Description
      - Information if Exploitability is ease.

    * - Source
      - nessus file > ``ReportHost/ReportItem/exploitability_ease``

    * - Post-processing
      - *none*

    * - Column type
      - ``debug``, ``default``