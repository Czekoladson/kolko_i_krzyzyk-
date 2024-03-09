pole = {'top-l':' ','top-m':' ','top-r':' ',        #Kod do poprawy :)
        'mid-l':' ','mid-m':' ','mid-r':' ',
        'low-l':' ','low-m':' ','low-r':' '}

def plansza_do_gier(plansza):
    print(plansza['top-l'] + '|' + plansza['top-m'] + '|' + plansza['top-r']) 
    print('-+-+-')
    print(plansza['mid-l'] + '|' + plansza['mid-m'] + '|' + plansza['mid-r'])
    print('-+-+-')
    print(plansza['low-l'] + '|' + plansza['low-m'] + '|' + plansza['low-r']) 

tura = 'X'
for i in range(9):
    plansza_do_gier(pole)
    print('Ruch gracza: ' + tura + ' w którym polu stawiasz znak?')
    move = input()
    pole[move] = tura
    if tura == 'X':
        tura = 'O'
    else:
        tura = 'X'

plansza_do_gier(pole)


    