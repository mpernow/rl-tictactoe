import random
import pickle
import math
import params

# Parent class maybe not necessary

class Strategy:
    """
    Parent class for strategies
    """
    def __init__(self, type):
        self.type = type

    def select_move(self, moves, board, symbol):
        """
        Selects a move from list
        """

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "random")

    def select_move(self, moves, board, symbol):
        # symbol included only for compatibility
        return random.choice(moves)

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

class Human(Strategy):
    def __init__(self):
        Strategy.__init__(self, "human")

    def select_move(self, moves, board, symbol):
        # symbol included only for compatibility
        move = input('Enter a square: ')
        try:
            move = int(move)
        except:
            ValueError('Move not understood')
        while move not in moves:
            print('Move not allowed.')
            move = input('Try again: ')
            try:
                move = int(move)
            except:
                ValueError('Move not understood')
        return move

    def reward(self, reward_value):
        """
        Taken care of by the human player's brain (if available).
        """
        pass

    def reset_history(self):
        """
        Not needed for human strategy but given for compatibility.
        """
        pass


class QStrategy(Strategy):
    def __init__(self, f_name=params.f_name):
        Strategy.__init__(self, "q-strategy")
        self.learning_rate = params.learning_rate
        self.discount_factor = params.discount_factor
        #self.exploration_rate = params.exploration_rate
        # Load pickled q table if exists and non-empty, otherwise make empty
        self.f_name = f_name
        try:
            f = open(self.f_name, 'rb')
            self.q = pickle.load(f)
            f.close()
        except (FileNotFoundError, EOFError):
            self.q = {}
        # self.q is dict of {state: [q-value for each action]}
        # Note that in the q dict, it is assumed that the player plays X
        # Exploration rate will have decay, depending on number of of played episodes,
        # which is stored in q.pkl
        if 'n' in self.q:
            self.n = self.q['n']
        else:
            self.n = 0
        self.exploration_rate = params.eps_min + \
          (params.eps_max - params.eps_min)*math.exp(-params.tau * self.n)
        self.history = {}

    def select_move(self, moves, board, symbol):
        # Get the state and set the X and O appropriately for the player
        state = board.get_state()
        if symbol == 'O':
                # Interchange X and O in state since Q-table assumes player plays X
                state = state.replace('X', '_').replace('O','X').replace('_','O')
        r = random.random()
        if r < self.exploration_rate:
            # Explore!
            move = random.choice(moves)
        else:
            # Exploit!
            if state in self.q:
                # Get best move that is also allowed
                # moves is array starting at 1, so offset, then add back at end:
                moves = [m-1 for m in moves]
                qs_allowed = [self.q[state][i] for i in moves]
                best_moves = [i for i, x in enumerate(qs_allowed) if x == max(qs_allowed)]
                move = moves[random.choice(best_moves)] + 1
            else:
                # Has not been experienced before, so pick random
                move = random.choice(moves)
        # Place the state and action in history:
        self.history[state] = move
        return move

    def reward(self, reward_val):
        """
        Updates the q-values based on the outcome of a game
        """
        # Remember the offset of moves array!
        for state in self.history:
            action = self.history[state] - 1
            if state in self.q:
                old_q = self.q[state][action]
            else:
                old_q = 0.
                self.q[state] = [0 for i in range(9)]
            next_state = state[:action]+'X'+state[action+1:]
            if next_state in self.q:
                next_q = max(self.q[next_state])
            else:
                next_q = 0.
            self.q[state][action] = (1. - params.learning_rate)*old_q + \
              params.learning_rate * (reward_val + params.discount_factor * next_q)
        self.n += 1
        self.q['n'] = self.n

    def reset_history(self):
        self.history = {}

    def save_q(self):
        """
        Saves the q function table using pickle
        """
        f = open(self.f_name, 'wb')
        pickle.dump(self.q, f)
        f.close()
