from State import State
import helper
from sys import stdout


def solve(currentState):
    """
        solve n-ything problem with hillClimbing Algorithm
        1. If total cost is equal to 0 then solved
        2. Else, get candidate of next state
        3. Search for minimal cost state
        4. If no minimal cost state lower than current cost, then solved
        5. Else, back to number 2
    """
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
