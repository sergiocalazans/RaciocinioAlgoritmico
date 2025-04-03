x = int(input('Entrada '))

cont = 0
w = 0

while cont < x:

    y = int(input('Entrada '))
    w = 1
    a = 0

    while w <= y:

        a += w
        w += 1
    
    print(y, a)
    cont += 1