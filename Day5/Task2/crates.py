#python script
#Day 5 Challenge 1
import time

tstart = time.time()
file1 = open('elves.txt','r')

crates = ["","","","","","","","",""]

crates[0] = ["S","M","R","N","W","J","V","T"]
crates[1] = ["B","W","D","J","Q","P","C","V"]
crates[2] = ["B","J","F","H","D","R","P"]
crates[3] = ["F","R","P","B","M","N","D"]
crates[4] = ["H","V","R","P","T","B"]
crates[5] = ["C","B","P","T"]
crates[6] = ["B","J","R","P","L"]
crates[7] = ["N","C","S","L","T","Z","B","W"]
crates[8] = ["L","S","G"]

Lines = file1.readlines()

for line in Lines:
	motions = line.rstrip().split(" ")
	count = 0
	letter = []
	
	counter = int(motions[1])
	
	motion3 = int(motions[3])-1
	
	while count < counter:
		letter.append(crates[motion3][len(crates[motion3]) - 1])	
		crates[motion3].pop(len(crates[motion3]) - 1)
		count +=1
		
	res = letter[::-1]
	
	for let in res:
		crates[int(motions[5])-1].append(let)
	

	letter = []
		
print("Final Letters : {} {} {} {} {} {} {} {} {}".format(crates[0][len(crates[0]) - 1],crates[1][len(crates[1]) - 1],crates[2][len(crates[2]) - 1],crates[3][len(crates[3]) - 1], crates[4][len(crates[4]) - 1], crates[5][len(crates[5]) - 1], crates[6][len(crates[6]) - 1], crates[7][len(crates[7]) - 1],crates[8][len(crates[8]) - 1]))
		
tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))