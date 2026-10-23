:blogpost: true

NFR v0.9.0: New report command - xlsx reports in CLI!
=====================================================

.. post:: 2026-10-23 18:00:00
   :tags: NFR, NFA
   :category: Tools, News
   :author: Damian

The latest release of **LimberDuck NFR** (nessus file reader) ``v0.9.0`` now include a new command: ``nfr report``.

Thanks to this new command, you can generate the same xlsx reports as |NFA| does, with ``scans``, ``hosts``,
``vulnerabilities`` and ``noncompliance`` worksheets, but without GUI.
Now you can generate reports automatically, e.g. in CI/CD pipeline or scheduled job.

.. admonition:: What's included?
   :class: hint

   - all four |NFA| standard reports, with the same columns,
   - debug columns, filtering out and skipping None Risk Factor results, as in |NFA| settings,
   - ``*.nessus`` files, ``*.zip`` files with ``*.nessus`` files inside and directories as source files,
   - target directory and target file name of your choice,
   - exit codes and quiet mode for pipelines.

Examples
--------

Install **LimberDuck NFR** with ``xlsx`` extra:

.. code-block:: shell

   pip install "nessus-file-reader[xlsx]"

Generate all reports for all nessus files in given directory and it's subdirectories:

.. code-block:: shell

   nfr report ./scans -o ./reports

Generate only vulnerabilities report without None Risk Factor results, with fixed file name:

.. code-block:: shell

   nfr report ./scans -o ./reports -rv --none-skip --suffix weekly --no-timestamp

.. seealso::

   For detailed usage guides, check out :ref:`nfr-report` section.

.. hint::
   You can download the latest version of **LimberDuck NFR** (nessus file reader) from |PyPI| using ``pip``.
   Read more on :ref:`nfr-upgrade` page.
