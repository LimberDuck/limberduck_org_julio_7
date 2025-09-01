:blogpost: true

Check for Update option in all LimberDuck Tools
===============================================

.. post:: 2025-09-01 20:00:00
   :tags: nfr nfa tnscm tsccm converter-csv
   :category: tools
   :author: Damian

New feature which will let you to quickly verify if you are running the latest version of LimberDuck tool. 

What's New?
-----------

For **nessus file reader (NFR)**, **TNSCM** and **TSCCM** you can now easily check if you are using the latest version of the tool. Simply run: 

- ``nfr --update-check`` or ``nfr -u``
- ``tnscm --update-check`` or ``tnscm -u``
- ``tsccm --update-check`` or ``tsccm -u``

.. code-block:: bash
   :caption: Example output when you use latest version of the tool.
   :emphasize-lines: 4

   % nfr -u
   nessus file reader (NFR) by LimberDuck 0.7.1

   > You are using the latest version of nessus-file-reader: 0.7.1

   > Read more:
   > https://limberduck.org/en/latest/tools/nessus-file-reader
   > https://github.com/LimberDuck/nessus-file-reader
   > https://github.com/LimberDuck/nessus-file-reader/releases


.. code-block:: bash
   :caption: Example output when you use outdated version of the tool.
   :emphasize-lines: 4-5

   % nfr -u
   nessus file reader (NFR) by LimberDuck 0.7.0

   > A new version of nessus-file-reader is available: 0.7.1 (you have 0.7.0)
   > Update with: pip install -U nessus-file-reader

   > Read more:
   > https://limberduck.org/en/latest/tools/nessus-file-reader
   > https://github.com/LimberDuck/nessus-file-reader
   > https://github.com/LimberDuck/nessus-file-reader/releases

For **nessus file analyzer (NFA)** and **Converter CSV** you can check for updates directly from the application menu.

Go to **Help** menu and click on **Check for Update**.

.. code-block:: bash
   :caption: Example output when you use latest version of the tool.
   :emphasize-lines: 1

   You are using the latest version of nessus file analyzer (NFA) by LimberDuck: 0.9.0

   Read more:
   Documentation
   GitHub
   Releases



.. code-block:: bash
   :caption: Example output when you use outdated version of the tool.
   :emphasize-lines: 1,3-4,6-7

   A new version of nessus file analyzer (NFA) by LimberDuck is available!

   Latest: 0.9.0
   You have: 0.8.9

   Update with:
   pip install -U nessus-file-analyzer

   Read more:
   Documentation
   GitHub
   Releases

In addition, in Help menu you can now find quick links to:

- Documentation
- GitHub page
- GitHub Releases page

.. important:: 
   
   :ref:`nfa-upgrade` to **NFA v0.9.0**.

   :ref:`nfr-upgrade` it to **NFR v0.7.1**.

   :ref:`converter-csv-upgrade` it to **Converter v0.4.0**.

   Upgrade to **TNSCM v0.0.7** with ``pip install --upgrade tnscm``

   Upgrade to **TSCCM v0.0.6** with ``pip install --upgrade tsccm``

