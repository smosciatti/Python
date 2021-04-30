import random
highest = 10
answer = random.randint(1,highest)
numTries = 0
foundIt = False
print ("Please guess a number between 1 and {} 0 for exit".format(highest))
while True:
    guess = int(input())
    if (guess == 0) or foundIt : #if push 0 or found it
        break
    if (guess == answer) and (numTries ==0):
        print("You gor it first time")
        foundIt = True
    else:
        if guess < answer :
            print ("Please guess highter")
        else:
            print ("Please guess lower")
            if guess == answer:
                print ("Well done, you guessed it")
                foundIt = True
