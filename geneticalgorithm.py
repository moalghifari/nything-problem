from numpy import random
from math import ceil
from copy import deepcopy
from time import sleep
from random import randint
from sys import stdout

from State import State
from InvalidInputError import InvalidInputError

POPULATION_NUMBER = 10
MUTATION_RATE = 0.2
GENERATION_LIMIT = 2000

def inputGA():
  global POPULATION_NUMBER, MUTATION_RATE, GENERATION_LIMIT

  # Input POPULATION_NUMBER
  while True:
    inputPopNumber = input('\rMasukkan Jumlah Populasi (default=10): ')
    if inputPopNumber == '':
      break
    try:
      inputPopNumber = int(inputPopNumber)
      if inputPopNumber <= 1:
        raise InvalidInputError
      POPULATION_NUMBER = inputPopNumber
      break
    except ValueError:
      stdout.write('\rMasukan bukan angka, coba lagi')
      # stdout.flush()
      sleep(2)
    except InvalidInputError:
      stdout.write('\rMasukan harus lebih dari 1, coba lagi')
      # stdout.flush()
      sleep(2)
  
  # Input MUTATION_RATE
  while True:
    inputMutRate = input('\rMasukkan Mutation Rate (default=0.2): ')
    if inputMutRate == '':
      break
    try:
      inputMutRate = float(inputMutRate)
      if inputMutRate <= 0:
        raise InvalidInputError
      MUTATION_RATE = inputMutRate
      break
    except ValueError:
      stdout.write('\rMasukan bukan float, coba lagi')
      stdout.flush()
      sleep(2)
    except InvalidInputError:
      stdout.write('\rMasukan harus lebih dari 0.0, coba lagi')
      stdout.flush()
      sleep(2)

  # Input GENERATION_LIMIT
  while True:
    inputGenLimit = input('\rMasukkan Batas Generasi (default=2000): ')
    if inputGenLimit == '':
      break
    try:
      inputGenLimit = int(inputGenLimit)
      if inputGenLimit <= 0:
        raise InvalidInputError
      GENERATION_LIMIT = inputGenLimit
      break
    except ValueError:
      stdout.write('\rMasukan bukan angka, coba lagi')
      stdout.flush()
      sleep(2)
    except InvalidInputError:
      stdout.write('\rMasukan harus lebih dari 0, coba lagi')
      stdout.flush()
      sleep(2)

def main(pawnInput):
  inputGA()

  population = generateListOfRandomPopulation(POPULATION_NUMBER, pawnInput)
  generation = 0
  bestIndividual = None

  while generation <= GENERATION_LIMIT:
    stdout.write('\rGeneration: {}'.format(generation))
    population = solve(population)
    if (bestIndividual == None or bestIndividual.totalHeuristic > population[0].totalHeuristic):
      bestIndividual = population[0]
    generation += 1
    if (population[0].totalHeuristic == 0):
      break
  
  print('\nPopulasi: {}'.format(POPULATION_NUMBER))
  print('Mutation Rate: {}'.format(MUTATION_RATE))

  return bestIndividual

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

  for _ in range(int(ceil(POPULATION_NUMBER/2.0))):
    # choose 2 parents randomly based on the fitness function
    parentIndex1 = random.choice(range(POPULATION_NUMBER), p=fitness)
    while True:
      parentIndex2 = random.choice(range(POPULATION_NUMBER), p=fitness)
      if parentIndex2 != parentIndex1:
        break
    # crossover those 2 parents, concate the children to childrenPopulation
    childrenPopulation += crossOver(population[parentIndex1], population[parentIndex2])
  
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

  while True:
    listOfPawn1 = deepcopy(state1.listOfPawn[:pivot] + state2.listOfPawn[pivot:])
    listOfPawn2 = deepcopy(state2.listOfPawn[:pivot] + state1.listOfPawn[pivot:])

    if not(isConflict(listOfPawn1)) and not(isConflict(listOfPawn2)):
      children.append(mutate(listOfPawn1))
      children.append(mutate(listOfPawn2))
      return children
    pivot = (pivot - 1) % (pawnCount + 1)

def isConflict(listOfPawn):
  for i in range(len(listOfPawn) - 1):
    j = i + 1
    while j < len(listOfPawn):
      if listOfPawn[i].x == listOfPawn[j].x and listOfPawn[i].y == listOfPawn[j].y:
        return True
      j += 1
  return False

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