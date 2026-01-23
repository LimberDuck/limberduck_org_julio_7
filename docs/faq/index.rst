:description: Do you have questions? Find the answers here.

FAQ
===

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