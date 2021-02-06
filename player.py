class Player:
    def __init__(self, value, strategy):
        self.value = value
        self.strategy = strategy

    def get_value(self):
        return self.value

    def move(self, moves, board):
        return self.strategy.select_move(moves, board, self.value)
# The below will be useful only for q-learning
#    def reward(self, reward_value):
#        self.strategy.reward(reward_value)
#
#    def reset_history(self):
#        self.strategy.reset_history()
