:description: Settings instruction for nessus file analyzer (nfa).

########
Settings
########

Settings are divided into two tabs, separately for source files and target files, as follows.

Source files options
====================

add debug data
--------------

:bdg-secondary-line:`add debug data` - turn on this option to get additional columns for selected report 
type like source file name with path, policy name and more.

..  note::
    Text in debug's columns headers is in blue color in the target file to let you 
    quickly distinguish them from default columns.
    This option is available for all report types.

.. seealso::
    Check :doc:`target-file/index` descriptions to get more details.

filter out None results
-----------------------

:bdg-secondary-line:`filter out None results` - turn on this option to automatically filter out plugins 
results with None Risk Factor and see in the target file only these which Risk Factor 
is equal to Low, Medium, High or Critical. 

.. note::
    Plugins results with None Risk Factor are not removed from target file, to see them use 
    filter option in column named *Risk Factor*. 
    This option is available for Vulnerability report type only.

skip None results
-----------------

:bdg-secondary-line:`skip None results` - turn on this option to completely skip plugins results with 
None Risk Factor and left in the target file only these which Risk Factor is equal 
to Low, Medium, High or Critical.

.. note::
    To see plugins results with None Risk Factor in target file you need to disable 
    this option and analyse selected files again.
    This option is available for Vulnerability report type only.


Target files options
====================

Change target directory
-----------------------

:bdg-secondary:`Change` button - click to change target directory and use it for generated output files.

.. note::
    :bdg-secondary:`Change` button is placed next to target directory field.

Set source directory as target directory
----------------------------------------

:bdg-secondary-line:`set source directory as target directory` turn on this option to automatically change target directory each time when you select new source file/-s and set target directory to be the same as source file/-s directory. 
    
.. note::
    If you use *Open directory* option to open source files this directory will be taken as target directory for all files including these from subdirectories.

Add suffix with current time
----------------------------

:bdg-secondary-line:`add suffix with "_YYYYMMDD_HHMMSS"` - turn on this option to add suffix into target filename with date and time in format ``_YYYYMMDD_HHMMSS``. 

.. note::
    Take a look below this option to see example target filename received that way.

    If you already turned on :bdg-secondary-line:`add custom suffix` option, turn it off and on again to change the sequence of these two options in target file name.

Add suffix with custom text
---------------------------

:bdg-secondary-line:`add custom suffix` - turn on this option if you want to add suffix into target filename which will contain text taken from field placed on the right side from this option. 
    
.. note:: 
    Take a look below this option to see target filename example received that way.

    If you already turned on :bdg-secondary-line:`add suffix with "_YYYYMMDD_HHMMSS"` option, turn it off and on again to change the sequence of these two options in target file name.
