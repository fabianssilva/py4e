# Use the file name mbox-short.txt as the file name
mailSenders = dict()
bigWord = None
bigCount = None

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:

    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        print(words)
        mailSender = words[1]
        mailSenders[mailSender] = mailSenders.get(mailSender, 0) + 1
        print(mailSenders)

    for word, count in mailSenders.items():
        if (bigCount is None) or (count > bigCount):
            bigWord = word
            bigCount = count


print(bigWord, bigCount)