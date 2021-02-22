class Player:
    def __init__(self, symbol, strategy):
        self.symbol = symbol
        self.strategy = strategy

    def move(self, moves, board):
        return self.strategy.select_move(moves, board, self.symbol)

    def reward(self, reward_value):
        self.strategy.reward(reward_value)

    def reset_history(self):
        self.strategy.reset_history()
