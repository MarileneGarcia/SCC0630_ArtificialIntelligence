#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" O objetivo do codigo da funcao principal 
e salvar os dados do arquivo de entrada em 
uma matriz de strings, e chamar os arquivos 
que vão executar os algoritmos """

import sys
from termcolor import colored
import copy
import busca_profundidade
import busca_largura
import os,time

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

  """ Matriz com os dados do arquivo fornecido """  
  for linha in arquivo:
    lista = []
    for coluna in linha : 
      if (coluna == "*"):
        lista.append(0)
      elif(coluna == "-"):
        lista.append(1)
      elif(coluna == "#"):
        lista.append(2)
      elif(coluna == "$"):
        lista.append(3)
    matriz.append(lista)
  arquivo.close()

  impressao(matriz)

""" Funcao para imprimir a matriz """
def impressao(matriz):
  os.system("clear")
  copia_matriz = copy.deepcopy(matriz)

  for a in range(int(len(copia_matriz[0])/2) - 5):
    print("", end = " ")
  print("LABIRINTO")

  caminho = []
  """ Matriz com os dados do arquivo fornecido """  
  for n in copia_matriz:
    for m in n:
      if(m == 0):
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

  """ Escolher o algoritmo a ser executado """
  print("\nOs algoritmos que podem realizar a busca pelos caminhos do labirinto são: ")
  print( "[ 0 ] Busca em profundidade")
  print( "[ 1 ] Busca em largura")
  print( "[ 2 ] Sair \n")
  valor_lido = input("Digite o número desejado e pressione 'enter': ")

  if(valor_lido == "0"):
    ini = time.time()
    lista = busca_profundidade.busca_profundidade(copia_matriz)
    fim = time.time()
    print("O tempo da busca em profundidade, de acordo com a estrategia de controle, foi: ", fim - ini)
    print("O caminho obtido pela busca em profundidade, de acordo com a estrategia de controle, foi: ")
    print(lista)

    # Salvar o resultado num arquivo
    arquivo_bp = open("resultado_busca_profundidade.txt", 'w')
    arquivo_bp.write('\n'.join('%s %s' % x for x in lista))
    arquivo_bp.close()
    
    print("\nDeseja realizar outro tipo de busca ?")
    print( "[ 0 ] Sim")
    print( "[ 1 ] Não")
    valor_lido = input("Digite o número desejado e pressione 'enter': ")
    if(valor_lido == "0"):
      impressao(matriz)
    else:
      return -1

  elif(valor_lido == "1"):
    ini = time.time()
    lista = busca_largura.busca_largura(copia_matriz)
    fim = time.time()
    print("O tempo da busca em largura, de acordo com a estrategia de controle, foi: ", fim - ini)
    print("O caminho obtido pela busca em largura, de acordo com a estrategia de controle, foi: ")
    print(lista)

    # Salvar o resultado num arquivo
    arquivo_bl = open("resultado_busca_largura.txt", 'w')
    arquivo_bl.write('\n'.join('%s %s' % x for x in lista))
    arquivo_bl.close()
    
    print("\nDeseja realizar outro tipo de busca ?")
    print( "[ 0 ] Sim")
    print( "[ 1 ] Não")
    valor_lido = input("Digite o número desejado e pressione 'enter': ")
    if(valor_lido == "0"):
      impressao(matriz)
    else:
      return -1

  elif(valor_lido == "2"):
    return -1


if __name__ == "__main__":
  main( )