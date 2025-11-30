from Listas.ListADT import ListADT


# -----------------------------
# Implementação de lista duplamente encadeada
# -----------------------------

class DoublyLinkedList(ListADT):
    """Implementação de lista duplamente encadeada."""

    class _DoublyNode:
        """Classe interna que representa um nó duplamente encadeado."""
        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

        def __str__(self):
            return str(self._elem) + ' ' if self._elem is not None else '|'

        @property
        def element(self):
            return self._elem

        @element.setter
        def element(self, elem):
            self._elem = elem

        @property
        def previous(self):
            return self._prev

        @previous.setter
        def previous(self, node):
            self._prev = node

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, node):
            self._next = node

    def __init__(self, size=0):
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._length = 0

        # Cria 'size' posições inicialmente vazias
        for _ in range(size):
            self.append(None)

    def __len__(self):
        return self._length

    def insert(self, index, elem):
        """
        Insere um elemento em uma posição específica da lista.
        Caso o índice seja maior que o tamanho atual, o elemento é inserido no fim.
        """
        if index >= self._length:
            index = self._length
        if self.empty():
            new_node = self._DoublyNode(elem, self._header, self._trailer)
            self._header.next = new_node
            self._trailer.previous = new_node
        elif index == 0:
            new_node = self._DoublyNode(elem, self._header, self._header.next)
            self._header.next.previous = new_node
            self._header.next = new_node
        else:
            this = self._header.next
            successor = this.next
            pos = 0
            while pos < index - 1:
                this = successor
                successor = this.next
                pos += 1
            new_node = self._DoublyNode(elem, this, successor)
            this.next = new_node
            successor.previous = new_node
        self._length += 1

    def remove(self, elemento):
        """Remove a primeira ocorrência de um elemento."""
        if not self.empty():
            node = self._header.next
            pos = 0
            found = False
            while not found and pos < self._length:
                if node.element == elemento:
                    found = True
                else:
                    node = node.next
                    pos += 1
            if found:
                node.previous.next = node.next
                node.next.previous = node.previous
                self._length -= 1

    def count(self, elem):
        """Conta quantas vezes um elemento aparece na lista."""
        result = 0
        this = self._header.next
        while this.next is not None:
            if this.element == elem:
                result += 1
            this = this.next
        return result

    def clear(self):
        """Esvazia completamente a lista."""
        self._header = self._DoublyNode(None, None, None)
        self._trailer = self._DoublyNode(None, None, None)
        self._header.next = self._trailer
        self._trailer.previous = self._header
        self._length = 0

    def index(self, elem):
        """Retorna o índice da primeira ocorrência de um elemento."""
        result = None
        pos = 0
        this = self._header.next
        while not result and pos < self._length:
            if this.element is elem:
                result = pos
                break
            this = this.next
            pos += 1
        return result

    def length(self):
        return self._length

    def empty(self):
        """Retorna True se a lista estiver vazia."""
        return self._length == 0

    def __str__(self):
        if not self.empty():
            result = ''
            aux = self._header
            result += str(aux)
            while aux.next:
                aux = aux.next
                result += str(aux)
            return result
        else:
            return '||'

    def remove_all(self, item):
        """Remove todas as ocorrências de um item."""
        while self.index(item) is not None:
            self.remove(item)

    def remove_at(self, index):
        """Remove o elemento em uma posição específica."""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        if index == 0:
            self._header.next = self._header.next.next
            self._header.next.previous = self._header
        elif index == self._length - 1:
            self._trailer.previous = self._trailer.previous.previous
            self._trailer.previous.next = self._trailer
        else:
            aux = self._header.next
            for _ in range(index):
                aux = aux.next
            aux.previous.next = aux.next
            aux.next.previous = aux.previous
        self._length -= 1

    def append(self, item):
        """Adiciona um elemento ao final da lista."""
        self.insert(self._length, item)

    def replace(self, index, item):
        """Substitui o elemento na posição especificada."""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._header.next
        for _ in range(index):
            aux = aux.next
        aux.element = item

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._header.next
        for _ in range(index):
            aux = aux.next
        return aux.element

    def __setitem__(self, index, value):
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        aux = self._header.next
        for _ in range(index):
            aux = aux.next
        aux.element = value