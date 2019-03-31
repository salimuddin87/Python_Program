* The threading module exposes all the methods of the thread module and provides some additional methods −
      * threading.activeCount() − Returns the number of thread objects that are active.
      * threading.currentThread() − Returns the number of thread objects in the caller's thread control.
      * threading.enumerate() − Returns a list of all thread objects that are currently active.

* In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −
      * run() − The run() method is the entry point for a thread.
      * start() − The start() method starts a thread by calling the run method.
      * join([time]) − The join() waits for threads to terminate.
      * isAlive() − The isAlive() method checks whether a thread is still executing.
      * getName() − The getName() method returns the name of a thread.
      * setName() − The setName() method sets the name of a thread.
