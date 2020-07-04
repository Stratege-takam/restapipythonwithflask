# Importer les classes ABC et abstractmethod dans le namespace abc
from abc import ABC, abstractmethod

class IAuthGradeService(ABC):

    @abstractmethod
    def unique_id(self, length = 12, isNumeric = False):
        pass

    @abstractmethod
    def hash_password(self, password):
        pass

    @abstractmethod
    def check_password(self, password, compare_password):
        pass

    @abstractmethod
    def generate_token(self, authjwt):
        pass

    @abstractmethod
    def create_an_application(self, authjwt):
        pass
