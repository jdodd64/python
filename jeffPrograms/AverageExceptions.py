def main():
	# Ask user for filename
	filename = input('Please enter a filename to access: ')

	# Call process_file(), passing the
	#		user-designated filename
	process_file(filename)

# The process_file() function takes one parameter (file).
#		It contains a loop that tries to loop through each
#		line of the file and convert the string to an integer,
#		then add that integer to the accumulator, 'total,'
#		then increases a counter by 1.
#
#	If it encounters an IOError or ValueError, these are
#		handled.
def process_file(file):
	counter = 0 	# Initiate counter
	total = 0			# Initiate accumulator

	
	try:
		f = open(file, 'r') # Open file
		for line in f:
			# Convert each line to an integer and add it to the accumulator
			total += int(line) # Increase the accumulator
			counter += 1 # Increment counter
			print('.')
		f.close() # Close file
		
		print('Found ' + str(counter) + ' numbers.')
		print('The total of these numbers is: ' + str(total))

	except IOError as e: # If the file cannot be found...
			print('Error:', e)
	except ValueError as e: # If the line cannot be converted to an integer...
			print('Error:', e)
			print('Invalid entry: ' + line)


# Start the program
main()
			