#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Objetivo: Realizar a busca em largura na matriz de dados 
    Variaveis de entrada: Matriz dos dados
    Variaveis de saida: Lista de tuplas com o caminho do algoritmo """
from termcolor import colored
import os,time

def busca_largura(matriz):
  time.sleep(0.5)
  os.system("clear")

  flag_r = 0
  flag_c = 0 
  elem_inicial = 0
  controle = 0

  """ Descobrindo a posicao inicial """
  for i in matriz:
    for j in i :
      if (j == 2):
        pos_lin = flag_r
        pos_col = flag_c
      flag_c += 1
    flag_c = 0
    flag_r += 1
  lista = []
  tupla = (pos_lin, pos_col)
  
  """ Seguindo a estrategia de controle 
  ir para cima, ir para direita, ir para esquerda, ir para baixo"""
  r = tupla[0]
  c = tupla[1]
  tupla = (r,c)
  lista.append(tupla)
  matriz[r][c] = 8

  for m in lista :
    # Marca atual posicao como visitada
    r = m[0]
    c = m[1]
    flag = 0
    
    # Verifica se a posicao de cima ja foi visitada, se não foi vai ser adicionado a lista
    if (r != 0):
      if(matriz [r - 1] [c] != 8 and matriz [r - 1] [c] != 1 and matriz [r - 1] [c] != -1):
        tupla = (r-1 , c)
        lista.append(tupla)

        if(matriz[r - 1][c] == 3):
          return lista
          
        matriz[r - 1][c] = 8
        flag += 1

    # Verifica se a posicao da direita ja foi visitada, se não foi vai ser adicionado a lista
    if (c != len(matriz[0])-1):
      if(matriz [r] [c + 1] != 8 and matriz [r] [c + 1] != 1 and matriz [r] [c + 1] != -1):
        tupla = (r , c+1)
        lista.append(tupla)

        if(matriz[r][c + 1] == 3):
          return lista

        matriz[r][c + 1] = 8
        flag += 1


    # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
    if (c != 0 ):
      if(matriz [r] [c - 1] != 8 and matriz [r] [c - 1] != 1 and matriz [r] [c - 1] != -1):
        tupla = (r , c-1)
        lista.append(tupla)

        if(matriz[r][c - 1] == 3):
          return lista

        matriz[r][c - 1] = 8
        flag += 1
    
    # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
    if (r != len(matriz)-1 ):
      if(matriz [r + 1] [c] != 8 and matriz [r + 1] [c] != 1 and matriz [r + 1] [c] != -1):
        tupla = (r+ 1 , c)
        lista.append(tupla)

        if(matriz[r + 1][c] == 3):
          return lista

        matriz[r + 1][c] = 8
        flag += 1

    if(flag == 0):
      matriz[r][c] = -1

    # Imprime os nos visitados
    print("Busca em largura: \n")
    for n in matriz:
      for m in n:
        if(m == 8):
          text = colored("#", "yellow")
          print (text, end = '')
        elif(m == -1):
          text = colored("#", "magenta")
          print (text, end = '')
        elif(m == 0):
          text = colored("#", "white")
          print (text, end = '')
        elif(m == 1):
          text = colored("#", "grey")
          print (text, end = '')
        elif(m == 2):
          text = colored("#", "red")
          print (text, end = '')
        elif(m == 3):
          text = colored("#", "blue")
          print (text, end = '')
      print("")
    time.sleep(0.1)
    os.system("clear")

  return lista