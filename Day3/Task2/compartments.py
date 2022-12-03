#python script
#day 3 challenge 2

file1 = open('elves.txt','r')

elf = 1
lastLine = ""
matchingList = ""

points=0

Lines = file1.readlines()

for line in Lines:
	match elf:
		case 1:
			lastLine = line.rstrip()
			elf = elf+1
		case 2:
			for letter in lastLine:
				if letter in line:
					matchingList += letter
			elf = elf+1
		case 3:
			for letter in matchingList:
				if letter in line:
					if letter.islower():
						points += ord(letter) - 96
						print("Matching letter: {}  Points: {}".format(letter, ord(letter)-96))
						elf=1
						matchingList=""
						break
					else:
						points += ord(letter) - 38
						print("Matching letter: {}  Points: {}".format(letter, ord(letter)-38))
						elf=1
						matchingList=""
						break	

print("Total Points: {}".format(points))
			
			