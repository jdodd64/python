def main():
	import random 	# Import 'random' library
	list = []		# Create empty list
	i = 0			# Initialize iterator for loop

	# This while loop will loop 6 times
	#	and append a random integer in
	#	the range 0..99 inclusive to
	#	the end of the 'list' list on
	#	each iteration.
	while i < 6:
		list.append(random.randint(0,99))
		i += 1

	# This for loop will iterate over
	#	each element in the 'list'
	#	list, printing out the element
	#	on each iteration.
	for n in list:
		print(n)

main()