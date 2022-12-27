class Neuronio:
    def __init__(self,func,*n):
        soma = 0
        for i in n:
            soma += i
        self.output = soma/len(n)
        print(f'Neurônio criado. Saída {self.output}')

    def polarizacao(self,*n):
        soma = 0
        for i in n:
            soma += i
        self.output = soma / len(n)


def zeroum(n=0):
    if n != 0:
        return 1
    else:
        return 0

def s(n=0):
    if n < -1:
        return -1
    elif n > 1:
        return 1
    else:
        return n


a = Neuronio(s,0.8)

a.polarizacao(0.8,0.6,1,-0.3)
y = a.output

print(f'Neurônio polarizado {y}')