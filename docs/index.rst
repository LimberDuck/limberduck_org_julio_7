.. LimberDuck documentation master file, created by
   sphinx-quickstart on Sun Jul  7 17:20:57 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


:layout: landing
:description: Tools designed to streamline and automate the work of cybersecurity professionals.

LimberDuck
==========

.. rst-class:: lead

   Tools designed to streamline and automate the work of cybersecurity professionals.

.. container:: buttons

    `Start here <about/>`_
    `GitHub <https://github.com/LimberDuck>`_


.. grid:: 1 1 2 3
    :gutter: 2
    :padding: 0
    :class-row: surface

    .. grid-item-card:: :octicon:`terminal` nessus file reader (``nfr``)
      :link: tools/nessus-file-reader/
      
      |nfr_pypi_downloads| |nfr_stars_from_users|

      CLI tool and python module which enables you to parse nessus files 
      with VA scan results performed using Tenable Nessus ® by Tenable, Inc.


    .. grid-item-card:: :octicon:`browser` nessus file analyzer (``nfa``)
      :link: tools/nessus-file-analyzer/

      |nfa_pypi_downloads| |nfa_stars_from_users|
      
      GUI tool which enables you to analyze nessus files 
      with VA scan results performed using Tenable Nessus ® by Tenable, Inc.

    .. grid-item-card:: :octicon:`browser` Converter CSV
      :link: tools/converter-csv/

      |converter_csv_pypi_downloads| |converter_csv_stars_from_users|
      
      GUI tool which enables you to convert multiple, large csv files to xlsx files.

    .. grid-item-card:: :octicon:`terminal` TNSCM
      :link: tools/tnscm/
      
      |tnscm_pypi_downloads| |tnscm_stars_from_users|

      CLI tool which enables you to manage 
      Tenable Nessus ® by Tenable, Inc. via API.

    .. grid-item-card:: :octicon:`terminal` TSCCM
      :link: tools/tsccm/
      
      |tsccm_pypi_downloads| |tsccm_stars_from_users|

      CLI tool which enables you to manage 
      Tenable Security Center ® by Tenable, Inc. via API.

    .. grid-item-card:: :octicon:`rocket` and more...

..  .. grid-item-card:: :octicon:`terminal` ``tnscm`` (Tenable Nessus CLI Manager)

..    CLI tool which enables you to perform actions on Tenable Nessus 
..    by (C) Tenable, Inc. via API.

..  .. grid-item-card:: :octicon:`terminal` ``tsccm`` (Tenable Security Center CLI Manager)

..    CLI tool which enables you to perform actions on Tenable Security Center 
..    by (C) Tenable, Inc. via API.


----

Testimonials
------------

.. pull-quote::

   I love the Nessus File Analyzer, so thank you so much for sharing and maintaining.

   -- nessus file analyzer's user

.. pull-quote::

   Tested everyday. Works perfect.

   -- nessus file analyzer's user

.. pull-quote::

   Brilliant work!

   -- nessus file analyzer's user

.. pull-quote::

   This tool is really helpful! Thanks for sharing this.

   -- nessus file analyzer's user

.. pull-quote::

   I found nessus file analyzer to be an excellent tool.

   -- nessus file analyzer's user

.. pull-quote::

   First of all... Great tool! You did a really great job! Thanks for developing such a wonderful tool!

   -- nessus file analyzer's user

.. pull-quote::

   I'm grateful for your software...

   -- nessus file analyzer's user


.. .. toctree::
..    :hidden:

..    start/index

.. toctree::
   :caption: Tools
   :hidden:

   tools/nessus-file-reader/index
   tools/nessus-file-analyzer/index
   tools/converter-csv/index
   tools/tnscm/index
   tools/tsccm/index

.. toctree::
   :caption: Notebooks
   :hidden:

   notebooks/cpe/cpe
   notebooks/cve/cve
   notebooks/cwe/cwe

.. toctree::
   :caption: Other
   :maxdepth: 1
   :hidden:

   cheat-sheets/nessus-cheat-sheet/index
   glossary/index
   blog/index
   faq/index


.. |nfa_pypi_downloads| image:: https://img.shields.io/pypi/dm/nessus-file-analyzer?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/nessus-file-analyzer
    :alt: PyPI - Downloads

.. |nfa_stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck/nessus-file-analyzer?label=Stars&style=social
    :target: https://github.com/LimberDuck/nessus-file-analyzer
    :alt: GitHub Stars

.. |nfr_pypi_downloads| image:: https://img.shields.io/pypi/dm/nessus-file-reader?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/nessus-file-reader
    :alt: PyPI - Downloads

.. |nfr_stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck/nessus-file-reader?label=Stars&style=social
    :target: https://github.com/LimberDuck/nessus-file-reader
    :alt: GitHub Stars

.. |converter_csv_pypi_downloads| image:: https://img.shields.io/pypi/dm/converter-csv?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/converter-csv
    :alt: PyPI - Downloads

.. |converter_csv_stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck/converter-csv?label=Stars&style=social
    :target: https://github.com/LimberDuck/converter-csv
    :alt: GitHub Stars

.. |tnscm_pypi_downloads| image:: https://img.shields.io/pypi/dm/tnscm?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/tnscm
    :alt: PyPI - Downloads

.. |tnscm_stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck/tnscm?label=Stars&style=social
    :target: https://github.com/LimberDuck/tnscm
    :alt: GitHub Stars

.. |tsccm_pypi_downloads| image:: https://img.shields.io/pypi/dm/tsccm?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/tsccm
    :alt: PyPI - Downloads

.. |tsccm_stars_from_users| image:: https://img.shields.io/github/stars/LimberDuck/tsccm?label=Stars&style=social
    :target: https://github.com/LimberDuck/tsccm
    :alt: GitHub Stars