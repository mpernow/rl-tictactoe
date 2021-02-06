import random

class Strategy:
    """
    Parent class for strategies
    """
    def __init__(self, type):
        self.type = type

    def select_move(self, moves, board):
        """
        Selects a move from list
        """
        ## player_value variable???

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "random")

    def select_move(self, moves):
        return moves[random.randrange(0, len(moves))]

class QStrategy(Strategy):
    # To be implemented
