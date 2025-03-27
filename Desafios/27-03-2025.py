
c = 1
s = 0
c1 = 0
c2 = 0

while c <= 20:

    if c % 3 == 0: # Contar os múltiplos de 3
        s += c
        c1 += 1

    elif c % 2 == 0: # Contar os múltiplos de 2
        c2 += 1
    
    c += 1

print(s, c1, c2)