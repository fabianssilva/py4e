score = input("Enter Score: ")
fscore = float(score)
grade = ""

if fscore < 0.0 or fscore > 1.0:
    print("Score must be between 0.00 and 1.00")
    quit()
elif fscore >= 0.9:
	grade = 'A'
elif fscore >= 0.8:
	grade = 'B'
elif fscore >= 0.7:
	grade = 'C'
elif fscore >= 0.6:
	grade = 'D'
elif fscore <= 0.6:
	grade = 'F'

print ("Grade is " + grade)