while True:
    
    hour = input('Podaj liczbę godzin: ')
    
    try:
        hours = float(hour)
    
    except:
        print('Błąd, podaj wartość numeryczną.')
        continue

    while True:
        
        per_hour = input('Podaj stawkę godzinową: ')

        try:
            per_hours = float(per_hour)
    
        except:
            print('Błąd, podaj wartość numeryczną.')
            continue    

        if hours > 40 :
            salary = 40 * per_hours + (hours - 40) * 1.5 * per_hours
            print('Wynagrodzenie:',round(salary, 2))
            break
        else :
            salary = hours * per_hours
            print('Wynagrodzenie:',round(salary, 2))
            break