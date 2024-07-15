:description: Building instruction for nessus file analyzer (nfa).

********
Building
********

.. note::
   This step is optional.
   
You can build an executable file for **nessus file analyzer** (``nfa``).

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
   
            pyinstaller --onefile --windowed --version-file=.\version.rc --icon=.\icons\LimberDuck-nessus-file-analyzer.ico  --name nessus-file-analyzer nessus_file_analyzer\__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``nessus-file-analyzer.exe``
   
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
   
           ~/.local/bin/pyinstaller --onefile --windowed --icon=./icons/LimberDuck-nessus-file-analyzer.ico --name nessus-file-analyzer nessus_file_analyzer\__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``nessus-file-analyzer``.

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
           
           pyinstaller --onefile --windowed --icon=./icons/LimberDuck-nessus-file-analyzer.ico --name nessus-file-analyzer nessus_file_analyzer\__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``nessus-file-analyzer``.
   