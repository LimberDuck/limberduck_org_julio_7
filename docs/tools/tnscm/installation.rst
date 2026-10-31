:description: Installation instruction for TNSCM.

Installation
============


.. note::

    It's advisable to use python virtual environment for below instructions. Read more about python virtual environment in `The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/>`_
    
    | Read about `virtualenvwrapper in The Hitchhiker’s Guide to Python! <https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper>`_:
    | `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io>`_ provides a set of commands which makes working with virtual environments much more pleasant.

.. important::

    **TNSCM** requires Python 3.11 or newer.

    .. versionchanged:: v0.1.0

       Python 3.10 is no longer supported.

Install **TNSCM**
    
.. code-block:: shell
    
    pip install tnscm

.. _tnscm-upgrade:

Upgrade
#######
    
To upgrade to newer version run:

.. code-block:: shell
    
    pip install --upgrade tnscm

Check if you are using the latest version:

.. code-block:: shell

    tnscm --update-check