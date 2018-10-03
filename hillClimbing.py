from State import State
import helper
from sys import stdout


def solve(currentState):
    stdout.write('\rCost terbaik: {} {}'.format(currentState.sameColorCost, currentState.diffColorCost))
    if (currentState.totalCost == 0):
        return currentState
    listOfStateCandidates = helper.getListPossibleState(currentState)
    minimalCostState = helper.getStateCostMin(listOfStateCandidates)
    if (minimalCostState.totalCost < currentState.totalCost):
        return solve(minimalCostState)
    else:
        return currentState

def main(pawnInput):
    initState = State(pawnInput=pawnInput)
    return solve(initState)