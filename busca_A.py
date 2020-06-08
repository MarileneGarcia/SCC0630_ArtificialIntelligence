#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Objetivo: Realizar a busca em Best-First Search na matriz de dados
    Variaveis de entrada: Matriz dos dados
    Variaveis de saida: Lista de tuplas com o caminho do algoritmo """
from termcolor import colored
import os, time

pos_lin = 0
pos_col = 0
fin_lin = 0
fin_col = 0
f5 = 0

def busca_A(matriz):
    global pos_lin 
    global pos_col
    global fin_lin 
    global fin_col
    global f5

    f5 = 0
    flag_r = 0
    flag_c = 0
    elem_inicial = 0
    controle = 0

    """ Descobrindo a posicao inicial e final"""
    for i in matriz:
        for j in i:

            if (j == 2):
                pos_lin = flag_r
                pos_col = flag_c

            if (j == 3):
                fin_lin = flag_r
                fin_col = flag_c
            flag_c += 1
        flag_c = 0
        flag_r += 1
    lista = []
    tupla = (pos_lin, pos_col)

    time.sleep(0.5)
    os.system("clear")
    
    imprime_matriz(matriz)
    # Definindo a heurística
    print("Digite 1 se o valor esta pra cima e direita")
    print("Digite 2 se o valor esta pra cima e esquerda")
    print("Digite 3 se o valor esta pra baixo e direita")
    print("Digite 4 se o valor esta pra baixo e esquerda")
    controle2 = int(input(""))
    os.system("clear")

    lista, controle = backtracking(matriz, lista, tupla, controle,controle2)
    return lista

def imprime_matriz(matriz):
    global f5
    # Imprime os nos visitados
    print("Custo do caminho: \n", f5) 
    print("Busca em A*: \n")
    matriz[pos_lin][pos_col] = 2
    for n in matriz:
        for m in n:
            if (m == 8):
                text = colored("#", "yellow")
                print(text, end='')
            elif (m == -1):
                text = colored("#", "magenta")
                print(text, end='')
            elif (m == 0):
                text = colored("#", "white")
                print(text, end='')
            elif (m == 1):
                text = colored("#", "grey")
                print(text, end='')
            elif (m == 2):
                text = colored("#", "blue")
                print(text, end='')
            elif (m == 3):
                text = colored("#", "red")
                print(text, end='')
        print("")


def backtracking(matriz, lista, tupla, a, controle2):
    global f5

    r = tupla[0]
    c = tupla[1]
    tupla = (r, c)
    lista.append(tupla)

    # Verifica se e a posicao desejada
    if (a == -1):
        return lista, a

    if (matriz[r][c] == 3):
        a = -1
        return lista, a
    

    # Marca atual posicao como visitada
    matriz[r][c] = 8

    imprime_matriz(matriz)
    time.sleep(0.1)
    os.system("clear")

    ####################### Opcao 1 ###########################
    # Verifica se e a posicao desejada
    while controle2 == 1 :
        # Heuristica e controle do caminho
        h1, h2, h3, h4 = 10000, 10000, 10000, 10000
        g1, g2, g3, g4 = 10000, 10000, 10000, 10000
        f1, f2, f3, f4 = 10000, 10000, 10000, 10000
        menor = 0

        # Verifica a heuristica e analisa o caminho
        if (r != 0):            
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                h1 = 1
                g1 = abs((r - 1) - fin_lin) + abs((c) - fin_col)
                f1 = h1 + g1

        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                h2 = 1
                g2 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f2 = h2 + g2

        if (r != len(matriz) - 1):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                h3 = 2
                g3 = abs((r + 1) - fin_lin) + abs((c) - fin_col)
                f3 = h3 + g3

        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                h4 = 2
                g4 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f4 = h4 + g4
        

        # Decide o menor custo 
        menor = f1
        if (f2 < menor):
            menor = f2
        if (f3 < menor):
            menor = f3
        if (f4 < menor):
            menor = f4

        #Custo total
        if(menor != 10000):
            f5 = f5 + menor
        
        else:
            matriz[r][c] = -1
            return lista, a

        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f1):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f2):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a,controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f3):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):         
                tupla = (r + 1, c)
                lista, a = backtracking(matriz, lista, tupla, a,controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                tupla = (r, c - 1)
                lista, a = backtracking(matriz, lista, tupla, a,controle2)
                if (a == -1):
                    return lista, a
  
    ####################### Opcao 2 ###########################
    while controle2 == 2:
        # Heuristica e controle do caminho
        h1, h2, h3, h4 = 10000, 10000, 10000, 10000
        g1, g2, g3, g4 = 10000, 10000, 10000, 10000
        f1, f2, f3, f4 = 10000, 10000, 10000, 10000
        menor = 0

        # Verifica a heuristica e analisa o caminho
        if (r != 0):            
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                h1 = 1
                g1 = abs((r - 1) - fin_lin) + abs((c) - fin_col)
                f1 = h1 + g1

        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                h2 = 2
                g2 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f2 = h2 + g2

        if (r != len(matriz) - 1):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                h3 = 2
                g3 = abs((r + 1) - fin_lin) + abs((c) - fin_col)
                f3 = h3 + g3

        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                h4 = 1
                g4 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f4 = h4 + g4
        
        # Decide o menor custo 
        menor = f1
        if (f2 < menor):
            menor = f2
        if (f3 < menor):
            menor = f3
        if (f4 < menor):
            menor = f4

        #Custo total
        if(menor != 10000):
            f5 = f5 + menor
        else:
            matriz[r][c] = -1
            return lista, a

        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f1):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f4):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                tupla = (r, c - 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f3):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                tupla = (r + 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f2):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a


    ####################### Opcao 3 ###########################
    while controle2 == 3:
        # Heuristica e controle do caminho
        h1, h2, h3, h4 = 10000, 10000, 10000, 10000
        g1, g2, g3, g4 = 10000, 10000, 10000, 10000
        f1, f2, f3, f4 = 10000, 10000, 10000, 10000
        menor = 0

        # Verifica a heuristica e analisa o caminho
        if (r != 0):            
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                h1 = 2
                g1 = abs((r - 1) - fin_lin) + abs((c) - fin_col)
                f1 = h1 + g1

        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                h2 = 1
                g2 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f2 = h2 + g2

        if (r != len(matriz) - 1):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                h3 = 1
                g3 = abs((r + 1) - fin_lin) + abs((c) - fin_col)
                f3 = h3 + g3

        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                h4 = 2
                g4 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f4 = h4 + g4
        

        # Decide o menor custo 
        menor = f1
        if (f2 < menor):
            menor = f2
        if (f3 < menor):
            menor = f3
        if (f4 < menor):
            menor = f4

        #Custo total
        if(menor != 10000):
            f5 = f5 + menor
        else:
            matriz[r][c] = -1
            return lista, a

        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f3):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                tupla = (r + 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f2):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f1):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f4):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                tupla = (r, c - 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a




    ####################### Opcao 4 ###########################
    while controle2 == 4:

         # Heuristica e controle do caminho
        h1, h2, h3, h4 = 10000, 10000, 10000, 10000
        g1, g2, g3, g4 = 10000, 10000, 10000, 10000
        f1, f2, f3, f4 = 10000, 10000, 10000, 10000
        menor = 0

        # Verifica a heuristica e analisa o caminho
        if (r != 0):            
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                h1 = 2
                g1 = abs((r - 1) - fin_lin) + abs((c) - fin_col)
                f1 = h1 + g1

        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                h2 = 2
                g2 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f2 = h2 + g2

        if (r != len(matriz) - 1):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                h3 = 1
                g3 = abs((r + 1) - fin_lin) + abs((c) - fin_col)
                f3 = h3 + g3

        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                h4 = 1
                g4 = abs((r) - fin_lin) + abs((c + 1) - fin_col)
                f4 = h4 + g4
    
        # Decide o menor custo 
        menor = f1
        if (f2 < menor):
            menor = f2
        if (f3 < menor):
            menor = f3
        if (f4 < menor):
            menor = f4

        #Custo total
        if(menor != 10000):
            f5 = f5 + menor
        else:
            matriz[r][c] = -1
            return lista, a

        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f3):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                tupla = (r + 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f4):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                tupla = (r, c - 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f1):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (menor == f2):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

    matriz[r][c] = -1
    return lista, a