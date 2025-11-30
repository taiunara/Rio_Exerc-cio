from Listas.ListADT import ListADT

# -----------------------------
# Implementação de lista encadeada simples
# -----------------------------

class Node:
    """Classe que representa um nó em uma lista encadeada simples."""

    def __init__(self, element=None, next=None):
        self.__element = element
        self.__next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, element):
        self.__element = element

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'|{self.__element}|'


class LinkedList(ListADT):
    """Implementação de lista encadeada simples."""

    def __init__(self, tamanho=0):
        self._head = None
        self._tail = None
        self._length = 0

        i = 0
        while i < tamanho:
            self.append(None)
            i += 1

    def insert(self, index, elem):
        """
        Insere um elemento em uma posição específica.
        A inserção pode ocorrer no início, meio ou fim da lista.
        """
        if index == 0:
            self.__insert_at_beginning(elem)
        elif index > self._length:
            self.__insert_at_end(elem)
        else:
            self.__insert_in_between(index, elem)
        self._length += 1

    def __insert_at_beginning(self, elem):
        """Insere um novo nó no início da lista."""
        n = Node(elem)
        if self.empty():
            self.__empty_list_insertion(n)
        else:
            n.next = self._head
            self._head = n

    def __insert_at_end(self, elem):
        """Insere um novo nó no final da lista."""
        n = Node(elem)
        if self.empty():
            self.__empty_list_insertion(n)
        else:
            self._tail.next = n
            self._tail = n

    def __empty_list_insertion(self, node):
        """Configura uma lista vazia para conter apenas um nó."""
        self._head = node
        self._tail = node

    def __insert_in_between(self, index, elem):
        """Insere um elemento no meio da lista."""
        n = Node(elem)
        pos = 0
        aux = self._head
        while pos < index - 1:
            aux = aux.next
            pos += 1
        n.next = aux.next
        aux.next = n

    # TODO: ajustar tail quando o último elemento for removido
    def remove(self, elem):
        """Remove a primeira ocorrência de um elemento da lista."""
        removed = False
        if not self.empty():
            aux = self._head
            if aux.element == elem:
                self._head = aux.next
                removed = True
            else:
                while aux.next and not removed:
                    prev = aux
                    aux = aux.next
                    if aux.element == elem:
                        prev.next = aux.next
                        removed = True
            if removed:
                self._length -= 1

    def count(self, elem):
        """Conta quantas vezes um elemento aparece na lista."""
        counter = 0
        if not self.empty():
            aux = self._head
            if aux.element is elem:
                counter += 1
            while aux.next:
                aux = aux.next
                if aux.element is elem:
                    counter += 1
        return counter

    def clear(self):
        """Remove todos os elementos da lista."""
        self._head = None
        self._tail = None
        self._length = 0

    def index(self, elem):
        """Retorna o índice da primeira ocorrência de um elemento."""
        result = None
        pos = 0
        aux = self._head
        while not result and pos < self._length:
            if aux.element is elem:
                result = pos
            aux = aux.next
            pos += 1
        return result

    def length(self):
        return self._length

    def empty(self):
        return self._head is None

    def remove_all(self, item):
        """Remove todas as ocorrências de um elemento."""
        while self.index(item) is not None:
            self.remove(item)

    def remove_at(self, index):
        """Remove o elemento em uma posição específica."""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        if index == 0:
            self._head = self._head.next
        else:
            aux = self._head
            i = 0
            while i < index - 1:
                aux = aux.next
                i += 1
            aux.next = aux.next.next
        self._length -= 1

    def append(self, item):
        """Adiciona um elemento ao final da lista."""
        self.insert(self._length, item)

    def replace(self, index, item):
        """Substitui o elemento na posição especificada."""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._head
        i = 0
        while i < index:
            aux = aux.next
            i += 1
        aux.element = item

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._head
            result += str(aux)
            while aux.next:
                aux = aux.next
                result += str(aux)
            return result
        else:
            return '||'

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._head
        i = 0
        while i < index:
            aux = aux.next
            i += 1
        return aux.element

    def __setitem__(self, index, value):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._head
        i = 0
        while i < index:
            aux = aux.next
            i += 1
        aux.element = value

    def __len__(self):
        return self._length
