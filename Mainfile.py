#! python3
from Indiv_functions import *

def game():
    # The full game put together - includes the option to play again
    global game_over
    global row1
    global row3
    global row5
    global play_1_mark
    global play_2_mark
    welcome()
    while True:
        if not game_over:
            player_1_turn(play_1_mark)
            winner(row1, row3, row5)
            if not game_over:
                player_2_turn(play_2_mark)
                winner(row1, row3, row5)
        else:
            if input("\nPlay again? Y/N: ").upper() == 'Y':
                game_over = False
                row1 = [' ','|',' ','|',' ']
                row3 = [' ','|',' ','|',' ']
                row5 = [' ','|',' ','|',' ']
                play_1_mark = ''
                play_2_mark = ''
                game()
            else:
                break

    print("\nThanks for playing!")
game()
