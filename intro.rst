Introduction
=============

SimX is a generic library for developing parallel, discrete event simulations in Python for simulating large, complex systems,  designed for both scalability and ease of use. Often while developing parallel simulations, the simulation developer has to take into account issues such as synchronization, distributed message passing and object serialization, to name a few; these tasks often involve steep learning curves and considerable software engineering expertise. 

SimX has been designed with these issues in mind: the main goal was to enable domain researchers to rapidly develop simulation applications and deploy it on clusters without having to get bogged down by the intricacies of parallel programming, managing MPI communication or worry about issues such as load balancing.

For scalability and performance, the core of SimX is written in C++, providing it with speed for frequently used functionality such as event-queueing, time advancement, domain partitioning and synchronization. APIs needed to develop a simulation application are exported to Python from C++; these along with Python wrappers in SimX enable application developers to program entirely in Python. 

Message passing uses the object serialization facility already present in Python via the fast `cPickles <https://docs.python.org/2.7/library/pickle.html#module-cPickle>`_ serialization library in combination with `MPI <http://mpich.org>`_. Any arbitrary Python object that can be serialized (or pickled, as it known in Python parlance) can be sent and received between simulation processes.

SimX also supports process oriented simulation, with the facility of suspending an executing simulated process and re-entering at the point of suspension. This is implemented using the Python `greenlets <http://greenlet.readthedocs.org/en/latest/>`_  module that can be used to simuate a large number of concurrent processes with very little overhead. A process oriented often greatly simplify the implementation of simulation models, especially those used for computer systems modeling.

While the flexibility of Python comes with a performance cost, the implementation of the core functionality in C++ provides a reasonable trade- off between ease-of-use and performance. For situations where performance is an over-riding concern, computationally intensive parts of the program can be re-written in pure C++. In fact the entire simulation application itself can be written in C++ as SimX allows for applications to be pure Python, a Python/C++ hybrid or even pure C++.

* Further Reading: *Sunil Thulasidasan, Lukas Kroc, Stephan Eidenbenz*, **Developing Parallel Discrete Event Simulations in Python: First Results and User Experiences with the SimX Library**, Proceedings of the 4th International Conference Simulation and Modeling Methodologies, Technologies and Applications (SIMULTECH 2014), Vienna, Austria `[PDF] <http://public.lanl.gov/sunil/pubs/simx.pdf>`_
