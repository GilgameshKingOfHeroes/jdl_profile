from random import randint
import time

Password = ''
WordLimit = 0
SPACES = '_'
PASSWORDguessesABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

Security = PASSWORDguessesABC[randint(0,25)]

def Hacking():
	Hacker = raw_input("Tracing complete. Please input new USR NAME:")
	print("USR NAME inputted. Welcome, " + Hacker + ". Initializing PASSWORD cracking subroutines")
	time.sleep(3)
	print("Subroutines initiated. Cracking sequence initiated.")
	time.sleep(6)
	print("WARNING WARNING: Security systems alerted to intrusion. Beginning sector sweep.")
	time.sleep(4)
	print("Automatic scripts have been aborted. Manual Override initiated. Enter PASSWORD code:")
	PASSCODE()

Hacking()

def PASSCODE():
	
	global Password, WordLimit, SPACES, PASSWORDguessesABC
	
	
