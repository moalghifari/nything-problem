from copy import deepcopy
from State import State

def getListPossibleState(state) :
    """
        return all possible next state for each pawn in current state
        possible next state for each pawn is all point that not filled with pawn
    """
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
    """
        return the state with minimum cost
    """
    stateMin = ListPossibleState[0]
    for unitState in ListPossibleState :
        if unitState.totalCost < stateMin.totalCost :
            stateMin = unitState
    return stateMin
