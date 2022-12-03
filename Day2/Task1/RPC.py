#python script
#day 2 challenge 1
import time

tstart = time.time()
points = 0

file1 = open('elves.txt','r')

Lines = file1.readlines()

for line in Lines:
		x = line.split("\n")
		y = x[0].split(" ")
		
		match y[0]:
			case "A":
				match y[1]:
					case "X":
						points += 4
					case "Y":
						points += 8
					case "Z":
						points += 3
			case "B":
				match y[1]:
					case "X":
						points += 1
					case "Y":
						points += 5
					case "Z":
						points += 9
			case "C":
				match y[1]:
					case "X":
						points += 7
					case "Y":
						points += 2
					case "Z":
						points += 6
						
file1.close
print("Total Points: {}".format(points))
tstop = (time.time() - tstart)
print ("Time : {}".format(tstop))