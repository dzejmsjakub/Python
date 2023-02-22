x = input('Podaj ilosc punktow od 0 do 100: ')

try:
    x1 = float(x)

    if 50 > x1 >= 0  :
        print('2,0')

    elif 60 > x1 >= 50 :
        print('3,0')

    elif 70 > x1 >= 60 :
        print('3,5')

    elif 80 > x1 >= 70 :
        print('4,0')

    elif 90 > x1 >= 80 :
        print('4,5')

    elif 100 >= x1 >= 90 :
        print('5,0')

    else :
        print('Niepoprawna wartosc')

except:
    print('Niepoprawna wartosc')
