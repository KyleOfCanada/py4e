inFile = input("Enter a file name: ")

if inFile == 'na na boo boo' :
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    quit()

try :
    fhand = open(inFile)
except:
    print("File not found :", inFile)
    quit()

counter = 0
for line in fhand :
    if line.startswith('Subject: ') :
        counter = counter + 1

print('There were', counter, 'subject lines in', inFile)
