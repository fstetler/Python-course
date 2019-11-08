"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, and ask if the players 
want to start a new game)"""


playing = True
while playing:

  p1 = int(input("Player one, input 1 for Rock, 2 for paper, 3 for scissor. "))
  p2 = int(input("Same for you, player two. "))

  if p1 == 1 and p2 == 2:
    print("Player two wins")
  if p1 == 1 and p2 == 3:
    print("player one wins")
  if p1 == 2 and p2 == 1:
    print("Player one wins")
  if p1 == 2 and p2 == 3:
    print("Player two wins")
  if p1 == 3 and p2 == 1:
    print("Player two wins")
  if p1 == 3 and p2 == 2:
    print("Player one wins")
  if p1 == p2:
    print("Youve picked the same")
  else:
    playing = False

  play_again = input("Want to play again? y for yes, n for no: ")
  if play_again == "y":
    playing = True
  else:
    playing = False

