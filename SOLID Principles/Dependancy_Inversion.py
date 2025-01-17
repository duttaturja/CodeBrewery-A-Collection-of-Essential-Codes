#Dependancey Inversion Principle
class NotificationService:
    def send(self, message):
        pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"sending email: {message}")

class Notification:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send(message)

#usage
email_service = EmailService()
notification = Notification(email_service)
notification.notify("Hello!")