inString = input('Give me a string:' )
inLetter = input('Give me a letter: ')

def count(string, letter) :
    counter = 0
    for letters in string :
        if letters == letter :
            counter = counter + 1
    print(counter)

count(inString, inLetter)
