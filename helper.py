from copy import deepcopy
from State import State

def getListPossibleState(state) :
    listState = []
    tempState = deepcopy(state)
    for pawn in tempState.listOfPawn :
        pawn.generatePossibleMoves(tempState.chessBoard)
        for pos in pawn.listOfPossibleMove :
            newState = deepcopy(tempState)
            newPawn = newState.searchPawn(pawn)
            newState.move(newPawn, pos)
            listState.append(newState)
    return listState


def getStateHeuristicMin(ListPossibleState) :
    stateMin = ListPossibleState[0]
    for unitState in ListPossibleState :
        if unitState.totalHeuristic < stateMin.totalHeuristic :
            stateMin = unitState
    return stateMin