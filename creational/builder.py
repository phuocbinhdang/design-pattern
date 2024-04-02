from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self):
        raise NotImplementedError()


class StdLogger(Logger):
    def log(self):
        print("Write log to std")


class FileLogger(Logger):
    def log(self):
        print("Write log to file")


class Notifier(ABC):
    @abstractmethod
    def send(self):
        raise NotImplementedError()


class EmailNotifier(Notifier):
    def send(self):
        print("Send notification to email")


class SMSNotifier(Notifier):
    def send(self):
        print("Send notification to SMS")


class DataLayer(ABC):
    @abstractmethod
    def save(self):
        raise NotImplementedError()


class MySQLDataLayer(DataLayer):
    def save(self):
        print("Save data to MySQL")


class MongoDataLayer(DataLayer):
    def save(self):
        print("Save data to Mongo")


class Uploader(ABC):
    @abstractmethod
    def upload(self):
        raise NotImplementedError()


class AWSS3Uploader(Uploader):
    def upload(self):
        print("Upload to AWS S3")


class GoogleDriveUploader(Uploader):
    def upload(self):
        print("Upload to Google Drive")


class Service:
    _name: str
    _logger: Logger
    _notifier: Notifier
    _data_layer: DataLayer
    _uploader: Uploader

    def __init__(
        self,
        name: str | None,
        logger: Logger | None,
        notifier: Notifier | None,
        data_layer: DataLayer,
        uploader: Uploader,
    ):
        self._name = name
        self._logger = logger
        self._notifier = notifier
        self._data_layer = data_layer
        self._uploader = uploader

    def do_business(self):
        print(f"{self._name if self._name else 'Some Service' } Do Business")

        if self._logger:
            self._logger.log()

        self._uploader.upload()
        self._data_layer.save()

        if self._notifier:
            self._notifier.send()


class Builder:
    _name: str
    _logger: Logger
    _notifier: Notifier
    _data_layer: DataLayer
    _uploader: Uploader

    def reset(self):
        self._name = None
        self._logger = None
        self._notifier = None
        self._data_layer = None
        self._uploader = None

    def set_name(self, name: str):
        self._name = name

    def set_logger(self, logger: Logger):
        self._logger = logger

    def set_notifier(self, notifier: Notifier):
        self._notifier = notifier

    def set_data_layer(self, data_layer):
        self._data_layer = data_layer

    def set_uploader(self, uploader):
        self._uploader = uploader

    def build(self) -> Service:
        return Service(
            name=self._name,
            logger=self._logger,
            notifier=self._notifier,
            data_layer=self._data_layer,
            uploader=self._uploader,
        )


class Director:
    _builder: Builder = Builder()

    def build_simple_service(self) -> Service:
        self._builder.reset()
        self._builder.set_data_layer(MySQLDataLayer())
        self._builder.set_uploader(AWSS3Uploader())

        return self._builder.build()

    def build_complex_service(self) -> Service:
        self._builder.reset()
        self._builder.set_name("Complex Service")
        self._builder.set_logger(StdLogger())
        self._builder.set_notifier(EmailNotifier())
        self._builder.set_data_layer(MongoDataLayer())
        self._builder.set_uploader(GoogleDriveUploader())

        return self._builder.build()


if __name__ == "__main__":
    builder = Builder()
    builder.reset()
    builder.set_name("My Service")
    builder.set_logger(FileLogger())
    builder.set_notifier(SMSNotifier())
    builder.set_data_layer(MySQLDataLayer())
    builder.set_uploader(AWSS3Uploader())
    service = builder.build()
    service.do_business()

    print("=============================================")

    director = Director()
    simple_serivice = director.build_simple_service()
    simple_serivice.do_business()

    print("=============================================")

    complex_serivice = director.build_complex_service()
    complex_serivice.do_business()
