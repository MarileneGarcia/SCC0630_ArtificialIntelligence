#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Objetivo: Realizar a busca em largura na matriz de dados 
    Variaveis de entrada: Matriz dos dados
    Variaveis de saida: Lista de tuplas com o caminho do algoritmo """

def busca_largura(matriz):
  pos_lin_ini = 0
  pos_col_ini = 0

  for elem_inicial in matriz[0]:
    pos_col_ini += 1
    if (elem_inicial == 2):
      break
  print(pos_col_ini)
