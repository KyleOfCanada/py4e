inpCount = 0
inpSum = 0

while True :
    inp = input("Enter a number: ")
    if inp == 'done':
        break

    try:
        inp = float(inp)

    except:
        print("Invalid input!")
        continue

    inpSum = inpSum + inp
    inpCount = inpCount + 1

if inpCount == 0:
    print("No numbers entered!")
else :
    inpMean = inpSum / inpCount
    print(inpSum, inpCount, inpMean)
