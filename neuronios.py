class Neuronio:
    def __init__(self,func,*n,msg=False):
        self.funcao = func #neurônio recebe a função atribuída  ele
        self.polarizacao(n,msg) #processa as entradas no neurônio e chama a função para calcular a saída (output)
        print(f'Neurônio criado. Saída {self.output}') if msg else ""

    def polarizacao(self, v,msg=False):
        media = soma(v) / len(v)
        self.output = self.funcao(media)
        print(f'Neurônio polarizado. Saída {self.output}') if msg else ""


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

def soma(n):
    s = 0
    for i in n:
        s += i
    return s


