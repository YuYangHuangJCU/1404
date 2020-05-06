"""
Program to play a user's guitars
"""
"""imports"""
from CP1404.prac_06. guitar import Guitar

def main():#Function for main functinalities
	"""unit tests after creation of the guitar object"""
	guitars = []#empty array

	print("My guitars! Enter a blank name to quit.")
	#use a while loop to collect input
	while(True):


		
		name = input("Name: ")
		if name == "":
			break
		year = int(input("Year: "))
		cost = float(input("Cost: "))

		#create instance and add to list
		new_guitar = Guitar(name, year, cost)
		print("{} added".format(new_guitar))
		guitars.append(new_guitar)

	#print all guitars added
	print("These are my guitars:")
	for i in range(len(guitars)):
		buffer = "Guitar {}: {} ({}), worth $ {:.2f}".format(
			i+1, guitars[i].name, guitars[i].year, guitars[i].cost)

		#determine if it vintage
		if guitars[i].is_vintage():
			buffer += " (vintage)"

		#print
		print(buffer)

if __name__ == "__main__":
	main()
