from random import randrange, random, randint
camadas = [5,3,7]
entradas = 2
tabela = [] #tabela[i,j,k] => i: camada; j: linha; k: coluna
b = []

#Criação de tabelas
for i in range(0,len(camadas)):
    a =[]
    for j in range(0,camadas[i]):
        linha = []
        for k in range(0,entradas):
            linha.append(random())
        a.append(linha)
        del linha
    tabela.append(a)
    del a

print(tabela)

for i in range(0,len(tabela)):
    print(f'Tabela {i}')
    for j in range(0,len(tabela[i])):
        for k in range(0,len(tabela[i][j])):
            print(f'{tabela[i][j][k]:,.3f}',end=' ')
        print("\n",end='')
    print('-='*30)


