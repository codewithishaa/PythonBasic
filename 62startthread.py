#The start() method is fundamental for beginning the execution of a thread.
from threading import Thread
from time import sleep

def my_function(arg):
   for i in range(arg):
      print("child Thread running", i)
      sleep(0.5)
thread = Thread(target = my_function, args = (10, ))
thread.start()
print("thread finished...exiting")