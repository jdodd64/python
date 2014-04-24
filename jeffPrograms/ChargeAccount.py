def main():
	accounts = []					# Initialize 'accounts' list
	path = 'charge_accounts.txt'	# Store the file path in a variable for easy changes
	f = open(path, 'r')				# Open the file
	searchLength = 7				# Define searchLength variable for input validation
	number = ''						# Initialize number variable
	search = False

	# Iterate over each line in the text file, appending
	#	each line to the 'accounts' list.
	for line in f:
		accounts.append(line.strip())
	f.close()						# Close the file.

	# This while loop asks the user for the account number
	#	to number. Unless its length is 7, it will
	#	prompt the user to try again.
	while len(number) != searchLength:
		number = input('Please enter your 7-digit account number: ')
		if len(number) != searchLength:
			print()
			print('The account number your entered was not 7 digits.')
			print('Please try again.')
			print()

	# Set 'search' equal to the result of calling
	#	searchAccounts(), passing the accounts list
	#	and user input as arguments
	search = searchAccounts(accounts, number)

	if search == True:
		print('You account number was found! >>> ' + number) 	# Search success statement
	else:
		print('You did not enter a valid account number.')		# Search failure statement

def searchAccounts(acc, num):
	for n in acc:
		if n == num:
			return True


main()