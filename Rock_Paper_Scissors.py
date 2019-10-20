"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""


"""def game():

	print("Lets play some Rock, Paper, or Scissors")

	p1 = int(input("Hello player one. Please input 1 for Rock, 2 for Paper, 3 for Scissor: "))
	p2 = int(input("And player two, same for you: "))

	if p1 == 1 and p2 == 2:
		print("Rock is beaten paper, player one wins")
	if p1 == 1 and p2 == 3:
		print("Rock beats scissors, player two wins")
	if p1 == 2 and p2 == 3:
		print("Paper is beaten by scissors, player two wins")
	if p1 == 2 and p2 == 1:
		print("Paper beats rock, player one wins")
	if p1 == 3 and p2 == 1:
		print("Scissors is beaten by rock, player two wins")
	if p1 == 3 and p2 == 2:
		print("Scissors beats paper, player one wins")
	if p1 == p2:
		print("Youve picked the same")


#if __name__ == '__main__':
play_again = str(input("Want to play rock, paper, scissors? y for yes, n for no: "))
while play_again == "y":
	game()
	play_again = str(input("Want to play rock, paper, scissors? y for yes, n for no: "))"""






playing = True
while playing:	
	p1 = int(input("Hello player one. Please input 1 for Rock, 2 for Paper, 3 for Scissor"))
	p2 = int(input("And player two, same for you: "))		
	
	if p1 == 1 and p2 == 2:
		print("Rock is beaten paper, player one wins")
	if p1 == 1 and p2 == 3:
		print("Rock beats scissors, player two wins")
	if p1 == 2 and p2 == 3:
	    print("Paper is beaten by scissors, player two wins")
	if p1 == 2 and p2 == 1:
		print("Paper beats rock, player one wins")
	if p1 == 3 and p2 == 1:
		print("Scissors is beaten by rock, player two wins")
	if p1 == 3 and p2 == 2:
		print("Scissors beats paper, player one wins")
	if p1 == p2:
		print("Youve picked the same")

	play_again = str(input("Want to play again? y = play, q = quit"))
	if play_again == "y":
		playing = True
	else:
		playing = False




"""def main():

	playing = True
	while playing:
		p1 = int(input("Hello player one. Please input 1 for Rock, 2 for Paper, 3 for Scissor. q for quit: "))
		p2 = int(input("And player two, same for you: "))
		if p1 !="q" and p2 !="q":
			if p1 == 1 and p2 == 2:
				print("Rock is beaten paper, player one wins")
			if p1 == 1 and p2 == 3:
				print("Rock beats scissors, player two wins")
			if p1 == 2 and p2 == 3:
			    print("Paper is beaten by scissors, player two wins")
			if p1 == 2 and p2 == 1:
				print("Paper beats rock, player one wins")
			if p1 == 3 and p2 == 1:
				print("Scissors is beaten by rock, player two wins")
			if p1 == 3 and p2 == 2:
				print("Scissors beats paper, player one wins")
			if p1 == p2:
				print("Youve picked the same")

main()

play_again = input("Want to play again? y for yes, n for no")
if play_again == "y":
	main()
else:	
	rolling = False
print("Thanks for playing")"""












#if __name__ == '__main__':
"""play_again = str(input("Want to play rock, paper, scissors? y for yes, n for no: "))
while play_again == "y":
	game()
	play_again = str(input("Want to play rock, paper, scissors? y for yes, n for no: "))"""





