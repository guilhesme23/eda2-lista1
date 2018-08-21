import os
import time

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

class Search(object):
  
  def __init__(self, array):
    self.array = array
    self.index_table = []
    self.updated = False
  
  def _search_menu(self):
    print('1 - Busca sequencial')
    print('2 - Busca sequencial com método da transposição')
    print('3 - Busca sequencial indexada')
    print('4 - Busca binária')
    print('0 - Voltar')
    option = input()
    return option

  def menu(self):
    """
    Inicia o menu de buscas.
    """
    back = False
    while(not back):
      opt = self._search_menu()

      if opt == '1':
        clear()
        entry = int(input('Insira um valor: '))
        start = time.process_time()
        print('Resultado: ' + str(self.sequencial(entry)))
        end = time.process_time()
        print('Tempo gasto: ' + str(end - start))
      elif opt == '2':
        clear()
        entry = int(input('Insira um valor: '))
        start = time.process_time()
        print('Resultado: ' + str(self.seq_transp(entry)))
        end = time.process_time()
        print('Tempo gasto: ' + str(end - start))
      elif opt == '0':
        back = True
        clear()
      else:
        pass

    return back

  def print_all(self):
    """
      Printa todos os elementos da lista.
    """
    print('Lista: \n\n')
    print(self.array)
    print('\n\n')
  
  def change_list(self, new_list):
    """
      Atualiza a lista.
    """
    self.updated = True
    self.array = new_list

  def sequencial(self, value):
    """
      Retorna o índice em que se encontra o valor procurado utilizando a busca sequencial.
      Caso o valor não exista na lista, retorna -1.
    """
    result = [index for index, x in enumerate(self.array) if x == value]
    if result == []:
      return -1
    else:
      return result[0]
  
  def seq_transp(self, value):
    """
      Implementa uma busca sequencial com método da transposição.
      Cada elemento buscado é trocado com o elemento 5 posições anterior na lista.
      Caso o valor não exista na lista, retorna -1.
    """
    result = -1
    for index, val in enumerate(self.array):
      if val == value:
        if index > 5:
          self.updated = True
          self.array[index], self.array[index - 5] = self.array[index - 5], self.array[index]
          index -= 5
        result = index
        break
    
    return result


