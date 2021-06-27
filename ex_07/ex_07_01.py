inFile = input("Enter a file name: ")
try :
    fhand = open(inFile)
except:
    print("File not found :", inFile)
    quit()

for line in fhand :
    line = line.rstrip()
    print(line.upper())
