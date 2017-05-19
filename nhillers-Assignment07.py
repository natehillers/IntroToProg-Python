# -------------------------------------------------#
# Title: Examples using Exceptions and Pickling
#
# Name: Nathaniel Hillers
# Date:  19 May 2017
# Description: This code will briefly give examples on how to
#     use both exceptions and pickling in python
# ChangeLog:
#   ver 1.0: 19 May 2017: started
#   ver 1.1: 19 May 2017: reformatted for better viewing in blog
# # -------------------------------------------------#

# First: Exceptions

# This is a simple try/except block that asks for a number
#     then multiplies it by 7)
# If the user chooses anything but a number, it will report
#     that the user has made a mistake
# Normally without the try/except block, the code will have
#     errored-out entirely, ruining the whole script

while (True):
    try:
        chosennum = float(input("Pick any number to multiply by 7: "))
        break
    except ValueError:
        print("You didn't choose a number! ")
print("You have chosen", str(chosennum), "!\nThat multiplied by 7 equals: ", 7 * chosennum)

# Second: Pickling
print('\n')

# 'Pickling' is not a module included by default so one must import it:

import pickle

# 'Pickling' refers to a process in which objects in python
#     are turned into a stream of bits or characters so
#     they can be saved elsewhere
# 'De-Pickling' is the opposite, so pickled objects can be
#     re-loaded into python

# First we will create something to pickle, in this case a list

topicklelist = ['first', 'second', 'third', 'etc']

# Since pickling requires saving to, and loading from, a file,
#     we will need to create a file:
# Take note of the mode the file is being opened in: 'wb'.
#     The 'w' is normal write mode, but since we are writing in
#    'bits' or binary data, we need to append the 'w' with a 'b',
#    so 'write' mode is now 'write-bits' mode

picklefile = open("pickletext.txt", 'wb')

# We will now 'write' the list we want to pickle.
# In 'pickling' terms, 'dump' = writing

pickle.dump(topicklelist, picklefile)
picklefile.close()

# If there were no other code below this line, you could run
#    the above code without errors and you would have a file called
#    'picklefile' with the pickled list (topicklelist) inside.

# We will now see how to load already-pickled objects
# Again, notice how the mode we are opening the file in has
#     a 'b' for bits. So 'read' mode is now 'read-bits' mode

newpicklefile = open("pickletext.txt", "rb")
newlist = pickle.load(newpicklefile)

# Finally, print out the new list to make sure it pickled and
#     depickled' correctly
print(newlist)

# One final note: Though the file with the pickled object looks
#     like random text when a person opens and reads it,
#     it is NOT encrypted in any way. Don't think it is safe for hiding data.
