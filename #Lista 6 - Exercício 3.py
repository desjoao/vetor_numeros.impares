impares = [0]*10
num = 0
qnt = 0

while qnt<10:
    num = int(input('Insira um número inteiro: '))
    if num%2!=0:
        qnt+=1
        for i in range(qnt-1, qnt):
            impares[i] = num
            

print(f'Os números informados que são ímpares são {impares}')
