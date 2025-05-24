from abc import ABC, abstractmethod

from model.index import PaymentInformationDTO


class PaymentProcessorStrategy(ABC):

    @abstractmethod
    def execute(self, payment_information_dto: PaymentInformationDTO) -> None:
        pass
