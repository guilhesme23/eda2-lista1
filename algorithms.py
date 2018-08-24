import os
import time

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

class Search(object):
  
  def __init__(self, array):
    self.array = array
    self.index_table = []
    self.updated = False
    self.ordered = False
  
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
      elif opt == '3':
        clear()
        entry = int(input('Insira um valor: '))
        start = time.process_time()
        print('Resultado: ' + str(self.indexed_search(entry)))
        end = time.process_time()
        print('Tempo gasto: ' + str(end - start))
      elif opt == '4':
        clear()
        entry = int(input('Insira um valor: '))
        start = time.process_time()
        print('Resultado: ' + str(self.bin_search(entry)))
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
    self.ordered = False
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
      Caso exista retorna o índice.
    """
    result = -1
    for index, val in enumerate(self.array):
      if val == value:
        if index > 5:
          self.updated = True
          self.ordered = False
          self.array[index], self.array[index - 5] = self.array[index - 5], self.array[index]
          index -= 5
        result = index
        break
    
    return result

  def _bin(self, value, min, max, l):
    """
      Função auxiliar que implementa o algoritmo da busca binária.
    """
    if min == max:
      return -1
    mid = int(min + max / 2)
    if l[mid][1] == value:
      return l[mid][1]
    elif l[mid][1] < value:
      return self._bin(value, mid, max, l)
    else:
      return self._bin(value, min, mid, l)

  def bin_search(self, value):
    """
      Implementa uma busca binária.
      Retorna o índice do valor procurado caso exista na lista.
      Retorna -1 caso não exista.
    """
    if not self.ordered:
      self.updated = True
      self.ordered = True
      self.array.sort()
    
    return self._bin(value, 0, (len(self.array) - 1), list(enumerate(self.array)))
  
  def gen_index_table(self, l):
    """
      Gera uma tabela de índices.
    """
    qtd = int(len(l) * 0.2)
    self.index_table = []
    step = int(len(l) / qtd)
    for index in range(1,qtd):
      index = index * step
      self.index_table.append(l[index])


  def indexed_search(self, value):
    """
      Implementa uma busca sequencial indexada.
      Retorna o indice do valor procurado caso exista na lista.
      Retorna -1 caso não exista.
    """
    if self.updated:
      if not self.ordered:
        self.array.sort()
      self.gen_index_table(list(enumerate(self.array)))
    index_table = self.index_table
    index = 0
    for kindex in range(0,(len(index_table) - 1)):
      if (index_table[kindex][1] > value) and (kindex == 0) :
        return -1
      elif index_table[kindex][1] == value:
        return index_table[kindex][0]
      if index_table[kindex][1] > value:
        index = index_table[kindex - 1][0]
        break
    array = list(enumerate(self.array))
    for i in range(index,(len(array) - 1)):
      if array[i][1] == value:
        return array[i][0]
      elif array[i][1] > value:
        return -1




