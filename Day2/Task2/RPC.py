#python script
#day 2 challenge 1

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
						points += 3
					case "Y":
						points += 4
					case "Z":
						points += 8
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
						points += 2
					case "Y":
						points += 6
					case "Z":
						points += 7

		

file1.close

print("Total Points: {}".format(points))