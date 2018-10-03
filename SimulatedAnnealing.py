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