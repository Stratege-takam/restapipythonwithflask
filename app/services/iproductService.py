# Importer les classes ABC et abstractmethod dans le namespace abc
from abc import ABC, abstractmethod


# Définir une interface
class IProductService(ABC):

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_product_by_id(self, id):
        pass

    @abstractmethod
    def update_product_by_id(self,id, product):
        pass

    @abstractmethod
    def delete_product_by_id(self, id):
        pass

    @abstractmethod
    def create_product(self, product):
        pass



