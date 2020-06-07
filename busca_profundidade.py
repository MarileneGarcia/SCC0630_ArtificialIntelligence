#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Objetivo: Realizar a busca em profundiade na matriz de dados 
    Variaveis de entrada: Matriz dos dados
    Variaveis de saida: Lista de tuplas com o caminho do algoritmo """
from termcolor import colored
import os,time

pos_lin = 0
pos_col = 0

def busca_profundidade(matriz):
  global pos_lin 
  global pos_col

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
  lista, controle = backtracking(matriz,lista,tupla,controle) 
  return lista

def backtracking(matriz, lista, tupla, a):
  """ Seguindo a estrategia de controle 
  ir para cima, ir para direita, ir para esquerda, ir para baixo"""
  r = tupla[0]
  c = tupla[1]
  tupla = (r,c)
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
  print("Busca em profundidade: \n")
  matriz[pos_lin][pos_col] = 2
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
        text = colored("#", "blue")
        print (text, end = '')
      elif(m == 3):
        text = colored("#", "red")
        print (text, end = '')
    print("")
    matriz[pos_lin][pos_col] = 2
  time.sleep(0.3)
  os.system("clear")
  
  # Verifica se a posicao de cima ja foi visitado, se não foi vai ser adicionado a lista
  if (r != 0):
    if(matriz [r - 1] [c] != 8 and matriz [r - 1] [c] != 1 and matriz [r - 1] [c] != -1):
      tupla = (r-1 , c)
      lista,a = backtracking(matriz,lista,tupla,a)
      if (a == -1):
        return lista, a


  # Verifica se a posicao da direita ja foi visitado, se não foi vai ser adicionado a lista
  if (c != len(matriz[0])-1):
    if(matriz [r] [c + 1] != 8 and matriz [r] [c + 1] != 1 and matriz [r] [c + 1] != -1):
      tupla = (r , c+1)
      lista,a = backtracking(matriz,lista,tupla,a)
      if (a == -1):
        return lista, a


  # Verifica se a posicao da esquerda ja foi visitado, se não foi vai ser adicionado a lista
  if (c != 0 ):
    if(matriz [r] [c - 1] != 8 and matriz [r] [c - 1] != 1 and matriz [r] [c - 1] != -1):
      tupla = (r , c-1)
      lista,a = backtracking(matriz,lista,tupla,a)
      if (a == -1):
        return lista, a
  
  # Verifica se a posicao de baixo ja foi visitado, se não foi vai ser adicionado a lista
  if (r != len(matriz)-1 ):
    if(matriz [r + 1] [c] != 8 and matriz [r + 1] [c] != 1 and matriz [r + 1] [c] != -1):
      tupla = (r+ 1 , c)
      lista,a = backtracking(matriz,lista,tupla,a)
      if (a == -1):
        return lista, a
  
  matriz[r][c] = -1
  return lista,a