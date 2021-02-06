class Player:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_symbol(self, symbol):
        self.symbol = symbol
        
    def move(self, moves, board):
        return self.strategy.select_move(moves, board)

    def reward(self, reward_value):
        self.strategy.reward(reward_value)

    def reset_history(self):
        self.strategy.reset_history()
