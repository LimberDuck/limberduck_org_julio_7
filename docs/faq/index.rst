:description: Do you have questions? Find the answers here.

FAQ
===

Are there any vulnerabilities identified in LimberDuck tools?
-------------------------------------------------------------

LimberDuck tools are regularly scanned using multiple tools to identify vulnerabilities and other security issues. 
If any new vulnerabilities are detected, they are assessed and remediated in a subsequent release.

What tools are used to identify vulnerabilities in LimberDuck tools?
--------------------------------------------------------------------

**Snyk**

Snyk notifies maintainers automatically when new issues are found in the monitored Projects to alert on possible new risks in these Projects. 
In addition Snyk sends weekly report emails to maintainers to provide a summary of the vulnerability status across all Projects.

Source: https://docs.snyk.io/platform-administration/snyk-hierarchy/manage-notifications

**Dependabot**

Dependabot informs maintainers about vulnerabilities in the dependencies that are used in a repository.

Source: https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart

**GitGuardian**

GitGuardian detects secrets and sensitive information in code repositories and alert maintainers of potential security risks.

Source:

- https://docs.gitguardian.com/platform/home
- https://docs.gitguardian.com/platform/configure-alerting/notifiers-integrations/email-alerting

**SonarQube**

SonarQube notifies maintainers about any new issues introduced by new code for any project.

Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications


Is the code actively maintained?
--------------------------------

**Yes.** Security vulnerabilities are assessed and remediated whenever they are identified. Issues reported by users are investigated, 
reproduced, and fixed whenever sufficient information is provided to diagnose the problem.

New features are implemented based on user needs, taking into account their value, complexity, and development effort.

If you would like to extend the current toolset with new features, visit :doc:`../../../contact/index` page and feel free to submit a feature request for assessment.

Do LimberDuck tools send Nessus data anywhere?
----------------------------------------------

**No.** All scan results processed by LimberDuck NFA or LimberDuck NFR are processed locally on the machine where the tools are run. 
No scan data is transmitted to external servers.


Do LimberDuck tools make any outbound calls?
--------------------------------------------

**Yes.** LimberDuck tools make a limited number of outbound calls.

.. important::
    
    LimberDuck tools do not transmit scan results, credentials, or locally processed data during any of these outbound calls.

.. tip::
    
    | The source code references for outbound HTTP requests can be found here:
    | https://github.com/search?q=org%3ALimberDuck+requests.get&type=code

**Automatically triggered calls.**

- Calls to https://pypi.org to automatically check whether a newer release is available and notify the user. The following addresses are used:
    - LimberDuck NFA: https://pypi.org/pypi/nessus-file-analyzer/json
    - LimberDuck NFR: https://pypi.org/pypi/nessus-file-reader/json
    - LimberDuck TNSCM: https://pypi.org/pypi/tnscm/json
    - LimberDuck TSCCM: https://pypi.org/pypi/tsccm/json
    - LimberDuck Converter CSV: https://pypi.org/pypi/converter-csv/json
- Calls to https://limberduck.github.io/data/announcements.json to retrieve user notifications and announcements. This applies to:
    - LimberDuck NFA
    - LimberDuck Converter CSV

**Calls triggered manually by the user.**

The following calls are initiated only when the user explicitly selects an action, such as opening a documentation, project link, update check.

.. tip::
    
    | Source code references for these calls can be found here:  
    | https://github.com/search?q=org%3ALimberDuck+url_open.open_website&type=code
    | https://github.com/search?q=org%3ALimberDuck+requests.get&type=code

- Checking if a newer release is available on PyPI:
    - LimberDuck NFA: https://pypi.org/pypi/nessus-file-analyzer/json
    - LimberDuck NFR: https://pypi.org/pypi/nessus-file-reader/json
    - LimberDuck TNSCM: https://pypi.org/pypi/tnscm/json
    - LimberDuck TSCCM: https://pypi.org/pypi/tsccm/json
    - LimberDuck Converter CSV: https://pypi.org/pypi/converter-csv/json
- Opening LimberDuck documentation:
    - LimberDuck NFA: https://limberduck.org/en/latest/tools/nessus-file-analyzer/
    - LimberDuck Converter CSV: https://limberduck.org/en/latest/tools/converter-csv/
- Opening the GitHub project page:
    - LimberDuck NFA: https://github.com/LimberDuck/nessus-file-analyzer/
    - LimberDuck Converter CSV: https://github.com/LimberDuck/converter-csv/
- Opening the GitHub release page:
    - LimberDuck NFA: https://github.com/LimberDuck/nessus-file-analyzer/releases
    - LimberDuck Converter CSV: https://github.com/LimberDuck/converter-csv/releases




Why NFA returns "not well-formed (invalid token)" error?
--------------------------------------------------------

This error may occur when you are trying to parse a ``.nessus`` file directly from 
`Nessus Default Data Directories <https://github.com/LimberDuck/nessus-cheat-sheet/blob/main/nessus-cheat-sheet.adoc#data-directories>`_
, such as: ``%PROGRAMDATA%\Nessus\nessus\users\<username>\reports``.

``.nessus`` files stored in Nessus Default Data Directories are not plain text files.

To properly parse ``.nessus`` files with **nessus file analyzer (NFA)** you need to first export the scan report from Nessus web interface as a ``.nessus`` file.

Can LimberDuck tools split .nessus files?
-----------------------------------------
Yes, LimberDuck tools can split `.nessus files`. The **nessus file reader (NFR)** has a command called ``file`` that allows you to split large Nessus files into smaller, more manageable chunks. This is particularly useful for improving performance during post-processing if your processing tool can't handle large files.

Check out the new feature in the documentation: :ref:`nfr-file-split`.


Why NFA returns "has host bits set" error?
------------------------------------------

Take a look at the **example** line log:

.. code-block::
    :caption: Example "has host bits set" error for address 192.168.11.0/23 
    :name: error-example-192-168-11-0-23

    [2025-01-30 15:05:29.395186] [action=info] [source_file_name=ERROR Parsing [1/1] nessus files]
    [2025-01-30 15:05:29.395186] [action=info] [source_file_name=192.168.11.0/23 has host bits set]


The part “has host bits set” says that you have put into the Nessus target field the wrong target address - ``192.168.11.0/23`` :

.. code-block::
    :linenos:
    :emphasize-lines: 1,2
    :caption: IP Calculator output for address 192.168.11.0/23
    :name: ipcalc-192-168-11-0-23

    Address:   192.168.11.0          11000000.10101000.0000101 1.00000000
    Netmask:   255.255.254.0 = 23    11111111.11111111.1111111 0.00000000
    Wildcard:  0.0.1.255             00000000.00000000.0000000 1.11111111
    =>
    Network:   192.168.10.0/23       11000000.10101000.0000101 0.00000000 (Class C)
    Broadcast: 192.168.11.255        11000000.10101000.0000101 1.11111111
    HostMin:   192.168.10.1          11000000.10101000.0000101 0.00000001
    HostMax:   192.168.11.254        11000000.10101000.0000101 1.11111110
    Hosts/Net: 510                   (Private Internet)

If your Netmask is ``/23`` and your network address is ``192.168.10.0`` and your goal is to scan the whole network, you should put into Nessus target field - ``192.168.10.0/23`` :

.. code-block::
    :linenos:
    :emphasize-lines: 1,2
    :caption: IP Calculator output for address 192.168.10.0/23
    :name: ipcalc-192-168-10-0-23

    Address:   192.168.10.0          11000000.10101000.0000101 0.00000000
    Netmask:   255.255.254.0 = 23    11111111.11111111.1111111 0.00000000
    Wildcard:  0.0.1.255             00000000.00000000.0000000 1.11111111
    =>
    Network:   192.168.10.0/23       11000000.10101000.0000101 0.00000000 (Class C)
    Broadcast: 192.168.11.255        11000000.10101000.0000101 1.11111111
    HostMin:   192.168.10.1          11000000.10101000.0000101 0.00000001
    HostMax:   192.168.11.254        11000000.10101000.0000101 1.11111110
    Hosts/Net: 510                   (Private Internet)

If your Netmask is ``/24`` and your goal was to scan the whole network, you should put into Nessus target field - ``192.168.11.0/24`` :

.. code-block::
    :linenos:
    :emphasize-lines: 1,2
    :caption: IP Calculator output for address 192.168.11.0/24
    :name: ipcalc-192-168-11-0-24

    Address:   192.168.11.0          11000000.10101000.00001011 .00000000
    Netmask:   255.255.255.0 = 24    11111111.11111111.11111111 .00000000
    Wildcard:  0.0.0.255             00000000.00000000.00000000 .11111111
    =>
    Network:   192.168.11.0/24       11000000.10101000.00001011 .00000000 (Class C)
    Broadcast: 192.168.11.255        11000000.10101000.00001011 .11111111
    HostMin:   192.168.11.1          11000000.10101000.00001011 .00000001
    HostMax:   192.168.11.254        11000000.10101000.00001011 .11111110
    Hosts/Net: 254                   (Private Internet)

If you aimed to scan only one IP address, you should put it into the Nessus target field - ``192.168.11.0`` (without mask ``/23``).

To pars data without issues:

1. Set scan again with, e.g., ``192.168.10.0/23`` or ``192.168.11.0`` or ``192.168.11.0/24``. 
2. Then try to pars your .nessus file again using nessus-file-analyzer.


.. tip::

    Use https://jodies.de/ipcalc to make sure that you use correct the IP Address and Netmask.