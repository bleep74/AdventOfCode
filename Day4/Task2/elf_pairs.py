#python script
#day 4 challenge 1
import time

tstart = time.time()
file1 = open('elves.txt','r')

pairTotals = 0


Lines = file1.readlines()


for line in Lines:
	pairs = line.split(",")
	coverage = pairs[0].rstrip().split("-")
	coverage1 = pairs[1].rstrip().split("-")
	
	range1 = range(int(coverage[0]),int(coverage[1])+1)
	range2 = range(int(coverage1[0]),int(coverage1[1])+1)
	
	for number in range1:
		if number in range2:
			print("Number : {} Range: {}".format(number, range2))
			pairTotals=pairTotals+1
			break

print("Total overlap pairs: {}".format(pairTotals))
tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))