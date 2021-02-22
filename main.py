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

def human_v_random(human_player=1):
    """
    Allows human to play versus random player
    """
    if human_player == 1:
        p1_strategy = strategies.Human()
        p2_strategy = strategies.RandomStrategy()
    else:
        human_player = 2
        p2_strategy = strategies.Human()
        p1_strategy = strategies.RandomStrategy()
    p1 = player.Player('X', p1_strategy)
    p2 = player.Player('O', p2_strategy)
    board = tictactoe.Board()
    message = 'Welcome to tic tac toe!\n'+\
    'You are playing against a random opponent and you are player '+str(human_player)+'.\n'+\
    'To make a move, enter the number of the square which you would like to play, labelled as:\n'+\
    '1, 2, 3\n4, 5, 6\n7, 8, 9\n\n'
    print(message)
    game = rl_game.Game(p1, p2, board)
    game.play_one()

def q_v_q():
    """
    Plays two Q-strategy players against each other
    """
    p1_strategy = strategies.QStrategy('q1.pkl')
    p2_strategy = strategies.QStrategy('q2.pkl')
    p1 = player.Player('X', p1_strategy)
    p2 = player.Player('O', p2_strategy)
    board = tictactoe.Board()
    game = rl_game.Game(p1, p2, board)
    game.play_one()
    p1.strategy.save_q()
    p2.strategy.save_q()

def train_q():
    """
    Trains the RL agent
    """
    p1_strategy = strategies.QStrategy('q1.pkl')
    p2_strategy = strategies.QStrategy('q2.pkl')
    p1 = player.Player('X', p1_strategy)
    p2 = player.Player('O', p2_strategy)
    board = tictactoe.Board()
    game = rl_game.Game(p1, p2, board)
    game.play_many(100)
    p1.strategy.save_q()
    p2.strategy.save_q()
    

if __name__ == '__main__':
    print('Welcome to tic tac toe!\n')
    print('These are your options: \n')
    print('1: View a Q vs. Q game\n')
    print('2: View a random vs. random game\n')
    print('3: Play a 2-player game\n')
    print('4: Play against random bot as player 1\n')
    print('5: Play against a random bot as player 2\n')
    print('6: Train the Q-learning agent\n')
    choice = input('Enter your choice: ')
    if not choice.isdigit():
        print('Enter a number next time')
    choice = int(choice)
    if choice == 1:
        q_v_q()
    elif choice == 2:
        random_v_random()
    elif choice == 3:
        tictactoe.two_player()
    elif choice == 4:
        human_v_random(1)
    elif choice == 5:
        human_v_random(2)
    elif choice == 6:
        train_q()
    else:
        print('Enter a valid choice next time')
        
