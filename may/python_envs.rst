


Introduction
==============

This is a guideline for running Python, creating a virtual environment
for the tutorial.



Running Python
==============

Installation
---------------

To check if Python is installed, run the following from a terminal::

  $ python3 --version


Otherwise, install Python 3 from the website [#]_.

.. [#] http://python.org

Invoking Python
---------------

The Python executable will behave differently depending on the command line options you give it:

* Start the Python REPL::

   $ python3

* Execute the ``file.py`` file::

    $ python3 file.py

* Execute the ``file.py`` file, and drop into REPL with namespace of ``file.py``::

   $ python3 -i file.py

* Execute the ``json/tool.py`` module::

   $ python3 -m json.tool

* Execute ``"print('hi')"`` ::

    $ python3 -c "print('hi')"

REPL
----

* Use the ``help`` function to read the documentation for a module/class/function. As a standalone invocation,
  you enter the help system and can explore various topics.
* Use the ``dir`` function to list contents of the namespace, or attributes of an object if you pass one in.

.. note::

  The majority of code in this book is written as if it were executed in a REPL. If you
  are typing it in, ignore the primary and secondary prompts (``>>>`` and ``...``).


Environments
================

Python 3 includes the ``venv`` module for creating a sandbox for your project or a *virtual environment*.

To create an environment on Unix systems, run::

  $ python3 -m venv /path/to/env

On Windows, run::

  c:\> c:\Python36\python -m venv c:\path\to\env

To enter or *activate* the environment on Unix, run::

  $ source /path/to/env/bin/activate

On Windows, run::

  c:\> c:\path\to\env\Scripts\activate.bat

Your prompt should have the name of the active virtual environment in parentheses.
To *deactivate* an environment on both platforms, just run the following::

  (env) $ deactivate

Installing Packages
-------------------

You should now have a ``pip`` executable, that will install a package from PyPI [#]_  into your virtual environment::

  (env) $ pip install django

.. [#] https://pypi.python.org/pypi

To uninstall a package run::

  (env) $ pip uninstall django

If you are having issues installing a package, you might want to look into alternative Python distributions such as Anaconda [#]_ that have prepackaged many harder to install packages.

.. [#] https://docs.continuum.io/anaconda/

Conda
-----

Even though Conda [#]_ is not part of Python, it is a common tool for managing it. Here are the Conda equivalents of virtual environments and pip. The commands are the same on Windows and Unix.

To create a Conda environment, run::

  $ conda create --name ENV_NAME python

To list Conda environments, run::

  $ conda info --envs

To activate a Conda environment, run::

  $ conda activate ENV_NAME

To deactivate a Conda environment, run::

  $ conda deactivate

To install a package, run::

  $ conda install django

.. [#] https://conda.io
