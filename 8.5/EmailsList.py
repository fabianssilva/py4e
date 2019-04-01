# Use the file name mbox-short.txt as the file name
mailSenders = list()
mailAddresses = 0

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:

    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        mailSender = words[1]
        mailSenders.append(mailSender)
        mailAddresses += 1
        print(mailSender)

print("There were", mailAddresses, "lines in the file with From as the first word")
