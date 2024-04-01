from abc import ABC, abstractmethod


class IMilkTea(ABC):
    def cost(self) -> float:
        raise NotImplementedError()


class MilkTea(IMilkTea):
    _price: float = 5.0

    def cost(self) -> float:
        return self._price


class MilkTeaDecorator(IMilkTea):
    _milk_tea: IMilkTea

    def __init__(self, milk_tea: IMilkTea):
        self._milk_tea = milk_tea

    def cost(self) -> float:
        return self._milk_tea.cost()


class WhiteBubbleDecorator(MilkTeaDecorator):
    _price: float = 1.5

    def __init__(self, milk_tea: IMilkTea):
        super().__init__(milk_tea)

    def cost(self) -> float:
        return self._price + super().cost()


class FruitPuddingDecorator(MilkTeaDecorator):
    _price: float = 3.0

    def __init__(self, milk_tea: IMilkTea):
        super().__init__(milk_tea)

    def cost(self) -> float:
        return self._price + super().cost()


class EggPuddingDecorator(MilkTeaDecorator):
    _price: float = 3.0

    def __init__(self, milk_tea: IMilkTea):
        super().__init__(milk_tea)

    def cost(self) -> float:
        return self._price + super().cost()


class BubbleDecorator(MilkTeaDecorator):
    _price: float = 1.0

    def __init__(self, milk_tea: IMilkTea):
        super().__init__(milk_tea)

    def cost(self) -> float:
        return self._price + super().cost()


class BlackSugarDecorator(MilkTeaDecorator):
    _price: float = 2.0

    def __init__(self, milk_tea: IMilkTea):
        super().__init__(milk_tea)

    def cost(self) -> float:
        return self._price + super().cost()


if __name__ == "__main__":
    milk_tea_1 = MilkTea()
    milk_tea_1 = EggPuddingDecorator(milk_tea_1)
    milk_tea_1 = FruitPuddingDecorator(milk_tea_1)
    milk_tea_1 = BlackSugarDecorator(milk_tea_1)
    milk_tea_1 = BubbleDecorator(milk_tea_1)
    print(
        f"Cost of milkTea with egg pudding, fruit pudding, black sugar, bubble: {milk_tea_1.cost()}"
    )

    milk_tea_2 = MilkTea()
    milk_tea_2 = EggPuddingDecorator(milk_tea_2)
    milk_tea_2 = BlackSugarDecorator(milk_tea_2)
    milk_tea_2 = WhiteBubbleDecorator(milk_tea_2)
    print(
        f"Cost of milkTea with egg pudding, black sugar, white bubble: {milk_tea_2.cost()}"
    )
