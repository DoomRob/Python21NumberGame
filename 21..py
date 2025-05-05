# Python code to play 21 Number game

# returns the nearest multiple to 4
def nMultiple(num):
	if num >= 4:
		near = num + (4 - (num % 4))
	else:
		near = 4
	return near

def gameLose():
	print ("\n\nYOU LOSE !, Better luck next time !")
	exit(0)
	
# checks whether the numbers are consecutive
def gameCheck(game_sequence):
	i = 1
	while i<len(game_sequence):
		if (game_sequence[i]-game_sequence[i-1])!= 1:
			return False
		i = i + 1
	return True

# starts the game
def gameStart():
	game_sequence = []
	last = 0
	while True:
		print ("Enter 'F' to take the first chance.")
		print("Enter 'S' to take the second chance.")
		chance = input('> ')
		
		# player takes the first chance
		if chance == "F":
			while True:
				if last == 20:
					gameLose()
				else:
					print ("\nYour Turn.")
					print ("\nHow many numbers do you wish to enter?")
					turn = int(input('> '))
					
					if turn > 0 and turn <= 3:
						comp = 4 - turn
					else:
						print ("Wrong input. You are disqualified from the game.")
						gameLose()
			
					i, j = 1, 1

					print ("Now enter the values")
					while i <= turn:
						a = input('> ')
						a = int(a)
						game_sequence.append(a)
						i = i + 1
					
					# store the last element of xyz.
					last = game_sequence[-1] 
					
					# checks whether the input 
					# numbers are consecutive
					if gameCheck(game_sequence) == True: 
						if last == 21:
							gameLose()
							
						else:
							#"Computer's turn."
							while j <= comp:
								game_sequence.append(last + j)
								j = j + 1
							print ("Order of inputs after computer's turn is: ")
							print (game_sequence)
							last = game_sequence[-1]
					else:
						print ("\nYou did not input consecutive integers.")
						gameLose()
						
		# player takes the second chance
		elif chance == "S":
			comp = 1
			last = 0
			while last < 20:
				#"Computer's turn"
				j = 1
				while j <= comp:
					game_sequence.append(last + j)
					j = j + 1
				print ("Order of inputs after computer's turn is:")
				print (game_sequence)
				if game_sequence[-1] == 20:
					gameLose()
					
				else:
					print ("\nYour turn.")
					print ("\nHow many numbers do you wish to enter?")
					inp = input('> ')
					inp = int(inp)
					i = 1
					print ("Enter your values")
					while i <= inp:
						game_sequence.append(int(input('> ')))
						i = i + 1
					last = game_sequence[-1]
					if gameCheck(game_sequence) == True:
						near = nMultiple(last)
						comp = near - last
						if comp == 4:
							comp = 3
						else:
							comp = comp
					else:
						# if inputs are not consecutive
						# automatically disqualified
						print ("\nYou did not input consecutive integers.")
						# print ("You are disqualified from the game.")
						gameLose()
			print ("\n\nCONGRATULATIONS !!!, YOU WIN !")
			exit(0)
			
		else:
			print ("wrong choice")
						
		
game = True
while game == True:
		print ("Player 2 is Computer.")
		print("Do you want to play the 21 number game? (Yes / No)")
		ans = input('> ')
		if ans =='Yes':
			gameStart()
		else:
			print ("Do you want quit the game?(yes / no)")
			nex = input('> ')
			if nex == "yes":
				print ("You are quitting the game...")
				exit(0)
			elif nex == "no":
				print ("Continuing...")
			else:
				print ("Wrong choice")
				