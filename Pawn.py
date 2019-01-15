from constants import WHITE_PAWN, BLACK_PAWN


class Pawn:
    def __init__(self, type, x, y) :
        """
            This is a constructor
            currentPawn is a dictionary
        """
        self.type = type
        self.x = x
        self.y = y
        self.listOfPossibleMove = []

    def outChessBoard(self, x, y) :
        """
            return True if a point is outside the chess board
        """
        if (x < 0 or x > 7 or y < 0 or y > 7) :
            return True
        else :
            return False

    def checkHorizontal(self, chessBoard) :
        """
            return possible move points of pawn by checking from horizontal and vertical side
            use for Rook and Queen
        """
        PossibleMove = []
        # check right
        for i in range(1,8) :
            if (self.outChessBoard(self.x+i, self.y) or (chessBoard[self.y][self.x+i] != '.')) :
                break
            else :
                PossibleMove.append([self.x+i, self.y])
        # check left
        for i in range(1,8) :
            if (self.outChessBoard(self.x-i, self.y) or (chessBoard[self.y][self.x-i] != '.')) :
                break
            else :
                PossibleMove.append([self.x-i, self.y])
        # check down
        for i in range(1,8) :
            if (self.outChessBoard(self.x, self.y+i) or (chessBoard[self.y+i][self.x] != '.')) :
                break
            else :
                PossibleMove.append([self.x,self.y+i])
        # check up
        for i in range(7) :
            if (self.outChessBoard(self.x, self.y-i) or (chessBoard[self.y-i][self.x] != '.')) :
                break
            else :
                PossibleMove.append([self.x,self.y-i])
        return PossibleMove
    def checkDiagonal(self, chessBoard) :
        """
            return possible move points of pawn by checking from diagonal side
            use for Bishop and Queen
        """
        PossibleMove = []
        # check diagonal down right
        for i in range(1,8) :
            if (self.outChessBoard(self.x+i, self.y+i) or (chessBoard[self.y+i][self.x+i] != '.')) :
                break
            else :
                PossibleMove.append([self.x+i, self.y+i])
        # check diagonal up left
        for i in range(1,8) :
            if (self.outChessBoard(self.x-i, self.y-i) or (chessBoard[self.y-i][self.x-i] != '.')) :
                break
            else :
                PossibleMove.append([self.x-i, self.y-i])
        # check diagonal down left
        for i in range(1,8) :
            if (self.outChessBoard(self.x-i, self.y+i) or (chessBoard[self.y+i][self.x-i] != '.')) :
                break
            else :
                PossibleMove.append([self.x-i, self.y+i])
        # check diagonal up right
        for i in range(1,8) :
            if (self.outChessBoard(self.x+i, self.y-i) or (chessBoard[self.y-i][self.x+i] != '.')) :
                break
            else :
                PossibleMove.append([self.x+i, self.y-i])
        return PossibleMove

    def checkHorizontalCost(self, pawn_color, Board) :
        """
            return cost of pawn by checking from horizontal and vertical side
            use for Rook and Queen
        """
        cost = 0
        # horizontal check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x+n, self.y)) and Board[self.y][self.x+n] in pawn_color) :
                cost += 1
                break
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x-n, self.y)) and Board[self.y][self.x-n] in pawn_color) :
                cost += 1
                break
        # vertical check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x, self.y-n)) and Board[self.y-n][self.x] in pawn_color) :
                cost += 1
                break
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x, self.y+n)) and Board[self.y+n][self.x] in pawn_color) :
                cost += 1
                break
        return cost
    def checkDiagonalCost(self, pawn_color, Board) :
        """
            return cost of pawn by checking from diagonal side
            use for Bishop and Queen
        """
        cost = 0
        # diagonal down right check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x+n, self.y+n)) and Board[self.y+n][self.x+n] in pawn_color) :
                cost += 1
                break
        # diagonal up left check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x-n, self.y-n)) and Board[self.y-n][self.x-n] in pawn_color) :
                cost += 1
                break
        # diagonal down left check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x-n, self.y+n)) and Board[self.y+n][self.x-n] in pawn_color) :
                cost += 1
                break
        # diagonal up right check
        for n in range(1,8) :
            if (not(self.outChessBoard(self.x+n, self.y-n)) and Board[self.y-n][self.x+n] in pawn_color) :
                cost += 1
                break
        return cost

    def generatePossibleMoves(self, chessBoard) :
        """
            return possible move points of pawn based on the type
        """
        self.listOfPossibleMove = []
        if (self.type == 'K' or self.type == 'k') :
            if (not(self.outChessBoard(self.x+1, self.y+2)) and (chessBoard[self.y+2][self.x+1] == '.')) : self.listOfPossibleMove.append([self.x+1, self.y+2])
            if (not(self.outChessBoard(self.x+2, self.y+1)) and (chessBoard[self.y+1][self.x+2] == '.')) : self.listOfPossibleMove.append([self.x+2, self.y+1])
            if (not(self.outChessBoard(self.x+1, self.y-2)) and (chessBoard[self.y-2][self.x+1] == '.')) : self.listOfPossibleMove.append([self.x+1, self.y-2])
            if (not(self.outChessBoard(self.x+2, self.y-1)) and (chessBoard[self.y-1][self.x+2] == '.')) : self.listOfPossibleMove.append([self.x+2, self.y-1])
            if (not(self.outChessBoard(self.x-1, self.y+2)) and (chessBoard[self.y+2][self.x-1] == '.')) : self.listOfPossibleMove.append([self.x-1, self.y+2])
            if (not(self.outChessBoard(self.x-2, self.y+1)) and (chessBoard[self.y+1][self.x-2] == '.')) : self.listOfPossibleMove.append([self.x-2, self.y+1])
            if (not(self.outChessBoard(self.x-1, self.y-2)) and (chessBoard[self.y-2][self.x-1] == '.')) : self.listOfPossibleMove.append([self.x-1, self.y-2])
            if (not(self.outChessBoard(self.x-2, self.y-1)) and (chessBoard[self.y-1][self.x-2] == '.')) : self.listOfPossibleMove.append([self.x-2, self.y-1])
        elif (self.type == 'Q' or self.type == 'q') :
            self.listOfPossibleMove.extend(self.checkDiagonal(chessBoard))
            self.listOfPossibleMove.extend(self.checkHorizontal(chessBoard))
        elif (self.type == 'R' or self.type == 'r') :
            self.listOfPossibleMove = self.checkHorizontal(chessBoard)
        elif (self.type == 'B' or self.type == 'b') :
            self.listOfPossibleMove = self.checkDiagonal(chessBoard)

    def calcCost(self, chessBoard, pawn_color) :
        """
            return cost of pawn based on the type
            cost is the number of pawn that can be attacked by itself
        """
        cost = 0
        if (self.type == 'K' or self.type == 'k') :
            if (not(self.outChessBoard(self.x+1, self.y-2)) and chessBoard[self.y-2][self.x+1] in pawn_color) :
                cost += 1
            if (not(self.outChessBoard(self.x+2, self.y-1)) and chessBoard[self.y-1][self.x+2] in pawn_color) :
                cost += 1
            if (not(self.outChessBoard(self.x+2, self.y+1)) and chessBoard[self.y+1][self.x+2] in pawn_color) :
                cost += 1
            if (not(self.outChessBoard(self.x+1, self.y+2)) and chessBoard[self.y+2][self.x+1] in pawn_color) :
                cost += 1
            if (not(self.outChessBoard(self.x-1, self.y+2)) and chessBoard[self.y+2][self.x-1] in pawn_color) :
                cost += 1
            if (not(self.outChessBoard(self.x-2, self.y+1)) and chessBoard[self.y+1][self.x-2] in pawn_color) :
                cost += 1
            if (not(self.outChessBoard(self.x-2, self.y-1)) and chessBoard[self.y-1][self.x-2] in pawn_color) :
                cost += 1
            if (not(self.outChessBoard(self.x-1, self.y-2)) and chessBoard[self.y-2][self.x-1] in pawn_color) :
                cost += 1
        elif (self.type == 'R' or self.type == 'r') :
            cost = self.checkHorizontalCost(pawn_color, chessBoard)
        elif (self.type == 'B' or self.type == 'b') :
            cost = self.checkDiagonalCost(pawn_color, chessBoard)
        elif (self.type == 'Q' or self.type == 'q') :
            cost = cost + self.checkHorizontalCost(pawn_color, chessBoard) + self.checkDiagonalCost(pawn_color, chessBoard)
        return cost

    def calcSameColorCost(self, chessBoard) :
        """
            return the same color pawn cost
            if black pawn then search for black pawn
            if white pawn then search for white pawn
        """
        if (self.type == 'K' or self.type == 'Q' or self.type == 'B' or self.type == 'R' ) :
            pawn_color = WHITE_PAWN
        else :
            pawn_color = BLACK_PAWN
        return self.calcCost(chessBoard, pawn_color)

    def calcDiffColorCost(self, chessBoard) :
        """
            return the different color pawn cost
            if black pawn then search for white pawn
            if white pawn then search for black pawn
        """
        if (self.type == 'K' or self.type == 'Q' or self.type == 'B' or self.type == 'R' ) :
            pawn_color = BLACK_PAWN
        else :
            pawn_color = WHITE_PAWN
        return self.calcCost(chessBoard, pawn_color)

    def move(self, currentPosition, chessBoard):
        """
            update list of PossibleMove and position of pawn
        """
        self.x = currentPosition[0]
        self.y = currentPosition[1]
        self.generatePossibleMoves(chessBoard)

    def isEqual(self, pawn):
        """
            return True if input pawn is equal with itself
        """
        return (self.type == pawn.type and self.x == pawn.x and self.y == pawn.y)
