import random
import os
from algorithms import Search

def mainMenu():
  print('1 - Criar lista aleatória')
  print('2 - Adicionar elemento na lista')
  print('3 - Remover elemento da lista')
  print('4 - Printar lista')
  print('5 - Buscas')
  print('0 - Sair')
  option = input()
  return option

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
  lst = []
  searcher = Search(lst)
  exit = False

  while(not exit):
    option = mainMenu()
    if option == '0':
      exit =  True
      clear()
    elif option == '1':
      clear()
      entry = int(input('Insira o tamanho da lista: '))
      lst = random.sample(range(0,3*entry), entry)
      searcher.change_list(lst)
    elif option == '2':
      clear()
      entry = int(input('Insira o valor: '))
      lst.append(entry)
      searcher.change_list(lst)
    elif option == '4':
      clear()
      searcher.print_all()
    elif option == '5':
      clear()
      searcher.menu()
    else:
      pass
