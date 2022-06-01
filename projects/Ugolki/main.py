# import pprint
# import collections
# import numpy as np

# START_POSITION = "bb6/bb6/8/8/8/8/6ww/6ww"


# class Game:
#     position = {}
#     turn = 'w'
#     move_number = 0
#
#     def __init__(self, position=START_POSITION, turn='w', move_number=0):
#         self.position = self.ufenPositionToArray(position)
#         self.turn = turn
#         self.move_number = move_number
#
#     def makeMove(self, fr, to):
#         fr = self.convertSquare(fr)
#         to = self.convertSquare(to)
#         if not (self.isValidSquare(fr) and self.isValidSquare(to)):
#             return 0
#         if not (self.fromNotEmpty(fr) and self.toIsEmpty(to)):
#             return 0
#         fr = np.fromiter(fr, dtype=int)
#         to = np.fromiter(to, dtype=int)
#         self.position[to[0]][to[1]] = self.position[fr[0]][fr[1]]
#         del self.position[fr[0]][fr[1]]
#
#     def boardOutput(self):
#         for i in self.position:
#             print(self.position[i])
#         # out = []
#         # for row in self.position:
#         # out_col = []
#         # if col in self.position:
#         #     for col in list(range(8)):
#         # if row in self.position[col]:
#         #     out_col.append(self.position[col][row])
#         # else:
#         #     out_col.append(' ')
#         # else:
#         #     out_col = [' ' for i in range(8)]
#         # out.append(out_col)
#         # print(np.rot90(np.fliplr(self.position)))
#
#     def convertSquare(self, sq):
#         sq = list(sq)
#         sq[0] = {
#             'a': 0,
#             'b': 1,
#             'c': 2,
#             'd': 3,
#             'e': 4,
#             'f': 5,
#             'g': 6,
#             'h': 7
#         }[sq[0]]
#         return str(sq[0]) + str(sq[1])
#
#     def isValidSquare(self, sq):
#         sq = np.fromiter(sq, dtype=int)
#         return (1 <= sq[0] <= 8) and (1 <= sq[1] <= 8)
#
#     def fromNotEmpty(self, fr):
#         fr = np.fromiter(fr, dtype=int)
#         if self.position[fr[0]][fr[1]] == '':
#             return 0
#         return 1
#
#     def toIsEmpty(self, to):
#         to = np.fromiter(to, dtype=int)
#         print(self.position[to[0]])
#         if (self.position[to[0]][to[1]] is None) or (self.position[to[0]][to[1]] == ''):
#             return 1
#         return 0
#
#     def notDiagonalMove(self, fr, to):
#         fr = np.fromiter(fr, dtype=int)
#         to = np.fromiter(to, dtype=int)
#         if fr[0] != to[0] and fr[1] != to[1]:
#             return 0
#         return 1
#
#     def isValidPartialMove(self, fr, to):
#         fr = np.fromiter(fr, dtype=int)
#         to = np.fromiter(to, dtype=int)
#         if abs(fr[0] - to[0]) + abs(fr[1] - to[1]) != 1:
#             return 0
#         return 1
#
#     def isValidPartialJump(self, fr, to):
#         fr = np.fromiter(fr, dtype=int)
#         to = np.fromiter(to, dtype=int)
#         if abs(fr[0] - to[0]) + abs(fr[1] - to[1]) != 2:
#             return 0
#         return 1
#
#     def hasNaighbourAt(self, own_sq, neighbour_sq):
#         own_sq = np.fromiter(own_sq, dtype=int)
#         neighbour_sq = np.fromiter(neighbour_sq, dtype=int)
#         if self.position[neighbour_sq[0]][neighbour_sq[1]] == '':
#             return 0
#         if abs(own_sq[0] - neighbour_sq[0]) + abs(own_sq[0] - neighbour_sq[0]) != 1:
#             return 0
#         return 1
#
#     def joinColRow(self, col, row):
#         str = ""
#         return str.join(col, row)
#
#     def getPossibleNearestSqures(self, sq):
#         sq = np.fromiter(sq, dtype=int)
#         squares = []
#         if self.isValidSquare(self.joinColRow(sq[0] - 1, sq[1])) \
#                 and self.toIsEmpty(sq, self.joinColRow(sq[0] - 1, sq[1])):
#             squares.append(self.joinColRow(sq[0] - 1, sq[1]))
#         if self.isValidSquare(self.joinColRow(sq[0] + 1, sq[1])) and self.toIsEmpty(sq,
#                                                                                     self.joinColRow(sq[0] + 1, sq[1])):
#             squares.append(self.joinColRow(sq[0] + 1, sq[1]))
#         if self.isValidSquare(self.joinColRow(sq[0], sq[1] - 1)) and self.toIsEmpty(sq,
#                                                                                     self.joinColRow(sq[0], sq[1] - 1)):
#             squares.append(self.joinColRow(sq[0], sq[1] - 1))
#         if self.isValidSquare(self.joinColRow(sq[0], sq[1] + 1)) and self.toIsEmpty(sq,
#                                                                                     self.joinColRow(sq[0], sq[1] + 1)):
#             squares.append(self.joinColRow(sq[0], sq[1]) + 1)
#         return squares
#
#     def getPossibleJumps(self, sq, possibleJumps=[]):
#         sq = np.fromiter(sq, dtype=int)
#         if self.isValidSquare(self.joinColRow(sq[0] - 2, sq[1])) \
#                 and self.hasNaighbourAt(sq, self.joinColRow(sq[0] - 1, sq[1])) \
#                 and self.toIsEmpty(sq, self.joinColRow(sq[0] - 2, sq[1])):
#             possibleJumps.append(self.joinColRow(sq[0] - 2, sq[1]))
#             return self.getPossibleJumps(self.joinColRow(sq[0] - 2, sq[1]), possibleJumps)
#         if self.isValidSquare(self.joinColRow(sq[0] + 2, sq[1])) \
#                 and self.hasNaighbourAt(sq, self.joinColRow(sq[0] + 1, sq[1])) \
#                 and self.toIsEmpty(sq, self.joinColRow(sq[0] + 2, sq[1])):
#             possibleJumps.append(self.joinColRow(sq[0] + 2, sq[1]))
#             return self.getPossibleJumps(self.joinColRow(sq[0] + 2, sq[1]), possibleJumps)
#         if self.isValidSquare(self.joinColRow(sq[0], sq[1] - 2)) \
#                 and self.hasNaighbourAt(sq, self.joinColRow(sq[0], sq[1] - 1)) \
#                 and self.toIsEmpty(sq, self.joinColRow(sq[0], sq[1] - 2)):
#             possibleJumps.append(self.joinColRow(sq[0], sq[1] - 2))
#             return self.getPossibleJumps(self.joinColRow(sq[0], sq[1] - 2), possibleJumps)
#         if self.isValidSquare(self.joinColRow(sq[0], sq[1] + 2)) \
#                 and self.hasNaighbourAt(sq, self.joinColRow(sq[0], sq[1] + 1)) \
#                 and self.toIsEmpty(sq, self.joinColRow(sq[0], sq[1] + 2)):
#             possibleJumps.append(self.joinColRow(sq[0], sq[1] + 2))
#             return self.getPossibleJumps(self.joinColRow(sq[0], sq[1] + 2), possibleJumps)
#
#     def listPieceValidMoves(self, sq):
#         possibleMoves = []
#         possibleMoves.append(self.getPossibleNearestSqures(sq))
#         possibleMoves.append(self.getPossibleJumps(sq, possibleMoves))
#
#     def getPieces(self, color):
#         for col in range(8):
#             pieces = []
#             if col in self.position:
#                 for row in range(8):
#                     # for row in reversed(range(8)):
#                     if row in self.position[col] and self.position[col][row] == color:
#                         pieces.append(self.position[col][row])
#         return pieces
#
#     def listValidMoves(self, color):
#         pieces = self.getPieces(color)
#         validMoves = []
#         for piece in pieces:
#             validMoves.append([piece, self.listPieceValidMoves(piece)])
#         return validMoves
#
#     # class BoardOutput:
#     #     def __init__(self, ufen_position=START_POSITION):
#     #         position = self.ufenPositionSplitter(ufen_position)
#     #         position = collections.deque(position)
#     #         pp = pprint.PrettyPrinter(indent=4)
#     #         # for row in range(0, 8):
#     #         #     out_row = []
#     #         #     for col in range(0, 8):
#     #         #         out_row.append(position.popleft())
#     #         #     pp.pprint(out_row)
#     #         for row in reversed(range(1, 9)):
#     #             out_row = []
#     #             for col in range('a', 'h'):
#     #                 out_row.append(str(col) + str(row))
#     #             pp.pprint(out_row)
#
#     def ufenPositionToArray(self, ufen_position):
#         position = ufen_position.split('/')
#         output = {}
#         # output = [[None] * 8] * 8
#         r = 0
#         for row in position:
#             c = 0
#             for square in row:
#                 if square.isnumeric():
#                     for empty_square in list(range(int(square))):
#                         output[r, c] = ' '
#                         c += 1
#                 else:
#                     output[r, c] = square
#                     c += 1
#             # output[r] =
#             r += 1
#         # print(np.matrix(output))
#         return output


# game = Game()
# game.boardOutput()
# game.makeMove('h1', 'h3')
# game.boardOutput()


# START_POSITION = {
#     0o0: 'b', 0o1: 'b',
#     0o10: 'b', 0o11: 'b',
#     0o66: 'w', 0o67: 'w',
#     0o76: 'w', 0o77: 'w',
# }
#
#
# class OctalGame:
#     position = {}
#     turn = 'w'
#     move_number = 0
#
#     def __init__(self, position=START_POSITION, turn='w', move_number=0):
#         self.position = position
#         self.turn = turn
#         self.move_number = move_number
#
#     def makeMove(self, fr, to):
#         fr = self.convertSquare(fr)
#         to = self.convertSquare(to)
#         if not (self.isValidSquare(fr) and self.isValidSquare(to)):
#             return 0
#         if not (self.fromNotEmpty(fr) and self.toIsEmpty(to)):
#             return 0
#         self.position[to] = self.position[fr]
#         del self.position[fr]
#         self.boardOutput()
#
#     def boardOutput(self):
#         counter = 0
#         rows = []
#         for i in list(range(8)):
#             row = []
#             for j in list(range(8)):
#                 if counter in self.position:
#                     row.append(self.position[counter])
#                 else:
#                     row.append(' ')
#                 counter += 1
#             rows.append(row)
#         print(np.rot90(np.fliplr(rows)))
#
#     def convertSquare(self, sq):
#         sq = list(sq)
#         sq[0] = {
#             'a': 0o0,
#             'b': 0o1,
#             'c': 0o2,
#             'd': 0o3,
#             'e': 0o4,
#             'f': 0o5,
#             'g': 0o6,
#             'h': 0o7
#         }[sq[0]]
#         sq[0] = sq[0] * 8
#         sq[1] = 8 - int(sq[1])
#         return int(sq[0] + sq[1])
#
#     def isValidSquare(self, sq):
#         return int(0o0) <= int(sq) <= int(0o77)
#
#     def fromNotEmpty(self, fr):
#         if self.position[fr] == '':
#             return 0
#         return 1
#
#     def toIsEmpty(self, to):
#         if (to not in self.position):
#             return 1
#         return 0
#
#     def isValidPartialMove(self, fr, to):
#         if abs(fr - to) == int(0o1) or abs(fr - to) == int(0o10):
#             return 1
#         return 0
#
#     def isValidPartialJump(self, fr, to):
#         if abs(fr - to) == int(0o2) or abs(fr - to) == int(0o20):
#             return 1
#         return 0
#
#     def hasNaighbourAt(self, own_sq, neighbour_sq):
#         if neighbour_sq not in self.position:
#             return 0
#         if abs(own_sq - neighbour_sq) != int(0o1) or abs(own_sq - neighbour_sq) != int(0o10):
#             return 0
#         return 1
#
#     def joinColRow(self, col, row):
#         str = ""
#         return str.join(col, row)
#
#     def getPossibleNearestSqures(self, sq):
#         squares = []
#         if self.isValidSquare(sq - int(0o1)) \
#                 and self.toIsEmpty(sq - int(0o1)):
#             squares.append(sq - int(0o1))
#         if self.isValidSquare(sq + int(0o1)) \
#                 and self.toIsEmpty(sq + int(0o1)):
#             squares.append(sq + int(0o1))
#         if self.isValidSquare(sq - int(0o10)) \
#                 and self.toIsEmpty(sq - int(0o10)):
#             squares.append(sq - int(0o10))
#         if self.isValidSquare(sq + int(0o10)) \
#                 and self.toIsEmpty(sq + int(0o10)):
#             squares.append(sq + int(0o10))
#         return squares
#
#     def getPossibleJumps(self, sq, possibleJumps=[]):
#         if self.isValidSquare(sq - int(0o2)) \
#                 and self.hasNaighbourAt(sq, sq - int(0o1)) \
#                 and self.toIsEmpty(sq - int(0o2)):
#             possibleJumps.append(sq - int(0o2))
#         if self.isValidSquare(sq + int(0o2)) \
#                 and self.hasNaighbourAt(sq, sq + int(0o1)) \
#                 and self.toIsEmpty(sq + int(0o2)):
#             possibleJumps.append(sq + int(0o2))
#         if self.isValidSquare(sq - int(0o20)) \
#                 and self.hasNaighbourAt(sq, sq - int(0o10)) \
#                 and self.toIsEmpty(sq - int(0o20)):
#             possibleJumps.append(sq - int(0o20))
#         if self.isValidSquare(sq + int(0o20)) \
#                 and self.hasNaighbourAt(sq, sq + int(0o10)) \
#                 and self.toIsEmpty(sq + int(0o20)):
#             possibleJumps.append(sq + int(0o20))
#
#         self.getPossibleJumps(sq - int(0o2), possibleJumps)
#         self.getPossibleJumps(sq + int(0o2), possibleJumps)
#         self.getPossibleJumps(sq - int(0o20), possibleJumps)
#         self.getPossibleJumps(sq + int(0o20), possibleJumps)
#         return 1
#
#     def listPieceValidMoves(self, sq):
#         possibleMoves = []
#         possibleMoves.append(self.getPossibleNearestSqures(sq))
#         possibleMoves.append(self.getPossibleJumps(sq, possibleMoves))
#
#     def getPieces(self, color):
#         return [k for k in self.position.keys() if self.position[k] == color];
#
#     def listValidMoves(self, color):
#         pieces = self.getPieces(color)
#         validMoves = []
#         for piece in pieces:
#             validMoves.append([piece, self.listPieceValidMoves(piece)])
#         return validMoves
#
#
# game = OctalGame()
# print(game.listValidMoves('w'))
# game.makeMove('h1', 'h3')
# print(game.listValidMoves('b'))

START_POSITION = {
    1: 'b', 2: 'b',
    9: 'b', 10: 'b',
    55: 'w', 56: 'w',
    63: 'w', 64: 'w',
}

GOAL = {'w': 1, 'b': 64}

MOVES_LIMIT = 80

class OneDimmentionGame:
    position = {}
    turn = 'w'
    move_number = 0

    def __init__(self, position=START_POSITION, turn='w', move_number=0):
        self.position = position
        self.turn = turn
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
        if self.position[fr] == '':
            return 0
        return 1

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

    def joinColRow(self, col, row):
        str = ""
        return str.join(col, row)

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

    def getPieces(self, color):
        return [k for k in self.position.keys() if self.position[k] == color];

    def listValidMoves(self, color):
        pieces = self.getPieces(color)
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



game = OneDimmentionGame()
game.play('w')
