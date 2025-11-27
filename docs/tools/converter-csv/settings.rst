:description: Settings instruction for Converter CSV.

########
Settings
########

Auto-detect separator
#####################

.. versionadded:: v0.6.0
    You can enable/disable auto-detect of separator in CSV files.

Mark checkbox :bdg-secondary-line:`Auto-detect separator` to automatically detected separators such as 
``,``, ``;``, ``tab``, ``|`` and ``:`` based on the first 5 lines. This option is enabled by default. Disable it 
to set the separator manually with Change separator option.

Change separator
################

If you don't use option to :bdg-secondary-line:`Auto-detect separator` you can click :bdg-secondary:`Change` 
button (next to **separator** filed) to change separator to one you have in your |csv| file, e.g., ``;``.

Change target directory
#######################

Click :bdg-secondary:`Change` button (next to **directory** field) to change target directory and use it for all output files.

Add suffix with current time
############################

Mark checkbox :bdg-secondary-line:`add suffix with "_YYYYMMDD_HHMMSS"` to add into each file name suffix with current time with given format.

Add suffix with custom text
###########################

Key-in custom suffix and mark checkbox :bdg-secondary-line:`add custom suffix` to add into each file name suffix with given text.