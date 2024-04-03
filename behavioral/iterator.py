from __future__ import annotations
from typing import List, Any


class Follower:
    _name: str

    def __init__(self, name: str):
        self._name = name

    def receive(self, message: str):
        print(f"{self._name} has received message: {message}")


class Iterator:
    def __iter__(self):
        raise NotImplementedError()

    def __next__(self):
        raise StopIteration()


class ArrayIterator(Iterator):
    _data: List[Any]
    _current_index: int

    def __init__(self, data: List[Any]):
        self._data = data
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index >= len(self._data):
            raise StopIteration()

        current_data = self._data[self._current_index]
        self._current_index += 1

        return current_data


class LinkedNode:
    _node: Any
    _next: Any | None

    def __init__(self, note: Any, next: Any | None = None):
        self._node = note
        self._next = next


class LinkedListIterator(Iterator):
    _current: LinkedNode

    def __init__(self, head):
        self._current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration()

        current_data = self._current._node
        self._current = self._current._next

        return current_data


class TreeNode:
    _root: Any
    _children: List[TreeNode]

    def __init__(self, root: Any, children: List[TreeNode] = []):
        self._root = root
        self._children = children


class TreeNodeIterator(Iterator):
    _data: List[Any]
    _current_index: int

    def __init__(self, tree_node: TreeNode):
        self._data = self.to_array(tree_node)
        self._current_index = 0

    def to_array(self, tree_node: TreeNode):
        data = [tree_node._root]
        for child in tree_node._children:
            data.extend(self.to_array(child))

        return data

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index >= len(self._data):
            raise StopIteration()

        current_data = self._data[self._current_index]
        self._current_index += 1

        return current_data


def send_message(iterator, message):
    for follower in iterator:
        follower.receive(message)


if __name__ == "__main__":
    message = "Hello"

    array_follower = [Follower(name) for name in ["Peter", "Mana", "Tom", "Henry"]]
    iterator = ArrayIterator(array_follower)

    for follower in iterator:
        follower.receive(message)

    print("============================================")

    linked_list_follower = LinkedNode(
        Follower("Meg"), LinkedNode(Follower("Tom"), LinkedNode(Follower("Thomas")))
    )

    iterator = LinkedListIterator(linked_list_follower)

    for follower in iterator:
        follower.receive(message)

    print("============================================")

    tree_follower = TreeNode(
        Follower("Vicky"),
        [
            TreeNode(
                Follower("Orgy"),
                [
                    TreeNode(Follower("Mary")),
                    TreeNode(Follower("Vincent")),
                    TreeNode(Follower("Chavis")),
                ],
            ),
            TreeNode(Follower("Bob"), [TreeNode(Follower("Alice"))]),
        ],
    )

    iterator = TreeNodeIterator(tree_follower)

    for follower in iterator:
        follower.receive(message)
