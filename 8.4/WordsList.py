# Use the file name mbox-short.txt as the file name
mailSenders = dict()
bigWord = None
bigCount = None
words = list()

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:

    wordsFromLine = line.split()

    for word in wordsFromLine:
        if word in words:
            continue
        else:
            words.append(word)


words.sort()
print(words)