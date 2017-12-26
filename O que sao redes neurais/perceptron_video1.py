# -*- coding: cp1252 -*-
import numpy as np
from random import *

def escolheValoresRandomicos():
    x1 = randint(0,1)
    x2 = randint(0,1)
    x3 = randint(0,1)

    w1 = randint(0, 8)
    w2 = randint(0, 8)
    w3 = randint(0, 8)

    limiar = randint(0, 11)

    return x1, w1, x2, w2, x3, w3, limiar

def perceptron(x1, w1, x2, w2, x3, w3, limiar):

    print(w1, w2, w3)
    print(x1, x2, x3)

    #fator dinheiro
    if(w1 >= 0 and w1 < 3):
        print ("Voc� se importa pouco com dinheiro.")
    elif(w1 >= 3 and w1 < 6):
        print ("Voc� se importa de forma mediana com dinheiro.")
    elif(w1 >= 6 and w1 < 9):
        print ("Voc� se importa muito com dinheiro.")

    #fator parceiro/a
    if(w2 >= 0 and w2 < 3):
        print ("Com ou sem amor voc� n�o liga muito de ir.")
    elif(w2 >= 3 and w2 < 6):
        print ("Voc� se importa um pouco de ir com seu par.")
    elif(w2 >= 6 and w2 < 9):
        print ("Seu amor vai? Isso � importante pra voc�!")   

    #fator dist�ncia
    if(w3 >= 0 and w3 < 3):
        print ("� longe? Se for, desanima.")
    elif(w3 >= 3 and w3 < 6):
        print ("Ok, voc� liga de andar um pouquinho.")
    elif(w3 >= 6 and w3 < 9):
        print ("Vai ser pertinho e isso te motiva muito!")

    print("\n")
    if(x1 == 0):
        print("Fator grana desligado.")
    elif(x1 == 1):
        print("Fator grana ligado.")

    if(x2 == 0):
        print("Fator par rom�ntico desligado.")
    elif(x2 == 1):
        print("Fator par rom�ntico ligado.")

    if(x3 == 0):
        print("Fator dist�ncia desligado.")
    elif(x3 == 1):
        print("Fator dist�ncia ligado.")

    print("\n")
    
    #limiar
    if(limiar >= 0 and limiar < 4):
        print ("Esse limiar est� frouxo.")
    elif(limiar >= 4 and limiar < 8):
        print ("Esse limiar est� mediano.")
    elif(limiar >= 8 and limiar < 12):
        print ("Esse limiar est� meio excessivo, n�o acha?")

    print("\n")
    
    output = w1 * x1 + w2 * x2 + w3 * x3

    return output

def main():
    x1, w1, x2, w2, x3, w3, limiar = escolheValoresRandomicos()
    output = perceptron(x1, w1, x2, w2, x3, w3, limiar)

    if(output >= limiar):
        print("Voc� foi ao show! Parab�ns!")
    else:
        print("Voc� desistiu, lament�vel.") 


if __name__ == "__main__":
    main()
