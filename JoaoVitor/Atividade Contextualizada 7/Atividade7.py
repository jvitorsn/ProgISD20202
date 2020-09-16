import time

#Dicionario no padrao RGB (red, green, blue) para resolucao de 8 bits por cor
cores = {
    "vermelho": (255, 0, 0), 
    "laranja": (255, 128, 0), 
    "amarelo": (255, 255, 0), 
    "verde": (0, 255, 0), 
    "turquesa": (0, 255, 255), 
    "azul": (0, 0, 255), 
    "branco": (255, 255, 255), 
    "off": (0, 0, 0)}

def setLed(numero_de_leds): #funcao para definir a cor dos leds individualmente
    led = []

    print ('Qual cor deseja para o led ' + str(numero_de_leds+1) + '? Digite qualquer outro valor para inserir parametros RGB de 8 bits especificos.')
    print (cores.keys())
    cor = input('insira a opcao desejada: ')
    cor = cor.lower() #CASE INSENSITIVE

    if (cor in cores):
        led.append(cores[cor])

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

        led.append([r, g, b, False])

    return led


def setDispositivo(): #set de todos os canais de uma mesma sessao
    qtos = int(input('Quantos dispositivos deseja? Numeros negativos serao considerados 0, e abortam a operacao.'))
    if (qtos < 0): qtos = 0

    dispositivo = []

    for i in range(qtos):
        dispositivo.append(setLed(i))

    return dispositivo


def threadFunc():
   for i in range(5):
       print('Hello from new Thread ')
       time.sleep(1)

lista = setDispositivo()
print(lista)

#threadFunc()