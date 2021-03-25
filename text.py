def revword(word):
    i = len(word)-1
    newString = ''
    while  i>=0:
        newString = newString + str(word[i])
        i = i-1
    return newString

def countword():
    fname = open("text.txt")
    fname = fname.read()
    fname = fname.lower()
    fname = fname.split()
    word = fname[0]
    counter = 1
    for findWord in fname:
        findWord=revword(findWord)
        if word==findWord:
            counter = counter + 1
    return (int(counter))