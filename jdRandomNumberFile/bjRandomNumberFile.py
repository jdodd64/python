# Import random module
import random

# Declare global variable for the filename
global FILENAME
FILENAME = './randomNumbers.txt'

def main():
	# Ask user for number of random numbers to generate
	numbers = int(input('How many random numbers would you like to generate? '))
	
	# Call 'create_file()' passing 'numbers' as the argument
	#		in order to generate the proper number of random
	#		numbers
	create_file(numbers)

	# Call 'read_file()' to read each random number in the
	#		the file and sum the numbers, then print the sum
	read_file(FILENAME)

# 'Create_file()' takes one parameter, the number the
#		user entered, then generates that many random
#		numbers, each on a separate line in the
#		'randomNumbers.txt' file.
def create_file(num):
	outFile = open(FILENAME, 'w') # Open FILENAME in write mode
	for x in range(0,num):
		outFile.write(str(random.randint(1,1000))+'\n')
	
	outFile.close() # Close the file

# 'Read_file()' takes one parameter (the filename).
#		It opens the 'randomNumbers.txt' file in
#		read mode, and adds each line (random number)
#		to the 'line_sum' accumulator. It then prints
#		the result.
def read_file(file):
	line_sum = 0 # Initialize accumulator
	inFile = open(FILENAME, 'r') # Open FILENAME in read mode
	for line in inFile:
		line_sum += int(line)

	inFile.close() # Close the file

	for x in range(0,5):
		print('.')

	print('The sum of all the random numbers in ' + FILENAME + ' is: ' + str(line_sum))

# Start the program
main()