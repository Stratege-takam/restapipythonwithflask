# Importer les classes ABC et abstractmethod dans le namespace abc
from abc import ABC, abstractmethod


# Définir une interface
class IUserService(ABC):

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self, id):
        pass

    @abstractmethod
    def update_user_by_id(self, id, user):
        pass

    @abstractmethod
    def delete_user_by_id(self, id):
        pass

    @abstractmethod
    def create_user(self, user):
        pass



