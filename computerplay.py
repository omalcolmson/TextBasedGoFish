import random
from random import choice


def bestChoice(compHand):  # tracks best card to ask based on hand only
    x1 = []
    x2 = []
    x3 = []
    for (k, v) in compHand.items():
        # track what duplicates hand contains
        if len(v) == 2 and k != "[Books]":
            x2.append(k)
        elif len(v) == 3 and k != "[Books]":
            x3.append(k)
        elif len(v) == 1 and k != "[Books]":
            x1.append(k)
    if len(x3) != 0:
        return x3[0]
    elif len(x2) != 0:
        return x2[0]
    else:
        return random.choice(x1)


def displayOnlyBooks(handDict, user):
    print()
    print("Player", str(user) + "'s Books:")
    print(handDict["[Books]"])


def displayScore(userHand, compHand):
    userCatches = len(userHand["[Books]"])
    compCatches = len(compHand["[Books]"])
    scoreboard = """

                █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀ █░█ █▀▄▀█ █▀▄▀█ ▄▀█ █▀█ █▄█
                █▄█ █▀█ █░▀░█ ██▄   ▄█ █▄█ █░▀░█ █░▀░█ █▀█ █▀▄ ░█░

        ==================================================================
        P L A Y E R {0} (Y O U) ...................................... {1}
        P L A Y E R {2} .............................................. {3}



        ▀█▀ █░█ ▄▀█ █▄░█ █▄▀ ▀ █▀   █▀▀ █▀█ █▀█   █▀█ █░░ ▄▀█ █▄█ █ █▄░█ █▀▀ █
        ░█░ █▀█ █▀█ █░▀█ █░█ ░ ▄█   █▀░ █▄█ █▀▄   █▀▀ █▄▄ █▀█ ░█░ █ █░▀█ █▄█ ▄


    """
    scores = ["1", "2"]
    scores.insert(1, userCatches)
    scores.insert(3, compCatches)
    print(scores)
    formattedScoreboard = scoreboard.format(
        scores[0], scores[1], scores[2], scores[3])
    print(formattedScoreboard)
