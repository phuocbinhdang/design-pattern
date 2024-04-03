from abc import ABC, abstractmethod


class Data:
    pass


class DataParser(ABC):
    @abstractmethod
    def parse(self) -> Data:
        raise NotImplementedError()


class MySQLParser(DataParser):
    def parse(self) -> Data:
        return {"data": "mysql"}


class MongoParser(DataParser):
    def parse(self):
        return {"data": "mongo"}


class FileParser(DataParser):
    def parse(self):
        return {"data": "file"}


class DataPersistent(ABC):
    @abstractmethod
    def save(self, data: Data):
        raise NotImplementedError()


class JSONFilePersistent(DataPersistent):
    def save(self, data: Data):
        print(f"Save {data} to JSON File")


class RPCServicePersistent(DataPersistent):
    def save(self, data: Data):
        print(f"Save {data} to RPC Service")


class AWSS3Persistent(DataPersistent):
    def save(self, data: Data):
        print(f"Save {data} to AWS S3")


class Bridge:
    def parse_and_save_data(self, parser: DataParser, storage: DataPersistent):
        data = parser.parse()
        storage.save(data)


# Usage

if __name__ == "__main__":
    bridge = Bridge()
    bridge.parse_and_save_data(MySQLParser(), JSONFilePersistent())
    bridge.parse_and_save_data(MongoParser(), RPCServicePersistent())
    bridge.parse_and_save_data(FileParser(), AWSS3Persistent())
