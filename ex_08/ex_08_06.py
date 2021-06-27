nums = list()

while True:

    inp = input('Enter a number: ')

    if inp == 'done':
        break

    try:
        num = float(inp)
    except ValueError:
        print('Not a number!')
        continue

    nums.append(num)

if len(nums) == 0:
    print('No numbers entered!')
else:
    print('Maximum:', max(nums))
    print('Minimum:', min(nums))
