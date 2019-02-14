#Define a function that accepts a string as an argument and returns False if the word is less than 8 characters long (or True otherwise).


def Words(string):
	return len(string) >= 8


print(Words("Win"))
