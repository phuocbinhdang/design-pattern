from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(message: str):
        pass


class EmailNotifier(Notifier):
    _email: str

    def __init__(self, email):
        self._email = email

    def send(self, message: str):
        print("Sending Notification")
        print(f"Email: {self._email}")
        print(f"{message}")


class SMSNotifier(Notifier):
    _phone_number: str

    def __init__(self, phone_number):
        self._phone_number = phone_number

    def send(self, message: str):
        print("Sending Notification")
        print(f"Phone number: {self._phone_number}")
        print(f"{message}")


class BanAccountService:
    _notifier: Notifier

    def __init__(self, notifier):
        self._notifier = notifier

    def execute(self, reason):
        message: str = f"Message: You are baned\nReason: {reason}"
        self._notifier.send(message)


if __name__ == "__main__":
    service: BanAccountService = BanAccountService(
        notifier=EmailNotifier(email="you@example.com")
    )

    service.execute("Used 3rd party software")

    service: BanAccountService = BanAccountService(
        notifier=SMSNotifier(phone_number="0123456789")
    )

    service.execute("Used 3rd party software")
