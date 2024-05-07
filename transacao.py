from abc import ABC, abstractmethod


class Transacao(ABC):
    @property
    def valor(self):
        pass
    
    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass