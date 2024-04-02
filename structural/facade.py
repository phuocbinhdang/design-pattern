from typing import List


class Product:
    _name: str
    _price: float

    def __init__(self, name, price):
        self._name = name
        self._price = price


class Inventory:
    _product: List[Product]

    def __init__(self):
        self._product = [
            Product("Apple", 2.5),
            Product("Orange", 3.0),
        ]

    def lookup(self, name) -> Product | None:
        for product in self._product:
            if product._name == name:
                return product

        return None


class Account:
    _name: str
    _balance: float

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, money):
        self._balance += money

    def withdraw(self, money):
        if money >= self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= money

    def get_balance(self) -> float:
        return self._balance


class AccountStorage:
    _accounts: List[Account]

    def __init__(self):
        self._accounts = [
            Account("Meg", 1000),
            Account("Tom", 300),
        ]

    def lookup(self, name) -> Account | None:
        for account in self._accounts:
            if account._name == name:
                return account

        return None


class FacadeService:
    _account_storage: AccountStorage
    _inventory: Inventory

    def __init__(self):
        self._account_storage = AccountStorage()
        self._inventory = Inventory()

    def buy_product(self, name, account_name):
        product = self._inventory.lookup(name)
        if not product:
            raise ValueError("Product not found")

        account = self._account_storage.lookup(account_name)
        if not account:
            raise ValueError("Account not found")

        if account.get_balance() < product._price:
            raise ValueError("Insufficient funds")

        account.withdraw(product._price)

    def deposit(self, account_name, money):
        account = self._account_storage.lookup(account_name)
        if not account:
            raise ValueError("Account not found")

        account.deposit(money)

    def fetch_balance(self, account_name):
        account = self._account_storage.lookup(account_name)
        if not account:
            raise ValueError("Account not found")

        return account.get_balance()


if __name__ == "__main__":
    service = FacadeService()

    # Case 1: Buy a product with an account
    product_name = "Apple"
    account_name = "Meg"
    try:
        service.buy_product(product_name, account_name)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Account Balance: {service.fetch_balance(account_name)}")

    # Case 2: Deposit 100 into VIP Account
    try:
        service.deposit(account_name, 100)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Account Balance: {service.fetch_balance(account_name)}")
