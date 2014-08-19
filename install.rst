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


**Step 1** Install Software Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The software packages  required prior to building SimX are

* `CMake <http://www.cmake.org>`_
*  Python's `setuptools <https://pypi.python.org/pypi/setuptools>`_.
*  `Boost C++ Libraries <http://www.boost.org>`_
*  `MPICH <http://mpich.org>`_ implementation of MPI (for parallel simulations. See :ref:`the note on MPI<mpi>` for installing without parallel support)

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

**Step 2** Build and Install SimX 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After installing the required packages, as described above, The build process is the same for any UNIX like platform (GNU/Linux, OS-X etc.) First download the the SimX source files, via one of the following methods:

* Download the latest source archive from the `SimX github site <https://github.com/sim-x/simx/archive/master.zip>`_

* Download a stable tarball from the `Python CheeseShop <https://pypi.python.org/pypi/simx/0.2>`_

* Checkout the source tree via anonymous git, using::

     git clone https://github.com/sim-x/simx.git

After extracting the tarball, change to the source root directory and type::

     python setup.py install

This will build SimX and install it to the appropriate Python site-packages directory. In the process, it will also automatically download and install `greenlets <https://pypi.python.org/pypi/greenlet>`_, a required module for simulating processes in SimX.

By default, SimX is installed into the system Python directories. To install into the user directory instead, type::

  python setup.py install --user

This will build and install SimX under the user's home directory. Python
2.6 or higher is required for user mode installation.


.. _mpi:

Bulding without MPI
********************

SimX uses MPI for message passing and synchronization in parallel simulations, specifically the MPICH implementation of MPI. If you do not wish to enable parallel simulations, SimX can be installed without parallel support. To do this, type::

   python setup.py build --without-mpi
   python setup.py install 


Other Options
*****************

By default SimX is built with the bundled `miniSSF library <http://www.primessf.net/minissf>`_ for distributed synchronization. SimX can also be built with its own native message passing library. For this, do the following::

 python setup.py build --without-ssf
 python setup.py install

This alternative build requires MPI (even for non-parallel builds); it also requires that your MPI installation  be fully multi-threaded (on the otherhand, SSF can run on both single and multi-threaded MPI). Depending on your computational setup and simulation needs, one or the other might perform better.  

 .. note::

  If disabling MPI, SimX will use miniSSF.


Once the above steps are completed, SimX is ready to be used like any other Python module.

.. code-block:: python

   >>> import simx
   >>> simx.init()
   MPI thread support: MPI_THREAD_MULTIPLE
   [ TOTAL MACHINES: 1 ]
   [ TOTAL PARALLELISM: 1 ]
   >>> simx.set_end_time(10)
   >>> simx.run()
   [ TOTAL TIMELINES: 0 ]
   [ TOTAL EVENTS: 0 ]
   [ INIT TIME: 7.49801 (s) ]
   [ RUN TIME: 1.7e-05 (s) ]
   [ EVENT RATE: 0 (evts/s) ]
    





