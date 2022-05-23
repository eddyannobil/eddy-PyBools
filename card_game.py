#!/usr/bin/env python3

#A simple simulated card game involving two players named
#James and Jane.

# James's strategy is as follows for all games:
# - Play the cards in the following order: 1st, 3rd, 5th, 2nd and 4th

# Jane's strategy is as follows for all games:
# - Play the cards in the following order: 5th, 1st, 2nd, 4th, and 3rd

# Both players stick to their strategies no matter what cards
# they are dealt.

# James won a coin toss and will play the first card to begin the game.

# The algorithm (logic) is as follows:
# 1. Check the value of player1's card to see if it's greater than or equal to player2's card and
#  save the result of that check to a boolean variable.
# 2. Manually compute the result of the first round to determine who plays first during the next round. 
# If the result of the first round is `True`, then player1 starts the next round again. 
# Otherwise, player2 will start the next round.
# 3. Repeat steps 1 and 2 until both players have played all their cards in the order of their strategies.
# 4. The person who wins the most rounds, wins the game.
# 5. Set the variable `winner` to the name of the winner (through the appropriate player variable below) at the end of each game, and 
# increment the `game` variable to signify the start of the next game.
# 6. Repeat the algorithm until all 3 games have been played and an overall winner can be determined.
# 7. Print the name of the overall winner to the terminal.


# Declare two variables `player1` and `player2` and set them as the
# names of the players in the game.


player1 = 'James'
player2 = 'Jane'

# Declare each of the suits (clubs, diamonds, hearts, and spades) as an int variable and set its value to its appropriate numerical value.
# (Remember: Each suit is given a numerical value based on the numerical equivalent of the letter it begins with. See the assignment overview
# for more details on this)
Clubs = 3
Diamonds = 4
Hearts = 8
Spades = 19
Ace = 14
King = 13
Queen = 12
Jack = 11
# Declare a variable `game` of type int and set it to the first round
# The games will be incremented by one after each game, by computing:
# game = game + 1
game = 1


# For game 1:
# James is dealt the following cards: 5 Hearts, 3 Clubs, Ace Clubs, King Diamonds, 2 Diamonds
# Jane is dealt the following cards: 2 Spades, Queen Spades, 10 Diamonds, 7 Clubs , Jack Hearts

# Declare a list for James's cards and save it to the variable `james_cards`
james_cards = [5 + Hearts, 3 + Clubs , Ace + Clubs , King + Diamonds, 2 + Diamonds]

# Declare another list for Jane's cards and save it to the variable `jane_cards`
jane_cards = [2 + Spades, Queen + Spades, 10 + Diamonds, 7 + Clubs, Jack + Hearts]
# For each list, recall that the number on each card is added to the numerical value of its suit to determine how many points it's worth.
# eg. 5 of hearts will be worth 13 points and so the entry in the list will be 5 + <the numerical value of hearts>.
#  Note: DO NOT COMPUTE THESE BY HAND. Rather, use the variables you declared above!

# Based on their strategies, play all 5 rounds of the game, and determine the winner at the end of the game.
# Set the variable `winner` to the name of the winner (through the appropriate player variable above) at the end of the game,
# Increment the `game` variable to signify the start of the next game.
round_1 = james_cards[0] > jane_cards[4] or james_cards[0] == jane_cards[4]
print(round_1)
print(player2 +' '+ 'wins round_1')

round_2 = jane_cards[0] > james_cards[2] or jane_cards[0] == james_cards[2]
print(round_2)
print(player2 +' '+ 'wins round_2')

round_3 = jane_cards[1] > james_cards[4] or jane_cards[1] == james_cards[4]
print(round_3)
print(player2 +' '+ 'wins round_3')

round_4 = jane_cards[3] > james_cards[1] or jane_cards[3] == james_cards[1]
print(round_4)
print(player2 +' '+ 'wins round_4')

round_5 = jane_cards[2] > james_cards[3] or jane_cards[2] == james_cards[3]
print(round_5)
print(player1 +' '+ 'wins round_5')

winner = player2
print('winner =' + ' '+ winner)
# For game 2:
game = game + 1
# James is dealt the following cards: 7 Clubs, 5 Spades, 2 Hearts, Jack Clubs, 2 Spades
# Jane is dealt the following cards: Jack Hearts, King Diamonds, 8 Clubs, 9 Hearts , 7 Spades
james_cards = [7 + Clubs, 5 + Spades , 2 + Hearts, Jack + Clubs , 2 + Spades]
jane_cards = [Jack + Hearts, King + Diamonds, 8 + Clubs, 9 + Hearts, 7 + Spades]
print(james_cards)
print(jane_cards)
# Follow the same algorithm to determine the winner of this game
round_1 = jane_cards[4] > james_cards[0] or jane_cards[4] == james_cards[0]
print(round_1)
print(player2 +' '+ 'wins round_1')

round_2 = jane_cards[0] > james_cards[2] or jane_cards[0] == james_cards[2]
print(round_2)
print(player2 +' '+ 'wins round_2')

round_3 = jane_cards[1] > james_cards[4] or jane_cards[1] == james_cards[4]
print(round_3)
print(player1 +' '+ 'wins round_3')

round_4 = james_cards[1] > jane_cards[3] or james_cards[1] == jane_cards[3]
print(round_4)
print(player1 +' '+ 'wins round_4')

round_5 = james_cards[3] > jane_cards[2] or james_cards[3] == jane_cards[2]
print(round_5)
print(player1 +' '+ 'wins round_5')

winner = player1
print('winner =' + ' '+ winner)
# Don't forget to increment the game variable!


# For game 3:
game = game + 1
# James is dealt the following cards: 10 Diamonds, 2 Clubs, 3 Spades, 7 Diamonds, 4 Spades
# Jane is dealt the following cards: Queen Hearts, 9 Diamonds, 4 Hearts, 2 Diamonds , Queen Hearts
james_cards = [10 + Diamonds, 2 + Clubs, 3 + Spades, 7 + Diamonds , 4 + Spades]
jane_cards = [Queen + Hearts, 9 + Diamonds, 4 + Hearts, 2 + Diamonds, Queen + Hearts]
print(james_cards)
print(jane_cards)

round_1 = james_cards[0] > jane_cards[4] or james_cards[0] == jane_cards[4] 
print(round_1)
print(player2 +' '+ 'wins round_1')

round_2 = jane_cards[0] > james_cards[2] or jane_cards[0] == james_cards[2]
print(round_2)
print(player1 +' '+ 'wins round_2')

round_3 = james_cards[4] > jane_cards[1] or james_cards[4] == jane_cards[1]
print(round_3)
print(player1 +' '+ 'wins round_3')

round_4 = james_cards[1] > jane_cards[3] or james_cards[1] == jane_cards[3]
print(round_4)
print(player2 +' '+ 'wins round_4')

round_5 = jane_cards[2] > james_cards[3] or jane_cards[2] == james_cards[3]
print(round_5)
print(player2 +' '+ 'wins round_5')

winner = player2
print('winner =' + ' '+ winner)

# Follow the same algorithm to determine the winner of this game
# Print the value of the game variable to signify the end of the game
print(game)


# Declare a variable `overall_winner` and set it equal to the player who won the most out of all 3 games
overall_winner = player2
print('overall_winner=' + '' + player2)
# Set this variable through the player number variable. Print the value of this variable.
