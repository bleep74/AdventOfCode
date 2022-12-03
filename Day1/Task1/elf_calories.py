#python script
#day 1 challenge 1

highestElf = 0
highestCalories = 0
elfCount=1
totalCalories = 0

file1 = open('elves.txt', 'r')


Lines = file1.readlines()

for line in Lines:
	if line=='\n':
		elfCount +=1
		totalCalories = 0
	else:
		totalCalories += int(line)
		if totalCalories > highestCalories:
			highestCalories = totalCalories
			highestElf = elfCount

file1.close
print("Elf with highest calories: {} ; Calorie Amount: {}".format(highestElf, highestCalories))