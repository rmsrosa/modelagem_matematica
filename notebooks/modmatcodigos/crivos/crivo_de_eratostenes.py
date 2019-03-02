#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Números primos segundo o crivo de Eratóstenes

Este código exibe todos os números primos abaixo de 100, utilizando 
o algoritmo do crivo de Eratóstenes.

Este código também pode ser importado como módulo. Nesse caso
ele disponibiliza a função que implementa o algoritmo, que pode
então ser executado com qualquer cota superior:

    * primos_ate: recebe um inteiro positivo e retorna uma lista
        com todos números primos entre 2 e este inteiro.
'''

import math

def primos_ate(cota_superior):
    '''
    Determinação dos números primos através do Crivo de Eratóstenes
    
    Esta função implementa o algoritmo do Crivo de Eratóstenes, para
    encontrar todos os números primos entre 2 e um número dado.
    
    Entrada:
    --------
        cota_superior: inteiro
            Um inteiro positivo até o qual a busca por números primos 
            será feita.
    
    Saída:
    ------
        primos: lista de inteiros
            Uma lista com os números primos encontrados.
            
    Exemplo:
    --------
    
        crivo_de_eratostenes(10)
            Retorna a lista [2, 3, 5, 7, 9], que são todos os primos 
            entre 2 e 10.
    '''

    assert (type(cota_superior) == int), f"A cota superior \
'{cota_superior}', dada como argumento da função, é do tipo \
'{type(cota_superior)}', mas deveria ser um inteiro positivo."

    assert (cota_superior > 0), f"A cota superior '{cota_superior}', \
dada como argumento da função, deveria ser um inteiro positivo."

    crivo = (cota_superior + 1) * [True] 
    # Compensar que o índice de arrays começa em 0 e termina em um 
    # a menos do seu comprimento

    for i in range(2,round(math.sqrt(cota_superior + 1))):
        # Varre os inteiros para negar, no crivo, os primos que 
        # são múltiplos desses inteiros
        if crivo[i]: 
            # Pula os que já foram negados
            for j in range(i**2, cota_superior + 1, i):
                crivo[j] = False

    primos = [i for i in range(2, cota_superior + 1) if crivo[i]]
    
    return primos

if __name__ == '__main__':
    print("Primos até 100 calculados pelo crivo de Eratóstenes:\n  ", primos_ate(100))