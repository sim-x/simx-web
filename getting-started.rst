Getting Started with SimX
===========================

Once you have built and installed SimX, as described in the :doc:`installation <install>` section, SimX can be used like any other Python module, inside a script or in interactive mode. For example,

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

The above code snippet simply initializes the simulation environment, and runs a dummy simulation (without any events) for 10 time units. 

Let's try and build a simple but non-trivial case that illustrates how to set up a simulation in SimX.


A HelloWorld Example
============================

The main objects in a SimX simulation application are  Entities and Services. Entities represent physical objects ( e.g. an agent) while services (which live on entities) represent the behavior of an agent. 

.. Processes represent simulated threads that execute concurrently 

Let us consider a simple ``HelloWorld``  example that consists of a  number of :class:`Person` entities and a :class:`HelloHandler` service attached to a :class:`Person` object.  In our simple set up, when a :class:`HelloHandler` service receives a :class:`Hello` message, it sends a :class:`Reply` message to the sending :class:`Person`, delivered at some specified time. 

Even though this example is highly simplified, it illustrates some of the key ideas for building a SimX application. The Python definition for the :class:`Person` entity is:

.. code-block:: python

   import simx

   class Person(simx.PyEntity):
     def __init__(self,ID,lp,entity_input):
       #do some initialization here
       self.install_service(HelloHandler,Address)


Each entity in a SimX application inherits from the :class:`PyEntity <simx.core.core.PyEntity>` class exported from SimX.  At the time of creation an entity is informed of its identity, the id of the simulation process (logical process or lp) on which it lives and any input parameters if required. 

.. The current simulation time is always available to entities (as well as services) via the \texttt{get\_now()} method.


Additional parameters are passed to the entity constructor via the :class:`entity_input` object. The :meth:`install_service <simx.pyentity_ext.install_service>` method is used to explicitly create services on an entity. While some initializations have been omitted here, the code above captures the essence of the Python class definition.

Let us also define  the two message objects, :class:`Hello` and :class:`Reply` which are quite simply:

.. code-block:: python

   class HelloMessage:
   	  def __init__(self, source_id, dest_id):
	    self.source_id = source_id
	    self.dest_id = dest_id
   
   class ReplyMessage: pass



Next consider the :class:`HelloHandler` service that lives on a :class:`Person`.

.. literalinclude:: hellohandler.py

Each service object in a SimX application inherits from the :class:`PyService <simx.core.core.PyService>` class exported from SimX. At creation time, a service is informed of its identity, the entity on which it lives  and any input parameters that have been passed in. Since a service and its entity always live in the same memory space, all the  entity functions and data members are available to a service object.

The :meth:`send_info <simx.core.core.PyService.send_info>` method referenced above is the communication work-horse of SimX and  follows the simple ``(what, when, who, where)`` paradigm. The parameters to it are:

*  object to be sent
*  the sending time (offset from current time)
*  the entity to send it to
*  The service address on the entity that will receive the message. 

Any Python object that can be pickled  can be sent and received inside through SimX.

In addition to sending, services are also capable of receiving messages.  Since the :class:`HelloHandler` service needs to receive more than one type of message, we define a Python dictionary  that hashes messagetypes to receive functions, as in:

.. code-block:: python

   #defined inside the HelloHandler class
   self.recv_function = {'HelloMessage':self.recv_HelloMessage,
                         'ReplyMessage':self.recv_ReplyMessage
   			 } 


All Python services are expected to define a :meth:`recv` function, which gets called each time a message is received at a service. Using  the dictionary as defined above, it then becomes quite straightforward to determine which of the two receive handlers defined above gets invoked.

.. code-block:: python

   #defined inside HelloHandler class
   def recv(self, msg):
       msg_type = msg.__class__.__name__
       self.recv_function[msg_type]( msg )


Finally, we put this all together and drive the simulation through a driver script

.. literalinclude:: helloworld.py

To run this example, simply type::

  > python helloworld.py

The output should look something like::

  MPI thread support: MPI_THREAD_MULTIPLE
  [ TOTAL MACHINES: 1 ]
  [ TOTAL PARALLELISM: 1 ]
  [ TOTAL TIMELINES: 1 ]
  [ TOTAL EVENTS: 2047 ]
  [ INIT TIME: 0.128268 (s) ]
  [ RUN TIME: 0.094685 (s) ]
  [ EVENT RATE: 9181.31 (evts/s) ]


Going Parallel with HelloWorld
-------------------------------

To parallelize the simulation, simply invoke the ``helloworld`` script via ``mpirun``. For a 4 processor run, do the following::

  mpirun -np 4 python helloworld.py

That's all there is to parallelizing -- the same simulation script works in both a sequential and parallel setting. SimX automatically partitions the domain and assigns entities and services to MPI processes and performs the needed synchronization.

The above command produces the following output::

  MPI thread support: MPI_THREAD_MULTIPLE
  MPI thread support: MPI_THREAD_MULTIPLE
  MPI thread support: MPI_THREAD_MULTIPLE
  MPI thread support: MPI_THREAD_MULTIPLE
  [ TOTAL MACHINES: 4 ]
  [ TOTAL PARALLELISM: 4 ]
  [ TRAINING LENGTH: 5.1e-08 (s) ]
  [ TOTAL TIMELINES: 4 ]
  [ TOTAL EVENTS: 2153 ]
  [ EPOCH LENGTH: 9.2e+09 (s) ]
  [ INIT TIME: 0.076896 (s) ]
  [ RUN TIME: 0.200104 (s) ]
  [ EVENT RATE: 7772.56 (evts/s) ]


Note that the 4-processor MPI run above actually ran slower than the single processor run. Welcome to the world of parallel simulations! Parallelism induces overhead since processes have to synchronize periodically, and the synchronization frequency is determined by the value supplied to the :meth:`set_min_delay <simx.config.set_min_delay>` method. The benefits of parallelism usually become apparent only for significantly large workloads; thus, a maxim to keep in mind for parallel simulations is:

.. note::

 In a parallel simulation, always use only the minimum amount of parallelism needed


Determining the right amount of parallelism, beyond which one experiences performance drops with increasing parallelism, is of course something of an art.


Further Reference: The SimX API Docs
-----------------------------------------

The ``HelloWorld`` example above touched upon only a very small subset of SimX functionality. More examples can be found in the SimX installation directory under the ``examples`` sub-directory. Refer to the :doc:`SimX API documentation <simx-doc>` for a complete list of available functionality.


