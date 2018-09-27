import copy
from State import State

def generateStateCandidates(currentState):
    listOfStateCandidates = []
    tempState = copy.deepcopy(currentState)
    for pawn in tempState.listOfPawn:
        pawn.generatePossibleMoves(tempState.chessBoard)
        for possibleMove in pawn.listOfPossibleMove:
            newState = copy.deepcopy(tempState)
            newPawn = newState.searchPawn(pawn)
            newState.move(newPawn, possibleMove)
            listOfStateCandidates.append(newState)
    return listOfStateCandidates

def getMinimalHeuristicState(listOfStateCandidates):
    state = listOfStateCandidates[0]
    for stateCandidate in listOfStateCandidates:
        if (stateCandidate.totalHeuristic < state.totalHeuristic):
            state = stateCandidate
    return state

def solve(currentState):
    currentState.printChessBoard()
    if (currentState.totalHeuristic == 0):
        return currentState
    listOfStateCandidates = generateStateCandidates(currentState)
    minimalHeuristicState = getMinimalHeuristicState(listOfStateCandidates)
    print(currentState.sameColorHeuristic, currentState.diffColorHeuristic)
    if (minimalHeuristicState.totalHeuristic < currentState.totalHeuristic):
        return solve(minimalHeuristicState)
    else:
        return currentState

def solveHill(pawnInput):
    initState = State(pawnInput=pawnInput)
    return solve(initState)