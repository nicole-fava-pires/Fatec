x = int(input(f'Digite um número inteiro e positivo: '))
i = 0
impar = []

while i < 7:
    impar = True
    if (x % 2 == 0):
        impar = False
        i = i - 1
    else:
       if impar == True:
            print(x)
    x = x + 1
    i = i + 1
