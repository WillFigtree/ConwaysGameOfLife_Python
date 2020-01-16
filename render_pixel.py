from graphics import *

def init_render(game_size):
    win = GraphWin("Conway's Game of Life", game_size, game_size)
    win.autoflush = False
    return win

def finalize_render(win):
    win.close()    # Close window when done

def update_render(win, game_state):
    width = len(game_state)
    height = len(game_state[0])

    # Clear window
    for item in win.items[:]:
        item.undraw()

    # Draw live cells
    for x in range(width):
        for y in range(height):
            if game_state[x][y] == 1:
                p = Point(x, y)
                p.draw(win)
    
    win.update()
