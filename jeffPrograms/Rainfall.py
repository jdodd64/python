def main():
	# Accumulate user input into list
	rainfall_list = get_rainfall()
	# Store the result of calc_rainfall_total() in rainfall_list_total
	rainfall_list_total = calc_rainfall_total(rainfall_list)
	# Store the result of calc_rainfall_avg() in rainfall_list_avg
	rainfall_list_avg = calc_rainfall_avg(rainfall_list, int(rainfall_list_total))

	# Print the results
	print()
	print('### RESULTS ###########################################')
	print('Rainfall total for the year:\t\t ' + str(rainfall_list_total) + ' inches')
	print('Average monthly rainfall:\t\t ' + '%.2f' % (rainfall_list_avg) + ' inches') # Use string formatting to limit result to 2 decimal places
	# This part has a lot of function calls in one line. It's slightly
	#		confusing at first glance, and I'm sure there's a better
	#		way to do this... but this was my initial attempt at solving 
	#		the problem, and it seemd to work fine.
	#	To determine the named month, determine_month() is called. The argument
	#		passed to the function is the index of the result of min(rainfall_list)
	#		and max(rainfall_list). The index corresponds to a key in the dictionary
	#		in determine_month(). The proper key is found and the value is returned,
	#		a named month. This process is identical for both the min and max
	#		save for the difference between using 'min' on one and 'max' on the other.
	print('Month with the least rainfall:\t\t ' + str(determine_month(rainfall_list.index(min(rainfall_list)))))
	print('Month with the highest rainfall:\t ' + str(determine_month(rainfall_list.index(max(rainfall_list)))))
	print('#######################################################')
	print()

# Get_rainfall iterates 12 times
#  accepting an integer from the
#  user and appending that number
#  to the rainfall list.
def get_rainfall():
	i = 0
	list = []
	
	# Add this just to explain program to user
	print('In this program you will enter rainfall data for each month of the year')
	print()
	print()
	
	while i < 12:
		try:
			# Get user input and append it to a list
			list.append(int(input('Enter the amount of rainfall for month ' + str(i+1) + ': ')))
			i += 1
		except ValueError: # Handle non-integer input
			print('You did not enter a valid number. Please try again.')
	return list

# calc_rainfall_total() iterates over
#		each of the elements in the list
#		passed and totals them in the
#		'total' accumulator.
def calc_rainfall_total(list):
	total = 0
	for e in list:
		total += e
	return total

# calc_rainfall_avg() calculates
#		the average of the list by
#		dividing the total by the
#		number of elements in the list
def calc_rainfall_avg(list, total):
	return total / len(list)

# determine_month() takes an integer
#		and finds the corresponding value
#		for that key in the below dictionary. 
#		The integer passed is the index of 
#		an element of	the rainfall_list.
def determine_month(num):
	return {
	0: "January",
	1: "February",
	2: "March",
	3: "April",
	4: "May",
	5: "June",
	6: "July",
	7: "August",
	8: "September",
	9: "October",
	10: "November",
	11: "December",
	}.get(num)


main()
