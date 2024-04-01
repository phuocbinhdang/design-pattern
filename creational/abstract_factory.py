from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def drink(self):
        pass


class Food(ABC):
    @abstractmethod
    def eat(self):
        pass


class Voucher(Drink, Food):
    _dink: Drink
    _food: Food

    def __init__(self, drink: Drink, food: Food):
        self._drink = drink
        self._food = food

    def drink(self):
        self._drink.drink()

    def eat(self):
        self._food.eat()


class Coffee(Drink):
    def drink(self):
        print("It's coffee, drinkable")


class Beer(Drink):
    def drink(self):
        print("It's beer, drinkable")


class Cake(Food):
    def eat(self):
        print("It's cake, eatable")


class GrilledOctopus(Food):
    def eat(self):
        print("It's grilled octopus, eatable")


class VoucherAbstractFactory(ABC):
    @abstractmethod
    def get_drink(self) -> Drink:
        pass

    @abstractmethod
    def get_food(self) -> Food:
        pass


class MorningVoucherFactory(VoucherAbstractFactory):
    def get_drink(self) -> Drink:
        return Coffee()

    def get_food(self) -> Food:
        return Cake()


class EveningVoucherFactory(VoucherAbstractFactory):
    def get_drink(self) -> Drink:
        return Beer()

    def get_food(self) -> Food:
        return GrilledOctopus()


if __name__ == "__main__":
    voucher_factory: VoucherAbstractFactory = MorningVoucherFactory()
    voucher_factory.get_drink().drink()
    voucher_factory.get_food().eat()

    voucher_factory: VoucherAbstractFactory = EveningVoucherFactory()
    voucher_factory.get_drink().drink()
    voucher_factory.get_food().eat()
