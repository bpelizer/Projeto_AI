print('-='*30 + 'Program Beginning' + '-='*30)
from random import randrange, random, randint
from neuronios import *
from datetime import datetime
import hashlib

camadas = [256*8,256*8,256*8,256*8,256*8,256*8,256*8,256*8,256*8,256]
entradas = 256*8
pesos = [] #pesos[i,j,k] => weights: i: layer; j: line; k: column
bias = [] #unused yet
msg = False #choose whether messages are shown or not

inicio = datetime.now()
print(f'Start: {inicio}')
#Tables Creation
print(f'Starting tables creation...')
for i in range(0,len(camadas)):
    a =[]
    if i ==0:
        col = entradas
    else:
        col = camadas[i-1]
    for j in range(0,camadas[i]):
        linha = []
        for k in range(0,col):
            linha.append(random()*randrange(-1,2,2))
        a.append(linha)
        del linha
    pesos.append(a)
    del a
print(f'Tables created.')
#Print Weights
if msg:
    for i in range(0, len(pesos)):
        print(f'Tabela {i}')
        for j in range(0, len(pesos[i])):
            for k in range(0, len(pesos[i][j])):
                print(f'{pesos[i][j][k]:,.3f}', end=' ')
            print("\n",end='')
        print('-='*30)

#Creation of neuron layers
print('Neurons creation...')
neuron =[]
for i in range(0,len(camadas)):
    a =[]
    for j in range(0,camadas[i]):
        a.append(Neuronio(s,random(),msg))
    neuron.append(a)
    del a
print('Neurons created')
#Entered data simulation
dados=[]
for i in range(0,entradas):
    dados.append(random()*randrange(-1,2,2))
print(f'Data: {dados}') if msg else ""

#Processamento - Parte Principal
print('Starting main data processing...')
for i in range(0,len(camadas)): #transition between layers
    if i == 0: #columns in first layer match data lenght
        col = entradas
    else:
        col = camadas[i-1] #number of columns in other layers are the same as number of neurons in preceding layer
    for j in range(0,camadas[i]): #j: number of neurons and columns in the layer
        x = []
        for k in range(0,col):
            if i ==0:
                x.append(dados[k] * pesos[i][j][k]) #first layer neurons will be polarized with weighted entry data
            else:
                x.append(neuron[i-1][k].output * pesos[i][j][k]) #from the second layer on neurons will be polarized with weigght ouputs of preceding layer neurons
        neuron[i][j].polarizacao(x,msg)
        del x
    print(f'Layer {i} processed.')
x =''
for i in neuron[-1]:
    if i.output <=0:
        x+= '0'
    else:
        x += '1'
print(f'Last layer output: {x}')
print(f'Last layer sha256: {hashlib.sha256(x.encode()).hexdigest()}')


fim = datetime.now()
print('Processing ended.')
print(f'Finish: {inicio}')
print(f'Processing time: {fim - inicio} seconds.')
print('-='*30+'End'+'-='*30)

