from constants import WHITE_PAWN, BLACK_PAWN
from State import State


class Pawn:
    def __init__(self, currentPawn) :
        """
            This is a constructor
            currentPawn is a dictionary
        """
        self.type = currentPawn["pawnType"]
        self.x = currentPawn["x"]
        self.y = currentPawn["y"]
        self.listOfPossibleMove = []
        self.sameColorHeuristic = 0
        self.diffColorHeuristic = 0

    def outChessBoard(self, x, y) :
        """
            return True if a point is outside the chess board
        """
        if (x < 0 or x > 7 or y < 0 or y > 7) :
            return True
        else :
            return False

    def checkHorizontal(self) :
        """
            return possible move points of pawn by checking from horizontal and vertical side
            use for Rook and Queen
        """
        PossibleMove = []
        # check right
        for i in range(1,8) :
            if (self.outChessBoard(self.x+i, self.y)) :
                break
            else :
                PossibleMove.append([self.x+i, self.y])
        # check left
        for i in range(1,8) :
            if (self.outChessBoard(self.x-i, self.y)) :
                break
            else :
                PossibleMove.append([self.x-i, self.y])
        # check down
        for i in range(1,8) :
            if (self.outChessBoard(self.x, self.y+i)) :
                break
            else :
                PossibleMove.append([self.x,self.y+i])
        # check up
        for i in range(7) :
            if (self.outChessBoard(self.x, self.y-i)) :
                break
            else :
                PossibleMove.append([self.x,self.y-i])
        return PossibleMove
    def checkDiagonal(self) :
        """
            return possible move points of pawn by checking from diagonal side
            use for Bishop and Queen
        """
        PossibleMove = []
        # check diagonal down right
        for i in range(1,8) :
            if (self.outChessBoard(self.x+i, self.y+i)) :
                break
            else :
                PossibleMove.append([self.x+i, self.y+i])
        # check diagonal up left
        for i in range(1,8) :
            if (self.outChessBoard(self.x-i, self.y-i)) :
                break
            else :
                PossibleMove.append([self.x-i, self.y-i])
        # check diagonal down left
        for i in range(1,8) :
            if (self.outChessBoard(self.x-i, self.y+i)) :
                break
            else :
                PossibleMove.append([self.x-i, self.y+i])
        # check diagonal up right
        for i in range(1,8) :
            if (self.outChessBoard(self.x+i, self.y-i)) :
                break
            else :
                PossibleMove.append([self.x+i, self.y-i])
        return PossibleMove

    def checkHorizontalHeuristic(self, pawn_color, Board) :
        """
            return heuristic of pawn by checking from horizontal and vertical side
            use for Rook and Queen
        """
        heuristic = 0
        # horizontal check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x+n, self.y)) and Board[self.y][self.x+n] in pawn_color) :
                heuristic += 1
                break
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x-n, self.y)) and Board[self.y][self.x-n] in pawn_color) :
                heuristic += 1
                break
        # vertical check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x, self.y-n)) and Board[self.y-n][self.x] in pawn_color) :
                heuristic += 1
                break
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x, self.y+n)) and Board[self.y+n][self.x] in pawn_color) :
                heuristic += 1
                break
        return heuristic
    def checkDiagonalHeuristic(self, pawn_color, Board) :
        """
            return heuristic of pawn by checking from diagonal side
            use for Bishop and Queen
        """
        heuristic = 0
        # diagonal down right check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x+n, self.y+n)) and Board[self.y+n][self.x+n] in pawn_color) :
                heuristic += 1
                break
        # diagonal up left check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x-n, self.y-n)) and Board[self.y-n][self.x-n] in pawn_color) :
                heuristic += 1
                break
        # diagonal down left check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x-n, self.y+n)) and Board[self.y+n][self.x-n] in pawn_color) :
                heuristic += 1
                break
        # diagonal up right check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x+n, self.y+n)) and Board[self.y-n][self.x+n] in pawn_color) :
                heuristic += 1
                break
        return heuristic

    def generatePossibleMoves(self, chessBoard) :
        """
            return possible move points of pawn based on the type
        """
        if (self.type == 'K' or self.type == 'k') :
            if (not(self.outChessBoard(self.x+1, self.y+2))) : self.listOfPossibleMove.append([self.x+1, self.y+2])
            if (not(self.outChessBoard(self.x+2, self.y+1))) : self.listOfPossibleMove.append([self.x+2, self.y+1])
            if (not(self.outChessBoard(self.x+1, self.y-2))) : self.listOfPossibleMove.append([self.x+1, self.y-2])
            if (not(self.outChessBoard(self.x+2, self.y-1))) : self.listOfPossibleMove.append([self.x+2, self.y-1])
            if (not(self.outChessBoard(self.x-1, self.y+2))) : self.listOfPossibleMove.append([self.x-1, self.y+2])
            if (not(self.outChessBoard(self.x-2, self.y+1))) : self.listOfPossibleMove.append([self.x-2, self.y+1])
            if (not(self.outChessBoard(self.x-1, self.y-2))) : self.listOfPossibleMove.append([self.x-1, self.y-2])
            if (not(self.outChessBoard(self.x-2, self.y-1))) : self.listOfPossibleMove.append([self.x-2, self.y-1])
        elif (self.type == 'Q' or self.type == 'q') :
            self.listOfPossibleMove.extend(self.checkDiagonal())
            self.listOfPossibleMove.extend(self.checkHorizontal())
        elif (self.type == 'R' or self.type == 'r') :
            self.listOfPossibleMove = self.checkHorizontal()
        elif (self.type == 'B' or self.type == 'b') :
            self.listOfPossibleMove = self.checkDiagonal()
        return self.listOfPossibleMove

    def calcHeuristic(self, chessBoard, pawn_color) :
        """
            return heuristic of pawn based on the type
            heuristic is the number of pawn that can be attacked by itself
        """
        heuristic = 0
        if (self.type == 'K' or self.type == 'k') :
            if (not(self.outChessBoard(self.x+1, self.y-2)) and chessBoard[self.y-2][self.x+1] in pawn_color) :
                heuristic += 1
            if (not(self.outChessBoard(self.x+2, self.y-1)) and chessBoard[self.y-1][self.x+2] in pawn_color) :
                heuristic += 1
            if (not(self.outChessBoard(self.x+2, self.y+1)) and chessBoard[self.y+1][self.x+2] in pawn_color) :
                heuristic += 1
            if (not(self.outChessBoard(self.x+1, self.y+2)) and chessBoard[self.y+2][self.x+1] in pawn_color) :
                heuristic += 1
            if (not(self.outChessBoard(self.x-1, self.y+2)) and chessBoard[self.y+2][self.x-1] in pawn_color) :
                heuristic += 1
            if (not(self.outChessBoard(self.x-2, self.y+1)) and chessBoard[self.y+1][self.x-2] in pawn_color) :
                heuristic += 1
            if (not(self.outChessBoard(self.x-2, self.y-1)) and chessBoard[self.y-1][self.x-2] in pawn_color) :
                heuristic += 1
            if (not(self.outChessBoard(self.x-1, self.y-2)) and chessBoard[self.y-2][self.x-1] in pawn_color) :
                heuristic += 1
        elif (self.type == 'R' or self.type == 'r') :
            heuristic = self.checkHorizontalHeuristic(pawn_color, chessBoard)
        elif (self.type == 'B' or self.type == 'b') :
            heuristic = self.checkDiagonalHeuristic(pawn_color, chessBoard)
        elif (self.type == 'Q' or self.type == 'q') :
            heuristic = heuristic + self.checkHorizontalHeuristic(pawn_color, chessBoard) + self.checkDiagonalHeuristic(pawn_color, chessBoard)
        return heuristic

    def calcSameColorHeuristic(self, chessBoard) :
        """
            return the same color pawn heuristic
            if black pawn then search for black pawn
            if white pawn then search for white pawn
        """
        if (self.type == 'K' or self.type == 'Q' or self.type == 'B' or self.type == 'R' ) :
            pawn_color = WHITE_PAWN
        else :
            pawn_color = BLACK_PAWN
        return self.calcHeuristic(chessBoard, pawn_color)

    def calcDiffColorHeuristic(self, chessBoard) :
        """
            return the different color pawn heuristic
            if black pawn then search for white pawn
            if white pawn then search for black pawn
        """
        if (self.type == 'K' or self.type == 'Q' or self.type == 'B' or self.type == 'R' ) :
            pawn_color = BLACK_PAWN
        else :
            pawn_color = WHITE_PAWN
        return self.calcHeuristic(chessBoard, pawn_color)


def main() :
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
        }, {
            'pawnType':'q',
            'pawnCount': 2
        }
    ]
    state = State(pawnInput=pawnInput)
    a = Pawn(state.listOfPawn[6])
    n = a.generatePossibleMoves(state.chessBoard)
    j = a.calcSameColorHeuristic(state.chessBoard)
    print("this pawn = ", state.listOfPawn[6])
    print("possible moves = ", n)
    print("same color heuristic = ", j)
    state.printChessBoard()


if __name__ == '__main__':
    main()
