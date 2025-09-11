:description: Installation instruction for nessus file analyzer (NFA).

############
Installation
############

.. hint::

    Since ``v0.10.0`` nessus file analyzer (NFA) comes with pre-built binaries for Windows, 
    Linux and macOS. You can download the latest version from 
    `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page. 
    You can still install it with ``pip`` and build it from source code if you want.

.. note::

    It's advisable to use python virtual environment for below instructions. Read more about python virtual environment in `The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/>`_
    
    | Read about `virtualenvwrapper in The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper>`_: 
    | `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io>`_ provides a set of commands which makes working with virtual environments much more pleasant.

Install **nessus file analyzer (NFA)**

.. code-block:: shell

    pip install nessus-file-analyzer

.. _nfa-upgrade:

Upgrade
#######
    
To upgrade to newer version run:

.. code-block:: shell
    
    pip install --upgrade nessus-file-analyzer
