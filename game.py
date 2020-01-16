# Initializes a new dead board
def init_game(game_size):
    game_state = [[0 for i in range(game_size)] for j in range(game_size)]
    return game_state

# Methods for generating interesting patterns
def create_blinker(x, y, game_state):
    game_state[x][y] = 1
    game_state[x + 1][y] = 1
    game_state[x + 2][y] = 1
    return game_state

def create_beacon(x, y, game_state):
    game_state[x][y] = 1
    game_state[x + 1][y] = 1
    game_state[x][y + 1] = 1
    game_state[x + 3][y + 2] = 1
    game_state[x + 2][y + 3] = 1
    game_state[x + 3][y + 3] = 1
    return game_state

def create_glider(x, y, game_state):
    game_state[x][y] = 1
    game_state[x + 2][y] = 1
    game_state[x + 1][y + 1] = 1
    game_state[x + 2][y + 1] = 1
    game_state[x + 1][y + 2] = 1
    return game_state

# Updates the game state according to conway's game of life rules
def update_game(game_state):
    
    # Begin with a dead game state
    # Game rules will be applied to fill in live cells from the current state
    width = len(game_state)
    height = len(game_state[0])
    new_game_state = [[0 for i in range(width)] for j in range(height)]

    # Apply game rules to current state
    # Rule 1: Any live cell with two or three neighbors survives.
    # Rule 2: Any dead cell with three live neighbors becomes a live cell.
    # Rule 3: All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    for x in range(width):
        for y in range(height):
            # Count live neighbours
            n = sum_neighbours(x, y, game_state)

            # Apply rule 1
            if game_state[x][y] == 1 and (n == 2 or n == 3):
                new_game_state[x][y] = 1
            
            # Apply rule 2
            if (game_state[x][y] == 0 and n == 3):
                new_game_state[x][y] = 1

            # Rule 3 is applied implicitly by beginning with a dead board

    return new_game_state

# helper function for assessing game rules
def sum_neighbours(x, y, game_state):
    width = len(game_state)
    height = len(game_state[0])

    # Determine up, down, left, right movement with board wrapping rules
    up =  y - 1 if y != 0 else height - 1
    down = y + 1 if y != height - 1 else 0
    left = x - 1 if x != 0 else width - 1
    right = x + 1 if x != width - 1 else 0

    # Sum the value of neighbouring cells
    s = (game_state[left][up] + game_state[x][up] + game_state[right][up] +
        game_state[left][y] + game_state[right][y] +
        game_state[left][down] + game_state[x][down] + game_state[right][down])
    return s
