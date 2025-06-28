:blogpost: true

nessus file reader (NFR) v0.6.0: Compare plugin severity
========================================================

.. post:: 2025-06-28 16:43:40
   :tags: nfr
   :category: tools
   :author: Damian

I'm excited to introduce a powerful new feature in **nessus file reader (NFR) v0.6.0** — the ``--plugin-severity`` option!  
Now you can effortlessly compare severity scores assigned to Nessus plugins, including Severity, Risk Factor, |CVSS| v2/v3/v4, |VPR|, and |EPSS| — all in a single view.

What's New?
-----------

With the new ``nfr scan --plugin-severity`` command, you can now:

- Compare severity metadata for each plugin across multiple scoring systems.
- Easily identify inconsistencies or patterns between |CVSS|, |VPR|, and |EPSS| values.
- Use powerful `JMESPath <https://jmespath.org>`_ to filter on specific Plugin IDs or other conditions.

Example::

   nfr scan --plugin-severity 192_168_1_1_1022nb.nessus

You'll get a tabular summary like:

::

   File name                  Report host name       PID    S  SL      RF        CVSSv2  CVSSv2L      CVSSv3  CVSSv3L    CVSSv4    CVSSv4L      VPR  VPRL      EPSS  EPSS%
   -------------------------  ------------------  ------  ---  ------  ------  --------  ---------  --------  ---------  --------  ---------  -----  ------  ------  -------
   192_168_1_1_1022nb.nessus  192.168.1.10         12217    2  Medium  Medium       5    Medium          5.3  Medium
   192_168_1_1_1022nb.nessus  192.168.1.10         42263    2  Medium  Medium       5.8  Medium          6.5  Medium
   192_168_1_1_1022nb.nessus  192.168.1.10         50686    2  Medium  Medium       5.8  Medium          6.5  Medium                            4.9  Medium  0.0596  6.0%

Filter with Precision
---------------------

Thanks to the new ``--filter`` option, you can apply custom filters using `JMESPath <https://jmespath.org>`_.

Examples:

- Show only a specific plugin::

    nfr scan --plugin-severity *.nessus -f "[?PID == '50686']"

- Show only plugins with |VPR| scores::

    nfr scan --plugin-severity file.nessus -f "[?VPR != null]"

- Show plugins with |CVSSv3| > ``4.0``::

    nfr scan --plugin-severity file.nessus -f "[?CVSSv3 > '4.0']"

- Combine filters::

    nfr scan --plugin-severity file.nessus -f "[?CVSSv3 > '3.8' && VPR > '4.0']"

Need Columns Descriptions?
--------------------------

Just run::

   nfr scan --plugin-severity-legend

It will print a clear legend explaining each column in the comparison table.

Python Module
-------------

For those who wants to create their own view there are new functions for plugins:

- ``severity_number_to_label(severity_number)`` - Convert a numeric severity level to its corresponding string label.
- ``cvssv2_score_to_severity(cvss_score)`` - Convert a |CVSS| v2 base score to its corresponding severity label.
- ``cvssv3_score_to_severity(cvss_score)`` - Convert a |CVSS| v3 base score to its corresponding severity label.
- ``cvssv4_score_to_severity(cvss_score)`` - Convert a |CVSS| v4 base score to its corresponding severity label.
- ``vpr_score_to_severity(vpr_score)`` - Convert a |VPR| score to its corresponding severity label.
- ``epss_score_decimal_to_percent(epss_score)`` - Convert an |EPSS| score from decimal format to a percentage string.

|TLDR|
------

Run with ``nfr scan --plugin-severity file_name.nessus`` to:

- Quickly compare how multiple scoring systems rank a plugi's risk.
- Apply flexible filters with `JMESPath <https://jmespath.org>`_ using ``-f`` or ``--filter``.
- Improve prioritization and remediation efforts by analyzing |VPR| and |EPSS| alongside |CVSS| scores.

.. seealso::

   Check out the new feature in the documentation: :ref:`nfr-scan-plugin-severity`.

.. important:: 
   
   :ref:`nfr-upgrade` now to **NFR v0.6.0** and supercharge your vulnerability scan analysis.

