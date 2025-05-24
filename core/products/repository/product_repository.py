from abc import abstractmethod


class ProductRepository:

    @abstractmethod
    def find_all(self):
        pass