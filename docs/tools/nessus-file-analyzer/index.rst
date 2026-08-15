:description: GUI tool which enables you to analyze nessus files.

NFA (nessus file analyzer)
==========================

|nfa_pepy_downloads| |github_downloads_latest_release| |github_downloads_all_releases| |stars_from_users| |latest_release| |latest_release_date| |license| |supported_platform| 

.. image:: ../../_static/img/LimberDuck-nessus-file-analyzer-logo.png
   :alt: LimberDuck nessus-file-analyzer logo
   :width: 120px
   :align: left
   :target: .

This is a |GUI| tool which enables you to parse multiple nessus files containing the 
results of scans performed by using *Tenable Nessus* or *Tenable Security Center* by 
© Tenable, Inc. used for |VA| [1]_ process. Parsed scan results are exported to a 
spreadsheet file for effortless analysis. 

Operational memory usage will 
be kept low while parsing even the largest of files. You can run it on your favorite 
operating system, whether it is Windows, macOS or GNU Linux. As a parsing result, you 
will receive spreadsheets with a summary view of the whole scan and/or all reported 
hosts. You will also be able to generate spreadsheets with a detailed view of all 
reported vulnerabilities [2]_ and/or noncompliance. It's free and Open Source [3]_ tool.

.. grid:: 2 3 4 4

    .. grid-item::

      .. button-link:: https://github.com/LimberDuck/nessus-file-analyzer/releases
         :color: primary
         :tooltip: Download

         :octicon:`download;1em;sd-color-primary-text` Download

    .. grid-item::

      .. button-link:: https://github.com/LimberDuck/nessus-file-analyzer/releases
         :color: primary
         :outline:
         :tooltip: Release notes

         :octicon:`note;1em;sd-color-primary-text` Release notes

    .. grid-item::

      .. button-link:: https://github.com/LimberDuck/nessus-file-analyzer
         :color: primary
         :outline:
         :tooltip: Source code

         :octicon:`code;1em;sd-color-primary-text` Source code

    .. grid-item::

      .. button-link:: https://github.com/LimberDuck/nessus-file-analyzer/discussions
         :color: primary
         :outline:
         :tooltip: Discussions

         :octicon:`comment-discussion;1em;sd-color-primary-text` Discussions

    .. grid-item::

      .. button-link:: https://github.com/LimberDuck/nessus-file-analyzer/issues
         :color: primary
         :outline:
         :tooltip: Issues

         :octicon:`issue-opened;1em;sd-color-primary-text` Issues

.. .. list-table:: nessus-file-analyzer details
..     :widths: 25 75
..     :stub-columns: 1

..     * - source code
..       - https://github.com/LimberDuck/nessus-file-analyzer

..     * - release notes
..       - https://github.com/LimberDuck/nessus-file-analyzer/releases

..     * - changelog
..       - https://github.com/LimberDuck/nessus-file-analyzer/blob/master/CHANGELOG.md

..     * - documentation
..       - https://nessus-file-analyzer.readthedocs.io




.. figure:: ../../_static/img/nfa.png
   :width: 600
   :align: center

   **nessus file analyzer (NFA)** main window running on macOS, but works as well on Windows and Linux. 

Technology stack
----------------

.. https://www.python.org/community/logos/
.. image:: ../../_static/img/logos/python-logo-only.svg
   :alt: Python logo
   :target: https://python.org
   :width: 70px

.. https://www.qt.io/brand/development/logo
.. image:: ../../_static/img/logos/Qt-logo-neon.svg
   :alt: Qt logo
   :target: https://www.qt.io
   :width: 70px

.. https://pl.wikipedia.org/wiki/PyQt
.. image:: ../../_static/img/logos/Python_and_Qt.svg
   :alt: PyQt logo
   :target: https://riverbankcomputing.com/software/pyqt
   :width: 80px

Latest NFA news
---------------

.. postlist::
   :language: en
   :date: %Y-%m-%d
   :format: {date} - {title}
   :list-style: circle
   :tags: NFA

Testimonials
------------

   Bar none your product is best in my career.

   -- |NFA| user

   I love the Nessus File Analyzer, so thank you so much for sharing and maintaining.

   -- |NFA| user

   Tested everyday. Works perfect.

   -- |NFA| user

   Brilliant work!

   -- |NFA| user

   This tool is really helpful! Thanks for sharing this.

   -- |NFA| user

   I found nessus file analyzer to be an excellent tool.

   -- |NFA| user

   First of all... Great tool! You did a really great job! Thanks for developing such a wonderful tool!

   -- |NFA| user

   I'm grateful for your software...

   -- |NFA| user

Stargazers over time
--------------------

.. https://starchart.cc/LimberDuck/nessus-file-analyzer.svg?background=%23ffffff00&axis=%23E57333&line=%23E57333

.. figure:: https://repostars.dev/api/embed?repo=LimberDuck%2Fnessus-file-analyzer&theme=lava
    :alt: Stargazers over time
    :align: center

    **nessus file analyzer (NFA)** GitHub repository stars over time.


----

.. rubric:: Footnotes

.. [1] read more about :term:`Vulnerability Assessment` in glossary
.. [2] read more about :term:`vulnerability` in glossary 
.. [3] read more about :term:`Open Source` in glossary

.. |license| image:: https://img.shields.io/github/license/LimberDuck/nessus-file-analyzer.svg?style=social
    :target: https://github.com/LimberDuck/nessus-file-analyzer/blob/master/LICENSE
    :alt: License

.. |supported_platform| image:: https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=social
    :target: https://github.com/LimberDuck/nessus-file-analyzer
    :alt: Supported platform

.. |stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck/nessus-file-analyzer?label=Stars&style=social
    :target: https://github.com/LimberDuck/nessus-file-analyzer
    :alt: GitHub Stars

.. |latest_release| image:: https://img.shields.io/github/v/release/LimberDuck/nessus-file-analyzer?label=Latest%20release&style=social
    :target: https://github.com/LimberDuck/nessus-file-analyzer/releases
    :alt: Latest Release version

.. |latest_release_date| image:: https://img.shields.io/github/release-date/limberduck/nessus-file-analyzer?label=released&style=social
    :target: https://github.com/LimberDuck/nessus-file-analyzer/releases
    :alt: GitHub Release Date

.. |pypi_downloads| image:: https://img.shields.io/pypi/dm/nessus-file-analyzer?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/nessus-file-analyzer
    :alt: PyPI - Downloads

.. |nfa_pepy_downloads| image:: https://img.shields.io/pepy/dt/nessus-file-analyzer?logo=PyPI&style=social   
    :target: https://pepy.tech/projects/nessus-file-analyzer
    :alt: pepy.tech - Total Downloads

.. |github_downloads_all_releases| image:: https://img.shields.io/github/downloads/LimberDuck/nessus-file-analyzer/total?style=social&label=All%20downloads%20since%20release%20v0.10&logo=GitHub
   :target: https://github.com/LimberDuck/nessus-file-analyzer/releases
   :alt: GitHub Downloads (all assets, all releases) since v0.10

.. |github_downloads_latest_release| image:: https://img.shields.io/github/downloads/LimberDuck/nessus-file-analyzer/latest/total?style=social&label=latest%20release%20downloads&logo=GitHub
   :target: https://github.com/LimberDuck/nessus-file-analyzer/releases/latest
   :alt: GitHub Downloads (all assets, latest release)

.. toctree::
   :hidden:

   installation
   running
   building
   using
   settings
   standard-reports/index
   advanced-reports/index
