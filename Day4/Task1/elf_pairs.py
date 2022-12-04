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
	
	test = 0
	
	if (int(coverage[0]) <= int(coverage1[0])) and (int(coverage[1]) >= int(coverage1[1])):
		print("Coverage : {} {} Coverage1: {} {}".format(coverage[0],coverage[1],coverage1[0],coverage1[1]))
		pairTotals = pairTotals+1
		test=1
		
	if (int(coverage1[0]) <= int(coverage[0])) and (int(coverage1[1]) >= int(coverage[1]) and test==0):
		print("Coverage : {} {} Coverage1: {} {}".format(coverage[0],coverage[1],coverage1[0],coverage1[1]))
		pairTotals = pairTotals+1
			
print("Total overlap pairs: {}".format(pairTotals))
tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))