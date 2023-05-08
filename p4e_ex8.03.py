numlist = list()

while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    if inp == 'list':
        print(numlist)
        continue
    
    try:
        value = float(inp)
    except:
        print('Enter numeric value.')
        continue

    numlist.append(value)

print('Average: ', sum(numlist)/len(numlist))