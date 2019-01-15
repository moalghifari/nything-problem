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
        self.nWhite = self.calcNWhite()
        self.nBlack = self.calcNBlack()
        self.sameColorCost = self.calcSameColorCost()
        self.diffColorCost = self.calcDiffColorCost()
        self.totalCost = self.calcTotalCost()

    def calcNWhite(self):
        """
            calculate amount of white pawn in chessBoard
        """
        nWhite = 0
        for pawn in self.listOfPawn:
            if (pawn.type.isupper()):
                nWhite += 1
        return nWhite

    def calcNBlack(self):
        """
            calculate amount of black pawn in chessBoard
        """
        nBlack = 0
        for pawn in self.listOfPawn:
            if (pawn.type.islower()):
                nBlack += 1
        return nBlack

    def generateChessBoardByListOfPawn(self):
        """
            update chessboard state
        """
        for pawn in self.listOfPawn:
            self.chessBoard[pawn.y][pawn.x] = pawn.type

    def generateRandomChessBoard(self, pawnInput):
        """
            update chessBoard state adjust to pawn input
            generateRandomPawn to generate new pawn
            with random position of each pawn input
        """
        for pawn in pawnInput:
            # nanti variabel pawn ini bentuknya dictionary gitu {'pawnType': 'xxx', 'pawnCount}: 10}
            # gunanya ** itu biar key pada variabel pawn disebar menjadi parameter fungsi generateRandomPawn
            self.generateRandomPawn(**pawn)

    def generateRandomPawn(self, pawnType, pawnCount):
        """
            generate new Pawn with random position based on
            type of pawn and number of pawn with the type
            new pawn defined and included into listOfPawn
            chessBoard adjust to new pawn
        """
        for i in range(pawnCount):
            while True:
                x = randint(0, 7)
                y = randint(0, 7)
                if (self.chessBoard[y][x] == '.'):
                    break

            newPawn = Pawn(pawnType, x, y)
            self.listOfPawn.append(newPawn)
            self.chessBoard[y][x] = pawnType

    # Print papan
    def printChessBoard(self):
        """
            showing the condition of chess board with pawns inside
        """
        for rows in self.chessBoard:
            print(' '.join(rows))

    def move(self, pawn, possibleMove):
        """

        """
        self.chessBoard[pawn.y][pawn.x] = '.'
        self.chessBoard[possibleMove[1]][possibleMove[0]] = pawn.type
        pawn.move(possibleMove, self.chessBoard)
        self.sameColorCost = self.calcSameColorCost()
        self.diffColorCost = self.calcDiffColorCost()
        self.totalCost = self.calcTotalCost()

    def calcSameColorCost(self):
        """
            return the same color pawn cost
        """
        cost = 0
        for pawn in self.listOfPawn:
            cost += pawn.calcSameColorCost(self.chessBoard)
        return cost

    def calcDiffColorCost(self):
        """
            return the different color pawn cost
        """
        cost = 0
        for pawn in self.listOfPawn:
            cost += pawn.calcDiffColorCost(self.chessBoard)
        return cost

    def calcTotalCost(self):
        return (self.sameColorCost-self.diffColorCost+(self.nWhite*self.nBlack*2))

    def searchPawn(self, pawnX):
        """
            return the same pawn with input pawn
        """
        for pawn in self.listOfPawn:
            if (pawn.isEqual(pawnX)):
                return pawn
