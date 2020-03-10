# The play_game() function starts the game.
from random import choice
import random
# The code below is an adaptation of the sample code to create a valid deck of cards.
nIm = 8
n = nIm - 1
r = range(n)
rp1 = range(n+1)
c = 0
card_dict = {}

# First card
c += 1
set = {*()}
for i in rp1:
    val = i+1
    set.add(val)
card_dict[c] = set
x = card_dict.get(1)


# n following cards
for j in r:
    c = c+1
    set = {*()}
    y = 1
    set.add(y)
    for k in r:
        val=(n+2 + n*j +k)
        set.add(val)
    card_dict[c] = set

# n x n following cards
for i in r:
    for j in r:
        c = c+1
        set = {*()}
        y = i+2
        set.add(y)
        for k in r:
            val=((n+1 +n*k + (i*k+j) % n)+1)
            set.add(val)
        card_dict[c] = set

# This code was provided in order to create a dictionary of the emojis.
import emoji
imageDict = dict()
fin = open('emoji_names.txt',"r")
lines = fin.readlines()
for i, el in enumerate(lines):
    imageDict[i+1] = emoji.emojize(el.strip())


def check_validity(deck, verbose=False):
    """Function to check that the deck is valid, i.e. that any two cards only have one emoji in common.
    Provides a verbose option which prints out the card numbers that are being checked and the number of
    common emojis (image ids)."""
    if verbose == False:
        for x in deck:
            valid_count = 0
            for i in deck:
                result = deck[x].intersection(deck[i])
                if result.__len__() == 1:
                    valid_count += 1
                else:
                    valid_count += 0
            if valid_count == deck.__len__()-1:
                continue
            else:
                return False
        return True
    else:
        for x in deck:
            valid_count = 0
            for i in deck:
                result = deck[x].intersection(deck[i])
                if result.__len__() == 1:
                    print("Checking Card", x, "and Card", i)
                    print("Image ids in common:", result.__len__())
                    valid_count += 1
                elif result.__len__() > 1 and result.__len__() < nIm:
                    print("Checking Card", x, "and Card", i)
                    print("Image ids in common:", result.__len__())
                    valid_count += 0
                else:
                    valid_count += 0
            if valid_count == deck.__len__()-1:
                continue
            else:
                return False
        return True

# The DobbleCard class is passed a card id number.
# On each instance it adds emojis which correspond to the card numbers to its set attribute.
class DobbleCard:
    def __init__(self, card_num):
        self.card_num = card_num
        self.set = {*()}
        for x in card_dict[card_num]:
            for y in imageDict:
                if x == y:
                    self.set.add(imageDict[y])

# The DobbleDeck has an attibute called full_deck which holds the validated deck of cards with their emojis.
class DobbleDeck:
    def __init__(self):
        self.full_deck = {}
    def add_card(self, card_number):
        """This function is passed a card id number. It creates an instance of the the DobbleCard class
        and adds each DobbleCard to its full_deck attribute."""
        self.card_number = card_number
        self.card = DobbleCard(card_number)
        self.full_deck[card_number] = self.card.set


    def remove_card(self, card):
        """This function removes a card from the full_deck attribute of the deck object."""
        self.card = card
        self.full_deck.pop(self.card)


    def play_card(self):
        """This function chooses a random card from the full_deck and returns it."""
        self.card = choice(list(self.full_deck))
        return (self.card)


def play_game():
    """This is the function that starts the game. Firstly, it calls the check validity function. If a valid card
    dictionary is produced, then the fucntion continues. If not, an error message is printed and the program ends.
    An instance of the DobbleDeck is created and the initial scores for the two players are set to 0. The user is
    asked to enter the number of rounds they want to play which must be an integer less than 56. On each two
    cards are printed to the screen. The user is asked to enter the winner (or draw) and the scores are updated.
    The second card from each round is assigned to the card_holder variable in order for it to be used as the first
    card in the next round. When the entered number of rounds has been reached the final score is printed and the
    program finishes."""
    check_validity(card_dict)
    if check_validity(card_dict) == True:
        deck = DobbleDeck()
        for x in card_dict:
            deck.add_card(x)
        playerA = 0
        playerB = 0
        while True:
            try:
                rounds = int(input("How many cards (<56)? "))
            except ValueError:
                print("Please enter a number < 56 ")
                continue
            if rounds <= 0 or rounds >= 56:
                print("Please enter a number > 0 and < 56 ")
            else:
                break
        print("If you want to record a draw type 'd' or 'D'.")
        print()
        round_count = 1
        card_holder = [*()]
        while round_count <= rounds:
            if card_holder == [*()]:
                first_card_num = deck.play_card()
                first_card_set = deck.full_deck[first_card_num]
                first_card = list(first_card_set)
                deck.remove_card(first_card_num)
                second_card_num = deck.play_card()
                second_card_set = deck.full_deck[second_card_num]
                second_card = list(second_card_set)
                print(first_card[0], first_card[1], first_card [2], "\t\t", second_card[0], second_card[1], second_card[2])
                print(first_card[3], first_card[4], first_card [5], "\t\t", second_card[3], second_card[4], second_card[5])
                print(first_card[6], first_card[7], "\t\t\t", second_card[6], second_card[7])
                deck.remove_card(second_card_num)
                for item in second_card:
                    card_holder.append(item)
                valid_input = ["A", "a", "B", "b", "d", "D"]
                while True:
                    answer = str(input("Who wins (A or B)? "))
                    if answer in valid_input:
                        break
                    else:
                        print("Please enter a valid input!")
                if answer == "A" or answer == "a":
                    playerA += 1
                    round_count += 1
                elif answer == "B" or answer == "b":
                    playerB += 1
                    round_count += 1
                elif answer == "D" or answer == "d":
                    round_count += 1
                print()
            else:
                first_card = card_holder
                second_card_num = deck.play_card()
                second_card_set = deck.full_deck[second_card_num]
                second_card = list(second_card_set)
                print(first_card[0], first_card[1], first_card[2], "\t\t", second_card[0], second_card[1],
                      second_card[2])
                print(first_card[3], first_card[4], first_card[5], "\t\t", second_card[3], second_card[4],
                      second_card[5])
                print(first_card[6], first_card[7], "\t\t\t", second_card[6], second_card[7])
                deck.remove_card(second_card_num)
                card_holder.clear()
                for item in second_card:
                    card_holder.append(item)
                valid_input = ["A", "a", "B", "b", "d", "D"]
                while True:
                    answer = str(input("Who wins (A or B)? "))
                    if answer in valid_input:
                        break
                    else:
                        print("Please enter a valid input!")
                if answer == "A" or answer == "a":
                    playerA += 1
                    round_count += 1
                elif answer == "B" or answer == "b":
                    playerB += 1
                    round_count += 1
                elif answer == "D" or answer == "d":
                    round_count += 1
                print()
        print()
        print("Score")
        print("A:",playerA)
        print("B:",playerB)


    else:
        print("There is an error in the deck of cards. Please make alterations.")

# Function call to start the game.
play_game()
