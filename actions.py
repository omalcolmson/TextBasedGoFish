"""Methods/functions that can be called on the hands"""


def displayBook(handDict, user):  # should be renamed to displayHand
    keys = list(handDict.keys())
    keys.sort()
    print("\nPlayer " + str(user) + "'s CARDS:")
    for key in keys:
        if len(handDict[key]) == 1:
            print(key + "'s:", handDict[key][0])
        else:
            print(key + "'s:", handDict[key])


# returns boolean value if given card appears within given hand of cards
def validChoice(choice, hand):
    if choice.strip() in hand.keys():
        return True
    else:
        return False


def editHandDict(handList, oldDict=None):
    if oldDict == None:
        myHand = {}
    else:
        myHand = oldDict
    for card in handList:  # not properly handling if a string is being passed
        if card[0] not in myHand.keys():
            myHand[card[0]] = [card]
        else:
            myHand[card[0]].append(card)
    if "[Books]" not in myHand.keys():
        myHand["[Books]"] = []
    newBooks = []
    for (k, v) in myHand.items():
        if len(v) == 4 and k != "[Books]":
            newBooks.append(k)
    if newBooks != []:
        myHand["[Books]"].append(newBooks)
    for key in newBooks:
        del myHand[key]
    return myHand


def withdrawHand(dictHand, card):
    withdrawn = (dictHand[card[0]])
    del dictHand[card[0]]
    return withdrawn
