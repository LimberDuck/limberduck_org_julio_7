################
Advanced reports
################

**LimberDuck NFA (nessus file analyzer)** ``v0.12.0`` and newer is able to 
generate additional advanced reports based on data extracted from specific Nessus plugins. 
These reports provide deeper insights into the Nessus scan results. 

.. .. attention::
..    As a temporary measure, if you want to use Software Enumeration report you need to install or 
..    upgrade NFA via ``pip``, check :doc:`../installation` instruction.

The advanced reports currently available are:

- :doc:`software-enumeration/index` - list of all software identified on scanned hosts along with their versions.


.. toctree::
   :maxdepth: 2
   :caption: Target file sections column list
   :hidden:
   
   software-enumeration/index

.. tip::
   Are you missing some report type? Do you have an idea for a new report? 
   Feel free to share your thoughts and suggestions via 
   `LimberDuck NFA GitHub Discussions`_,
   `LimberDuck NFA GitHub Issues`_
   or :doc:`../../../contact/index` us directly.
