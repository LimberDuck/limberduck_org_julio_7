:description: Using instruction for nessus file analyzer (nfa).

#####
Using
#####

*****************
Open nessus files
*****************

You have a few possibilities to open your nessus files in **nessus file analyzer** (``nfa``).

.. versionadded:: v0.5.0
   You can open nessus files from inside a ZIP archive. You don't need to unzip nessus files anymore.

**OPTION 1** - by opening file\\-s

1. Open **nessus file analyzer** (``nfa``).
2. Go to Menu *File*.
3. Choose *Open file\\-s* if you want to open one or more nessus files at once.

**OPTION 2** - by opening directory

1. Open **nessus file analyzer** (``nfa``).
2. Go to Menu *File*.
3. Choose *Open directory* if you want to open all nessus files from selected directory and its subdirectories.

**OPTION 3** - by use of |OS| contextual menu

1. On |OS| level select one or more nessus files in your |OS| file browser.
2. Click |RMB| on selected file\\-s and choose from contextual menu option *Open with...*.
3. Choose **nessus file analyzer** (``nfa``) to open selected file\\-s.

**OPTION 4** - by file\\-s Drag & Drop

1. On |OS| level select one or more nessus files in your |OS| file browser.
2. Simple drag and drop selected file\\-s on **nessus file analyzer** (``nfa``) window.

**OPTION 5** - by directory Drag & Drop

1. On |OS| level select one or more directories containing nessus files in your |OS| file browser. 
2. Simple drag and drop selected directory or directories on **nessus file analyzer** (``nfa``) window.

******************
Select report type
******************

Select one or more report types: scan, host, vulnerabilities, noncompliance.

- ``scan`` - if you want to see sum-up from point of view of the whole scan. 

  .. seealso::
    :class: dropdown

    Check :doc:`target-file/section-scan` description to get more details.

- ``host`` - if you want to see sum-up from point of view of particular scanned host. 

  .. seealso::
    :class: dropdown

    Check :doc:`target-file/section-host` description to get more details.

- ``vulnerabilities`` - if you want to see list of vulnerabilities reported in this scan for all scanned hosts. 

  .. seealso::
    :class: dropdown

    Check :doc:`target-file/section-vulnerabilities` description to get more details.

- ``noncompliance`` - if you want to see list of noncompliance reported in this scan for all scanned hosts. 

  .. seealso::
    :class: dropdown

    Check :doc:`target-file/section-noncompliance` description to get more details.

*********
Configure
*********

Configure **nessus file analyzer** (``nfa``) to fit target file to your exact needs.

.. seealso::
    Check :doc:`settings` to get more details.

******************
Initialize analyze
******************

Click :bdg-secondary:`Start` button to initiate analyze of all provided nessus files.

****************
Open target file
****************

Click :bdg-secondary:`Open` button to open target directory where output file has been saved.
