:description: Running instruction for nessus file analyzer (NFA).

#######
Running
#######

.. hint::

    Since ``v0.10.0`` nessus file analyzer (NFA) comes with pre-built binaries for Windows, 
    Linux and macOS. You can download the latest version from 
    `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page. 
    You can still install it with ``pip`` and build it from source code if you want.

If you decided to download pre-build version follow :ref:`build-version-limberduck-nfa` instruction. 
If you decided to install from |PyPI| follow :ref:`source-version-limberduck-nfa` instruction.

.. _build-version-limberduck-nfa:

Build version
#############


.. tabs::

  .. group-tab:: Windows

    1. Go to `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page.
    2. Select and download from the Assets list the ZIP archive with ``-windows`` suffix.
    3. In the Terminal run, e.g., below command to verify the checksum of downloaded file:
    
       .. code-block:: powershell
       
            Get-FileHash .\LimberDuck-NFA-vX.Y.Z-windows.zip -Algorithm SHA256

       .. important::
       
            The output should match the checksum provided in the `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page!

    4. Unzip the archive.
    5. Go to unzipped folder and click on ``LimberDuck NFA.exe`` file to start **NFA**.
    6. If you see Windows message protecting from opening, click on **More info** and then click on **Run anyway**.
   
  .. group-tab:: Linux (Ubuntu)

    1. Go to `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page.
    2. Select and download from the Assets list the ZIP archive with ``-linux`` suffix.
    3. In the Terminal run, e.g., below command to verify the checksum of downloaded file:

       .. code-block:: shell
       
            sha256sum LimberDuck-NFA-vX.Y.Z-macos-arm64.zip

       .. important::
       
            The output should match the checksum provided in the `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page!
    4. Unzip the archive.
    5. Go to unzipped folder and click on ``LimberDuck-NFA`` file to start **NFA**.

    .. error::

        If you run **NFA** and window does not open, go to Terminal and run ``LimberDuck-NFA``, if you see below error:

        .. code-block:: shell

            ~$ LimberDuck-NFA
            qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
            This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

            Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.

            Aborted (core dumped)


        Run below to fix it:

        .. code-block:: shell

            sudo apt-get install --reinstall libxcb-xinerama0

        Click on ``LimberDuck-NFA`` file again to start **NFA**.

  .. group-tab:: macOS

    1. Go to `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page.
    2. Select and download from the Assets list the ZIP archive with ``-macos-arm64`` suffix if you have MacBook with Apple Silicon, if Intel based choose ``-macos``.
    3. In the Terminal run, e.g., below command to verify the checksum of downloaded file:

       .. code-block:: shell
       
            sha256sum LimberDuck-NFA-vX.Y.Z-macos-arm64.zip

       .. important::
       
            The output should match the checksum provided in the `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page!
    4. Unzip the archive.
    5. Go to unzipped folder and run ``LimberDuck NFA.app`` file to start **NFA**.
    6. If you see macOS message protecting from opening, open Terminal and run below command:

       .. code-block:: shell
       
            xattr -dr com.apple.quarantine LimberDuck\ NFA.app

    7. Click on ``LimberDuck NFA.app`` file again to start **NFA**.


.. _source-version-limberduck-nfa:

Source version
##############

Once you have **nessus file analyzer (NFA)** installed you can run it in Terminal with command:

.. code-block:: shell

    nessus-file-analyzer

.. attention::

    Remember to open your Python virtual environment first, if you decided to use it. 
    If you use `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io>`_, 
    mentioned in the :doc:`installation` instruction, 
    you can do it with the command ``workon <name_of_your_virtualenvironment>``. 
    To exit your Python virtual environment, use the command ``deactivate``.

.. tip::
    
    Optionally for Linux and macOS run with ``&`` at the end to start the process in the background.
    
    .. code-block:: shell
        
        nessus-file-analyzer&

Make a shortcut to **nessus file analyzer (NFA)** to run it even faster.

.. tabs::

  .. group-tab:: Windows

   1. Run ``where`` command in ``cmd`` to get ``your_path_to_nessus-file-analyzer``

      .. code-block:: shell
        
            where nessus-file-analyzer.exe
   2. Copy path return in previous command.
   3. Go, e.g., to Desktop.
   4. Right click on Desktop and choose ``New > Shortcut``.
   5. Paste returned path.
   6. Click ``Next``.
   7. Click ``Finish``.

  .. group-tab:: Linux (Ubuntu)

   1. Run ``which`` command in Terminal to get ``your_path_to_nessus-file-analyzer``
    
      .. code-block:: shell
        
            which nessus-file-analyzer

   2. Run ``ln`` command in Terminal with path return in previous command to create a link:
    
      .. code-block:: shell

            ln -s your_path_to_nessus-file-analyzer ~/Desktop/

   .. error::
   
       If you have installed **nessus file analyzer (NFA)** on Ubuntu without 
       python virtual environment, and see below error:
   
       .. code-block:: shell
   
           ~$ nessus-file-analyzer
           nessus-file-analyzer: command not found
   
   
       Add below to ``~/.bashrc`` to fix it:
   
       .. code-block:: shell
   
           # set PATH so it includes user's private ~/.local/bin if it exists
           if [ -d "$HOME/.local/bin" ] ; then
               PATH="$HOME/.local/bin:$PATH"
           fi

   .. error::

       If you run **nessus file analyzer (NFA)** and see below error:
   
       .. code-block:: shell
   
           ~$ nessus-file-analyzer
           qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
           This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
   
           Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl, xcb.
   
           Aborted (core dumped)
   
   
       Run below to fix it:
   
       .. code-block:: shell
   
           sudo apt-get install --reinstall libxcb-xinerama0

  .. group-tab:: macOS

   1. Run ``which`` command in Terminal to get ``your_path_to_nessus-file-analyzer``
    
      .. code-block:: shell
        
            which nessus-file-analyzer
    
   2. Open ``bin`` folder where ``nessus-file-analyzer`` is located.

   3. Right click on ``nessus-file-analyzer`` and choose an option ``Make alias``.
    
   4. Move your alias, e.g., to Desktop.

