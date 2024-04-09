from abc import ABC, abstractmethod
import time


class DataStorage(ABC):
    @abstractmethod
    def get_value(self) -> int:
        raise NotImplementedError()


class RealDataStorage(DataStorage):
    def get_value(self) -> int:
        time.sleep(2)
        return 100


class ProxyDataStorage(DataStorage):
    _cached_value: int
    _real_storage: DataStorage

    def __init__(self, real_storage: DataStorage):
        self._cached_value = None
        self._real_storage = real_storage

    def get_value(self) -> int:
        if self._cached_value is not None:
            return self._cached_value

        value = self._real_storage.get_value()
        self._cached_value = value

        return value


class ValueService:
    _storage: DataStorage

    def __init__(self, storage: DataStorage):
        self._storage = storage

    def fetch_value(self) -> int:
        return self._storage.get_value()


if __name__ == "__main__":
    value_service = ValueService(ProxyDataStorage(RealDataStorage()))

    value = value_service.fetch_value()
    print(value)  # First call involves a delayed response

    value = value_service.fetch_value()
    print(value)  # Subsequent calls retrieve from cache, faster
