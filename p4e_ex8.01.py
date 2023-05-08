# friends = ['Joseph', 'Glen', 'Sally']

# for friend in friends:
#     print('Happy New Year', friend + '!')

# print('Done!')
# print(friends[1])

# ------

# total = 0
# count = 0

# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done': break
    
#     try:
#         value = float(inp)
#     except:
#         print('Enter numeric value.')
#         continue
    
#     total = total + value
#     count = count + 1

# print('Average: ', total/count)

# -----

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