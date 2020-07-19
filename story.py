# File name: story.py
# Programming Language: Python 2.7
# Author: Radoslav Bourov
# Program Describtion: This program creates a story 
# by first prompting the user for several keywords in 
# the form of questions. 
# The questiones are as follows:
# 1.)  The name of a favorite animal (keyword1)
# 2.)  The name of a good friend (keyword2)
# 3.)  The name of a one-word fun activity (keyword3)
# 4.)  The name of a favorite villain (keyword4)
# 5.)  The name of a one-word non-fun activity (keyword5)

# String type variables are initialized
keyword1 = str()
keyword2 = str()
keyword3 = str()
keyword4 = str()
keyword5 = str()

# Welcome message is printed and user is prompted for input
print """Welcome to the Story Generator. 
Please answer the following questions. 
The story will be genereated based off your answers."""
print ""
keyword1 = raw_input("What is the name of your favorite animal? ")
keyword2 = raw_input("What is the name of a good friend of yours?  ")
keyword3 = raw_input("What is the name of a one-word fun activity you enjoy? ")
keyword4 = raw_input("What is the name of your favorite villain? ")
keyword5 = raw_input("Name a one-word non-fun activity. ")
print ""
print ""

# Then story is generated and printed
print "The story generated by your answers is as follows:"
print ""
print "One day, there was a " + keyword1 + " walking around a busy street in New York. " + keyword2 + " was also walking on the same street. You were " + keyword3 + " as usual at your favorite " + keyword3 + " spot a block down." + " Then the " + keyword4 + " burst through the building near by. " + " You were in shock, then began to wonder what evil plot " + keyword4 + " was up to, now. Therefore, you began " + keyword5 + " in order to look inconspicuous. That is when you began following the " + keyword4 + ". " + "While you were excited about this event, you were kind of upset that you had to" + " stop " + keyword3 + ". You then continued to follow " + keyword4 + ". All the sudden, the " + keyword1 + " appeared next to you, so you decided to pet it and lost track of the " + keyword4 +". Agrily, you began to walk faster. It was then that you ran into " + keyword2 + " and decided to go watch a movie, instead."
print ""

# Promt user to press enter to exit the program after they have read the story
raw_input("Press the Enter key to close this window.")
