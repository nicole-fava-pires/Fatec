#Determine se um número par, ímpar, positivo e negativo 
num = int(input(f"Digite um número inteiro: "))

if num > 0:
    if (num % 2 == 0):
        print(f"Esse é um número par e positivo!")
    if (num % 2 != 0):
        print(f"Esse é número ímpar e positivo!")

else:
    if (num % 2 == 0):
        print(f"Esse é um número par e negativo!")
    if (num % 2 != 0):
        print(f"Esse é um númer ímpar e positivo!")

