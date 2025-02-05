:description: Running instruction for Converter CSV.

Running
=======

Once you have Converter CSV installed you can run it in Terminal with command:

.. code-block:: shell

   converter-csv

.. attention::

    Remember to open your Python virtual environment first, if you decided to use it. 
    If you use `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io>`_, 
    mentioned in the :doc:`installation` instruction, 
    you can do it with the command ``workon <name_of_your_virtualenvironment>``. 
    To exit your Python virtual environment, use the command ``deactivate``.

.. tip::
    
    Optionally for Linux and macOS run with ``&`` at the end to start the process in the background.
    
    .. code-block:: shell
        
        converter-csv&

Make a shortcut to **Converter CSV** to run it even faster.

.. tabs::

  .. group-tab:: Windows

   1. Run ``where`` command in ``cmd`` to get ``your_path_to_converter-csv``

      .. code-block:: shell
        
            where converter-csv.exe
   2. Copy path return in previous command.
   3. Go, e.g., to Desktop.
   4. Right click on Desktop and choose ``New > Shortcut``.
   5. Paste returned path.
   6. Click ``Next``.
   7. Click ``Finish``.

  .. group-tab:: Linux (Ubuntu) / macOS

   1. Run ``which`` command in Terminal to get ``your_path_to_converter-csv``
    
      .. code-block:: shell
        
            which converter-csv

   2. Run ``ln`` command in Terminal with path return in previous command to create a link:
    
      .. code-block:: shell

            ln -s your_path_to_converter-csv ~/Desktop/

   .. error::
   
       If you have installed **Converter CSV** on Ubuntu without 
       python virtual environment, and see below error:
   
       .. code-block:: shell
   
           ~$ converter-csv
           converter-csv: command not found
   
   
       Add below to ``~/.bashrc`` to fix it:
   
       .. code-block:: shell
   
           # set PATH so it includes user's private ~/.local/bin if it exists
           if [ -d "$HOME/.local/bin" ] ; then
               PATH="$HOME/.local/bin:$PATH"
           fi

   .. error::

       If you run **Converter CSV** and see below error:
   
       .. code-block:: shell
   
           ~$ converter-csv
           qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
           This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
   
           Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.
   
           Aborted (core dumped)
   
   
       Run below to fix it:
   
       .. code-block:: shell
   
           sudo apt-get install --reinstall libxcb-xinerama0

  .. group-tab:: macOS

   1. Run ``which`` command in Terminal to get ``your_path_to_converter-csv``
    
      .. code-block:: shell
        
            which converter-csv
    
   2. Open ``bin`` folder where ``converter-csv`` is located.

   3. Right click on ``converter-csv`` and choose an option ``Make alias``.
    
   4. Move your alias, e.g., to Desktop.

