
variaveis = "o que sao e como utilizar"

Listas = []

tuplas = []

list_comprehensions = "exemplo"
inteiros = [1, 3, 4, 5, 7, 8, 9]
pares = [x for x in inteiros if x % 2 == 0]

inteiros = [1, 3, 4, 5, 7, 8]
quadrados = [n*n for n in inteiros]

frutas = ["maçã", "banana", "laranja", "melancia"]
lista = [fruta.upper() for fruta in frutas]


leitura_de_arquivo = 'outro exemplo'

arquivo = open("palavras.txt", "w")
arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.close()

logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()

# Se desejamos ler linha a linha de nosso arquivo, podemos utilizar a função readline().
# Ela nos retorna uma linha por vez, e faz com que a nossa leitura seja feita de modo mais controlado.
# Também existe a função read() que por sua vez lê o arquivo inteiro.

# Repare que o with usa a função open. Repare também que não fechamos o arquivo. Isso não é mais necessário pois o
# Python vai cuidar disso e, mesmo com erro, garantirá o fechamento do arquivo! Muito melhor não?

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)

# Sabemos que quebrar uma grande função complexa em pequenas funções é uma boa prática por causa de diversos fatores, mas podemos citar como os principais deles:
#
# Dar manutenção ao código fica muito mais fácil, visto que agora podemos examinar vários pequenos blocos, que são muito mais fáceis de compreender do que um grande bloco de código.
# Ao quebrar uma grande função, também estamos deixando ela com menos responsabilidades, com a meta de atingir o ideal de que cada função tenha apenas uma única responsabilidade.
# O código também fica muito mais fácil de testar, pois se temos diversas funções pequenas, conseguimos testar uma a uma em busca de erros no código.
# E por último, a legibilidade do código aumenta muito, pois dando nomes semânticos a cada uma das funções menores, conseguimos deixar bem claro o que aquela parte do código deve fazer e facilita o entendimento do todo como um geral.
