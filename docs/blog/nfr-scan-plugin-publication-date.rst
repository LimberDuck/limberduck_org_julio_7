:blogpost: true

NFR v0.8.0: New scan command option - Plugin Publication Date
=============================================================

.. post:: 2026-02-07 08:05:03
   :tags: NFR
   :category: Tools, News
   :author: Damian

The latest release of **NFR** (nessus file reader) ``v0.8.0`` now include a powerful new feature: 
vulnerabilities summary by **Plugin Publication Date**.

Thanks to these new feature, you can now generate summaries of plugins based on their publication date, 
allowing you to identify potential gaps in your vulnerability management strategy.

.. admonition:: Why is it worth to check plugin publication date?
   :class: hint

   It allows you to quickly identify how many previously recognized vulnerabilities have not yet been remediated.
   
   Some of the plugins are associated with |CVE| identifiers, in these cases the plugin publication date is 
   usually close to the |CVE| publication date.
   
   | **Example:**
   | Plugin ID: `83344 <https://www.tenable.com/plugins/nessus/83344>`_
   | Plugin name: Ubuntu 14.04 LTS : Libtasn1 vulnerability (USN-2604-1)
   | Plugin publication date: 5/12/2015
   | CVE: `CVE-2015-3622 <https://www.tenable.com/cve/CVE-2015-3622>`_
   | CVE publication date: 2015-05-12


Examples
--------

``nfr scan --plugin-publication-date bar year``
...............................................

.. code-block:: shell
   
   nfr scan -plpd bar year -f "[?risk_factor != 'None']" file1 dir1 dir2

.. figure:: ../../_static/img/limberduck-nfr-plpd-bar-year.png
    :alt: Example bar chart showing the number of plugins by publication year.
    :align: center

    Example bar chart showing the number of plugins by publication year.

``nfr scan --plugin-publication-date line year``
................................................

.. code-block:: shell

   nfr scan -plpd line year -f "[?risk_factor != 'None']" file1 dir1 dir2

.. figure:: ../../_static/img/limberduck-nfr-plpd-line-year.png
    :alt: Example line chart showing the number of plugins by publication year.
    :align: center

    Example line chart showing the number of plugins by publication year.

.. seealso::

   For detailed usage guides, check out :ref:`nfr-scan-plugin-publication-date-option` section.

.. hint:: 
   You can download the latest version of **NFR** (nessus file reader) from |PyPI| using ``pip``.
   Read more on :ref:`nfr-upgrade` page.