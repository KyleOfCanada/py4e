while True :
    inp = input("Enter a number: ")
    if inp == 'done':
        break

    try:
        inp = float(inp)
    except:
        print("Invalid input!")
        continue

    try:
        inpMax = max(inpMax, inp)
        inpMin = min(inpMin, inp)
    except:
        inpMax = inp
        inpMin = inp

try:
    print(inpMax, inpMin)
except:
    print("No numbers entered!")
