from random import *

rand_num = randint(1,10)
right_guess = False

while(right_guess == False):
	user_num = int(raw_input("Guess the number!"))
	if (user_num == rand_num):
		right_guess = True
	elif(user_num > rand_num):
		print "Your number is greater than the generated number"
	else:
		print "Your number is smaller than the generated number"

print "You have guessed the number correctly --", rand_num
