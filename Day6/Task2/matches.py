#python script
#Day 6 Challenge 2
import time

tstart = time.time()
file1 = open('elves.txt','r')


Lines = file1.readlines()

for line in Lines:

	length = len(line)
	count = 0
	lower = 0
	upper = 14
	matches = 0
	
	while count < length:
		substring = line[lower:upper]
		ticker = 0
		for character in substring:
			ticker += 1
			#print("Character : {}  Substring: {}".format(character,substring))
			if substring.count(character) > 1:
				matches = 0
				break
			else:
				matches += 1
				
		if matches == 14:
			print("Character Upper Limit: {}".format(upper))
			break
		lower += ticker
		upper += ticker
		count += ticker
		


tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))