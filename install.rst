Installation
------------
There are a couple of different ways to install SimX, either via pre-built packages (available for Fedora Linux) or building from source. For source-builds, we strongly recommend installing  the software prerequisites using a package manager for your system.


Pre-built packages for GNU/Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prebuilt packages are available for recent versions of Fedora (19 and 20). First add the following repository to yum::

  > sudo yum-config-manager \ 
    --add-repo=http://download.opensuse.org/repositories/Education/Fedora_<v>/Education.repo

Replace 'v' with your Fedora release number in the above command. Then::

  > sudo yum install python-simx

We are working on packaging for other distributions; in the meantime, please follow the instructions for building from source below.

Building from source
~~~~~~~~~~~~~~~~~~~~
Building from sources is a two-step process: installing the SimX dependencies and then building the SimX sources. 


Installing Software Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The software packages  required prior to building SimX are

* `CMake <http://www.cmake.org>`_
*  Python's `setuptools <https://pypi.python.org/pypi/setuptools>`_.
*  `Boost C++ Libraries <http://www.boost.org>`_
*  `MPICH <http://mpich.org>`_ implementation of MPI

Unless you're a glutton for punishment, install the above packages via a package manager. See instructions below for your system.

GNU/Linux
***********
For installing software dependencies on Fedora, one would do something like::
  
  sudo yum install cmake python-devel mpich2-devel boost-devel

On Ubuntu, this would be something like::
  
  sudo apt-get install cmake python-dev boost-devel mpich2 mpich2-dev 

Depending on your specific distribution, you might have to use the name ``mpich`` instead of ``mpich2`` in the above commands. Once you  have succesfully installed the prerequisite packages, proceed to :ref:`installation<install>`.
 
..
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   The SimX build system uses `CMake <http://www.cmake.org>`_  and Python's `setuptools <https://pypi.python.org/pypi/setuptools>`_. In addition, SimX also requires the MPICH implementation of MPI and  the Boost C++ libraries. The easiest way to install these dependencies would be to use your platform's package installer.



OS X
******
Consistency is the key to a pain-free installation on OS X (do not be discouraged by this; SimX works quite nicely on OS X. We know this because most of the SimX delopment was done on a macbook pro) Specifically, the dynamic Python linkages for SimX, Boost and the Python interpretet have all got to be against the same Python library. The following instructions will achieve just that.

First install `macports <http://www.macports.org>`_, a package manager for OS X. Then, do the following::

  sudo port install cmake boost py-setuptools
  sudo port install mpich mpich-devel 

If you already have another version of MPI installed, make sure that the macports MPICH installtion is made active by typing::

  sudo port select --set mpi <mpi-port-name>

For ``<mpi-port-name>`` see the macports on-screen message when mpich was installed.

Also, make sure that the location of port binaries (typically ``/opt/local/bin``) is in your PATH environment variable, and that this path is searched before ``/usr/bin`` etc. Otherwise, while building SimX, CMake will use the default Python version bundled with OS-X leading to problems while linking.

Once you  have succesfully installed the prerequisite packages, proceed to :ref:`installation<install>`.
 

.. _install:

Building and Installing Simx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First download sources

