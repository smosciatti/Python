low =1
high = 1000
print ("Please think if a number between {} and {}".format(low,high))
input("Press ENTER to start")
guesses = 1
while True:
    guess = low +(high -low) //2
    high_low = input("My guess is {}. Should I guess highter or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()
    if high_low == 'h':
        #Guess highter
        low = guess +1
    elif high_low == 'l':
        #Guess lower
        high = guess -1
    elif high_low =="c":
        print ("I got it in {} guesses".format(guesses))
        break
    else:
        print ("Please enter h,l or c")
    guesses = guesses +1