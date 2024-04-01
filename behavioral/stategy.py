from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(message: str):
        raise NotImplementedError()


class EmailNotifier(Notifier):
    _email: str

    def __init__(self, email):
        self._email = email

    def send(self, message: str):
        print(f"Sending to email {self._email}: {message}")


class SMSNotifier(Notifier):
    _phone_number: str

    def __init__(self, phone_number: str):
        self._phone_number = phone_number

    def send(self, message: str):
        print(f"Sending to phone {self._phone_number}: {message}")


class BanAccountService:
    _notifier: Notifier

    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def execute(self):
        self._notifier.send("You are baned")


if __name__ == "__main__":
    service = BanAccountService(notifier=EmailNotifier(email="you@example.com"))
    service.execute()

    service = BanAccountService(notifier=SMSNotifier(phone_number="0123456789"))
    service.execute()
