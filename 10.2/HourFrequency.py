# Use the file name mbox-short.txt as the file name
mailHours = dict()
hours = tuple()

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:

    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        hoursSender = words[5]
        hour = hoursSender[:2]

        mailHours[hour] = mailHours.get(hour, 0) + 1


hours = sorted(mailHours.items())
for k,v in hours:
    print(k, v)

