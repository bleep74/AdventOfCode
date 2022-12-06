#python script
#Day 5 Challenge 1
import time

tstart = time.time()
file1 = open('elves.txt','r')


Lines = file1.readlines()

for line in Lines:

	length = len(line)
	count = 0
	lower = 0
	upper = 4
	matches = 0
	
	while count < length:
		substring = line[lower:upper]
		
		for character in substring:
			#print("Character : {}  Substring: {}".format(character,substring))
			if substring.count(character) > 1:
				matches = 0
				break
			else:
				matches += 1
				
		if matches == 4:
			print("Character Upper Limit: {}".format(upper))
		
		lower += 1
		upper += 1
		count += 1
		


tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))