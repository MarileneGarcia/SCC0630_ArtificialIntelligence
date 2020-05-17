#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" O objetivo do codigo da funcao principal 
e salvar os dados do arquivo de entrada em 
uma matriz de strings, e chamar os arquivos 
que vão executar os algoritmos """

import sys
from termcolor import colored

def main( ) :
  matriz = []
  arquivo = open(sys.argv[1], 'r')
  
  """ Leitura do numero de linhas e colunas """
  primeira_linha = arquivo.readline()
  flag = 0
  n_linha = ""
  n_coluna = ""
  for i in primeira_linha:
    if(i != " " and flag == 0):
      n_linha = n_linha + i
    elif (i != " " and flag >= 1):
      n_coluna = n_coluna + i  
    else:
      flag += 1
  n_linha = int(n_linha)
  n_coluna = int(n_coluna)
  
  for a in range(int(n_coluna/2) - 5):
    print("", end = " ")
  print("LABIRINTO")

  """ Matriz com os dados do arquivo fornecido """  
  for linha in arquivo:
    lista = []
    for coluna in linha : 
      if (coluna == "*"):
        text = colored("#", "white")
        print (text, end = '')
        lista.append(0)
      elif(coluna == "-"):
        text = colored("#", "grey")
        print (text, end = '')
        lista.append(1)
      elif(coluna == "#"):
        text = colored("#", "blue")
        print (text, end = '')
        lista.append(2)
      elif(coluna == "$"):
        text = colored("#", "red")
        print (text, end = '')
        lista.append(3)
    print("")
    matriz.append(lista)
  arquivo.close()

  """ Escolher o algoritmo a ser executado """
  print("\nOs algoritmos que podem realizar a busca pelos caminhos do labirinto são: ")
  print( "[ 0 ] Busca em profundidade")
  print( "[ 1 ] Busca em largura")
  print( "[ 2 ] Busca Best-First Search")
  print( "[ 3 ] Busca A*")
  print( "[ 3 ] Hill Climbing \n")
  valor_lido = input("Digite o algortimo desejado e pressione 'enter': ")
  



if __name__ == "__main__":
  main( )