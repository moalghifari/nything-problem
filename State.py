from random import randint

import constants

class State:

    # Initialization
    def __init__(self, chessBoard=constants.EMPTY_CHESS_BOARD, listOfPawn=[], pawnInput=[]):
        self.chessBoard = chessBoard
        self.listOfPawn = listOfPawn
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
                if (self.chessBoard[x][y] == '.'):
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

    def move(self, pawn, possibleMove):
        self.chessBoard[pawn.x][pawn.y] = '.'
        self.chessBoard[possibleMove.x][possibleMove.y] = pawn.type
        pawn.move(possibleMove)

    
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
    for i in state.listOfPawn:
        print(i)

if __name__ == '__main__':
    main()
