b = True

while b:

    a = int(input(': '))
    x = a // 2
    s = 0
    s1 = 0
    x += a % 2

    for i in range(0, x):

        s1 += a - (x + 1)
        s += a - i
    
    print('s:', s, 's1:', s1)
    b = input(': ') == 's'
