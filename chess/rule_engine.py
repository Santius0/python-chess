"""
Saves the current state of the game
"""


class GameState:
    def __init__(self):
        self.move_log = []
        self.board = [['-' for x in range(8)] for y in range(8)]
        self.board[0][0] = 'wR'
        self.board[1][0] = 'wN'
        self.board[2][0] = 'wB'
        self.board[3][0] = 'wQ'
        self.board[4][0] = 'wK'
        self.board[5][0] = 'wB'
        self.board[6][0] = 'wN'
        self.board[7][0] = 'wR'
        for x in range(8):
            self.board[x][1] = 'wP'

        for x in range(8):
            self.board[x][6] = 'bP'
        self.board[0][7] = 'bR'
        self.board[1][7] = 'bN'
        self.board[2][7] = 'bB'
        self.board[3][7] = 'bQ'
        self.board[4][7] = 'bK'
        self.board[5][7] = 'bB'
        self.board[6][7] = 'bN'
        self.board[7][7] = 'bR'

    def valid_move(self, start, stop):
        if self.board[start[0]][start[1]] == '-':
            return False
        return True

    def move_piece(self, start, stop):
        if self.valid_move(start, start):
            self.board[stop[0]][stop[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = '-'


class Move:
    def __init__(self):
        self.start = ()
        self.stop = ()

    def validate(self):
        return True