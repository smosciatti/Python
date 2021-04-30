low =1
high = 1000
print ("Please think if a number between {} and {}".format(low,high))
input("Press ENTER to start")
guesses = 1
guess = 1
while True:
    guesses = low +(high -low) //2
    high_low = input("My guess is {}. Should I guess highter or lower? "
                     "Enter h or l, or c if my guess was correct"
                     .format(guesses)).casefold()
    if high_low == 'h':
        #Guess highter
        low = guesses +1
    elif high_low == 'l':
        #Guess lower
        high = guesses -1
    elif high_low =="c":
        print ("I got it in {} guesses".format(guess))
        break
    else:
        print ("Please enter h,l or c")
    guess = guess +1