from abc import ABC, abstractmethod

class IMaillingService(ABC):

    @abstractmethod
    def normalize_attach(self, attachements):
       pass

    @abstractmethod
    def send(self,  subject, recipients, body, ishtml = False, attachements = None,sender= None, sendername= None):
        pass

