import threading
from safe_printer import Variables

# a variable to break the while loop to stop safe printer when its done
s = 0

def info():
    """
    Made by SaN

    i was making a project so i was using many prints and the normal print() function in python it will be buggy
    so i decided to make a safe printer to not get any more bugs.
    yeah there is chance to get buggy prints but it will rarely happend.
    i will make many more projects that can fix bugs in python
    i tried many safe printing but they didn't realy work

    Yeak i know thats a simple code but its like an idea for you to make good projects! without print bugs.
    Yeah maybe that's an easy code for you but maybe its's not for other people, Because there is many people that really need this code, For example me, Before this idea i was looking everywhere just to make a safe printer but i really dont find good one.

    - This safe printer is slower than normal python print() function. 

    Thank you for using my safe printer! <3 
    """

def start():
    """
    Creating thread for safe printer

    to print something, just try:
    -> sprint("The text that you want print!")
    - You can use colors in the text too! it will print anything that you will add to Variables.printing
    For more informations check info() function description.
    """
    threading.Thread(target=printer).start() # creating a thread to run the safe printer, without breaking any other codes.

def stop():
    """
    A function to stop the thread for safe printer
    """
    global s
    s = s + 1
    return

def printer():
    """
    A function to print texts that you add to Variables.printing
    When you use: sprint("Hello world!") , it will print the text without bugs
    - Note: Please do not call this function! only call start() to start the thread! and to print something just try sprint("text")
    For more informations check info() function description.
    """
    global s
    while s == 0:
        if len(Variables.printing) == 0: # it will skip if there is no more texts or there isn't any text to print.
            pass
        else: # if it detect a text in the list it will start printing it.
            text = Variables.printing[0]
            print(text)
            Variables.printing.remove(text) # removing the text from the list to not print it again!

def sprint(text):
    """
    You can use this function to print the text that you want. 
    """
    Variables.printing.append(text)
    return
