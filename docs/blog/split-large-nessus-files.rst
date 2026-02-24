:blogpost: true

nessus file reader (NFR) v0.5.0: Split large Nessus files
=========================================================

.. post:: 2025-05-03 13:00:00
   :tags: NFR
   :category: Tools, News
   :author: Damian

I'm excited to introduce a new feature in **nessus file reader (NFR) v0.5.0** that will significantly improve your workflow when dealing with large Nessus scan result files. The new ``--split`` option in the ``nfr file`` command allows you to split Nessus files into smaller, more manageable chunks — perfect for improving performance during post-processing if your processing tool can't deal with large files.

.. seealso::

   Check out the new feature in the documentation: :ref:`nfr-file-split`.

.. important:: 
   
   :ref:`nfr-upgrade` now to **NFR v0.5.0** and start splitting.