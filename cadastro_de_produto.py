#!/usr/bin/env python3 

"""Cadastro de produto"""
__version__ = "0.1.0"

produto = {
    "nome": "Coca_cola"
    produto_cor1 = "preto"
    produto_cor2 = "vermelho"
    produto_cor3 = "branco"
    produto_preco = 5.69
    produto_dimensao_altura = 5.50
    produto_dimensao_largura = 3
    produto_em_estoque = True
    produto_codigo = 1234
    produto_codebar = None      
}


compra = ("Pedro", produto_nome, 3)
total_compra = compra[2] * produto_preco

print(
    f"O cliente {compra[0]} comprou {compra[1]}"
    f" e pagou o total de {total_compra}"    
)
