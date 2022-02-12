# Returns an int representative of the score acheived by rolling the dice
def roll():
    return 10

# Returns the odds of roll() returning a given Score
def probabilityOfScoring(score):
    return 0.5

# Returns a float between 0 and 1 based on the odds a given Score will result in a win
def probabilitySpeWin(Score, playersYetTogo, rollsAvailable, shittiestScoreYet):
    # Assumes rollsAvailable is 1 UNFINISHED

    # This works since a Score value is == the number of dice rolls it will beat
    if (Score > shittiestScoreYet):
        return 1
    else:
        return 1-((36-Score)/36)**playersYetTogo

# Assumes currentScore < shittiestScoreYet
# Returns a float between 0 and 1 based on the odds that a roll() will result in a win
def probabilityHypWin(playersYetTogo, rollsRemaining, shittiestScoreYet, rollsAvailable):
    # Assumes rollsAvaiable == 1 UNFINISHED

    # This is the sum of the odds of each roll being rolled times the odds of it winning, with any score that is larger than the shittiest score yet being a guarenteed win
    rProb = 0
    for i in range(36):
        nProb += probabilityOfScoring(i)*probabilitySpeWin(i, playersYetTogo, rollsAvailable, shittiestScoreYet)
    return rProb

# Returns true if one should roll() again, false otherwise
def shouldRoll(shittiestScoreYet, rollsAvailable, rollsRemaining, playersYetTogo, currentScore):
    return probabilitySpeWin(currentScore, playersYetTogo, rollsAvailable) < probabilityHypWin(playersYetTogo, rollsRemaining, shittiestScoreYet, rollsAvailable)

# Simulates a turn done by the first player to go
# Returns an int representative of their score.
# Note: The mxRolls field should be updated to the number of rolls the first player spent
def firstTurn(numPlayers, mxRolls):
    return 1

# Simulates a turn done by a non-first player
# returns an int representative of their score.
def playerTurn(shittiestScoreYet, rollsAvailable, playersYetTogo):
    pScore = 0
    for i in range(rollsAvailable): # for every roll we have avaliable to us
        #If we arent in the clear, and we should roll
        if (pScore < shittiestScoreYet and shouldRoll(shittiestScoreYet, rollsAvailable, rollsAvailable - i, playersYetTogo, pScore)):
            pScore = roll()
        else:
            break

    return pScore

# Simulates a fully automatic match
# Has a negligible return
def playMatch(numPlayers, mxRolls):
    worstScore = firstTurn(numPlayers, mxRolls)
    print("The first player scored a " + str(worstScore) + " using " + str(mxRolls) + " rolls.\n")
    for i in range(1, numPlayers):
        pscore = playerTurn(worstScore, mxRolls, numPlayers-i-1)
        print("Player number: " + str(i+1) + " acheived a score of " + str(pscore) + ".\n")
        worstScore = min(worstScore, pscore)
    return 0


def main():
    #playMatch(6, 3)
    print("Hi")

if __name__ == "__main__":
    main()