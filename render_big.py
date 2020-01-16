from graphics import *

square_size = 10    # Size of cells (px)
gap_size = 0        # Size of gap between cells (px)
fill = "black"      # Live cell fill color
outline = "white"   # Live cell outline color

def init_render(game_size):
    win_size = (game_size * square_size) + ((game_size - 1) * gap_size)
    win = GraphWin("Conway's Game of Life", win_size, win_size)
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
                p_tl = Point(x * (square_size + gap_size), y * (square_size + gap_size))
                p_br = Point(p_tl.x + square_size, p_tl.y + square_size)
                r = Rectangle(p_tl, p_br)
                r.setFill(fill)
                r.setOutline(outline)
                r.draw(win)
    win.update()
    
