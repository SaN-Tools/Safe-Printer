from safe_printer.Printer import *
from safe_printer.Variables import *

# An example code to show you how to use the safe printer.

# Before doing anything you will need to call the start function:

start() # without calling this function it won't print anything.

for i in range(1000):
    sprint(f"Counter: {i}") # now you can check your console it print the text that you add!

# now to stop the safe printer thread you need call this function: stop() you can use any method that you want but i liked to use while method to call the stop function
while len(printing) > 0:
    pass
stop()


# Do not use this method to stop the function:
"""

if len(printing) == 0:
    stop()

""" # If you try to use this method it won't stop the safe printer thread because safe printer is printing the text and remove it one by one


# - Note: if you select a text in the console and after that you unselect printer start few bugs(1-4 depends on how long you select it) because selecting a text in the console will stop the printing, and when you unselect it will print all in a short time and it will make the printer to bug.
