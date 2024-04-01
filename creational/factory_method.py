from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def set_destination(destination: str):
        pass

    @abstractmethod
    def send(message: str):
        pass


class EmailNotifier(Notifier):
    _email: str

    def set_destination(self, destination):
        self._email = destination

    def send(self, message: str):
        print("Sending Notification")
        print(f"Email: {self._email}")
        print(f"{message}")


class SMSNotifier(Notifier):
    _phone_number: str

    def set_destination(self, destination):
        self._phone_number = destination

    def send(self, message: str):
        print("Sending Notification")
        print(f"Phone number: {self._phone_number}")
        print(f"{message}")


class NotifierFactory:
    def create(self, type) -> Notifier:
        if type == "sms":
            return SMSNotifier()

        if type == "email":
            return EmailNotifier()

        raise Exception(f"Type {type} notifier not support")


class BanAccountService:
    _notifier: Notifier

    def __init__(self, notifier):
        self._notifier = notifier

    def execute(self, reason):
        message: str = f"Message: You are baned\nReason: {reason}"
        self._notifier.send(message)


if __name__ == "__main__":
    notifier_factory = NotifierFactory()
    notifier: Notifier = notifier_factory.create("sms")
    notifier.set_destination("0123456789")

    service: BanAccountService = BanAccountService(notifier=notifier)

    service.execute("Used 3rd party software")
