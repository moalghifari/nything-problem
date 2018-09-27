from numpy import random
from math import ceil
from copy import deepcopy

from State import State

POPULATION_NUMBER = 10
MUTATION_RATE = 0.01


def main(pawnInput):
  population = generateListOfRandomPopulation(POPULATION_NUMBER, pawnInput)
  return solve(population)

# totalPopulationHeuristic: sum of all heuristic of all states in population
# fitness function = 1 - heuristic / totalPopulationHeuristic

def solve(population):
  totalPopulationHeuristic = 0.0
  fitness = []
  childrenPopulation = []

  # check if there is a state with the best heuristic, if there is one, then return the state
  for individual in population:
    if individual.totalHeuristic == 0:
      return individual

  for individual in population:
    totalPopulationHeuristic += individual.totalHeuristic

  # calculate fitness function for each individual
  for individual in population:
    fitness.append(1 - individual.totalHeuristic / totalPopulationHeuristic)

  print('Total Heuristik Populasi: ' + str(totalPopulationHeuristic))
  for individual in population:
    print('individu: ' + str(individual.totalHeuristic))
  print(fitness)

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

  return solve(childrenPopulation)

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
  
def mutate(listOfPawn):
  if random.choice([True, False], p=[MUTATION_RATE, 1-MUTATION_RATE]):
    index = random.choice(range(len(listOfPawn)))
    while True:
      x = random.choice(range(8))
      y = random.choice(range(8))
      if not filter(lambda pawn: pawn.x == x and pawn.y == y, listOfPawn):
        break
    listOfPawn[index].x = x
    listOfPawn[index].y = y
    return State(listOfPawn=listOfPawn)
  else:
    return State(listOfPawn=listOfPawn)


def mainBet():
  inputPawn = [
    {
      'pawnType': 'K',
      'pawnCount': 2
    }, 
    {
      'pawnType': 'B',
      'pawnCount': 2
    }, 
    {
      'pawnType': 'R',
      'pawnCount': 2
    }, 
    {
      'pawnType': 'Q',
      'pawnCount': 2
    }
  ]

  res = main(inputPawn)

  res.printChessBoard()

mainBet()