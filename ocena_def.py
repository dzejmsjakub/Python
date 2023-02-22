def computegrade(value):
    if 0.5 > value >= 0.0 :
        return('2,0')
    elif 0.6 > value >= 0.5 :
        return('3,0')
    elif 0.7 > value >= 0.6 :
        return('3,5')
    elif 0.8 > value >= 0.7 :
        return('4,0')
    elif 0.9 > value >= 0.8 :
        return('4,5')
    elif 1.0 >= value >= 0.9:
        return('5,0')
    else:
        return('Incorrect value!')

x = input('Enter value between 0.0 and 1.0: ')

try:
    value = float(x)

    print(computegrade(value))

except:
    print('Incorrect value!')
