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

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "random")

    def select_move(self, moves, board):
        return moves[random.randrange(0, len(moves))]

    def reward(self, reward_value):
        """
        Not needed for random strategy but given for compatibility.
        """
        pass

    def reset_history(self):
        """
        Not needed for random strategy but given for compatibility.
        """
        pass

class QStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "q-strategy")
    # To be implemented
