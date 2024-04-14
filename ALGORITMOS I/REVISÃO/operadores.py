#Repetição
media = 0
num = 0
soma_num = 0

for i in range (1,6):
    num = int(input(f'Digite a idade: '))
    if num <= 0 or num > 100:
        print(f'Digite um número válido!')
        
    else:
        soma_num = soma_num + num

media = soma_num / 5
print(f'A média das das idades é: {media}')

