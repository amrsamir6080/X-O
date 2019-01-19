from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] +' | '  + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] +' | '  + board[3])
    print('   |   |')
#.............................................................................
import random

def choose_first(): 
    
    if random.randint(0,1) == 0 :
        return 'player 2'
    else:
        return 'player 1'
#.............................................................................
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True        
#.............................................................................
def place_marker(board,marker,position):
    board[position] = marker    
#.............................................................................
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9]or not space_check(board,position):
        position = int(input('choose a position : (1-9) '))
    return position    
#.............................................................................
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'X'):
        marker = input('player1 : choose X: or O: ').upper()   
    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')    
#.............................................................................
def space_check(board,position):
    return board[position] == ' '  
#.............................................................................
def win_check(board,mark):
    return((board[1]==board[2]==board[3]==mark)or
    (board[4]==board[5]==board[6]==mark)or
    (board[7]==board[8]==board[9]==mark)or
    (board[1]==board[4]==board[7]==mark)or
    (board[2]==board[5]==board[8]==mark)or
    (board[3]==board[6]==board[9]==mark)or
    (board[1]==board[5]==board[9]==mark)or
    (board[3]==board[5]==board[7]==mark))
#.............................................................................
def replay():
    
    return input('you wanna play again ? ').lower().startswith('y')              
#.............................................................................
print('welcome to X & O')

while True:
    the_board = [' ']*10
    player1_marker , player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('ready to play ? y or n ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on :
        if turn == 'player 1':
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won :)')
                game_on = False  
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game !')
                    break
                else:
                    turn = 'player 2'
        else:
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player 2 has won :)')
                game_on = False  
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game !')
                    break
                else:
                    turn = 'player 1'
    

    if not replay():
        break
    
    