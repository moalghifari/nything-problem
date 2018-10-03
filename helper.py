from copy import deepcopy
from State import State

def getListPossibleState(state) :
    listState = []
    tempState = deepcopy(state)
    for pawn in tempState.listOfPawn :
        for i in range(8):
            for j in range(8):
                if tempState.chessBoard[j][i] == '.':
                    newState = deepcopy(tempState)
                    newPawn = newState.searchPawn(pawn)
                    newState.move(newPawn, (i, j))
                    listState.append(newState)
    return listState


def getStateCostMin(ListPossibleState) :
    stateMin = ListPossibleState[0]
    for unitState in ListPossibleState :
        if unitState.totalCost < stateMin.totalCost :
            stateMin = unitState
    return stateMin