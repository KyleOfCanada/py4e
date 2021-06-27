nums = list()

while True :
    
    inp = input('Enter a number: ')

    if inp == 'done' :
        break

    try:
        num = float(inp)
    except:
        print('Not a number!')
        continue

    nums.append(num)

print('Maximum:', max(nums))
print('Minimum:', min(nums))
