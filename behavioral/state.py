from __future__ import annotations
from abc import ABC, abstractmethod

"""
Flow Order State  

[Start] --> Created --> Cancelled --> [End]
			    |
				|
				Paid --> Delivered --> Finished --> [End]
"""


class OrderState(ABC):
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError()

    def cancel(self):
        raise Exception("Invalid action")

    def pay(self):
        raise Exception("Invalid action")

    def deliver(self):
        raise Exception("Invalid action")

    def finish(self):
        raise Exception("Invalid action")


class OrderStateCreated(OrderState):
    _order: Order

    def __init__(self, order: Order):
        self._order = order

    def cancel(self):
        self._order.update_state(OrderStateCancelled(self._order))

    def pay(self):
        self._order.update_state(OrderStatePaid(self._order))

    def __str__(self) -> str:
        return "Created"


class OrderStateCancelled(OrderState):
    _order: Order

    def __init__(self, order: Order):
        self._order = order

    def __str__(self) -> str:
        return "Cancelled"


class OrderStatePaid(OrderState):
    _order: Order

    def __init__(self, order: Order):
        self._order = order

    def deliver(self):
        self._order.update_state(OrderStateDelivered(self._order))

    def __str__(self) -> str:
        return "Paid"


class OrderStateDelivered(OrderState):
    _order: Order

    def __init__(self, order: Order):
        self._order = order

    def finish(self):
        self._order.update_state(OrderStateFinished(self._order))

    def __str__(self) -> str:
        return "Delivered"


class OrderStateFinished(OrderState):
    _order: Order

    def __init__(self, order: Order):
        self._order = order

    def __str__(self) -> str:
        return "Finished"


class Order:
    _state: OrderState

    def __init__(self):
        self._state: OrderState = OrderStateCreated(self)

    def update_state(self, state: OrderState):
        self._state = state
        print(f"Order has changed state to: {state}")

    def current_state(self) -> OrderState:
        return self._state

    def cancel(self):
        self._state.cancel()

    def pay(self):
        self._state.pay()

    def deliver(self):
        self._state.deliver()

    def finish(self):
        self._state.finish()


if __name__ == "__main__":
    order = Order()
    order.pay()
    order.deliver()
    order.finish()

    print("===========================")

    order_2 = Order()
    order_2.cancel()

    print("===========================")

    order_3 = Order()
    order_3.deliver()  # will be error
