from config.settings import init_app, Message, app_param

class MaillingService():
    def __init__(self, subject, recipients, body, ishtml = False, attachements = None,sender= None):
        if not sender:
            sender = app_param['MAIL_USERNAME']
        self.__msg = Message(subject, sender=sender, recipients=recipients, html = ishtml)
        self.__msg .body = body
        if attachements:
            self.normalize_attach(attachements)

    def normalize_attach(self, attachements):
        files = []
        for file in attachements:
            self.__msg .attach(filename="", content_type="",data=file)

    def send(self):
        init_app.mail.send(self.__msg)

