import copy
from State import State

def generateStateCandidates(currentState):
    listOfStateCandidates = []
    for pawn in currentState.listOfPawn:
        for possibleMove in pawn.listOfPossibleMove:
            newState = copy.deepcopy(currentState)
            newState.move(pawn, possibleMove)
            listOfStateCandidates.append(newState)
    return listOfStateCandidates

def getMinimalHeuristicState(listOfStateCandidates):
    state = listOfStateCandidates[0]
    for stateCandidate in listOfStateCandidates:
        if (stateCandidate.totalHeuristic < state.totalHeuristic):
            state = stateCandidate
    return state

def solve(currentState):
    if (currentState.totalHeuristic == 0):
        return currentState
    listOfStateCandidates = generateStateCandidates(currentState)
    minimalHeuristicState = getMinimalHeuristicState(listOfStateCandidates).totalHeuristic
    if (minimalHeuristicState.totalHeuristic >= currentState.totalHeuristic):
        return currentState
    else:
        solve(minimalHeuristicState)

def solveHill(pawnInput):
    initState = State(pawnInput=pawnInput)
    finalState = solve(initState)
    finalState.printChessBoard()