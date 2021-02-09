import strategies
import player
import tictactoe
import rl_game

def random_v_random(n=1):
    """
    Plays two random players against each other
    """
    p1_strategy = strategies.RandomStrategy()
    p2_strategy = strategies.RandomStrategy()
    p1 = player.Player('X', p1_strategy)
    p2 = player.Player('O', p2_strategy)
    board = tictactoe.Board()
    game = rl_game.Game(p1, p2, board)
    game.play_one()

if __name__ == '__main__':
    random_v_random()
    
