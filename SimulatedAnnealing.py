import constants
from State import State
import numpy
import random
import Pawn
from copy import deepcopy
import helper

def solve(state, type, value) :
    if (state.totalHeuristic == 0):
        return state
    tempSolution = deepcopy(state)
    temperatur = 99999
    i = 0
    while not((temperatur <= 0) or (i >= 50 ) or (tempSolution.totalHeuristic == 0)) :
        listPossibleState = helper.getListPossibleState(tempSolution)
        newSolution = helper.getStateHeuristicMin(listPossibleState)
        if (tempSolution.totalHeuristic > newSolution.totalHeuristic) :
            tempSolution = newSolution
        else :
            delta = newSolution.totalHeuristic-tempSolution.totalHeuristic
            if numpy.exp(-delta/temperatur) > random.uniform(0,1) :
                tempSolution = newSolution
            else:
                return tempSolution
        if (type == '1') :
            temperatur = temperatur
        elif (type == '2') :
            temperatur = temperatur - int(value)
        else :
            temperatur = temperatur*(1-int(value))
        i=+1
    return tempSolution

def main(pawnInput):
    print ("Solusi SA")
    print(" *•.¸*•.¸¤ Pilih jenis temperatur yang diinginkan ¤¸.•*¸.•* "),
    print(">> 1. Constant")
    print(">> 2. Linear")
    print(">> 3. Logaritmic\n")
    inputT = input(">> Pilihan : ")
    print(" *•.¸*•.¸¤ Masukan Nilai Pengurangan Temperatur ¤¸.•*¸.•* "),
    value = input(">> ")
    initState = State(pawnInput=pawnInput)
    return solve(initState, inputT, value)