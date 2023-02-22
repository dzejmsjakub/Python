def computegrade(value):
    if 50 > value >= 0 :
        return('2,0')
    elif 60 > value >= 50 :
        return('3,0')
    elif 70 > value >= 60 :
        return('3,5')
    elif 80 > value >= 70 :
        return('4,0')
    elif 90 > value >= 80 :
        return('4,5')
    elif 100 >= value >= 90:
        return('5,0')
    else:
        return('Incorrect value!')

x = input('Enter the number of points between 0 and 100: ')

try:
    value = float(x)

    print(computegrade(value))

except:
    print('Incorrect value!')
