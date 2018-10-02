from State import State
import helper

def solve(currentState):
    if (currentState.totalHeuristic == 0):
        return currentState
    listOfStateCandidates = helper.getListPossibleState(currentState)
    minimalHeuristicState = helper.getStateHeuristicMin(listOfStateCandidates)
    if (minimalHeuristicState.totalHeuristic < currentState.totalHeuristic):
        return solve(minimalHeuristicState)
    else:
        return currentState

def main(pawnInput):
    initState = State(pawnInput=pawnInput)
    return solve(initState)