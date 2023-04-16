def computepay(hours, rate):  
    if hours > 40 :
        salary = 40 * rate + (hours - 40) * 1.5 * rate
    else :
        salary = hours * rate
    return salary
    
        
while True:
    h = input('Enter the number of hours: ')
    try:
        a = float(h)
    except:
        print("Error, please enter numberic input.")
        continue
    
    while True:
        r = input('Enter the hourly rate: ')
        try:
            b = float(r)
            break
        except:
            print("Error, please enter nuneric input.")
            continue
    
    print('Salary: ', computepay(a, b))
