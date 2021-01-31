import copy

class Board:

    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]

    def get_result(self):
        """
        Returns 1 if player 1 wins, 2 if player 2 wins, 0 if no win,
        and -1 if an error has occurred.
        """
        # Make list of rows, cols, diags to check
        board_copy = copy.deepcopy(self.board)
        to_check = board_copy[:]
        for col in range(3):
            to_check.append([board_copy[r][col] for r in range(3)])
        to_check.append([board_copy[i][i] for i in range(3)])
        to_check.append([board_copy[i][2-i] for i in range(3)])
        #print(to_check)

        # Check if anyone has won
        p1_win = ['X', 'X', 'X']
        p2_win = ['O', 'O', 'O']
        if (p1_win in to_check) and (p2_win in to_check):
            return -1
        elif (p1_win in to_check):
            return 1
        elif (p2_win in to_check):
            return 2
        else:
            return 0

    def get_moves(self):
        """
        Returns list of available moves as indexed 1 through 9
        """
        moves = []
        for i in range(1,10):
            if self.board[(i - 1) // 3][(i - 1) % 3] == 0:
                moves.append(i)
        return moves

    def print_board(self):
        """
        Prints the board
        """
        ch = lambda x: ' ' if x == 0 else x
        board =[' '*5 + '|' + ' '*5 + '|' + ' '*5,
                ' '*2+ch(self.board[0][0]) + ' '*2 + '|' + ' '*2+ch(self.board[0][1]) + ' '*2 + '|' + ' '*2+ch(self.board[0][2]) + ' '*2,
                ' '*5 + '|' + ' '*5 + '|' + ' '*5,
                '-'*17,
                ' '*5 + '|' + ' '*5 + '|' + ' '*5,
                ' '*2+ch(self.board[1][0]) + ' '*2 + '|' + ' '*2+ch(self.board[1][1]) + ' '*2 + '|' + ' '*2+ch(self.board[1][2]) + ' '*2,
                ' '*5 + '|' + ' '*5 + '|' + ' '*5,
                '-'*17,
                ' '*5 + '|' + ' '*5 + '|' + ' '*5,
                ' '*2+ch(self.board[2][0]) + ' '*2 + '|' + ' '*2+ch(self.board[2][1]) + ' '*2 + '|' + ' '*2+ch(self.board[2][2]) + ' '*2,
                ' '*5 + '|' + ' '*5 + '|' + ' '*5]
        print('\n')
        [print(line) for line in board]
        print('\n')

    def move(self, pos, val):
        """
        Executes a move.
        Note: does not check if correct, so this should be done before.
        """
        self.board[(pos - 1) // 3][(pos - 1) % 3] = val

def two_player():
    b = Board()
    print('Welcome to tic tac toe!\nTo make a move, enter the number of the square which you would like to play, labelled as:\n1, 2, 3\n4, 5, 6\n7, 8, 9')

    current = 1
    b.print_board()
    
    while b.get_moves():
        move = input('Player ' + str(current) + ', enter a square: ')
        try:
            move = int(move)
        except:
            ValueError('Move not understood')
        while move not in b.get_moves():
            print('Move not allowed.')
            move = input('Try again: ')
            try:
                move = int(move)
            except:
                ValueError('Move not understood')
        b.move(move, ['X','O'][current-1])
        current = [2,1][current-1]
        b.print_board()
        state = b.get_result()
        if state == 1:
            print('Player 1 wins')
            break
        elif state == 2:
            print('Player 2 wins')
            break

    if (not b.get_moves()) and (b.get_result() == 0):
        print('Draw!')
        
if __name__ == '__main__':
    two_player()
