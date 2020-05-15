#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def main( ) :
  arquivo_entrada = sys.argv[1] 
  #arquivo_saida = sys.argv[2]
  
  matriz = []
  arquivo = open(arquivo_entrada, 'r')
  
  primeira_linha = arquivo.readline()
  
  flag = 0
  n_linha = ""
  n_coluna = ""
  for i in primeira_linha:
    if(i != " " and flag == 0):
      n_linha = n_linha + i
    
    elif (i != " " and flag >= 1):
      n_coluna = n_coluna + i

    #Aperfeicoar o erro ou tirar com a justificativa de deveria haver outro codigo so com essa funcao
    #elif (i != " " and flag > 1):
      #raise Exception("Arquivo fora de formato, envie apenas duas dimensões para a matriz") 
    
    else:
      flag = flag + 1

  ##colocar uma verificacao de erro aq
  for linha in arquivo:
    lista = []
    for coluna in linha :
      lista.append(coluna)
    matriz.append(lista)

  print(matriz)
  arquivo.close()


if __name__ == "__main__":
  main( )