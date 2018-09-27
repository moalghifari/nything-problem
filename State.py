from random import randint
from copy import deepcopy
from Pawn import Pawn
import constants

class State:

    # Initialization
    def __init__(self, chessBoard=constants.EMPTY_CHESS_BOARD, listOfPawn=[], pawnInput=[]):
        self.chessBoard = deepcopy(chessBoard)
        self.listOfPawn = deepcopy(listOfPawn)
        if pawnInput:
            self.generateRandomChessBoard(pawnInput)
        if (listOfPawn and (chessBoard == constants.EMPTY_CHESS_BOARD)):
            self.generateChessBoardByListOfPawn()
        self.sameColorHeuristic = self.calcSameColorHeuristic()
        self.diffColorHeuristic = self.calcDiffColorHeuristic()
        self.totalHeuristic = self.calcTotalHeuristic()

    def generateChessBoardByListOfPawn(self):
        for pawn in self.listOfPawn:
            self.chessBoard[pawn.y][pawn.x] = pawn.type

    # Generate Random Pawn Pada Papan Sesuai dengan Input
    def generateRandomChessBoard(self, pawnInput):
        for pawn in pawnInput:
            # nanti variabel pawn ini bentuknya dictionary gitu {'pawnType': 'xxx', 'pawnCount}: 10}
            # gunanya ** itu biar key pada variabel pawn disebar menjadi parameter fungsi generateRandomPawn
            self.generateRandomPawn(**pawn)

    def generateRandomPawn(self, pawnType, pawnCount):
        for i in range(pawnCount):
            while True:
                x = randint(0, 7)
                y = randint(0, 7)
                if (self.chessBoard[x][y] == '.'):
                    break

            newPawn = Pawn(pawnType, x, y)
            self.listOfPawn.append(newPawn)
            self.chessBoard[y][x] = pawnType

    # Print papan
    def printChessBoard(self):
        for baris in self.chessBoard:
            print(' '.join(baris))

    def move(self, pawn, possibleMove):
        self.chessBoard[pawn.y][pawn.x] = '.'
        self.chessBoard[possibleMove[1]][possibleMove[0]] = pawn.type
        pawn.move(possibleMove, self.chessBoard)
        self.sameColorHeuristic = self.calcSameColorHeuristic()
        self.diffColorHeuristic = self.calcDiffColorHeuristic()
        self.totalHeuristic = self.calcTotalHeuristic()

    def calcSameColorHeuristic(self):
        heuristic = 0
        for pawn in self.listOfPawn:
            heuristic += pawn.calcSameColorHeuristic(self.chessBoard)
        return heuristic
    
    def calcDiffColorHeuristic(self):
        heuristic = 0
        for pawn in self.listOfPawn:
            heuristic += pawn.calcDiffColorHeuristic(self.chessBoard)
        return heuristic

    def calcTotalHeuristic(self):
        return (self.calcSameColorHeuristic())

    def searchPawn(self, pawnX):
        for pawn in self.listOfPawn:
            if (pawn.isEqual(pawnX)):
                return pawn

# Test Main Program
def main():
    #TES
    pawnInput = [
        {
            'pawnType': 'K',
            'pawnCount': 2
        }, {
            'pawnType':'B',
            'pawnCount': 2
        }, {
            'pawnType':'R',
            'pawnCount': 2
        }, {
            'pawnType':'Q',
            'pawnCount': 2
        }
    ]
    state = State(pawnInput=pawnInput)
    state.printChessBoard()
    
    print("DiffColorHeuristic : ", state.calcDiffColorHeuristic())
    print("SameColorHeuristic : ", state.calcSameColorHeuristic())
    print("TotalHeuristic : ", state.calcTotalHeuristic())

if __name__ == '__main__':
    main()
