#!/user/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de criança agrupadas por sala 
que frequentam cada uma das atividades.
"""

__version__ = "0.1.0"

# Dados
sala1 = ["Erick", "Maria", "Pedro", "Jóse", "Fernanda"]
sala2 = ["Joana", "Paula", "João", "Isadora", "Ana"]

aula_ingles = ["Erick", "João", "Pedro", "Paula", "Fernanda"]
aula_musica = ["Paula", "José", "Maria", "Isadora"]
aula_danca = ["Joana", "Pedro", "Isadora"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca),
]

# Lista alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print (f"Alunos da atividade, {nome_atividade}\n")
    print ("-" * 40)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade: 
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"{nome_atividade} sala1 ", atividade_sala1)
    print(f"{nome_atividade} sala2 ", atividade_sala2)

    print()
    print("#" * 40)
