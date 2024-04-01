from threading import Lock, Thread
from uuid import uuid4, UUID
from typing import Dict, Any


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Repository(metaclass=SingletonMeta):
    _id: UUID

    def __init__(self, id: UUID):
        self._id = id


def test_singleton_repository(id: UUID):
    repository = Repository(id)
    print(repository._id)


if __name__ == "__main__":
    process1 = Thread(target=test_singleton_repository, args=(uuid4(),))
    process2 = Thread(target=test_singleton_repository, args=(uuid4(),))
    process1.start()
    process2.start()
