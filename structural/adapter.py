from typing import Callable


def execute_function(func: Callable):
    try:
        func()
    except Exception as err:
        print(err)


def execute_function_adapter(other_func: Callable, message: str):
    def func():
        return other_func(message)

    execute_function(func)


def handler():
    print("Message")


def message_handler(message: str):
    print(f"Message: {message}")


if __name__ == "__main__":
    execute_function(handler)
    execute_function_adapter(message_handler, "Hello")
