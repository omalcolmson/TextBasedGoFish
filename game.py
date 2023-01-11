import random
from random import randrange
from cards import Cards
from actions import editHandDict, withdrawHand, displayBook, validChoice
from computerplay import bestChoice, displayScore, displayOnlyBooks

# GAME INTRO MESSAGE #
print()
print("██╗░░░░░███████╗████████╗██╗░██████╗  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗  ░██████╗░░█████╗░")
print("██║░░░░░██╔════╝╚══██╔══╝╚█║██╔════╝  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝  ██╔════╝░██╔══██╗")
print("██║░░░░░█████╗░░░░░██║░░░░╚╝╚█████╗░  ██████╔╝██║░░░░░███████║░╚████╔╝░  ██║░░██╗░██║░░██║")
print("██║░░░░░██╔══╝░░░░░██║░░░░░░░╚═══██╗  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░  ██║░░╚██╗██║░░██║")
print("███████╗███████╗░░░██║░░░░░░██████╔╝  ██║░░░░░███████╗██║░░██║░░░██║░░░  ╚██████╔╝╚█████╔╝")
print("╚══════╝╚══════╝░░░╚═╝░░░░░░╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ░╚═════╝░░╚════╝░")
print()
print("                         ███████╗██╗░██████╗██╗░░██╗██╗ ")
print("                         ██╔════╝██║██╔════╝██║░░██║██║ ─▀▀▌───────▐▀▀")
print("                         █████╗░░██║╚█████╗░███████║██║ ─▄▀░◌░░░░░░░▀▄")
print("                         ██╔══╝░░██║░╚═══██╗██╔══██║╚═╝ ▐░░◌░▄▀██▄█░░░▌")
print("                         ██║░░░░░██║██████╔╝██║░░██║██╗ ▐░░░▀████▀▄░░░▌")
print("                         ╚═╝░░░░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝ ═▀▄▄▄▄▄▄▄▄▄▄▄▀═")

# SETTING UP THE GAME
deck = Cards()
values = ['A', 'K', 'Q', 'J', '2',
          '3', '4', '5', '6', '7', '8', '9', '10']
deck.shuffle()
dealtCards = deck.deal()
hand1 = dealtCards.pop(0)
hand2 = dealtCards.pop(0)
hand1.sort()  # might be somewhat redundant now since i sort whenever i print
hand2.sort()
orgHand1 = editHandDict(hand1)
orgHand2 = editHandDict(hand2)
drawPile = ()
bookList = []
user = 1
userHand = orgHand1
compHand = orgHand2

# GAME INSTRUCTIONS AND NOTES ABOUT GAME FORMAT
print("\nGAME INSTRUCTIONS AND RULES: \nOBJECTIVE: Obtain as many card sets of the same value (4 possible; e.g., 10D, 10S, 10C, 10H). These are referred to as 'books'. \nYour turn only ends if you receive a card you were NOT looking for, so you keep your turn as long as you either draw your card of interest from the pile, or receive it from the other player. \nNOTE ABOUT FORMAT: Please enter the appropriate input based on the text prompts. Additionally, to indicate the number '10', enter '1'.")
game = True
while game:
    displayBook(userHand, user)
    print()
    # comment this line below out if you want to play the game #
    # displayBook(compHand, "2")
    ############################################################
    while user == 1 and game:  # human turn
        keys = userHand.keys()
        if len(keys) == 1:
            if deck.deck != []:
                drawn = deck.drawDeck()
                editHandDict(drawn, userHand)
            else:
                print(
                    "There are no more cards left to draw from! The game is over. Time to tally your books.")
                game = False
        elif game and len(keys) > 1:
            print("\nYOU ARE PLAYER", user, "\nIt is now Player 1's turn.")
            choice = input("\nWhat card value would you like to ask for? ")
            while validChoice(choice.strip().upper(), userHand) == False:
                choice = input(
                    "\nYou can only ask for a card value in your hand. Please select again. ")
            if validChoice(choice.strip().upper(), compHand) == True:
                print(
                    "\nIt looks like Computer had some cards. They are now in your hand.")
                withdrawn = withdrawHand(compHand, choice.strip().upper())
                print(withdrawn)
                editHandDict(withdrawn, userHand)
                displayBook(userHand, user)
                print()
                displayOnlyBooks(compHand, "2")
                # comment this line below out if you want to play the game #
                # displayBook(compHand, "2")
                ############################################################
                print(
                    "\nSince you got the card you were looking for, you get another turn!")
            elif validChoice(choice.strip().upper(), compHand) == False:
                x = input(
                    "\nComputer says, go fish! Press the ENTER key to continue.")
                if x == "":
                    drawn = deck.drawDeck()
                    if choice.upper() == drawn[0]:
                        print("\nYou were looking for a", choice.strip().upper(),
                              "and drew a ", drawn + "! You get to go again")
                        editHandDict([drawn], userHand)
                        displayBook(userHand, user)
                        displayOnlyBooks(compHand, "2")
                    else:
                        editHandDict([drawn], userHand)
                        displayBook(userHand, user)
                        displayOnlyBooks(compHand, "2")
                        user = 2

    while user == 2 and game:
        keys = compHand.keys()
        if len(keys) == 1:
            if deck.deck != []:
                drawn = deck.drawDeck()
                editHandDict([drawn], compHand)
            else:
                print(
                    "\nThere are no more cards left to draw from! The game is over. Time to tally your books.")
                game = False
        elif game and len(keys) > 1:
            choice = bestChoice(compHand)
            print("It is now Player 2's turn. \nComputer is looking for " +
                  str(choice) + ".")
            response = input("Do you have any " + str(choice) +
                             "'s? Hit [Y] to withdraw them, or [N] to tell Computer to go fish:  ")
            if validChoice(choice, userHand) == True:
                while response.strip().upper() != "Y":  # checks for user cheating
                    print("No cheating! You have a", choice,
                          "and you must give it to Computer.")
                    response = input("Hit [Y] to give up the cards: ")
                withdrawn = withdrawHand(userHand, choice)
                editHandDict(withdrawn, compHand)
                displayOnlyBooks(compHand, user)
                print(
                    "\nSince Computer got the card they were looking for, they get to go again!")
            elif validChoice(choice, userHand) == False:
                while response.strip().upper() != "N":
                    response = input(
                        "It looks like you don't have the card(s) Computer is looking for! Press [N] to tell them to go fish!  ")
                drawn = deck.drawDeck()
                if drawn[0] == choice:
                    print("Computer was looking for", choice,
                          "and found", drawn + "! They get to go again.")
                    editHandDict([drawn], compHand)
                    displayOnlyBooks(compHand, user)
                else:
                    editHandDict([drawn], compHand)
                    displayOnlyBooks(compHand, user)
                    user = 1

displayScore(userHand, compHand)
