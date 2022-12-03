#python script
#day 3 challenge 1

file1 = open('elves.txt','r')

points=0

Lines = file1.readlines()

for line in Lines:
	compartment1 = line[:int(len(line)/2)].rstrip()
	compartment2 = line[int(len(line)/2):].rstrip()
	
	print("compartment 1: {} ; compartment 2: {}".format(compartment1,compartment2))
	
	for letter in compartment1:
		if letter in compartment2:
		
			if letter.islower():
				points += ord(letter) - 96
				print("Matching letter: {}  Points: {}".format(letter, ord(letter)-96))
				break
			else:
				points += ord(letter) - 38
				print("Matching letter: {}  Points: {}".format(letter, ord(letter)-38))
				break
			

print("Total Points: {}".format(points))
			
			