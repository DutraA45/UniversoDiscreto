# -*- coding: cp1252 -*-
import numpy as np
from random import *

def escolheValoresRandomicos():

    x1 = randint(0, 1) #fator dinheiro
    x2 = randint(0, 1) #fator amigos/namorado(a)
    x3 = randint(0, 1) #fator dist�ncia

    #quanto maior o valor, mais se motiva a ir com $$$
    w1 = randint(0, 8)
    #quanto maior o valor, mais se motiva a ir com amigos
    w2 = randint(0, 8)
    #quanto maior o valor, mais se motiva a ir se for perto
    w3 = randint(0, 8)

    #quanto maior o valor, mais r�gido � pra ir ao show
    limiar = randint(0, 11)

    return x1, w1, x2, w2, x3, w3, limiar

def perceptron(x1, w1, x2, w2, x3, w3, limiar):

    #fator dinheiro
    if(w1 >= 0 and w1 < 3): #se cair aqui, significa que o f� n�o se motiva a ir pelo dinheiro
        print("Voc� n�o se motiva com dinheiro pra ir ao show da Anitta")
    elif(w1 >= 3 and w1 < 6):
        print("Voc� se motiva um pouco com $$$ pra ir no show da Anitta")
    elif(w1 >= 6 and w1 < 9):
        print("Voc� se motiva f�cil a ir ao show se tiver dinheiro!")

    #fator amigos
    if(w2 >= 0 and w2 < 3):
        print("Nem seus amigos conseguem te empurrar pra ver o show")
    elif(w2 >= 3 and w2 < 6):
        print("Seus amigos empurram um pouquinho, vai, pra ver a Anitta")
    elif(w2 >= 6 and w2 < 9):
        print("Com os seus amigos topando, � alta a probabilidade de voc� ir ao show")

    #fator distancia
    if(w3 >= 0 and w3 < 3):
        print("Seja longo ou perto, a dist�ncia pouco te motiva")
    elif(w3 >= 3 and w3 < 6):
        print("Se o show for perto, isso te d� um empurr�ozinho pra ir ao show")
    elif(w3 >= 6 and w3 < 9):
        print("� perto e isso te d� um empurr�oz�o pra ir ao show da Anitta")

    print("\n")

    #imprimindo as vari�veis x
    if(x1 == 0):
        print("Fator dinheiro est� desligado")
    elif(x1 == 1):
        print("Fator dinheiro est� ligado")
        
    if(x2 == 0):
        print("Fator amigos est� desligado")
    elif(x2 == 1):
        print("Fator amigos est� ligado")

    if(x3 == 0):
        print("Fator dist�ncia est� desligado")
    elif(x3 == 1):
        print("Fator dist�ncia est� ligado")

    print("\n")
    
    #imprimindo o limiar
    if(limiar >= 0 and limiar < 4):
        print("O limiar escolhido est� frouxo")
    elif(limiar >= 4 and limiar < 8):
        print("O limiar escolhido est� flex�vel")
    elif(limiar >= 8 and limiar < 12):
        print("O limiar escolhido est� rigoroso")

    output = w1 * x1 + w2 * x2 + w3 * x3

    return output


def main():
    x1, w1, x2, w2, x3, w3, limiar = escolheValoresRandomicos()
    output = perceptron(x1, w1, x2, w2, x3, w3, limiar)

    if(output >= limiar):
        print("Matheus vai ao show da Anitta! =)")
    else:
        print("Matheus desistiu de ir na Anitta! =(")

if __name__ == "__main__":
    main()
