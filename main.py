from render_big import init_render, update_render, finalize_render
from game import *
from time import sleep


game_size = 30      # num x and y cells
game_rate = 10      # fps
game_length = 500   # number of iterations to perform

def main():
    # initialize
    game_state = init_game(game_size)
    game_state = create_blinker(2, 2, game_state)
    game_state = create_beacon(5, 5, game_state)
    game_state = create_glider(5, 20, game_state)

    win = init_render(game_size)

    # run game loop
    for i in range(game_length):
        game_state = update_game(game_state)
        update_render(win, game_state)
        sleep(1 / game_rate)

    # finalize
    finalize_render(win)

main()