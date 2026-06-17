from abc import ABC, abstractmethod

class Sender(ABC):
    @abstractmethod
    def sends(self):
        pass
class Template(ABC):
    @abstractmethod
    def templates(self):
        pass

class EmailSender(Sender):
    def sends(self):
        return f"Email has sent !"
class EmalilTemplates(Template):
    def templates(self):
        return f"email template has built"

class SMSsender(Sender):
    def sends(self):
        return f"sms has sent"
class SMSTemplate(Template):
    def templates(self):
        return f"sms template has built"
    
    
class NotificationSystem(ABC):
    @abstractmethod
    def create_sender(self):
        pass
    @abstractmethod
    def create_template(self):
        pass
    
class EmailFactory(NotificationSystem):
    def create_sender(self):
        return EmailSender()
    def create_template(self):
        return EmalilTemplates()
class SMSFactory(NotificationSystem):
    def create_sender(self):
        return SMSsender()
    def create_template(self):
        return SMSTemplate()
    
factory_email=EmailFactory()
sendss=factory_email.create_sender()
templatess=factory_email.create_template()
print(sendss.sends())
print(templatess.templates())

factory_sms=SMSFactory()
sendsms=factory_sms.create_sender()
templatesms=factory_sms.create_template()
print(sendsms.sends())
print(templatesms.templates())   
    
       