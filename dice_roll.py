from random import *

def print_rand():
	print randint(1,6)

print_rand()
input = raw_input("Would you like to roll the dice again?(Yes/No?):")
if(input.lower() == 'yes'):
	print_rand()
	
