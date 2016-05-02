import sys

class VerbosityCounter():
    reader()

def reader():
    file = sys.argv[1]
    prompt = input("Enter a filename: ")
    with open(prompt) as f:
        text = f.read()
    callback(text)
    f.close()

def callback(text):
    t = 0
    end = 0
    count = len(text)
    for t in range(0, count):
        if text[t] == '.' or text[t] == '!' or text[t] == '?':
            end += 1

    words = text.split()

    actualwords = 0
    testwords = 0

    for i in words:
        testwords = words[n]
        testwords = len(testwords)
        if testwords >=3:
            actualwords += 1
            n +=1

    num = len(words)
    print("The number of words in this document is:", len(words), "The number of actual words is:", len())
    print("The average number of words per sentence in this document is:", actualwords/end)

