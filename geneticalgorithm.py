from State import State
from numpy import random

POPULATION_NUMBER = 10
MUTATION_RATE = 0.1

# totalPopulationHeuristic: sum of all heuristic of all states in population
# fitness function = 1 - heuristic / totalPopulationHeuristic

def solve(pop=[], pawnInput=[]):
  totalPopulationHeuristic = 0
  fitness = []

  if not pop and not pawnInput:
    raise Exception('Cannot solve nything problem using genetic algorithm without pawn information')
  elif pop:
    population = pop
  else:
    population = generateListOfRandomPopulation(POPULATION_NUMBER, pawnInput)

  for individual in population:
    totalPopulationHeuristic += individual.getTotalHeuristic()

  # counting fitness function for each individual
  for individual in population:
    fitness.append(1 - float(individual.getTotalHeuristic()) / totalPopulationHeuristic)

  for i in POPULATION_NUMBER:
    



  



def generateListOfRandomPopulation(populationNumber, pawnInput):
  population = []
  for i in range(populationNumber):
    population.append(State(pawnInput=pawnInput))
  return population

def crossover(state1, state2):
