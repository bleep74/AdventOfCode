#python script
#day 1 challenge 2
import time

tstart = time.time()

highestElf = 0
highestCalories = 0
elfCount=1
totalCalories = 0

elfArray=[]

file1 = open('elves.txt', 'r')


Lines = file1.readlines()

for line in Lines:
	if line=='\n':
		elfArray.append(totalCalories)
		elfCount +=1
		totalCalories = 0
	else:
		totalCalories += int(line)
		if totalCalories > highestCalories:
			highestCalories = totalCalories
			highestElf = elfCount

file1.close

elfArray.sort()

topThreeElves = elfArray[len(elfArray)-1] + elfArray[len(elfArray)-2] + elfArray[len(elfArray)-3]

print("Calorie Amount for top 3: {}".format(topThreeElves))
tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))