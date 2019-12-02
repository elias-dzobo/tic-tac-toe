import random 

def display_board(board):
	print('  ___+___+___ ' )
	print( ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ' )
	print('  ___+___+___ ' )
	print( ' | ' + board[6] + ' | ' + board[5] + ' | ' + board[4] + ' | ' )
	print('  ___+___+___ ' )
	print( ' | ' + board[3] + ' | ' + board[2] + ' | ' + board[1] + " | " )
	print('  ___+___+___ ' )

def display_board_test():
	print('  ___+___+___ ' )
	print( ' | ' + '7' + ' | ' + '8' + ' | ' + '9' + ' | ' )
	print('  ___+___+___ ' )
	print( ' | ' + '6' + ' | ' + '4' + ' | ' + '3' + ' | ' )
	print('  ___+___+___ ' )
	print( ' | ' + '3' + ' | ' + '2' + ' | ' + '1' + " | " )
	print('  ___+___+___ ' )

def player_input():
	player_marker = ''
	#while player_marker != 'X' or player_marker != 'O':
	player_marker = input(' Do you want to be X or O: ').upper
	if player_marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')


def place_marker(board, marker, position):
	board[position] = marker

	


def win_check(board, marker):
	return((board[1] == marker and board[2] == marker and board[3] == marker) or #last row
	(board[4] == marker and board[5] == marker and board[6] == marker) or #second row
	(board[7] == marker and board[8] == marker and board[9] == marker) or # first row
	(board[1] == marker and board[4] == marker and board[9] == marker) or # first column
	(board[2] == marker and board[5] == marker and board[8] == marker) or # second column
	(board[3] == marker and board[6] == marker and board[7] == marker) or # 3rd column
	(board[1] == marker and board[5] == marker and board[7] == marker) or # diagonal one
	(board[3] == marker and board[5] == marker and board[9] == marker)) # disagonal two

def choose_first():
	who_first = random.randint(0,1)
	if who_first == 0:
		return 'Player 1'
	else:
		return 'Player 2'

def space_check(board, position):

	return board[position] == ' '

def full_board_check(board):
	for i in range(0, 10):
		if space_check(board, i):
			return False
	return True

def full_board_checker(board):
	if (board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9]) != ' ':
		return True


def player_choice(board):
	position = ' '
	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
		position = input('Choose your next position: (1-9) ')
	return int(position)

def replay():
	play_again = input('Do you want to play again? \n yes or no')
	if play_again == ' yes' or play_again == ' YES':
		return True
	elif play_again == ' no' or play_again == ' NO':
		return False
	

print('Welcome to Tic Tac Toe')

player_input()

while True:
	print('Study Board layout and positions')
	display_board_test()
	theBoard = [ ' ' ] * 10
	player1_marker, player2_marker = player_input()
	whose_turn = choose_first()
	print(whose_turn +  ' would go first')
	game_on = True


	while game_on:
		if whose_turn == 'Player 1':

			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player1_marker, position)



			if win_check(theBoard, player1_marker):
				display_board(theBoard)
				print('Congratulations Player 1 has won')
				game_on = False

			else:
				if full_board_checker(theBoard):
					display_board(theBoard)
					print('game is a draw')
					break
				else:
					whose_turn = 'Player 2'


		else:
			display_board(theBoard)
			position = player_choice(theBoard)
			place_marker(theBoard, player2_marker, position)

			if win_check(theBoard, player2_marker):
				display_board(theBoard)
				print('Congratulations player 2  wins')
				game_on = False

			else:
				if full_board_checker(theBoard):
					display_board(theBoard)
					print('game is a draw')
					break
				else:
					whose_turn = 'Player 1'


	if not replay():
		break








