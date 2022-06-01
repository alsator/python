START_POSITION = {'b': [1,2,9,10], 'w': [55,56,63,64]}

GOAL = {'w': [1,2,9,10], 'b': [55,56,63,64]}

MOVES_LIMIT = 80

class Agent:
    position = {}
    color = ''
    move_number = 0

    def __init__(self, color, position=START_POSITION, goal=GOAL[color], move_number=0):
        self.position = position
        self.color = color
        self.move_number = move_number

    def makeMove(self, source, target):
        if not (self.isValidSquare(source) and self.isValidSquare(target)):
            return 0
        if not (self.fromNotEmpty(source) and self.toIsEmpty(target)):
            return 0
        self.position[target] = self.position[source]
        del self.position[source]
        print(self.convertSquare(source) + " -> " + self.convertSquare(target))

    def boardOutput(self):
        rows = []
        for i in list(range(1,9)):
            row = []
            for j in list(range(1,9)):
                pos = (i - 1) * 8 + j
                if pos in self.position:
                    row.append(self.position[pos])
                else:
                    row.append(' ')
            print(row)
            rows.append(row)
        print('\n')

    def convertSquare(self, sq):
        v = sq % 8
        h = sq * -1 // 8 * -1
        v = {
            1:'a',
            2:'b',
            3:'c',
            4:'d',
            5:'e',
            6:'f',
            7:'g',
            0:'h'
        }[v]
        return str(v) + str(h)

    def isValidSquare(self, sq):
        return 1 <= sq <= 64

    def isNeighbour(self, source, target):
        if (abs(source % 8 - target % 8) == 0 and abs(source - target) == 8):
            # same vertical
            return 1
        if (abs(source * -1 // 8 * -1 - target * -1 // 8 * -1) == 0 and abs(source - target) == 1):
            # same horizontal
            return 1
        return 0

    def fromNotEmpty(self, fr):
        if fr in self.position:
            return 1
        return 0

    def toIsEmpty(self, to):
        if (to not in self.position):
            return 1
        return 0

    def isValidPartialMove(self, fr, to):
        if abs(fr - to) == 1 or abs(fr - to) == 8:
            return 1
        return 0

    def isValidPartialJump(self, source, target):
        if not self.isValidSquare(target):
            return 0
        if not self.toIsEmpty(target):
            return 0
        if (abs(source % 8 - target % 8) == 0 and abs(source - target) == 16):
            # same vertical
            return 1
        if (abs(source * -1 // 8 * -1 - target * -1 // 8 * -1) == 0 and abs(source - target) == 2):
            # same horizontal
            return 1
        return 0

    def hasNaighbourAt(self, sourse, target):
        if target not in self.position:
            return 0
        if not self.isNeighbour(sourse, target):
            return 0
        if not self.isValidSquare(target):
            return 0
        if self.toIsEmpty(target):
            return 0
        return 1

    def getPossibleNearestSqures(self, sq):
        squares = []
        if self.isValidSquare(sq - 1) \
                and self.toIsEmpty(sq - 1) \
                and self.isNeighbour(sq, sq - 1):
            squares.append(sq - 1)
        if self.isValidSquare(sq + 1) \
                and self.toIsEmpty(sq + 1) \
                and self.isNeighbour(sq, sq +1):
            squares.append(sq + 1)
        if self.isValidSquare(sq - 8) \
                and self.toIsEmpty(sq - 8) \
                and self.isNeighbour(sq, sq - 8):
            squares.append(sq - 8)
        if self.isValidSquare(sq + 8) \
                and self.toIsEmpty(sq + 8) \
                and self.isNeighbour(sq, sq + 8):
            squares.append(sq + 8)
        return squares

    def getPossibleJumps(self, sq, possibleJumps=[], path=[]):
        path.append(sq)
        if self.isValidPartialJump(sq, sq - 2) \
                and self.hasNaighbourAt(sq, sq - 1) \
                and not possibleJumps.__contains__(sq - 2) \
                and self.toIsEmpty(sq - 2):
            possibleJumps.append(sq - 2)
        if self.isValidPartialJump(sq, sq + 2) \
                and self.hasNaighbourAt(sq, sq + 1) \
                and not possibleJumps.__contains__(sq + 2) \
                and self.toIsEmpty(sq + 2):
            possibleJumps.append(sq + 2)
        if self.isValidPartialJump(sq, sq - 16) \
                and self.hasNaighbourAt(sq, sq - 8) \
                and not possibleJumps.__contains__(sq - 16) \
                and self.toIsEmpty(sq -16):
            possibleJumps.append(sq - 16)
        if self.isValidPartialJump(sq, sq + 16) \
                and self.hasNaighbourAt(sq, sq + 8) \
                and not possibleJumps.__contains__(sq + 16) \
                and self.toIsEmpty(sq + 16):
            possibleJumps.append(sq + 16)

        if possibleJumps.__contains__(sq - 2) and not path.__contains__(sq - 2):
            self.getPossibleJumps(sq - 2, possibleJumps, path)
        if possibleJumps.__contains__(sq + 2) and not path.__contains__(sq + 2):
            self.getPossibleJumps(sq + 2, possibleJumps, path)
        if possibleJumps.__contains__(sq - 16) and not path.__contains__(sq - 16):
            self.getPossibleJumps(sq - 16, possibleJumps, path)
        if possibleJumps.__contains__(sq + 16) and not path.__contains__(sq + 16):
            self.getPossibleJumps(sq + 16, possibleJumps, path)
        return

    def listPieceValidMoves(self, sq):
        possibleMoves = self.getPossibleNearestSqures(sq)
        possibleJumps = []
        self.getPossibleJumps(sq, possibleJumps, [])
        return possibleMoves + possibleJumps

    def listValidMoves(self, color):
        pieces = self.position[self.color]
        validMoves = []
        for piece in pieces:
            validMoves.append([piece, self.listPieceValidMoves(piece)])
        return validMoves

    def estimateMove(self, source, target):
        color = self.position[source]
        goal = self.getGoal(color)
        verticals2goal = abs(goal - target) % 8
        horizontals2goal = abs(goal - target) // 8
        return verticals2goal + horizontals2goal

    def getGoal(self, color):
        enemyHome = {
            'w': {1,2,9,10},
            'b': {64,63,56,55}
        }[color]

        for sq in enemyHome:
            if sq not in self.position or self.position[sq] != color:
                return sq
        exit

    def chooseMove(self, color):
        validMoves = self.listValidMoves(color)
        estimations = []
        min = 16
        for movePossibilities in validMoves:
            source = movePossibilities[0]
            targets = movePossibilities[1]
            for target in targets:
                estimations.append([source, target, self.estimateMove(source, target)])
        for estimation in estimations:
            if estimation[2] < min:
                min = estimation[2]
                choosen = estimation
        return choosen

    def play(self,color):
        moves_counter = 0
        while(moves_counter <= MOVES_LIMIT):
            self.boardOutput()
            choosen = self.chooseMove(color)
            self.makeMove(choosen[0], choosen[1])
            moves_counter += 1
            if color == 'w':
                color = 'b'
            else: 
                color = 'w'

game = Agent()
game.play('w')
