import random
import csv

cores = {
    "vermelho": [(255, 0, 0), False],
    "laranja": [(255, 128, 0), False], 
    "amarelo": [(255, 255, 0), False], 
    "verde": [(0, 255, 0), False],
    "turquesa": [(0, 255, 255), False],
    "azul": [(0, 0, 255), False],
    "branco": [(255, 255, 255), False]}

class matrizEletrodos:
        #classe para definicao da matriz das sessoes, foi feito dessa forma para permitir mais de uma matriz caso as sessoes sejam em interface cerebro cerebro

    def __init__(self):
        self.eeg = []
        
    def aquisicao(self):
        buf = [] #armazena as leituras de cada scan para compor uma linha nova no log

        for i in range(32):
            buf.append(random.random()) #gera valores de amplitude entre 0 e 1      

        self.eeg.append(buf) #resolucao da afericao de 7 bits
        
    def gerarLog(self):

        with open (str(self) )
        print(str(self.eeg))


class setDispositivos:
    #classe para a criacao dos leds

    def __init__(self, quantidade):
        self.qtos = quantidade
        self.leds = []


    def setLed(self, numero_de_leds): #funcao para definir a cor dos leds individualmente
        led = [] #A estrutura de dados segue o padrao de lista com (R, G, B, on/off em booleana)

        print ('Qual cor deseja para o led do dispositivo ' + str(numero_de_leds+1) + '? Digite qualquer outro valor para inserir parametros RGB de 8 bits especificos.')
        print (cores.keys())
        cor = input('insira a opcao desejada: ')
        cor = cor.lower() #CASE INSENSITIVE

        if (cor in cores):
                led = cores[cor]

        else:
                r = int(input('Insira um valor de 0 a 255 para o parametro R (valores acima de 255 e abaixo de 0, serao considerados 255 e 0, respectivamente): '))
                if (r > 255): r = 255
                elif (r < 0): r = 0
                
                g = int(input('Insira um valor de 0 a 255 para o parametro G (valores acima de 255 e abaixo de 0, serao considerados 255 e 0, respectivamente): '))
                if (g > 255): g = 255
                elif (g < 0): g = 0
                
                b = int(input('Insira um valor de 0 a 255 para o parametro B (valores acima de 255 e abaixo de 0, serao considerados 255 e 0, respectivamente): '))
                if (b > 255): b = 255
                elif (b < 0): b = 0

                led = [(r, g, b), False]
        
        return led


    def setDispositivo(self): #set de todos os canais de uma mesma sessao
        if (self.qtos < 0): self.qtos = 0
        
        for i in range(qtos):
                self.leds.append(setDispositivos.setLed(self, i))

        return self.leds

    def __str__(self):
        return str(self.leds)

#qtos = int(input('Quantos dispositivos deseja? Numeros negativos serao considerados 0, e abortam a operacao.'))
#a = setDispositivos(qtos)
#a.setDispositivo()

matriz1 = matrizEletrodos()

matriz1.aquisicao()
matriz1.aquisicao()

print(str(len(matriz1.eeg[1])) + '\n')
print(matriz1.eeg[1])

#print (a)

