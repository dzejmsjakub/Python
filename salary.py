hour = input('Podaj liczbę godzin: ')

try:
    hours = float(hour)

    per_hour = input('Podaj stawkę godzinową: ')
    per_hours = float(per_hour)


    if hours > 40 :
        salary = 40 * per_hours + (hours - 40) * 1.5 * per_hours
        print('Wynagrodzenie:',round(salary, 2))

    else :
        salary = hours * per_hours
        print('Wynagrodzenie:',round(salary, 2))

except:
    print('Błąd, podaj wartość numeryczną')
