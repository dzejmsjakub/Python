num = 0 # number
tot = 0 # total
smallest = None
largest = None

while True:
    sval = input('Enter a number: ') # string value    
    
    if sval == 'done':
        break 
    
    try:
        fval = float(sval) # float value
    
    except:
        print('Invalid input!')
        continue  
    
    if smallest == None or smallest < fval:
        smallest = fval
    
    if largest == None or largest > fval:
        largest = fval  
    
    num = num + 1 # number counting
    tot = tot + fval # total counting

print(smallest, largest)
print(tot, num, tot/num)