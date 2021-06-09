from pprint import pprint

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
    novo_aluno = []
    cont = 0 # total de notas de cada aluno
    soma = 0 # soma das notas de cada aluno
    for nota in notas_aluno:
        nota_nova = nota*2
        novo_aluno.append(nota_nova)
        cont += 1
        soma += nota_nova
    novas_notas.append(novo_aluno)
    media_aluno = soma / cont
    medias.append(media_aluno)
    print(novo_aluno, media_aluno)

pprint(novas_notas)
