:description: Building instruction for nessus file analyzer (NFA).

########
Building
########

.. hint::

    Since ``v0.10.0`` nessus file analyzer (NFA) comes with pre-built binaries for Windows, 
    Linux and macOS. You can download the latest version from 
    `GitHub Releases <https://github.com/LimberDuck/nessus-file-analyzer/releases>`_ page. 
    You can still install it with ``pip`` and build it from source code if you want.

.. note::
   This step is optional.
   
You can build an executable file for **nessus file analyzer (NFA)**.

.. tabs::

  .. group-tab:: Windows

   1. Clone **nessus file analyzer** repository using below command in Git Bash:
   
      .. code-block:: shell
   
            git clone https://github.com/LimberDuck/nessus-file-analyzer.git
   
   2. Install requirements using below command
   
      .. code-block:: shell
   
            pip install -r .\requirements.txt
   
   3. Run **nessus file analyzer** using below command
   
      .. code-block:: shell
   
            python -m nessus_file_analyzer
   
   4. Upgrade setuptools using below command
   
      .. code-block:: shell
   
            pip install --upgrade setuptools
   
   5. Install PyInstaller
   
      .. code-block:: shell
   
            pip install PyInstaller
   
   6. Build your own executable file using below command
   
      .. code-block:: shell
   
            pyinstaller --onefile --windowed --version-file=.\version.rc --icon=.\icons\LimberDuck-NFA.ico  --name "LimberDuck NFA" nessus_file_analyzer\__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``LimberDuck NFA.exe``
   
  .. group-tab:: Linux (Ubuntu)

   1. Clone **nessus file analyzer** repository using below command
   
      .. code-block:: bash
   
           git clone https://github.com/LimberDuck/nessus-file-analyzer.git
   
   2. Install requirements using below command
   
      .. code-block:: bash
   
           pip install -r ./requirements.txt
   
   3. Run **nessus file analyzer** using below command
   
      .. code-block:: bash
   
           python -m nessus_file_analyzer
   
   4. Upgrade setuptools using below command
   
      .. code-block:: bash
   
           pip install --upgrade setuptools
   
   5. Install PyInstaller
   
      .. code-block:: bash
   
           pip install PyInstaller
   
   6. Build your own executable file using below command
   
      .. code-block:: bash
   
           ~/.local/bin/pyinstaller --onefile --windowed --icon=./icons/LimberDuck-NFA.ico --name "LimberDuck-NFA" nessus_file_analyzer/__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``LimberDuck-NFA``.

  .. group-tab:: macOS

   1. Clone **nessus file analyzer** repository using below command
   
      .. code-block:: bash
   
           git clone https://github.com/LimberDuck/nessus-file-analyzer.git
   
   2. Install requirements using below command
   
      .. code-block:: bash
   
           pip3.6 install -r ./requirements.txt
   
   3. Run **nessus file analyzer** using below command
   
      .. code-block:: bash
   
           python -m nessus_file_analyzer
   
   4. Upgrade setuptools using below command
   
      .. code-block:: bash
   
           pip install --upgrade setuptools
   
   5. Install PyInstaller
   
      .. code-block:: bash
   
           pip install PyInstaller
   
   6. Build your own executable file using below command
   
      .. code-block:: bash
           
           pyinstaller --onefile --windowed --icon=./icons/LimberDuck-NFA.ico --name "LimberDuck NFA" nessus_file_analyzer/__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``LimberDuck NFA.app``.
   