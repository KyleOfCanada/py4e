inFile = input("Enter a file name: ")
try :
    fhand = open(inFile)
except:
    print("File not found :", inFile)
    quit()

counter = 0
sum = 0
for line in fhand :
    if line.startswith('X-DSPAM-Confidence:') :
        spcPos = line.find(' ')
        line = line[spcPos:]
        line = line.strip()
        line = float(line)
        sum = sum + line
        counter = counter + 1
    else :
        continue

print('Average spam confidence: ', sum / counter)
