from random import randint
from copy import deepcopy

import constants

class State:

    # Initialization
    def __init__(self, chessBoard=constants.EMPTY_CHESS_BOARD, listOfPawn=[], pawnInput=[]):
        self.chessBoard = deepcopy(chessBoard)
        self.listOfPawn = deepcopy(listOfPawn)
        if pawnInput:
            self.generateRandomChessBoard(pawnInput)
        self.sameColorHeuristic = self.calcSameColorHeuristic
        self.diffColorHeuristic = self.calcDiffColorHeuristic
        self.totalHeuristic = self.calcTotalHeuristic

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
                if (self.getElmtChessBoard(x, y) == '.'):
                    break

            self.listOfPawn.append({
                'pawnType': pawnType, 
                'x': x,
                'y': y
            })
            self.chessBoard[y][x] = pawnType

    # Menghitung heuristic
    def calcSameColorHeuristic(self):
        # Sekar's code
        return 999999
    def calcDiffColorHeuristic(self):
        # Sekar's code
        return 999999
    def calcTotalHeuristic(self):
        # Sekar's code
        return 999999

    # Print papan
    def printChessBoard(self):
        for baris in self.chessBoard:
            print(' '.join(baris))

    # Getter dan Setter
    def getChessBoard(self):
        return self.chessBoard
    def getListOfPawn(self):
        return self.listOfPawn
    def getElmtChessBoard(self, kol, bar):
        return self.chessBoard[bar][kol]
    def getElmtListOfPawn(self, idx):
        return self.listOfPawn[idx]
    def getSameColorHeuristic(self):
        return self.sameColorHeuristic
    def getDiffColorHeuristic(self):
        return self.diffColorHeuristic
    def getTotalHeuristic(self):
        return self.totalHeuristic
    def setChessBoard(self, chessBoard):
        self.chessBoard = chessBoard
    def setListOfPawn(self, listOfPawn):
        self.listOfPawn = listOfPawn
    def setElmtChessBoard(self, kol, bar, pawn):
        self.chessBoard[bar][kol] = pawn
    def setElmtListOfPawn(self, idx, pawn):
        self.listOfPawn[idx] = pawn
    def setSameColorHeuristic(self, sameColorHeuristic):
        self.sameColorHeuristic = sameColorHeuristic
    def setDiffColorHeuristic(self, diffColorHeuristic):
        self.diffColorHeuristic = diffColorHeuristic
    def setTotalHeuristic(self, totalHeuristic):
        self.totalHeuristic = totalHeuristic
    
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
    for i in state.getListOfPawn():
        print(i)

if __name__ == '__main__':
    main()
