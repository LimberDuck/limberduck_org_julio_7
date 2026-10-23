:description: Using instruction for LimberDuck NFA (nessus file analyzer).

#####
Using
#####

Open nessus files
#################

You have a few possibilities to open your nessus files in **LimberDuck NFA (nessus file analyzer)**.

.. versionadded:: v0.5.0
   You can open nessus files from inside a ZIP archive. You don't need to unzip nessus files anymore.

**OPTION 1** - by opening file\\-s

1. Open **LimberDuck NFA (nessus file analyzer)**.
2. Go to Menu *File*.
3. Choose *Open file\\-s* if you want to open one or more nessus files at once.

**OPTION 2** - by opening directory

1. Open **LimberDuck NFA (nessus file analyzer)**.
2. Go to Menu *File*.
3. Choose *Open directory* if you want to open all nessus files from selected directory and its subdirectories.

**OPTION 3** - by use of |OS| contextual menu

1. On |OS| level select one or more nessus files in your |OS| file browser.
2. Click |RMB| on selected file\\-s and choose from contextual menu option *Open with...*.
3. Choose **LimberDuck NFA (nessus file analyzer)** to open selected file\\-s.

**OPTION 4** - by file\\-s Drag & Drop

1. On |OS| level select one or more nessus files in your |OS| file browser.
2. Simple drag and drop selected file\\-s on **LimberDuck NFA (nessus file analyzer)** window.

**OPTION 5** - by directory Drag & Drop

1. On |OS| level select one or more directories containing nessus files in your |OS| file browser. 
2. Simple drag and drop selected directory or directories on **LimberDuck NFA (nessus file analyzer)** window.

Select report type
##################

Select one or more report from standard report types: scan, host, vulnerabilities, noncompliance.

- ``scan`` - if you want to see sum-up from point of view of the whole scan. 
  Check :doc:`standard-reports/section-scan` to get more details.

- ``host`` - if you want to see sum-up from point of view of particular scanned host. 
  Check :doc:`standard-reports/section-host` to get more details.

- ``vulnerabilities`` - if you want to see list of vulnerabilities reported in this scan for all scanned hosts. 
  Check :doc:`standard-reports/section-vulnerabilities` to get more details.

- ``noncompliance`` - if you want to see list of noncompliance reported in this scan for all scanned hosts. 
  Check :doc:`standard-reports/section-noncompliance` to get more details.

If you need other reports, check :doc:`advanced-reports/index` section to see what else you can get from your Nessus files.

Configure
#########

Configure **LimberDuck NFA (nessus file analyzer)** to fit target file to your exact needs.

.. seealso::
    :class: dropdown

    Check :doc:`settings` to get more details.

Initialize analyze
##################

Click :bdg-secondary:`Start` button to initiate analyze of all provided nessus files.

Open target file
################

Click :bdg-secondary:`Open` button to open target directory where output file has been saved.

Help menu
#########

Check for Update
================

.. versionadded:: v0.11.0
   It will notify you automatically with every run of the **LimberDuck NFA (nessus file analyzer)** if a new version is available.

Select ``Help > Check for Update`` option to check if you are using the latest version of **LimberDuck NFA (nessus file analyzer)**.

Check Announcements
===================

.. versionadded:: v0.11.0
   It will fetch latest LimberDuck's announcements with every run of the **LimberDuck NFA (nessus file analyzer)**.

Select ``Help > Check Announcements`` option to fetch latest LimberDuck's announcements.


Documentation
=============

Select ``Help > Documentation`` option to open online **LimberDuck NFA (nessus file analyzer)** documentation.

GitHub
======

Select ``Help > GitHub`` option to open **LimberDuck NFA (nessus file analyzer)** GitHub project page.

Releases
========

Select ``Help > Releases`` option to open **LimberDuck NFA (nessus file analyzer)** GitHub Releases page.