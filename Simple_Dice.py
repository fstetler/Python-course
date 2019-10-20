import random

def roll(sides=6):
	num_rolled = random.randint(1,6)
	return num_rolled

def main():
	sides = 6
	num_rolled = roll(sides)
	print(num_rolled)

main()
