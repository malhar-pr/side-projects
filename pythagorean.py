import time

pyth_list=[]	#Creates an empty list that will hold the tuples containing Pythagorean/Fermat triplets
power_list=[]	#Creates an empty list that will cache the value of each index raised to the specified exponent in the given range
print("---------------------------------------------------------------------\nMALHAR'S PYTHAGOREAN TRIPLET GENERATOR / FERMAT'S LAST THEOREM SOLVER\n---------------------------------------------------------------------")
UserInput1 = input("What power will be selecting? \n")
UserInput2=input("And till what range would you like to go to? \n")
UserInput3=input("Would you like to be 100% accurate? [1/0] \n")
if UserInput3 == '0':
	UserInput4 = input("Order of accuracy (put 0 if 100% accurate): ")
	order=int(UserInput4)	#typecasts the user-input value to int

start=time.process_time()	#stores current process time in variable to calculate time elapsed to run the code

power=int(UserInput1)		#typecasts the user-input value to int
crange=int(UserInput2)		#typecasts the user-input value to int

def append_check(accornot):
	"""
		Inputs: Takes in variable "accornot" which determines if the user requires an accurate answer or not
		Appends a tuple containing the triplet that satisfies the condition to the list, "pyth_list"
		Returns: nothing
	
	""" 
	if accornot == '1':
		if (power_list[a] + power_list[b] == power_list[c]):	#Compares exact condition
			pyth_list.append((a,b,c))
	elif accornot == '0':
		if (power_list[a] + power_list[b] < (1+(pow(10,-order)))*power_list[c]) and (power_list[a] + power_list[b] > (1-(pow(10,-order)))*power_list[c]):
			#compares approximate condition within required order parameter
			pyth_list.append((a,b,c))
	else:
		print("Invalid Input")


for var in range(crange):				
	power_list.append(pow(var,power))	#creates cache of the value of each index raised to the specified exponent in the given range, to reduce time complexity

for c in range(crange):
	for b in range(c):
		for a in range(b):
			append_check(UserInput3)	#calls the function that checks for the condition and appends to list if condition is True
	if crange>=10000:
		if not (c%(crange/1000)):
			print(str(c/(crange/100)) + "% complete\r",)
	elif crange<10000:
		if not (c%(crange/100)):
			print(str(int(c/(crange/100))) + "% complete\r",)	#Gives loading indicator to show how much has completed

del power_list		#Deletes cache of value of indices raised to the specified exponent

if (pyth_list)==[]:	#If no results are found
	print ("Search Complete. No results found.")
else:
	print ("The list of triplets are: ") 
	print(pyth_list)

del pyth_list

a1 = input("Runtime of the program is {} seconds. Press any key to exit".format(time.process_time()-start))



