from Rio_atv.Listas.ListADT import ListADT


# -----------------------------
# Implementação baseada em lista nativa do Python
# -----------------------------


class MyList(ListADT):
    """Implementação simples de lista usando a lista nativa do Python."""

    def __init__(self, tamanho=0):
        self.__data = [None] * tamanho

    def index(self, elemento):
        return self.__data.index(elemento)

    def clear(self):
        self.__data = []

    def count(self, elemento):
        return self.__data.count(elemento)

    def remove(self, elemento):
        self.__data.remove(elemento)

    def insert(self, indice, elemento):
        self.__data.insert(indice, elemento)

    def length(self):
        return len(self.__data)

    def remove_all(self, item):
        while item in self.__data:
            self.__data.remove(item)

    def remove_at(self, index):
        self.__data.pop(index)

    def append(self, item):
        self.__data.append(item)

    def replace(self, index, item):
        self.__data[index] = item

    def __getitem__(self, key):
        return self.__data[key]

    def __delitem__(self, key):
        del self.__data[key]

    def __repr__(self):
        return repr(self.__data)

    def __str__(self):
        return str(self.__data)

    def __len__(self):
        return len(self.__data)

    def __contains__(self, item):
        return item in self.__data

    def __setitem__(self, key, value):
        self.__data[key] = value
