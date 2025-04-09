num = int(input("\nDigite um número: "))
x = 1
triangular = 0
list_num_triangulares = []

while True:
    triangular = (x * (x + 1)) // 2
    
    list_num_triangulares += [triangular]

    if triangular == num:
        print("\né triangular")
        break
    elif triangular > num:
        print("\nnão é triangular")
        break

    x += 1

print(f"\n{list_num_triangulares}")

    
