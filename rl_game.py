class Game:

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.player1.set_symbol('X')
        self.player2.set_symbol('O')
        self.board = board
        self.player1_wins = 0
        self.player2_wins = 0
        self.draws = 0

    def play_game(self):
        """
        Plays a game between player 1 and player 2
        """
        current_player = self.player1
        while (self.board.get_moves()):
            # There are available moves to be made
            moves = self.board.get_moves()
            selected_move = current_player.move(moves, copy.deepcopy(self.board.board))
            self.board.move(selected_move, current_player.symbol)

            #self.board.print_board()
            
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1

        result = self.board.get_result()
        if result == 1:
            self.player1.reward(win_reward)
            self.player2.reward(lose_reward)
        elif result == 2:
            self.player2.reward(win_reward)
            self.player1.reward(lose_reward)
        else:
            self.player1.reward(draw_reward)
            self.player2.reward(draw_reward)

        self.player1.reset_history()
        self.player2.reset_history()
                
            
