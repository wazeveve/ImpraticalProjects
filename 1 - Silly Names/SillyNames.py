# Primeiro projeto do Livro "Impratical Python Projects" neste arquivo estarão dois códigos
# O código que eu tentei desenvolver usando o Pseudocódigo do livro
# E o código que consta no livro

## Código Desenvolvido pelo pseudocódigo
# Para desenvolver este código onde eu tive dúvidas eu pesquisei na documentação do Python
# Para otimizar o processo de aprendizado.


# Importação de bibliotecas
import random
from rich import print

## Load a list of first names and Surnames

first_names = ['Gabriel', 'Max', 'Ana', 'Vin', 'Mia', 'Brad']
surnames = ['Venancio','Mohamed', 'Freitas', 'Queiroz', 'Pitt', 'Diesel']


# print the names in the screen in order and in red font
# Para imprimir em vermelho foi usado a biblioteca rich
# Para isso foi necessário usar o comando "python -m pip install rich" e logo após "python -m rich"
# para imprimir usamos o comando [red] text [/red]

while True:
    # Choose a first name at random and assign the name to a variable
    selected_fn = random.choice(first_names)

    # Choose a surname at random and assign the surname to a variable
    selected_surname = random.choice(surnames)

    print(' [red] ' + selected_fn + " " + selected_surname + '[/red]')
    # Ask the user to quit or play again

    tentar_novamente = input('Tentar novamente? (n para sair)') #Ok eu dei uma colada no código do livro
    if tentar_novamente.lower() == 'n':
        break


# Foi um pouco complicado mas deu certo, foi necessário algumas pesquisas, a maioria foi no site da Asimov Academy ou Stack Overflow

# Código que está no livro
# Bibliotecas importadas no código do livro
import sys, random 

print("Welcome to the Psych 'Sidekick Name Picker. \n")
print("A name just like Sean would pick for Gus: \n\n") # Não entendi a referência but...

first = ('Baby Oil', 'Bad News', 'Big Burps', 'Bill', 'Bob') # Haviam mais nomes porém são muitos!

last = ('Bigmeat', 'Clovenhoof', 'Johnson', 'Guster', 'Henderson')

while True:
    firstName = random.choice(first)

    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr) #idk why but it doesnt paint the text :)
    print("\n\n")

    try_again = input("\n\nTry Again? (Press Enter else n to quit) \n")
    if try_again.lower() == 'n':
        break

input("\n Press Enter to exit.")


# Primeiro código, uma experiência bacana, deu pra quebrar um pouco a cabeça mas foi relativamente fácil.