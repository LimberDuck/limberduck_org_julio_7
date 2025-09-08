:description: Running instruction for Converter CSV.

#######
Running
#######

.. hint::

    Since ``v0.4.1`` Converter CSV comes with pre-built binaries for Windows, Linux and macOS. You can download the latest version from 
    `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page. 
    You can still install it with ``pip`` and build it from source code if you want.

If you decided to download pre-build version follow :ref:`build-version-limberduck-converter-csv` instruction. 
If you decided to install from |PyPI| follow :ref:`source-version-limberduck-converter-csv` instruction.

.. _build-version-limberduck-converter-csv:

Build version
#############

.. tabs::

  .. group-tab:: Windows

    1. Go to `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page.
    2. Select and download from the Assets list the ZIP archive with ``-windows`` suffix.
    3. In the Terminal run, e.g., below command to verify the checksum of downloaded file:
    
       .. code-block:: powershell
       
            Get-FileHash .\LimberDuck-Converter-CSV-vX.Y.Z-windows.zip -Algorithm SHA256

       .. important::
       
            The output should match the checksum provided in the `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page!

    4. Unzip the archive.
    5. Go to unzipped folder and click on ``LimberDuck Converter CSV.exe`` file to start **Converter CSV**.
    6. If you see Windows message protecting from opening, click on **More info** and then click on **Run anyway**.
   
  .. group-tab:: Linux (Ubuntu)

    1. Go to `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page.
    2. Select and download from the Assets list the ZIP archive with ``-linux`` suffix.
    3. In the Terminal run, e.g., below command to verify the checksum of downloaded file:

       .. code-block:: shell
       
            sha256sum LimberDuck-Converter-CSV-vX.Y.Z-macos-arm64.zip

       .. important::
       
            The output should match the checksum provided in the `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page!
    4. Unzip the archive.
    5. Go to unzipped folder and click on ``LimberDuck-Converter-CSV`` file to start **Converter CSV**.

    .. error::

        If you run **Converter CSV** and window does not open, go to Terminal and run ``LimberDuck-Converter-CSV``, if you see below error:

        .. code-block:: shell

            ~$ LimberDuck-Converter-CSV
            qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
            This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

            Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

            Aborted (core dumped)


        Run below to fix it:

        .. code-block:: shell

            sudo apt-get install --reinstall libxcb-xinerama0

        Click on ``LimberDuck-Converter-CSV`` file again to start **Converter CSV**.

  .. group-tab:: macOS

    1. Go to `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page.
    2. Select and download from the Assets list the ZIP archive with ``-macos-arm64`` suffix if you have MacBook with Apple Silicon, if Intel based choose ``-macos``.
    3. In the Terminal run, e.g., below command to verify the checksum of downloaded file:

       .. code-block:: shell
       
            sha256sum LimberDuck-Converter-CSV-vX.Y.Z-macos-arm64.zip

       .. important::
       
            The output should match the checksum provided in the `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page!
    4. Unzip the archive.
    5. Go to unzipped folder and run ``LimberDuck Converter CSV.app`` file to start **Converter CSV**.
    6. If you see macOS message protecting from opening, open Terminal and run below command:

       .. code-block:: shell
       
            xattr -dr com.apple.quarantine LimberDuck\ Converter\ CSV.app

    7. Click on ``LimberDuck Converter CSV.app`` file again to start **Converter CSV**.

.. _source-version-limberduck-converter-csv:

Source version
##############

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

  .. group-tab:: Linux (Ubuntu)

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

