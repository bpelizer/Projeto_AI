print('-='*30 + 'Início do Programa' + '-='*30)
from random import randrange, random, randint
from neuronios import *
from datetime import datetime

camadas = [6,3,5,9]
entradas = 7
pesos = [] #pesos[i,j,k] => i: camada; j: linha; k: coluna
bias = [] #ainda não utilizado

inicio = datetime.now()
#Criação de tabelas
for i in range(0,len(camadas)):
    a =[]
    if i ==0:
        col = entradas
    else:
        col = camadas[i-1]
    for j in range(0,camadas[i]):
        linha = []
        for k in range(0,col):
            linha.append(random())
        a.append(linha)
        del linha
    pesos.append(a)
    del a

#impressão da pesos de pesos
for i in range(0, len(pesos)):
    print(f'Tabela {i}')
    for j in range(0, len(pesos[i])):
        for k in range(0, len(pesos[i][j])):
            print(f'{pesos[i][j][k]:,.3f}', end=' ')
        print("\n",end='')
    print('-='*30)


#Criação das camadas de neurônios

neuron =[]
for i in range(0,len(camadas)):
    a =[]
    for j in range(0,camadas[i]):
        a.append(Neuronio(s,random(),msg=True))
    neuron.append(a)
    del a

#criação de entrada simulada
dados=[]
for i in range(0,entradas):
    dados.append(random())

print(f'Os dados são: {dados}')

#Processamento - Parte Principal

for i in range(0,len(camadas)): #transição entre camadas
    if i == 0:
        col = entradas
    else:
        col = camadas[i-1]
    for j in range(0,camadas[i]): #número de neurônios na camada e número de colunas na linha
        x = []
        for k in range(0,col):
            if i ==0:
                x.append(dados[k] * pesos[i][j][k])
            else:
                x.append(neuron[i-1][k].output * pesos[i][j][k])
        neuron[i][j].polarizacao(x,msg=True)
        del x
fim = datetime.now()
print(f'O processamento levou {fim - inicio} segundos.')
print('Programa Finalizado')


