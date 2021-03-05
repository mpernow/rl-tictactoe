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

    def select_move(self, moves, board):
        """
        Selects a move from list
        """

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "random")

    def select_move(self, moves, board):
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

    def select_move(self, moves, board):
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
    def __init__(self, symbol, f_name=params.f_name):
        Strategy.__init__(self, "q-strategy")
        self.learning_rate = params.learning_rate
        self.discount_factor = params.discount_factor
        # Load pickled q table if exists and non-empty, otherwise make empty
        self.f_name = f_name
        try:
            f = open(self.f_name, 'rb')
            self.q = pickle.load(f)
            f.close()
        except (FileNotFoundError, EOFError):
            self.q = {}
        # self.q is dict of {state: [q-value for each action]}
        if 'n' in self.q:
            self.n = self.q['n']
        else:
            self.n = 0
        self.exploration_rate = params.eps_min + \
          (params.eps_max - params.eps_min)*math.exp(-params.tau * self.n)
        # Keep track of history of states, actions in game to update q-table
        self.history = {}
        # Keep track of the updated entries of q-table to be saved
        self.new_q = {}
        # For reading and updating q-table, need to know symbol:
        self.symbol = symbol

    def select_move(self, moves, board):
        state = board.get_state()
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
        # Loop over each state from this game and update q-value
        for state in self.history:
            # Offset moves array!
            action = self.history[state] - 1
            if state in self.q:
                old_q = self.q[state][action]
            else:
                old_q = 0.
                self.q[state] = [0 for i in range(9)]
            next_state = state[:action] + self.symbol + state[action+1:]
            # Discounted future reward: Choose opponent's best move, then look at my q-values after that
            if (next_state in self.q) and (next_state.count(' ')>=2): # Only if I will move again
                # Possible moves:
                next_moves = [i for i, x in enumerate(next_state) if x == ' ']
                qs_allowed = [self.q[next_state][i] for i in next_moves]                            
                best_moves = [i for i, x in enumerate(qs_allowed) if x == max(qs_allowed)]
                next_move = next_moves[random.choice(best_moves)] # want index, not place on board
                # Make best move for opponent
                other_symb = 'O' if self.symbol=='X' else 'X'
                nextnext_state = next_state[:next_move] + other_symb + next_state[action+1:]
                # Best q-value for next move:
                if nextnext_state in self.q:
                    next_q = max([self.q[nextnext_state][i] for i in next_moves])
                else:
                    next_q = 0.
            else:
                next_q = 0.
            self.q[state][action] = (1. - params.learning_rate)*old_q + \
              params.learning_rate * (reward_val + params.discount_factor * next_q)
            # Keep track of which ones have changed:
            self.new_q[state] = self.q[state]
        self.n += 1
        self.q['n'] = self.n

    def reset_history(self):
        self.history = {}

    def save_q(self):
        """
        Saves the q function table using pickle
        To avoid conflict with other player having saved their moves since we last loaded,
        we reload it, update only our updated actions (these have no overlap between players),
        and save that q-table.
        """
        try:
            f = open(self.f_name, 'rb')
            loaded_q = pickle.load(f)
            f.close()
        except (FileNotFoundError, EOFError):
            loaded_q = {}
        for state in self.new_q:
            loaded_q[state] = self.new_q[state]
            loaded_q['n'] = self.n
        f = open(self.f_name, 'wb')
        pickle.dump(loaded_q, f)
        f.close()
        # Finally, clear the history:
        self.new_q = {}
