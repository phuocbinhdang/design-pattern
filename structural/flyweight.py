from typing import List, Dict


class Sender:
    _name: str
    _avatar: bytes

    def __init__(self, name: str, avatar: bytes):
        self._name = name
        self._avatar = avatar


class ChatMessage:
    _content: str
    _sender: Sender

    def __init__(self, content: str, sender: Sender):
        self._content = content
        self._sender = sender


class SenderFlyweight:
    _cache_sender: Dict[str, Sender]

    def __init__(self):
        self.cache_sender = {}

    def set_sender(self, name: str, sender: Sender):
        self.cache_sender[name] = sender

    def get_sender(self, name: str) -> Sender:
        if name not in self.cache_sender:
            raise Exception(f"Sender with name '{name}' not found in cache")

        return self.cache_sender[name]


if __name__ == "__main__":
    sender_factory = SenderFlyweight()
    sender_factory.set_sender("Peter", Sender("Peter", bytearray(1024 * 300)))  # 300kb
    sender_factory.set_sender("Mary", Sender("Mary", bytearray(1024 * 400)))  # 400kb

    chat_messages_with_flyweight: List[ChatMessage] = [
        ChatMessage("Hi", sender_factory.get_sender("Peter")),
        ChatMessage("Oh here you are", sender_factory.get_sender("Mary")),
        ChatMessage("What are you doing?", sender_factory.get_sender("Peter")),
        ChatMessage("I'm fishing", sender_factory.get_sender("Mary")),
        ChatMessage("I'm relaxing", sender_factory.get_sender("Mary")),
    ]  # over 700kb

    chat_messages_without_flyweight: List[ChatMessage] = [
        ChatMessage("Hi", Sender("Peter", bytearray(1024 * 300))),
        ChatMessage("Oh here you are", Sender("Mary", bytearray(1024 * 400))),
        ChatMessage("What are you doing?", Sender("Peter", bytearray(1024 * 300))),
        ChatMessage("I'm fishing", Sender("Mary", bytearray(1024 * 400))),
        ChatMessage("I'm relaxing", Sender("Mary", bytearray(1024 * 400))),
    ]  # over 1800kb
