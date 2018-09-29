from numpy import random
from math import ceil
from copy import deepcopy
from time import sleep
from random import randint

from State import State

POPULATION_NUMBER = 10
MUTATION_RATE = 0.1


def main(pawnInput):
  population = generateListOfRandomPopulation(POPULATION_NUMBER, pawnInput)
  generation = 0

  # while generation <= 5000:
  while True:
    population = solve(population)
    generation += 1
    if (population[0].totalHeuristic == 0):
      break

  result = {
    'state': population[0],
    'population': POPULATION_NUMBER,
    'generation': generation,
    'mutationRate': MUTATION_RATE
  }

  return result

# totalPopulationHeuristic: sum of all heuristic of all states in population
# fitness function = 1 - heuristic / totalPopulationHeuristic

def solve(population):
  totalPopulationHeuristic = 0.0
  fitness = []
  childrenPopulation = []

  population.sort(key=lambda individual: individual.totalHeuristic)

  for individual in population:
    totalPopulationHeuristic += individual.totalHeuristic

  # calculate fitness function for each individual
  for individual in population:
    fitness.append(individual.totalHeuristic / totalPopulationHeuristic)
  fitness.sort(reverse=True)

  # Testing
  # print('Total Heuristik Populasi: ' + str(totalPopulationHeuristic))
  # for individual in population:
  #   print('individu: ' + str(individual.totalHeuristic))
  # print(fitness)
  # Testing

  for _ in range(int(ceil(POPULATION_NUMBER/2.0))):
    # choose 2 parents randomly based on the fitness function
    parent1 = random.choice(population, p=fitness)
    while True:
      parent2 = random.choice(population, p=fitness)
      if parent2 != parent1:
        break
    # crossover those 2 parents, concate the children to childrenPopulation
    childrenPopulation += crossOver(parent1, parent2)
  
  # If there is an odd number of population -> generate excess one children and needs to be removed
  if len(childrenPopulation) > POPULATION_NUMBER:
    childrenPopulation.pop()

  return childrenPopulation

def generateListOfRandomPopulation(populationNumber, pawnInput):
  population = []
  for _ in range(populationNumber):
    population.append(State(pawnInput=pawnInput))
  return population

def crossOver(state1, state2):
  children = []
  pawnCount = len(state1.listOfPawn)

  pivot = random.choice(range(pawnCount))

  listOfPawn1 = deepcopy(state1.listOfPawn[:pivot] + state2.listOfPawn[pivot:])
  listOfPawn2 = deepcopy(state2.listOfPawn[:pivot] + state1.listOfPawn[pivot:])

  children.append(mutate(listOfPawn1))
  children.append(mutate(listOfPawn2))
  
  return children

def isPosOccupied(x, y, listOfPawn):
  for pawn in listOfPawn:
    if (x == pawn.x and y == pawn.y):
      return True
  return False

def mutate(listOfPawn):
  if random.choice([True, False], p=[MUTATION_RATE, 1-MUTATION_RATE]):
    index = random.choice(range(len(listOfPawn)))
    while True:
      x = randint(0, 7)
      y = randint(0, 7)
      if not isPosOccupied(x, y, listOfPawn):
        break
    listOfPawn[index].x = x
    listOfPawn[index].y = y
    return State(listOfPawn=listOfPawn)
  else:
    return State(listOfPawn=listOfPawn)