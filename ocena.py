x = input('Podaj wartosc pomiedzy 0.0 a 1.0: ')

try:
    x1 = float(x)

    if 0.5 > x1 >= 0.0  :
        print('2,0')

    elif 0.6 > x1 >= 0.5 :
        print('3,0')

    elif 0.7 > x1 >= 0.6 :
        print('3,5')

    elif 0.8 > x1 >= 0.7 :
        print('4,0')

    elif 0.9 > x1 >= 0.8 :
        print('4,5')

    elif 1.0 >= x1 >= 0.9 :
        print('5,0')

    else :
        print('Niepoprawna wartosc')

except:
    print('Niepoprawna wartosc')
