from __future__ import annotations
from typing import List


class Point:
    _x: int
    _y: int

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def clone(self) -> Point:
        """Creates a shallow copy of the Point object."""
        return Point(self._x, self._y)


class Node:
    _value: Point
    _children: List[Point]

    def __init__(self, value, children):
        self._value = value
        self._children = children

    def clone(self) -> Node:
        """Creates a deep copy of the Node object and its children."""
        children_clone = [child.clone() for child in self._children]
        return Node(self._value.clone(), children_clone)


if __name__ == "__main__":
    # Case 1: Clone without prototype design pattern
    p1 = Point(1, 2)
    p2 = p1
    p1._x = 3
    print(p1.__dict__, p2.__dict__)  # Output should be: (3, 2) (1, 2)

    # Case 2: Clone with prototype design pattern
    p3 = Point(1, 2)
    p4 = p3.clone()

    p3._x = 3
    print(p3.__dict__, p4.__dict__)  # Output should be: (3, 2) (1, 2)

    n1 = Node(Point(5, 6), [Point(1, 2), Point(2, 3)])
    n2 = n1.clone()

    n1._children[0]._x = 10
    print(n1._children[0]._x, n2._children[0]._x)  # Output should be: 10 1
