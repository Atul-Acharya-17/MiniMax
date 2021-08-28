# MiniMax

Basic MiniMax Framework to solve any simple board game

### Function Parameters

Parameters  | Description | Type
------------- | ------------- | -------------
state  | State to evaluate on | n-Dimensional List
max_depth  | Max depth of search tree | integer
is_maximizing | If the current player is maximizing or not | boolean
heuristic | Heuristic function that returns value of the state | func(state) -> integer / float
is_terminal | Function that returns if the the state is a terminal state of not | func(state) -> boolean
get_next_states | Function that returns a list of all possible next states | func(state) -> list :: [state]

### Usage

```python
from minimax.minimax import MiniMax

# Define the heuristic, is_terminal and get_next_state functions in your driver code

# TicTacToe Example

board = [['O', '', ''], ['', 'X', ''], ['X', '', '']]
max_depth = 3

minimax = MiniMax()

best_move, best_value = minimax.solve(board, max_depth, False, heuristic, is_terminal, get_next_states)

print(best_move)
print(best_value)
```