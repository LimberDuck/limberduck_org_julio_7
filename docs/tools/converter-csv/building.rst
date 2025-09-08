:description: Building instruction for Converter CSV.

########
Building
########

.. hint::

    Since ``v0.4.1`` Converter CSV comes with pre-built binaries for Windows, 
    Linux and macOS. You can download the latest version from 
    `GitHub Releases <https://github.com/LimberDuck/converter-csv/releases>`_ page. 
    You can still install it with ``pip`` and build it from source code if you want.

.. note::
   This step is optional.
   
You can build an executable file for **Converter CSV**.

.. tabs::

  .. group-tab:: Windows

   1. Clone **Converter CSV** repository using below command in Git Bash:
   
      .. code-block:: shell
   
            git clone https://github.com/LimberDuck/converter-csv.git
   
   2. Install requirements using below command
   
      .. code-block:: shell
   
            pip install -r .\requirements.txt
   
   3. Run **Converter CSV** using below command
   
      .. code-block:: shell
   
            python -m converter_csv
   
   4. Upgrade setuptools using below command
   
      .. code-block:: shell
   
            pip install --upgrade setuptools
   
   5. Install PyInstaller
   
      .. code-block:: shell
   
            pip install PyInstaller
   
   6. Build your own executable file using below command
   
      .. code-block:: shell
   
            pyinstaller --onefile --windowed --version-file=.\version.rc --icon=.\icons\LimberDuck-Converter-CSV.ico  --name "LimberDuck Converter CSV" converter_csv\__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``LimberDuck Converter CSV.exe``
   
  .. group-tab:: Linux (Ubuntu)

   1. Clone **Converter CSV** repository using below command
   
      .. code-block:: bash
   
           git clone https://github.com/LimberDuck/converter-csv.git
   
   2. Install requirements using below command
   
      .. code-block:: bash
   
           pip install -r ./requirements.txt
   
   3. Run **Converter CSV** using below command
   
      .. code-block:: bash
   
           python -m converter_csv
   
   4. Upgrade setuptools using below command
   
      .. code-block:: bash
   
           pip install --upgrade setuptools
   
   5. Install PyInstaller
   
      .. code-block:: bash
   
           pip install PyInstaller
   
   6. Build your own executable file using below command
   
      .. code-block:: bash
   
           ~/.local/bin/pyinstaller --onefile --windowed --icon=./icons/LimberDuck-Converter-CSV.ico --name "LimberDuck-Converter-CSV" converter_csv/__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``LimberDuck-Converter-CSV``.

  .. group-tab:: macOS

   1. Clone **Converter CSV** repository using below command
   
      .. code-block:: bash
   
           git clone https://github.com/LimberDuck/converter-csv.git
   
   2. Install requirements using below command
   
      .. code-block:: bash
   
           pip3.6 install -r ./requirements.txt
   
   3. Run **Converter CSV** using below command
   
      .. code-block:: bash
   
           python -m converter-csv
   
   4. Upgrade setuptools using below command
   
      .. code-block:: bash
   
           pip install --upgrade setuptools
   
   5. Install PyInstaller
   
      .. code-block:: bash
   
           pip install PyInstaller
   
   6. Build your own executable file using below command
   
      .. code-block:: bash
           
           pyinstaller --windowed --icon=./icons/LimberDuck-Converter-CSV.ico --name "LimberDuck Converter CSV" converter_csv/__main__.py
   
   7. Go to ``dist`` catalog to find executable file ``LimberDuck Converter CSV.app``.
   