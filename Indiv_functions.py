#! python3

from Rows import *

play_1_mark = ''
play_2_mark = ''
game_over = False

def welcome():
    # Intro bit - so it doesn't keep showing over and over with each player go
    print(' '.join(row1_start))
    print('-'.join(row2_start))
    print(' '.join(row3_start))
    print('-'.join(row4_start))
    print(' '.join(row5_start))
    print('''\nWelcome to Tic Tac Toe! You should know the rules already - first in a horizontal, diagonal or vertical 
line to three wins. To choose your position, pick a number that corresponds to the position on the grid above.\n''')

def display():
    # Displays the tic tac toe board
    print(' '.join(row1))
    print('-'.join(row2))
    print(' '.join(row3))
    print('-'.join(row4))
    print(' '.join(row5))

def board_value():
    # Gets the value for the row
    board_num = ''
    while board_num not in range(1,10):
        board_num = int(input("\nPlease pick the number for where you'd like to go on the board: "))
    return board_num

def player_1_turn(play_1_mark):
    # Puts the mark on the board for player 1
    print('Player 1\'s turn.')

    # Validates the user input - keeps asking until they select a variety of O or X
    while play_1_mark not in ['O', 'X']:
        play_1_mark = input("Player 1: Do you want to be X or O? ")

    nums_dictionary = {1: 0, 2: 2, 3: 4, 4: 0, 5: 2, 6: 4,
                       7: 0, 8: 2, 9: 4}
    board_move = board_value()

    # Retrieves the dictionary key for row 1, row 2 and so on
    if board_move in range(1,4):
        if row1[(nums_dictionary[board_move])] == ' ':
            row1[(nums_dictionary[board_move])] = play_1_mark
            display()
        else:
            print("Someone already did that move!")
            player_1_turn()
    elif board_move in range(4,7):
        if row3[(nums_dictionary[board_move])] == ' ':
            row3[(nums_dictionary[board_move])] = play_1_mark
            display()
        else:
            print("Someone already did that move!")
            player_1_turn()
    else:
        if row5[(nums_dictionary[board_move])] == ' ':
            row5[(nums_dictionary[board_move])] = play_1_mark.upper()
            display()
        else:
            print("Someone already did that move!")
            player_1_turn()


def player_2_turn(play_2_mark):
    # Puts the mark on the board for player 2
    print('Player 2\'s turn.')
    while play_2_mark == '':
        if play_1_mark.upper() == 'X':
            play_2_mark = 'O'
            print('Player 2, you will be O.')
        else:
            play_2_mark = 'X'
            print('Player 2, you will be X.')

    nums_dictionary = {1: 0, 2: 2, 3: 4, 4: 0, 5: 2, 6: 4,
                       7: 0, 8: 2, 9: 4}
    board_move = board_value()

    # Retrieves the dictionary key for row 1, row 2 and so on
    if board_move in range(1, 4):
        if row1[(nums_dictionary[board_move])] == ' ':
            row1[(nums_dictionary[board_move])] = play_2_mark.upper()
            display()
        else:
            print("Someone already did that move!")
            player_2_turn()
    elif board_move in range(4, 7):
        if row3[(nums_dictionary[board_move])] == ' ':
            row3[(nums_dictionary[board_move])] = play_2_mark.upper()
            display()
        else:
            print("Someone already did that move!")
            player_2_turn()
    else:
        if row5[(nums_dictionary[board_move])] == ' ':
            row5[(nums_dictionary[board_move])] = play_2_mark.upper()
            display()
        else:
            print("Someone already did that move!")
            player_2_turn()

def winner(row1, row3, row5):
    # Checks to see if the criteria for winning has been met
    global game_over

    if play_1_mark == 'X':
        if row1 == ['X','|','X','|','X'] or row3 == ['X','|','X','|','X'] or row5 == [
            'X','|','X','|','X']:
            game_over = True
            print("\nPlayer 1, you win!")
        elif (row1[0] == 'X' and row3[0] == 'X' and row5[0] == 'X') or (
                row1[2] == 'X' and row3[2] == 'X' and row5[2] == 'X') or (
                row1[4] == 'X' and row3[4] == 'X' and row5[4] == 'X'):
            game_over = True
            print("\nPlayer 1, you win!")
        elif (row1[0] == 'X' and row3[2] == 'X' and row5[4] == 'X') or (
                row1[4] == 'X' and row3[2] == 'X' and row5[0] == 'X'):
            game_over = True
            print("\nPlayer 1, you win!")
        elif row1 == ['O','|','O','|','O'] or row3 == ['O','|','O','|','O'] or row5 == [
            'O','|','O','|','O']:
            game_over = True
            print("\nPlayer 2, you win!")
        elif (row1[0] == 'O' and row3[0] == 'O' and row5[0] == 'O') or (
                row1[2] == 'O' and row3[2] == 'O' and row5[2] == 'O') or (
                row1[4] == 'O' and row3[4] == 'O' and row5[4] == 'O'):
            game_over = True
            print("\nPlayer 2, you win!")
        elif (row1[0] == 'O' and row3[2] == 'O' and row5[4] == 'O') or (
                row1[4] == 'O' and row3[2] == 'O' and row5[0] == 'O'):
            game_over = True
            print("\nPlayer 2, you win!")
        elif (' ' not in row1) and (' ' not in row3) and (' ' not in row5):
                game_over = True
                print("\nYou tied!")
    elif play_1_mark == 'O':
        if row1 == ['X','|','X','|','X'] or row3 == ['X','|','X','|','X'] or row5 == [
            'X','|','X','|','X']:
            game_over = True
            print("\nPlayer 2, you win!")
        elif (row1[0] == 'X' and row3[0] == 'X' and row5[0] == 'X') or (
                row1[2] == 'X' and row3[2] == 'X' and row5[2] == 'X') or (
                row1[4] == 'X' and row3[4] == 'X' and row5[4] == 'X'):
            game_over = True
            print("\nPlayer 2, you win!")
        elif (row1[0] == 'X' and row3[2] == 'X' and row5[4] == 'X') or (
                row1[4] == 'X' and row3[2] == 'X' and row5[0] == 'X'):
            game_over = True
            print("\nPlayer 2, you win!")
        elif row1 == ['O', '|', 'O', '|', 'O'] or row3 == ['O', '|', 'O', '|', 'O'] or row5 == [
            'O', '|', 'O', '|','O']:
            game_over = True
            print("\nPlayer 1, you win!")
        elif (row1[0] == 'O' and row3[0] == 'O' and row5[0] == 'O') or (
                row1[2] == 'O' and row3[2] == 'O' and row5[2] == 'O') or (
                row1[4] == 'O' and row3[4] == 'O' and row5[4] == 'O'):
            game_over = True
            print("\nPlayer 1, you win!")
        elif (row1[0] == 'O' and row3[2] == 'O' and row5[4] == 'O') or (
                row1[4] == 'O' and row3[2] == 'O' and row5[0] == 'O'):
            game_over = True
            print("\nPlayer 1, you win!")
        elif (' ' not in row1) and (' ' not in row3) and (' ' not in row5):
            game_over = True
            print("\nYou tied!")
