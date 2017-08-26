import random

def runsimul(winrate):
    games = 82
    lostlastgame = False
    for game in range(games):
        num = random.random()
        lostthisgame = num >= winrate
        if lostlastgame and lostthisgame: return 1
        lostlastgame = lostthisgame
    return 0

if __name__ == "__main__":
    numlost = 0
    winrate = .8
    number_simulations=100000   #increasing this number leads to a much greater accuracy, but takes longer.
                                #our calculated number was found using 10 million simulations.
    for i in range(number_simulations):
        numlost = numlost + runsimul(winrate)
    print("% of seasons that the warriors do not ever lose consecutive games: " + str(1-(1.0*numlost/number_simulations)) + "%")

    #This is the code we used to discover the 50% number: uncomment and it
    #will print the first winrate that leads to 50% of games being won.
    #playing with the winrate and removing the quit() statement will give more information.
    #90.38% is the % we ended up with.

    # accuracy = 1000
    # for winrate in xrange(9 * accuracy, 10 * accuracy, 1):
    #     win = 1.0 * winrate / accuracy / 10
    #     numlost = 0
    #     for i in range(100000):
    #         numlost += runsimul(win)
    #
    #     if numlost < 50000:
    #         print win
    #         quit()