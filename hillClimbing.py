def generateStateCandidates(currentState):
    listOfStateCandidates = []
    return listOfStateCandidates

def getMinimalHeuristicState(listOfStateCandidates):
    state = listOfStateCandidates[0]
    for stateCandidate in listOfStateCandidates:
        if (stateCandidate.getTotalHeuristic() < state.getTotalHeuristic()):
            state = stateCandidate
    return state

def solve(currentState):
    if (currentState.getTotalHeuristic() == 0):
        return currentState
    listOfStateCandidates = generateStateCandidates(currentState)
    minimalHeuristicState = getMinimalHeuristicState(listOfStateCandidates).getTotalHeuristic()
    if (minimalHeuristicState.getTotalHeuristic() >= currentState.getTotalHeuristic()):
        return currentState
    else:
        solve(minimalHeuristicState)