total = 0
count = 0

while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    
    try:
        value = float(inp)
    except:
        print('Enter numeric value.')
        continue
    
    total = total + value
    count = count + 1

print('Average: ', total/count)