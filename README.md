# rl-tictactoe

A tic tac toe game to explore reinforcement learning of strategies.

It can be used easily from the command line. Just run main.py, and you are shown several options:
1. View a game between two players using the learned strategy
2. Play against another human player (moves are played by entering the number of the square that you wish to play)
3. Train the strategy using Q-learning. This runs several games between two Q-learning players and saves the learned strategy to `q.pkl`
4. Simulate several games between the Q-learned strategy and a random strategy for comparison (Q-learned strategy is player 1)
5. Simulate several games between the Q-learned strategy and a random strategy for comparison (Q-learned strategy is player 2)
6. Play a game against the Q-learned strategy (you are player 1)
7. Play a game against the Q-learned strategy (you are player 2)

The code is structured into several files with different classes defined in them. The most important one is `stratetegies.py` which implements the different strategies (human player, random player and Q-learning). The file `q.pkl` contains the Q-table of state-action pairs. It is loaded when a player with Q-learning strategy is instantiated, and it is updated during training. The file `print_q.py` reads and prints to the terminal. In `params.py`, the relevant parameters are defined. These are:
* Reward values for win, loss, draw
* Learning rate
* Discounting factor
* Exploration rate and its decay constant.

During training, the Q-agent randomly chooses whether to explore or exploit (exploit means to pick a random move). This is so that all moves will be explored during training, since otherwise it can easile get stuck in a local optimum. As the Q-agent becomes more experienced, it will exploit its known strategies more and explore less, which is implemented as an exponentially decreasing exploration rate with number of games seen.

After each game during training, the agent will updates its Q-values according to the reward values given in `params.py`. If it won, it will increase the Q-values associated with its chosen moves and if it lost, it will decrease them. If the result is a draw, it makes sense to give a small reward.

Update of the $q$ function for state-action pair $(s,a)$ is given by
$$
q(s,a) \leftarrow (1-\alpha) q(s,a) + \alpha (R + \gamma \max_{a'}q(s',a'))
$$

<img src="https://render.githubusercontent.com/render/math?math=q(s%2Ca)%20leftarrow%20(1-alpha)%20q(s%2Ca)%20%2B%20alpha%20(R%20%2B%20gamma%20max_%7Ba%7Dq(s%2Ca))">

Here, $\alpha$ is the learning rate, $R$ the reward value and $\gamma$ the discount factor. This last term is there to favour moves which result in future advantage. It is calculated by looking for the maximum Q-value possible in the next move (since there are two players, it makes the best move for the opponent and then looks what its best Q-value can be in the next move).

The result is an agent which is almost impossible to beat. When playing against itself, it draws about 97% of the time. Player 1 wins about 2.5% of the time and player 2 wins about 0.5% of the time, due to the advantage that player 1 has of starting. When playing against a random opponent, if player 1 is the Q-learning agent it wins 98% of the time and if player 2 is the Q-learning agent, it wins 85% of the time.