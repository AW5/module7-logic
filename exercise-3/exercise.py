# This script contains a program for a simple guessing game!

# Define a function `print_hot_or_cold()` that takes in two arguments (the `target`
# and the `guess`), and prints out an appropriate message based on how close
# the guess is to the target:
#

def print_hot_or_cold(target,guess):
    a = abs(guess - target)
    if a<1:
        return("got it!")
    elif a<=1:
        return("scalding hot")
    elif a<=3:
        return("very warm")
    elif a<=5:
        return("warm")
    elif a<=8:
        return("cold")
    elif a<=13:
        return("very cold")
    else:
        return("icy freezing miserably cold")

print_hot_or_cold(3,23)



# Distance    Message
# -------------------
# The same    "got it!"
# Within 1	  "scalding hot"
# Within 3	  "very warm"
# Within 5	  "warm"
# Within 8	  "cold"
# Within 13	  "very cold"
# > 13 away	  "icy freezing miserably cold"
#
# Be sure to consider both positive AND negative distances!
# BONUS: Also print out whether the guess is high or low



# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is (use your previous function!). Note that
# you will need to convert the input into a number.


def guess_number(target):
    a = input("Input the guess")
    if target==int(a):
        return("You got it")
    else:
        return("Try one more time")

guess_number(5)

#
# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next module)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. This is an example of **recursion**.

def guess_number(target):
    '''input target, and let other people guess until he/she get the target'''
    a = input("Input the guess")
    while target!=int(a):
        a=input("Another try")
    else:
        return("You got it")

guess_number(3)



# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# use of the range of numbers before asking them for a guess.
