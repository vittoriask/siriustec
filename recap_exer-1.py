# Questao 1: selecione o numero 2 nos objetos abaixo
# Exemplo: para selecionar o numero do 2 em lista1 = [[1,3,4],5,[1,3,[2]]]
# devemos acessar o terceiro elemento da lista, o qual e uma nova lista
# dentro desta nova lista devemos acessar o terceiro elemento que e [2]
# e entao devemos acessar o primeiro elemento de [2]
# Isto e, nosso codigo fica lista1[2][2][0]

# item (a)
lista = [1,3,[1,3,{1:3,3:2}]]
print(lista[2][2][3])


# item (b)[]
dict1 = {'a':1, 'b':[1,3,{'a':1, 'b':2}]}
print(dict1['b'][2]['b'])

# item (c)
mat = [[1,3,4],[5,6,8],[[1,2,3]]]
print(mat[2][0][1])




# Questao 2: Vamos falar um pouco sobre matrizes. Para mais informacoes veja https://pt.wikipedia.org/wiki/Matriz_(matem%C3%A1tica)
# Use lacos de repeticao para criar uma matriz 3x3 em que cada posicao a(i,j) recebe o valor i*j
# Exemplo: o elemento a(2,3) e o elemento que esta na segunda linha e na terceira coluna
# e este elemento deve receber o numero 2*3, isto e, a(2,3) = 6
# A solução deste exercício deve ser [[0,0,0],[0,1,2],[0,2,4]]

mat = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        mat[l][c] = 1 * c

print(mat)




# Questão 3: Considere o dicionário a seguir:
compras = {'itens':['banana','maçã','uva','laranja'],
           'quantidade':[5,10,1,7],
           'preço_unitario':[1.20, 1.10, 3.15, 4.25]}

# item (a)
# Para cada item do dicionário imprima na tela uma frase do tipo:
# "O valor unitário da banana é 1.20; as 5 bananas custarão 6.00"

for i in range(4):
    itens = compras['itens'] [i]
    quantidade = compras ['quantidade'] [i]
    preço_unitario = compras ['preço_unitario'] [i]
    print(f"O valor unitario da {itens} é {preço_unitario}, as {quantidade} custarão {quantidade * preço_unitario}")


# item (b)
# Calcule o total da compra

total = 0

for i in range(4):
    compras = quantidade * preço_unitario
    total += compras

print(total)



# Questão 4: Dada uma lista qualquer de número positivos, escreva uma função que ordena a lista do menor para o maior
# Exemplo: lista1 = [5,2,4,3,1], retorna new_list = [1,2,3,4,5]

def ordena(lista1):
    new_list = []
    for i in range(len(lista1)):
        new_list.append(min(lista1))
        lista1.remove(min(lista1))
    
    return new_list




# Questão 5: Vamos brincar de adivinha! Seu desafio é criar uma função que recebe um número como
# parâmetro e pede para que o jogador tente adivinhá-lo! Se o jogador acertar, dê os parabéns,
# caso contrário avise se ele deve chutar um número maior ou menor do que o número chutado.
# O programa deve continuar pedindo por um chute até que o jogador acerte!

def adivinha(number):
    while True:
        chute = int(input("Escolhi um numero inteiro, tente adivinhar qual:"))
        if chute == number:
            print("Parabéns você acertou!")
            break
        elif chute < number:
            print("Que tal tentar um numero maior")
        else:
            print("Que tal tentar um numero menor")

###print(adivinha(4))

# Questão 6
# Em python, laços de repetição podem ser escritos de uma forma diferente:
# Considere o código abaixo:
'''
cubes = []
for x in [1,2,3,4,5]:
    cubes.append(x**3)
print(cubes)
'''
# Este código pode ser escrito como: 
'''
cubes = [x**3 for x in [1,2,3,4,5]]
print(cubes)
'''
# Essa forma é chamada list comprehension e, em geral, é mais interessante no python
# pois é executado mais rapidamente do que o laço usual e torna o código menor e mais fácil de ler

# Exercício: Use list comprehension para criar uma função que recebe uma lista numérica
# e retorna os valores da lista em dobro

def quadrado(list):
    return [2*x for x in lista ]

###print(quadrado[1,2,3,4])


