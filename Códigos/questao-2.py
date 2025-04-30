n = int(input("Digite uma quantidade de números: "))

x = 1

num = int(input("Digite um número: "))

a = num
b = num
s = num

while x < n:

    num = int(input("Digite um número: "))
    s += num

    if num < a:
        a = num
    elif num > b:
        b = num
    
    x += 1
    print(s / x)

print("Valor de a: ", a, "Valor de b: ", b)