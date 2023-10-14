"""
Tic Tac Toe Player
"""
import copy


X = "X"
O = "O"
EMPTY = None

def initial_state_end():
  return [[X,     EMPTY, EMPTY],
          [EMPTY, O,     EMPTY],
          [EMPTY, EMPTY, X]]

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for row in board:
      for cell in row:
        if cell == X:
          x += 1
        elif cell == O:
          o += 1
    if x == 5:
      return None
    if x > o:
      return O
    else: 
      return X
    



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
      
    for i in range(3):
      for j in range(3):
        if board[i][j] == EMPTY:
          x = (i,j)
          possible_actions.append(x)

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i, j) = action
  
    New_board = copy.deepcopy(board)
    "print(New_board)"
    try: 
      if New_board[i][j] == EMPTY:
        New_board[i][j] = player(board)
        return New_board
    except: raise Exception("action invalid")

def wins(player_choice, board):

#WINS BY ROW 

    for row in board:
      count_x = 0
      for cell in row:
        if cell == player_choice:
          count_x += 1
      if count_x == 3:
        return player_choice

#WINS BY COLUMN 
    
    for i in range(3):      
      count_y = 0
      for row in board:
        if row[i] == player_choice:    
          count_y += 1
      if count_y == 3:
        return player_choice


#WINS DIAGONAL

    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == player_choice:
      return player_choice
    elif board[0][2] == board[1][1] and board[0][2]== board[2][0] and board[2][0] == player_choice:
      return player_choice
    else:
      return None


def winner(board):
  """
  Returns the winner of the game, if there is one.
  """

  if wins(X, board) == X:
     return X
  elif wins(O, board) == O:
     return O
  else: 
    return None
  

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == X:
      return True
    elif winner(board) == O:
      return True
    return actions(board) == [] 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
      return 1
    elif winner(board) == O:
      return -1
    else: 
      return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    """
    if terminal(board):
      return None 
    if player(board) == X:
      
      optimal_action = None
      best_value = -5000000000
      
      for action in actions(board):
        new_board = result(board, action)
        action_outcome = maxvalue(new_board)
        if action_outcome > best_value:
          best_value = action_outcome
          optimal_action = action
      return optimal_action
    
    elif player(board) == O:
      optimal_action = None
      best_value = 1000000000000
      for action in actions(board):
          new_board = result(board, action)
          action_outcome = minvalue(new_board)
          if action_outcome < best_value:
              best_value = action_outcome
              optimal_action = action
      return optimal_action
      
    
def maxvalue(board):

    if terminal(board):
        return utility(board)

    value = -1000000
    possible_actions = actions(board)
    for act in possible_actions:
      new_board = result(board, act)
      min_value = minvalue(new_board)
      value = max(value, min_value)
      if value == 1:
        break
    return value


def minvalue(board):

    if terminal(board):
        return utility(board)

    value = 1000000
    possible_actions = actions(board)
    for act in possible_actions:
      new_board = result(board, act)
      max_value = maxvalue(new_board)
      value = min(value , max_value)
      if value == -1:
        break 
    return value
    

        


