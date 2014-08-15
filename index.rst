.. SimX documentation master file, created by
   sphinx-quickstart on Thu Aug 14 14:29:46 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**SimX**: Parallel Simulation Library for Python
====================================================

SimX is a library for developing parallel, discrete-event simulations in Python. Written in C++ and Python, SimX enables rapid development of parallel simulations entirely in Python by providing the simulation modeler with core functionality such as processes, event queuing, time advancement, domain partitioning, synchronization and message passing. 

SimX has been designed for both ease-of-use and scalability; applications built using SimX can be executed on multi-core workstations or high performance clusters and can also be easily integrated with other Python tools for scientific computing. 


Installation
------------


Pre-built packages
~~~~~~~~~~~~~~~~~~
Prebuilt packages are available for Fedora 19 and 20. First add the following repository to yum::

  > sudo yum-config-manager \ 
    --add-repo=http://download.opensuse.org/repositories/Education/Fedora_<v>/Education.repo

Replace 'v' with your Fedora release number in the above command. Then::

  > sudo yum install python-simx


Building from source
~~~~~~~~~~~~~~~~~~~~

**Step 1**: Installing Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SimX build system uses `CMake <http://www.cmake.org>`_  and Python's `setuptools <https://pypi.python.org/pypi/setuptools>`_. In addition, SimX also requires the MPICH implementation of MPI and  the Boost C++ libraries. The easiest way to install these dependencies would be to use your platform's package installer.

GNU/Linux
****************

On Fedora, one would do::
  
  sudo yum install cmake 

OS-X
*******
On OS-X, the best way to install SimX dependencies would be via `macports <http://www.macports.org>`_. After installing macports, do the following::

  sudo port install cmake boost py-setuptools
  sudo port install mpich mpich-devel 

.. sudo port select --set mpi <mpi-port-name>

.. (for mpi-port-name see on-screen messages when mpich was installed.

make sure ``/opt/local/bin`` (or whatever path macports binaries are located in) is in your PATH environment variable, and that this path is searched before ``/usr/bin`` etc. Otherwise, while building SimX, CMake will use the default Python version with OS-X leading to problems while linking.

**Step 2**: Download SimX 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


**Step 3**: Build SimX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. Contents:

.. .. toctree::
..   :maxdepth: 2


:doc:`simx-doc`

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

