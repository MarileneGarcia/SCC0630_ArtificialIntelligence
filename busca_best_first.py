#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Objetivo: Realizar a busca em Best-First Search na matriz de dados
    Variaveis de entrada: Matriz dos dados
    Variaveis de saida: Lista de tuplas com o caminho do algoritmo """
from termcolor import colored
import os, time

pos_lin = 0
pos_col = 0

def busca_best_first(matriz):
    global pos_lin 
    global pos_col

    flag_r = 0
    flag_c = 0
    elem_inicial = 0
    controle = 0

    """ Descobrindo a posicao inicial """
    for i in matriz:
        for j in i:
            if (j == 2):
                pos_lin = flag_r
                pos_col = flag_c
            flag_c += 1
        flag_c = 0
        flag_r += 1
    lista = []
    tupla = (pos_lin, pos_col)

    time.sleep(0.5)
    os.system("clear")
    
    imprime_matriz(matriz)
    # Faz o controle do valor para o metodo de busca Best-First Search
    print("Digite 1 se o valor esta pra cima e direita")
    print("Digite 2 se o valor esta pra cima e esquerda")
    print("Digite 3 se o valor esta pra baixo e direita")
    print("Digite 4 se o valor esta pra baixo e esquerda")
    controle2 = int(input(""))
    os.system("clear")
    
    lista, controle = backtracking(matriz, lista, tupla, controle,controle2)
    return lista

def imprime_matriz(matriz):
    # Imprime os nos visitados
    print("Busca em Best First Search: \n")
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

def backtracking(matriz, lista, tupla, a,controle2):

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

    #Verifica a opçao escolhida para otimizar a busca (heuristica)

    if (controle2 == 1) :
        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (r != 0):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a,controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a,controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (r != len(matriz) - 1):
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

    elif (controle2 == 2):
        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (r != 0):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                tupla = (r, c - 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (r != len(matriz) - 1):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                tupla = (r + 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

    elif (controle2 == 3):
        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (r != len(matriz) - 1):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                tupla = (r + 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (r != 0):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                tupla = (r, c - 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

    elif (controle2 == 4):
        # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
        if (r != len(matriz) - 1):
            if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
                tupla = (r + 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
        if (c != 0):
            if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
                tupla = (r, c - 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
        # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
        if (r != 0):
            if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
                tupla = (r - 1, c)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a

        # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
        if (c != len(matriz[0]) - 1):
            if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
                tupla = (r, c + 1)
                lista, a = backtracking(matriz, lista, tupla, a, controle2)
                if (a == -1):
                    return lista, a
    matriz[r][c] = -1
    return lista, a