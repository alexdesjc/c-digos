import unittest
from heapq import heappush, heappop

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    iguais  = [x for x in lista if x == pivot]
    menores = [x for x in lista if x <  pivot]
    maiores = [x for x in lista if x >  pivot]
    return quicksort(menores) + iguais + quicksort(maiores)

def heapsort(lista):
  h = []
  for x in lista:
    heappush(h, x)
  return [heappop(h) for i in range(len(h))]

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quicksort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quicksort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quicksort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quicksort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_desordenada_vinte(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], quicksort([11, 12, 13, 14, 15, 16, 17, 18, 19, 9, 7, 1, 8, 5, 10, 3, 6, 4, 2, 0]))

    def teste_lista_ordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quicksort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    unittest.main()
