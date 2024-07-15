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
      :link: /tools/nessus-file-reader/
      
      |nfr_pypi_downloads|

      |CLI| tool and python module which enables you to parse nessus files 
      with |VA| scan results performed using Tenable Nessus ® by Tenable, Inc.


    .. grid-item-card:: :octicon:`browser` nessus file analyzer (``nfa``)
      :link: /tools/nessus-file-analyzer/

      |nfa_pypi_downloads|
      
      |GUI| tool which enables you to analyze nessus files 
      with |VA| scan results performed using Tenable Nessus ® by Tenable, Inc.

    .. grid-item-card:: :octicon:`rocket` and more...

..  .. grid-item-card:: :octicon:`terminal` ``tnscm`` (Tenable Nessus CLI Manager)

..    |CLI| tool which enables you to perform actions on Tenable Nessus 
..    by (C) Tenable, Inc. via API.

..  .. grid-item-card:: :octicon:`terminal` ``tsccm`` (Tenable Security Center CLI Manager)

..    |CLI| tool which enables you to perform actions on Tenable Security Center 
..    by (C) Tenable, Inc. via API.


----

.. rubric:: testimonials


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


.. |nfa_pypi_downloads| image:: https://img.shields.io/pypi/dm/nessus-file-analyzer?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/nessus-file-analyzer
    :alt: PyPI - Downloads

.. |nfr_pypi_downloads| image:: https://img.shields.io/pypi/dm/nessus-file-reader?logo=PyPI&style=social   
    :target: https://pypistats.org/packages/nessus-file-reader
    :alt: PyPI - Downloads