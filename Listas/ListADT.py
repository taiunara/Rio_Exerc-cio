from abc import ABC, abstractmethod


class ListADT(ABC):
    """
    Classe abstrata que define o contrato para estruturas de dados do tipo lista.
    Todas as listas concretas devem herdar e implementar esses métodos.
    """

    @abstractmethod
    def insert(self, indice, elemento):
        """
        Insere o valor <elemento> na posição <indice>.
        Deve garantir que, se já existir um valor nessa posição, ele não seja sobrescrito.
        """
        ...

    @abstractmethod
    def remove(self, elemento):
        """Remove a primeira ocorrência de <elemento> da lista."""
        ...

    @abstractmethod
    def count(self, elemento):
        """Conta quantas vezes <elemento> aparece na lista."""
        ...

    @abstractmethod
    def clear(self):
        """Remove todos os elementos da lista."""
        ...

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro índice em que <elemento> aparece na lista."""
        ...

    @abstractmethod
    def length(self):
        """Retorna o tamanho (número de elementos) da lista."""
        ...

    @abstractmethod
    def remove_all(self, item):
        """Remove todas as ocorrências de <item> da lista."""
        ...

    @abstractmethod
    def remove_at(self, index):
        """Remove o elemento localizado na posição <index>."""
        ...

    @abstractmethod
    def append(self, item):
        """Adiciona <item> ao final da lista (concatenação)."""
        ...

    @abstractmethod
    def replace(self, index, item):
        """Substitui o elemento na posição <index> por <item>."""
        ...
