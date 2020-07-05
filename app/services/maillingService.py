from app.config.settings import init_app, Message, app_param
from app.services.imaillingService import IMaillingService


class MaillingService(IMaillingService):

    def normalize_attach(self, attachements):
        files = []
        for file in attachements:
            self.__msg .attach(filename="", content_type="",data=file)

    def send(self, subject, recipients, body, ishtml=False, attachements=None, sender=None, sendername=None):
        if not sender:
            sender = app_param['MAIL_USERNAME']
            sendername = app_param['MAIL_NAME']
        self.__msg = Message(subject, sender=(sendername, sender), recipients=recipients, html=ishtml)
        self.__msg.body = body
        if attachements:
            self.normalize_attach(attachements)
        init_app.mail.send(self.__msg)

