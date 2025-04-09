num = int(input("Digite um número: "))

x = 0
triangular = 0

while True:
    triangular = (x * (x + 1)) // 2
    
    if triangular == num:
        print("é triangular")
        break
    elif triangular > num:
        print("não é triangular")
        break

    x += 1

    
