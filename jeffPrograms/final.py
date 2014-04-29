# This global variable is used to determine
#		how many items will be entered into the
#		list.
COUNT = 20

def main():
	l_numbers = [] # Initialize numbers list
	c = 0 # Initialize counter

	# This for loop appends 'COUNT' numbers
	#		to l_numbers by calling get_num()
	#		to grab obtain user input
	for i in range(0, COUNT):
		c +=1 
		l_numbers.append(get_num(c))


	# Print the results
	print()
	print('#### RESULTS ####')
	print('The lowest number in the list is:\t', min(l_numbers))
	print('The highest number in the list is:\t', max(l_numbers))
	print('The sum of the list is:\t\t\t', list_sum(l_numbers))
	print('The average of the list is:\t\t', list_avg(l_numbers))
	print()

# get_num takes one argument, 'counter' which
#		is simply used to show the user how many
#		numbers they've entered.
#
# get_num tries to obtain 'float' input from
#		the user. It handles 'ValueError' exceptions
#		and loops back to the input prompt if an
#		exception is thrown. Otherwise, it returns
#		the input back to the 'for' loop in main()
def get_num(counter):
	while True:
		try:
			print(counter, ". ", sep='', end='') # Print the counter for the user
			num = float(input('Please enter a number to be added to the list: ')) # Get user input
		except ValueError: # This handles incorrect input
			print('That is not a valid number. Try again...') # Error msg
		else:
			return num # Return user input to the for loop in main()

#	list_sum() takes one argument, 'list.'
#		Each item is iterated over and
#		accumulated in the 'total' variable
def list_sum(list):
	total = 0
	for n in list:
		total += n
	return total

#	list_avg() takes one argument, 'list.'
#		First, list_sum() is called to
#		figure the total. Then that total
#		is averaged and returned.
def list_avg(list):
	total = list_sum(list)
	return total / len(list)



main()