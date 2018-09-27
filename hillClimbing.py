from State import State
import helper

def solve(currentState):
    currentState.printChessBoard()
    if (currentState.totalHeuristic == 0):
        return currentState
    listOfStateCandidates = helper.getListPossibleState(currentState)
    minimalHeuristicState = helper.getStateHeuristicMin(listOfStateCandidates)
    print(currentState.sameColorHeuristic, currentState.diffColorHeuristic)
    if (minimalHeuristicState.totalHeuristic < currentState.totalHeuristic):
        return solve(minimalHeuristicState)
    else:
        return currentState

def solveHill(pawnInput):
    initState = State(pawnInput=pawnInput)
    return solve(initState)