inpMax = None
while True :
    inp = input("Enter a number: ")
    if inp == 'done':
        break

    try:
        inp = float(inp)
    except:
        print("Invalid input!")
        continue

    if inpMax is None :
        inpMax = inp
        inpMin = inp
    elif inp > inpMax :
        inpMax = inp
    elif inp < inpMin :
        inpMin = inp

try:
    print(inpMax, inpMin)
except:
    print("No numbers entered!")
