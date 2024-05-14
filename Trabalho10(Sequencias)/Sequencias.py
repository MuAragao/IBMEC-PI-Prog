# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:24:33 2024

@author: muaragao
"""

def bombom(dinheiro,preco):
    return float(dinheiro)//preco, dinheiro%preco

def maisbombom(dinheiro,preco):
    return preco - bombom(dinheiro,preco)[1]

def lista(n):
    if n%2==0:
        return list(range(2,n+1,2))
    else:
        return list (range(2,n,2))