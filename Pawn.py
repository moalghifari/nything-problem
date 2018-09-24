from constants import WHITE_PAWN, BLACK_PAWN

class Pawn:
    def __init__(self, type, x, y) :
        self.type = type
        self.x = x
        self.y = y
        self.listOfPossibleMove = []
        self.sameColorHeuristic = 0
        self.diffColorHeuristic = 0

    def outChessBoard(self, x, y) :
        if (x < 0 | x > 7 | y < 0 | y > 7)

    def generatePossibleMoves(self, chessBoard) :
        if (self.type == 'K' | self.type == 'k') :
            self.listOfPossibleMove.append(self.x+1, self.y+2)
            self.listOfPossibleMove.append(self.x+2, self.y+1)
            self.listOfPossibleMove.append(self.x+1, self.y-2)
            self.listOfPossibleMove.append(self.x+2, self.y-1)
            self.listOfPossibleMove.append(self.x-1, self.y+2)
            self.listOfPossibleMove.append(self.x-2, self.y+1)
            self.listOfPossibleMove.append(self.x-1, self.y-2)
            self.listOfPossibleMove.append(self.x-2, self.y-1)
        if (self.type == 'Q' | self.type == 'q') :
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x+i, self.y+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x-i, self.y-i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x-i, self.y+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x+i, self.y-i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x-i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.y+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.y-i)
        if (self.type == 'R' | self.type == 'r') :
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x-i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.y+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.y-i)
        if (self.type == 'B' | self.type == 'b') :
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x+i, self.y+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x-i, self.y-i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x-i, self.y+i)
            for i in range(8) :
                if (cornerChessBoard()) :
                    break
                else :
                    self.listOfPossibleMove.append(self.x+i, self.y-i)

    def calcSameColorHeuristic(self, chessBoard) :
        checkY = self.y
    	checkX = self.x
    	heuristic = 0

    	if (self.type =='K') :
    		if (chessBoard[checkX+1][checkY-2] in WHITE_PAWN) :
    			heuristic += 1
    		if (chessBoard[checkX+2][checkY-1] in WHITE_PAWN) :
    			heuristic += 1
    		if (chessBoard[checkX+2][checkY+1] in WHITE_PAWN) :
    			heuristic += 1
    		if (chessBoard[checkX+1][checkY+2] in WHITE_PAWN) :
    			heuristic += 1
    		if (chessBoard[checkX-1][checkY+2] in WHITE_PAWN) :
    			heuristic += 1
    		if (chessBoard[checkX-2][checkY+1] in WHITE_PAWN) :
    			heuristic += 1
    		if (chessBoard[checkX+2][checkY-1] in WHITE_PAWN) :
    			heuristic += 1
    		if (chessBoard[checkX+1][checkY-2] in WHITE_PAWN) :
    			heuristic += 1

    	if (self.type == 'R') :
    		# horizontal check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX+n][checkY] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX-n][checkY] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    		# vertical check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX][checkY-n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		stop = False
    		while (stop == False) :
    			if (chessBoard[checkX][checkY+n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    	if (self.type == 'B')
    	# diagonal right check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX+n][checkY-n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		stop = False
    		while (stop == False) :
    			if (chessBoard[checkX-n][checkY+n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    		# diagonal left check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX-n][checkY-n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		stop = False
    		while (stop == False) :
    			if (chessBoard[checkX+n][checkY+n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    	if (self.type == 'Q') :
    		# horizontal check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX+n][checkY] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX-n][checkY] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    		# vertical check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX][checkY-n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		stop = False
    		while (stop == False) :
    			if (chessBoard[checkX][checkY+n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    		# diagonal right check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX+n][checkY-n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		stop = False
    		while (stop == False) :
    			if (chessBoard[checkX-n][checkY+n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    		# diagonal left check
    		stop = False
    		n = 1
    		while (stop == False) :
    			if (chessBoard[checkX-n][checkY-n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1
    		stop = False
    		n = 1
    		stop = False
    		while (stop == False) :
    			if (chessBoard[checkX+n][checkY+n] in WHITE_PAWN)
    				heuristic += 1
    				stop = True
    			else :
    				n += 1

    	return heuristic

    def calcDiffColorHeuristic(self, chessBoard) :
