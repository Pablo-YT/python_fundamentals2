#Create a function that converts Fahrenheit temperatures to Celsius in a file called exercise6.py.

#Start with prompting the user for a temperature in Fahrenheit. Then call your function and pass in the user input as a parameter.

#Your function should:

#have one parameter: the temperature in Fahrenheit
#do the conversion with this formula: C = (F - 32) x 5/9
#ensure that the parameter you pass in is a number by converting it with int()
#Output the result in a full sentence using string interpolation.



print("What is the current temperature?")

Fahrenheit = int(input())

def temp_change(Fahrenheit):
	Celsius = (Fahrenheit - 32) * 5/9
	return	Celsius


print("The Celsius Degree You Entered Is {}.".format(temp_change(Fahrenheit))) 

