import re

fh = open("regex_sum_383305.txt")
text = fh.read()
total = 0

numberList = re.findall("[0-9]+", text)

for value in numberList:
    total += int(value)

print(total)
