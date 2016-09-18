from random import randint

NEPNEPscore = 0
computerScore = 0
Ties = 0
choices = ['Rock','Paper','Scissors']
Quiting = ['Yes', 'No']

def Play():
	global NEPNEPscore, computerScore, Ties

	computer = choices[randint(0,2)]

	NEPNEP = False

	while NEPNEP == False:
		NEPNEP = input('What shall you choose? Rock, Paper, or Scissors?')
		if NEPNEP == computer:
			print('Nepu! We tied!')
			Ties += 1
		elif NEPNEP == 'Rock':
			if computer == 'Paper':
				print('HAHAHA!! ' + computer + ' covers ' + NEPNEP + '! Your opponent has just scored a point!')
				computerScore += 1
			else:
				print('NEPU! ' + NEPNEP + ' SMASHES ' + computer + '! You have just scored a point!')
				NEPNEPscore += 1
		elif NEPNEP == 'Paper':
			if computer == 'Scissors':
				print('Foolishness ' + computer + ' slices ' + NEPNEP + '! Your opponent has just scored a point!')
				computerScore += 1
			else:
				print('YATTA! ' + NEPNEP + ' chokes ' + computer + '! You have just scored a point!')
				NEPNEPscore += 1
		elif NEPNEP == 'Scissors':
			if computer == 'Rock':
				print('NYAAA! ' + computer + ' obliterates ' + NEPNEP + '! Your opponent has just scored a point!')
				computerScore += 1
			else:
				print('...meow... ' + NEPNEP + ' skewers ' + computer + '! You have just scored a point!')
				NEPNEPscore += 1
		else:
			NEPNEP = input('Do you want to quit? (y/n) ')
			if NEPNEP == 'y':
				print("Here's the scores! You have", NEPNEPscore, "points, your opponent has", computerScore, "points, and your number of ties is", Ties)
				break
			else:
				print("Okay! Let's keep playing!")
		NEPNEP = False
		computer = choices[randint(0,2)]
		Quiting = ['Yes', 'No']
Play()
