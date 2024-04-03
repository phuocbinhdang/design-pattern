from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_product(self, product: Product):
        raise NotImplementedError()

    @abstractmethod
    def visit_category(self, category: Category):
        raise NotImplementedError()

    @abstractmethod
    def visit_user(self, user: User):
        raise NotImplementedError()


class PrinterVisitor(Visitor):
    def visit_product(self, product: Product):
        print(f"Print product: {product._name}")

    def visit_category(self, category: Category):
        print(f"Print category: {category._title}")

    def visit_user(self, user: User):
        print(f"Print user: {user._first_name} {user._last_name}")


class LoggerVisitor(Visitor):
    def visit_product(self, product: Product):
        print(f"Log product: {product._name}")

    def visit_category(self, category: Category):
        print(f"Log category: {category._title}")

    def visit_user(self, user: User):
        print(f"Log user: {user._first_name} {user._last_name}")


class Visitable(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        raise NotImplementedError()


class Category(Visitable):
    _title: str

    def __init__(self, title: str):
        self._title = title

    def accept(self, visitor: Visitor):
        visitor.visit_category(self)


class Product(Visitable):
    _name: str

    def __init__(self, name: str):
        self._name = name

    def accept(self, visitor: Visitor):
        visitor.visit_product(self)


class User(Visitable):
    _first_name: str
    _last_name: str

    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    def accept(self, visitor: Visitor):
        visitor.visit_user(self)


if __name__ == "__main__":
    items: list[Visitable] = [
        Category(title="Programming"),
        Product(name="Visitor Design Pattern"),
        User(first_name="Hello", last_name="World"),
    ]

    printer_visitor = PrinterVisitor()

    for item in items:
        item.accept(printer_visitor)

    print("=========================================")

    logger_visitor = LoggerVisitor()

    for item in items:
        item.accept(logger_visitor)
