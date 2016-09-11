from random import randint

NEPNEPscore = 0
computerScore = 0
Ties = 0
choices = ['Rock','Paper','Scissors']

def Play():

	computer = choices[randint(0,2)]

	NEPNEP = False

	while NEPNEP == False:
		NEPNEP = input('What shall you choose? Rock, Paper, or Scissors?')
		if NEPNEP == computer:
			print('Nepu! We tied!')
			Ties + 1
		elif NEPNEP == 'Rock':
			if computer == 'Paper':
				print('HAHAHA!!', computer, 'covers', NEPNEP)
				computerScore + 1
			else:
				print('NEPU!', NEPNEP, 'SMASHES', computer)
				NEPNEPscore + 1
		elif NEPNEP == 'Paper':
			if computer == 'Scissors':
				print('Foolishness', computer, 'slices', NEPNEP)
				computerScore + 1
			else:
				print('YATTA!', NEPNEP, 'chokes', computer)
				NEPNEPscore + 1
		elif NEPNEP == 'Scissors':
			if computer == 'Rock':
				print('NYAAA!', computer, 'obliterates', NEPNEP)
				computerScore + 1
			else:
				print('...meow...', NEPNEP, 'skewers', computer)
				NEPNEPscore + 1
		NEPNEP = False
		computer = choices[randint(0,2)]
Play()
