import constants
from State import State
import numpy
from numpy import random
from random import randint
import Pawn
from copy import deepcopy
import helper
from sys import stdout


def solve(state, type, temperatur, value) :
    """
        solve n-ything problem with Simulated Annealing Algorithm
        1. If total cost is equal to 0 then solved
        2. Else, tempSolution is currentState
        3. Get candidate of next state
        4. Generate new solution by randomly choose one in candidate of next state
        5. If new solution's total cost is lower than current cost, then go to number 2
        6. Else, depend on a function will determine whether tempSolution or new solution to be the new tempSolution
        7. Repeat number 2 until 6 until 1000 times
    """
    if (state.totalCost == 0):
        return state
    tempSolution = deepcopy(state)
    i = 0
    probability = 1
    while not((temperatur <= 1.0e-15) or (i >= 1000 ) or (tempSolution.totalCost == 0)) :
        stdout.write('Cost terbaik: {} {} | Iterasi: {} | Temperatur: {} | Probability: {}\r'.format(tempSolution.sameColorCost, tempSolution.diffColorCost, i, "%.15f" % temperatur, "%.15f" % probability))
        listPossibleState = helper.getListPossibleState(tempSolution)
        newSolution = random.choice(listPossibleState)
        if (tempSolution.totalCost > newSolution.totalCost) :
            tempSolution = newSolution
        else :
            delta = newSolution.totalCost-tempSolution.totalCost
            probability = numpy.exp(-delta/temperatur)
            if random.choice([True,False], p=[probability, 1-probability]):
                tempSolution = newSolution
        """
            Type of temperature change :
            type 1 : Constant
            type 2 : Linear
            type 3 : Logaritmic
        """
        if (type == '1') :
            temperatur = temperatur
        elif (type == '2') :
            temperatur = temperatur - value
        else :
            temperatur = temperatur*(1-value)
        i+=1
    stdout.write('Cost terbaik: {} {} | Iterasi: {} | Temperatur: {} | Probability: {}\r'.format(tempSolution.sameColorCost, tempSolution.diffColorCost, i, "%.15f" % temperatur, "%.15f" % probability))
    return tempSolution

def main(pawnInput):
    """
        main function of Simulated Annealing
    """
    typeF = 3
    temperatur = 10
    value = 0.2
    print("Pilih jenis fungsi temperatur yang diinginkan (default: 3)"),
    print("1. Constant")
    print("2. Linear")
    print("3. Logaritmic")
    inputTypeF = input(">> Pilihan: ")
    if (inputTypeF):
        typeF = inputTypeF
    print("Masukan Nilai Temperatur Awal (default: 10)"),
    inputTemperatur = input(">> ")
    if (inputTemperatur):
        temperatur = float(inputTemperatur)
    print("Masukan Nilai Pengurangan Temperatur (default: 0.2)"),
    inputValue = input(">> ")
    if (inputValue):
        value = float(inputValue)
    initState = State(pawnInput=pawnInput)
    return solve(initState, typeF, temperatur, value)
