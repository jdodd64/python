import random
GLOBAL FILENAME = 'randomNumbers.txt'

def main():
	# Ask user for number of random numbers to generate
	numbers = int(input('How many random numbers would you like to generate? '))

	# Call 'create_file()' passing 'numbeers' as the argument
	#		in order to generate the proper number of random
	#		numbers
	create_file(numbers)
	read_file(FILENAME)





def create_file(num):
	f = open(FILENAME, 'w')
	for x in range(0,num):
		f.write(random.randint(1,1000))

def read_file(file):





















main()