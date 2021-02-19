import copy
from params import win_reward, lose_reward, draw_reward

class Game:

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.player1_wins = 0
        self.player2_wins = 0
        self.draws = 0

    def play_one(self):
        """
        Plays a game between player 1 and player 2
        """
        current_player = self.player1
        while (self.board.get_moves()) and (self.board.get_result() == 0):
            # There are available moves to be made
            if (current_player == self.player1):
                print('Player 1')
            else:
                print('Player 2')
            moves = self.board.get_moves()
            selected_move = current_player.move(moves, copy.deepcopy(self.board.board))
            self.board.move(selected_move, current_player.symbol)

            self.board.print_board()
            
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1

        result = self.board.get_result()
        if result == 1:
            self.player1.reward(win_reward)
            self.player2.reward(lose_reward)
            print('Player 1 wins')
        elif result == 2:
            self.player2.reward(win_reward)
            self.player1.reward(lose_reward)
            print('Player 2 wins')
        else:
            self.player1.reward(draw_reward)
            self.player2.reward(draw_reward)
            print('Draw')

        self.player1.reset_history()
        self.player2.reset_history()
                
    def play_many(self, number):
        """
        Calls play_one() several times.
        """
        # To be implemented
        return 0
