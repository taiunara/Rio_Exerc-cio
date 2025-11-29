""" Escreva um programa em Python que simula um ecosistema.
Este ecosistema consiste de um rio, modelado como uma lista,
que contÃ©m dois tipos de animais: ursos e peixes.

No ecosistema, cada elemento da lista deve ser um objeto do
tipo Urso, Peixe ou None (que indica que a posiÃ§Ã£o do rioq
estÃ¡ vazia).

A cada rodada do jogo, baseada num processo aleatÃ³rio, cada
animal tenta se mover para uma posiÃ§Ã£o da lista adjacente (a
esquerda ou direita) ou permanece na sua mesma posiÃ§Ã£o.

Se dois animais do mesmo tipo colidirem (urso com urso ou peixe com peixe),
eles permanecem nas suas posiÃ§Ãµes originais, mas uma nova instÃ¢ncia do
animal deve ser posicionada num local vazio, aleatoriamente determinado.

Se um Urso e um peixe colidirem, entretanto, o peixe morre e o urso fica no lugar do peixe

Se ursos ou peixes decidirem se mover para uma posiÃ§Ã£o inexistente da lista, eles ficam no mesmo lugar"""
import random
from abc import ABC, abstractmethod
from random import randint

import logging

from Rio_atv.Listas.DoubleLinkedList import DoublyLinkedList
from Rio_atv.Listas.LinkedList import LinkedList
from Rio_atv.Listas.MyList import MyList

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)


class Animal(ABC):

    def mover(self) -> int:
        """
        Generates a random movement.

        The `mover` function calculates a random step, which could be -1, 0, or 1.
        This can simulate a simple random movement in one-dimensional space.

        Returns:
            int: The random movement value, either -1, 0, or 1.
        """
        return randint(-1, 1)

    @abstractmethod
    def reproduzir(self, animal) -> (bool, int):
        """
        An abstract method that needs to be implemented to model the reproduction behavior
        of an animal. This method provides a contract for subclasses to define the logic
        specific to the reproduction of their respective animal types.

        Args:
            animal: The animal involved in the reproduction process.

        Returns:
            Tuple[bool, int]: A tuple where the first element is a boolean indicating if
            the reproduction was successful, and the second element is an integer
            representing the number of offspring produced.
        """
        ...


class Urso(Animal):

    def __init__(self):
        self.vida = random.randint(2, 3)

    def reproduzir(self, animal) -> (bool, int):
        result = False, 0
        if isinstance(animal, Urso):
            result = True, 1
        return result

    def __repr__(self):
        return f'Urso(Vida={self.vida})'

    def __str__(self):
        return f'Urso(Vida={self.vida})'


class Peixe(Animal):

    def reproduzir(self, animal):
        result = False, 0
        if isinstance(animal, Peixe):
            result = True, 1
        return result


    def __repr__(self):
        return 'Peixe'

    def __str__(self):
        return 'Peixe'


class NPC(ABC):
    ...


class Agua(NPC):

    def __repr__(self):
        return 'Agua'

    def __str__(self):
        return 'Agua'

class Toca(NPC):
    def __init__(self):
        self.ocupante = None

    def esta_vazia(self):
        return self.ocupante is None

    def tentar_entrar(self, animal):
        """
        O peixe tenta entrar na toca.
        Retorna True se entrou, False caso contrário.
        """
        if isinstance(animal, Peixe) and self.ocupante is None:
            self.ocupante = animal
            return True
        return False

    def __repr__(self):
        if self.ocupante:
            return f"Toca({self.ocupante})"
        return "Toca()"

    def __str__(self):
        return self.__repr__()

class Ecossistema(ABC):

    @abstractmethod
    def executar(self):
        pass


class Rio(Ecossistema):

    def __init__(self, tamanho, rodadas=10):
        logging.info(f'Inicializando o rio com tamanho {tamanho} e {rodadas} rodadas')
        self.__rodadas = rodadas
        self.__rio = LinkedList(tamanho)
        for i in range(len(self.__rio)):
            self.__rio[i] = None
        self.__qtd_urso = int(len(self.__rio) * 0.2)
        self.__qtd_peixe = int(len(self.__rio) * 0.4)
        self.__qtd_tocas = int(len(self.__rio) * 0.1)
        self.__popular_rio(self.__qtd_tocas, Toca)
        self.__popular_rio(self.__qtd_urso, Urso)
        self.__popular_rio(self.__qtd_peixe, Peixe)
        self.__preencher_npc(Agua)
        logging.info(f'Rio inicializado: {self}')

    def __popular_rio(self, qtd, classe):
        while qtd > 0:
            pos = randint(0, len(self.__rio) - 1)
            if self.__rio[pos] is None:
                logging.debug(f'{classe} posicionado na posição {pos}')
                self.__rio[pos] = classe()
                qtd -= 1

    def __preencher_npc(self, classe):
        for i in range(0, len(self.__rio)):
            if self.__rio[i] is None:
                self.__rio[i] = classe()

    def __has_empty_position(self):
        for i in range(len(self.__rio)):
            if self.__rio[i] is None:
                return True
        return False

    def __contem_agua(self):
        result = False
        for i in self.__rio:
            if isinstance(i, Agua):
                result = True
                break
        return result

    def executar(self):
        rodada = 0
        while rodada < self.__rodadas:
            logging.info(f'Iniciando rodada {rodada + 1}')
            self.__rodada()
            logging.info(f'Estado do rio após rodada {rodada + 1}: {self}')
            rodada += 1

    def __rodada(self):
        visitados = set()
        for i in range(len(self.__rio)):
            if i in visitados:
                continue
            objeto = self.__rio[i]  # objeto na posiÃ§Ã£o i
            if isinstance(objeto, (Urso, Peixe)):  # apenas animais se movem
                movimento = objeto.mover()
                destino = (i + movimento) % len(self.__rio)
                logging.debug(f'{objeto} na posição {i} tenta mover para {destino}')
                if destino == i:
                    logging.debug(f'{objeto} na posição {i} permanece no lugar')
                    continue
                alvo = self.__rio[destino]  # o que estÃ¡ no destino
                visitado = self.__colidir(objeto, alvo, i, destino)
                if visitado:
                    visitados.add(destino)
            
            for i in range(len(self.__rio)):
                if isinstance(self.__rio[i], Toca):
                    toca = self.__rio[i]
                    if toca.ocupante is not None:
                        saida = i + randint(-1, 1)
                        if 0 <= saida < len(self.__rio):
                            if isinstance(self.__rio[saida], Agua):
                                self.__rio[saida] = toca.ocupante
                                toca.ocupante = None

    def __colidir(self, objeto, alvo, origem: int, destino: int):
        """
        Trata a colisão ou interação de um animal com o que está na posição de destino.
        """
        if isinstance(alvo, Agua):
            if isinstance(objeto, Urso):
                objeto.vida -= 1
                if objeto.vida <= 0:
                    logging.debug(f'{objeto} em {origem} morreu de fraqueza!')
                    self.__rio[origem] = Agua()
                    return True
            logging.debug(f'{objeto} move de {origem} para Água em {destino}')
            self.__rio[destino] = objeto
            self.__rio[origem] = Agua()
            return True

        if isinstance(objeto, Urso) and isinstance(alvo, Peixe):
            logging.debug(f'{objeto} em {origem} come peixe em {destino}')
            self.__rio[destino] = objeto
            self.__rio[origem] = Agua()
            objeto.vida = min(objeto.vida + 1, 3)
            return True

        if isinstance(objeto, Peixe) and isinstance(alvo, Urso):
            logging.debug(f'Peixe em {origem} é comido por urso em {destino}')
            self.__rio[origem] = Agua()
            alvo.vida = min(alvo.vida + 1, 3)
            return True

        if isinstance(alvo, Toca):
            if isinstance(objeto, Peixe):
                entrou = alvo.tentar_entrar(objeto)
                if entrou:
                    logging.debug(f'{objeto} entrou na Toca em {destino}')
                    self.__rio[origem] = Agua()
                    return True
                else:
                    logging.debug(f'{objeto} tentou entrar na Toca em {destino}, mas não conseguiu')
                    return False
            logging.debug(f'Urso tentou entrar em Toca em {destino} — bloqueado.')
            return False
        if isinstance(objeto, Urso) and isinstance(alvo, Urso):
            if objeto.vida == alvo.vida:
                if self.__has_empty_position():
                    logging.debug(f'{objeto} e {alvo} têm mesma vida ({objeto.vida}) e reproduzem')
                    self.__popular_rio(1, Urso)
                return False
            else:
                if objeto.vida > alvo.vida:
                    logging.debug(f'{objeto} ({objeto.vida}) vence {alvo} ({alvo.vida}) e ganha 1 vida')
                    objeto.vida += 1
                    alvo.vida -= 1
                else:
                    logging.debug(f'{alvo} ({alvo.vida}) vence {objeto} ({objeto.vida}) e ganha 1 vida')
                    objeto.vida -= 1
                    alvo.vida += 1
                if objeto.vida <= 0:
                    logging.debug(f'{objeto} morreu na briga em {origem}')
                    self.__rio[origem] = Agua()
                if alvo.vida <= 0:
                    logging.debug(f'{alvo} morreu na briga em {destino}')
                    self.__rio[destino] = Agua()
                return True
        reproduz, qtd = objeto.reproduzir(alvo)
        if reproduz and self.__has_empty_position():
            logging.debug(f'{objeto} e {alvo} reproduzem em {origem} e {destino}')
            self.__popular_rio(qtd, objeto.__class__)
            return True
        if type(objeto) == type(alvo):
            logging.debug(f'{objeto} e {alvo} colidem em {destino}, permanecem no lugar')
            return False

        return False

    def __repr__(self):
        return self.__rio.__repr__()

    def __str__(self):
        return self.__rio.__str__()
