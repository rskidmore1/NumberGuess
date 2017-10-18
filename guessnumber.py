import random 
import numpy



def guess():
  endRange = raw_input("Please select an end range:") 
  endRange = float(endRange)
  guess = raw_input("Please guess a number:") 
  guess = int(guess) 
  rand = random.random()
  randfloat = rand * endRange
  randint = int(randfloat)
  if guess == randint:
    print "Great job, you guessed right!"
  else:
    print "No the number was %i" % randint 

def guessClose():
  endRange = raw_input("Please select an end range:") 
  endRange = float(endRange)
  guess = raw_input("Please guess a number:") 
  guess = int(guess) 
  rand = random.random()
  randfloat = rand * endRange
  randint = int(randfloat)
  if guess == randint:
    print "Great job, you guessed right!"
  elif numpy.isclose(guess, randint, rtol=0.1, atol=0.0):
    print "Close. Your guess: %i. Random number: %i" %( guess, randint)
  else:
    print "Number was: %i" %randint


#guess() 
guessClose()


