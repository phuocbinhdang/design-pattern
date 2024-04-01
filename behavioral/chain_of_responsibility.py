from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List, Dict


class Context:
    _url: str
    _content: str
    _data: Dict[str, Any]

    def __init__(self, url, content: str = None, data: Dict[str, Any] = None):
        self._url = url
        self._content = content
        self._data = data


class Handler(ABC):
    @abstractmethod
    def execute(self, context: Context):
        raise NotImplementedError()


class CheckingUrlHandler(Handler):
    def execute(self, context: Context):
        print(f"Checking url: {context._url}")


class FetchContentHandler(Handler):
    def execute(self, context: Context):
        print(f"Fetching content from url: {context._url}")
        context._content = "some content from url"


class ExtractDataHandler(Handler):
    def execute(self, context: Context):
        print(f"Extracting data from content: {context._content}")
        context._data = {
            "title": "Apple",
            "price": 10.0,
        }


class SaveDataHandler(Handler):
    def execute(self, context: Context):
        print(f"Saving data to database: {context._data}")


class HandlerStorage:
    _handlers: List[Handler] = []

    def add(self, handler: Handler):
        self._handlers.append(handler)

    def execute(self, url: str):
        context = Context(url)

        for handler in self._handlers:
            handler.execute(context)

        print(f"Context: {context.__dict__}")


class WebCrawler:
    def __init__(self, handle_storage: HandlerStorage):
        self.handle_storage = handle_storage

    def crawl(self, url: str):
        self.handle_storage.execute(url)


if __name__ == "__main__":
    handle_storage = HandlerStorage()
    handle_storage.add(CheckingUrlHandler())
    handle_storage.add(FetchContentHandler())
    handle_storage.add(ExtractDataHandler())
    handle_storage.add(SaveDataHandler())

    crawler = WebCrawler(handle_storage)
    crawler.crawl("https://some-rich-content-website/some-page")
