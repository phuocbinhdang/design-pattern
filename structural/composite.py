from __future__ import annotations
from typing import List


class Item:
    def cost(self) -> float:
        raise NotImplementedError()


class Product(Item):
    _name: str
    _price: float

    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def cost(self) -> float:
        return self._price


class Box(Item):
    _children: List[Item]

    def __init__(self, children: List[Item]):
        self._children = children

    def cost(self) -> float:
        return sum(item.cost() for item in self._children)


if __name__ == "__main__":
    box = Box(
        [
            Product("Mouse", 20.5),
            Box(
                [
                    Product("Keyboard", 60),
                    Product("Charger", 15),
                ]
            ),
        ]
    )

    print(box.cost())
