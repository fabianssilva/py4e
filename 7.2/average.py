# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lineCount = 0
valueTotal = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        words = line.split()
        lineCount += 1
        valueTotal += float(words[1])
        print(words)

averageNumber = (float(valueTotal/lineCount))

print("Average spam confidence: {0:.12f}".format(averageNumber))
