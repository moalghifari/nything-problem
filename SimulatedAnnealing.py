import constants
import State
import numpy
import random
from copy import deepcopy


def getListPossibleState(state) :
    listState = []
    for pawn in initState.getListOfPawn() :
        for pos in createPawn.getListPossiblePawn(initState.chessBoard) :
            newState = deepcopy(state)
            newState.move(pawn, pos)
            listState.append(newState)
    return listState


def getStateHeuristicMin(ListPossibleState) :
    stateMin = ListPossibleState[0]
    for unitState in ListPossibleState :
        if unitState.getTotalHeuristic() < stateMin.getTotalHeuristic() :
            stateMin = unitState
    return stateMin

def Solve(state, type, value) :
    tempSolution = state
    temperatur = 99999
    i = 0
    while ((temperatur = 0) or (i = 10000 )) :
        listPossibleState = getListPossibleState(state)
        newSolution = getStateHeuristicMin(listPossibleState)
        if (tempSolution.getTotalHeuristic() > newSolution.getTotalHeuristic()) :
            tempSolution = newSolution
        else :
            delta = newSolution.getTotalHeuristic()-tempSolution.getTotalHeuristic()
            if numpy.exp(-delta/temperatur) > random.uniform(0,1) :
                tempSolution = newSolution
        if (type == '1') :
            temperatur = temperatur
        elif (type == '2') :
            temperatur = temperatur - value
        else :
            temperatur = temperatur*(1-value)
        i=+1