import random

x = random.randint(1,100)
y = ''

while y != x:
	y = input("What number i'm thinking: ")
	if y > x:
		print("Go low")
	elif y < x:
		print("Go high")
	elif y == x:
		print("You guessed it!")
