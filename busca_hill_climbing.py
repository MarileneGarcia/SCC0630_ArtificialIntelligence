#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Objetivo: Realizar a busca em hill climbing de dados
    Variaveis de entrada: Matriz dos dados
    Variaveis de saida: Lista de tuplas com o caminho do algoritmo """
from termcolor import colored
import os, time
import copy

def busca_hill_climbing(matriz):
    time.sleep(0.5)
    os.system("clear")

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

    '''Começando a Verificar os Tempos dos Caminhos'''
    copia_matriz = copy.deepcopy(matriz)
    aux = secondT1 =0

    seconds = time.time()
    lista, controle = backtrackingCimaDir(copia_matriz, lista, tupla, controle)
    seconds2 = time.time()

    secondT1 = seconds2 - seconds
    aux=secondT1
    listAux = copy.deepcopy(lista)
    lista =[]
    controle = 0
    copia_matriz = copy.deepcopy(matriz)
    seconds = time.time()
    lista, controle = backtrackingBaixoDir(copia_matriz, lista, tupla, controle)
    seconds2 = time.time()
    secondT2 = seconds2 - seconds
    """Verificaçao qual caminho levou menos tempo"""
    secondT1 = seconds2 - seconds
    if (aux > secondT1):
        aux = secondT1
        listAux = copy.deepcopy(lista)
        print(listAux)
    lista = []
    controle = 0
    copia_matriz = copy.deepcopy(matriz)

    seconds = time.time()
    lista, controle = backtrackingCimaEsq(copia_matriz, lista, tupla, controle)
    seconds2 = time.time()

    secondT1 = seconds2 - seconds
    if (aux > secondT1):
        listAux = copy.deepcopy(lista)
        print(listAux)
        aux = secondT1
        print(listAux)    
    lista = []
    controle = 0
    copia_matriz = copy.deepcopy(matriz)

    seconds = time.time()
    lista, controle = backtrackingBaixoEsq(copia_matriz, lista, tupla, controle)
    seconds2 = time.time()
    aux = seconds2 - seconds
    if (aux > secondT1):
       aux = secondT1
       control = 0
       listAux = copy.deepcopy(lista)
       print(listAux)

    return listAux

def imprime_matriz(matriz):
    print("Busca em Hill Climbing: \n")
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
                text = colored("#", "red")
                print(text, end='')
            elif (m == 3):
                text = colored("#", "blue")
                print(text, end='')
        print("")
    time.sleep(0.08)
    os.system("clear")

def backtrackingCimaDir(matriz, lista, tupla, a):
    """ Seguindo a estrategia de controle
    ir para cima, ir para direita, ir para baixo, ir para esquerda"""
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

    # Imprime os nos visitados
    imprime_matriz(matriz)
    print(lista)

    # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
    if (r != 0):
        if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
            tupla = (r - 1, c)
            lista, a = backtrackingCimaDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
    if (c != len(matriz[0]) - 1):
        if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
            tupla = (r, c + 1)
            lista, a = backtrackingCimaDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
    if (r != len(matriz) - 1):
        if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
            tupla = (r + 1, c)
            lista, a = backtrackingCimaDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
    if (c != 0):
        if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
            tupla = (r, c - 1)
            lista, a = backtrackingCimaDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    matriz[r][c] = -1
    return lista, a

def backtrackingBaixoDir(matriz, lista, tupla, a):
    """ Seguindo a estrategia de controle
    ir para baixo, ir para direita, ir para cima, ir para esquerda"""
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

    # Imprime os nos visitados
    imprime_matriz(matriz)
    print(lista)

    # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
    if (r != len(matriz) - 1):
        if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
            tupla = (r + 1, c)
            lista, a = backtrackingBaixoDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a


    # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
    if (c != len(matriz[0]) - 1):
        if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
            tupla = (r, c + 1)
            lista, a = backtrackingBaixoDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a
    # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
    if (r != 0):
        if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
            tupla = (r - 1, c)
            lista, a = backtrackingBaixoDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
    if (c != 0):
        if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
            tupla = (r, c - 1)
            lista, a = backtrackingBaixoDir(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    matriz[r][c] = -1
    return lista, a

def backtrackingCimaEsq(matriz, lista, tupla, a):
    """ Seguindo a estrategia de controle
    ir para cima, ir para esquerda, ir para cima, ir para baixo"""
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

    # Imprime os nos visitados
    imprime_matriz(matriz) 
    print(lista)

    # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
    if (r != 0):
        if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
            tupla = (r - 1, c)
            lista, a = backtrackingCimaEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
    if (c != 0):
        if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
            tupla = (r, c - 1)
            lista, a = backtrackingCimaEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
    if (r != len(matriz) - 1):
        if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
            tupla = (r + 1, c)
            lista, a = backtrackingCimaEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
    if (c != len(matriz[0]) - 1):
        if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
            tupla = (r, c + 1)
            lista, a = backtrackingCimaEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a



    matriz[r][c] = -1
    return lista, a

def backtrackingBaixoEsq(matriz, lista, tupla, a):
    """ Seguindo a estrategia de controle
    ir para baixo, ir para esquerda, ir para cima, ir para baixo"""
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

    # Imprime os nos visitados
    imprime_matriz(matriz)
    print(lista)

    # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
    if (r != len(matriz) - 1):
        if (matriz[r + 1][c] != 8 and matriz[r + 1][c] != 1 and matriz[r + 1][c] != -1):
            tupla = (r + 1, c)
            lista, a = backtrackingBaixoEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
    if (c != 0):
        if (matriz[r][c - 1] != 8 and matriz[r][c - 1] != 1 and matriz[r][c - 1] != -1):
            tupla = (r, c - 1)
            lista, a = backtrackingBaixoEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
    if (r != 0):
        if (matriz[r - 1][c] != 8 and matriz[r - 1][c] != 1 and matriz[r - 1][c] != -1):
            tupla = (r - 1, c)
            lista, a = backtrackingBaixoEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a
    # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
    if (c != len(matriz[0]) - 1):
        if (matriz[r][c + 1] != 8 and matriz[r][c + 1] != 1 and matriz[r][c + 1] != -1):
            tupla = (r, c + 1)
            lista, a = backtrackingBaixoEsq(matriz, lista, tupla, a)
            if (a == -1):
                return lista, a

    matriz[r][c] = -1
    return lista, a