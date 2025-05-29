#!/usr/bin/env python3 

"""Cadastro de produto"""
__version__ = "0.1.0"

import pprint

produto = {
    "nome": "Coca_cola",
    "cores": ["preto", "vermelho", "branco"], 
    "preco": 5.69,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 1234,
    "codebar": None      
}

cliente = {
    "nome": "Pedro"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

#pprint.pprint(compra)

total_compra = compra['quantidade'] * compra ['produto']['preco']

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de BRL {total_compra} "
)
