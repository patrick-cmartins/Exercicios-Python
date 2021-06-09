## Imports ##
from pprint import pprint

## Funções ##
def calcula_media(notas_aluno):
    cont = 0 # total de notas de cada aluno
    soma = 0 # soma das notas de cada aluno
    for nota in notas_aluno:
        cont += 1
        soma += nota
    media_aluno = soma / cont
    return media_aluno

def converte_notas(notas_aluno):
    novo_aluno = []
    for nota in notas_aluno:
        novo_aluno.append(nota*2)

    return novo_aluno

## Programa Principal ##

notas_sala = [
    [7, 9, 4.5],
    [5, 7, 9],
    [0, 10, 6.8],
    [4, 8, 9.2, 3, 7, 5],
    [0, 10, 6.8],
    [4, 8, 9.2],
    
]

print('antes', notas_sala)

novas_notas = []
medias = []

for notas_aluno in notas_sala:
    novo_aluno = converte_notas(notas_aluno)
    media_aluno = calcula_media(novo_aluno)
    medias.append(media_aluno)
    novas_notas.append(novo_aluno)
    print(novo_aluno, media_aluno)

pprint(novas_notas)
