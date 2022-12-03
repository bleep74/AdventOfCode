#python script
#day 3 challenge 1
import time

tstart = time.time()
file1 = open('elves.txt','r')

points=0

Lines = file1.readlines()

for line in Lines:
	compartment1 = line[:int(len(line)/2)].rstrip()
	compartment2 = line[int(len(line)/2):].rstrip()
		
	for letter in compartment1:
		if letter in compartment2:
			if letter.islower():
				points += ord(letter) - 96
				break
			else:
				points += ord(letter) - 38
				break
			
print("Total Points: {}".format(points))
tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))
			