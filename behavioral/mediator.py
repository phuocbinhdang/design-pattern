from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import threading
import time


class Airplane(ABC):
    @abstractmethod
    def request_take_off(self):
        raise NotImplementedError()

    @abstractmethod
    def request_lane(self):
        raise NotImplementedError()

    @abstractmethod
    def take_off(self, runway: int):
        raise NotImplementedError()

    @abstractmethod
    def land(self, runway: int):
        raise NotImplementedError()


class CommercialAirplane(Airplane):
    _aircraft_number: str
    _mediator: AirTrafficControlTower

    def __init__(self, aircraft_number: str, mediator: AirTrafficControlTower):
        self._aircraft_number = aircraft_number
        self._mediator = mediator

    def request_take_off(self):
        self._mediator.request_take_off(self)

    def request_lane(self):
        self._mediator.request_lane(self)

    def take_off(self, runway: int):
        print(f"{self._aircraft_number} takes off on runway: {runway}")
        time.sleep(2)

    def land(self, runway: int):
        print(f"{self._aircraft_number} lands on runway: {runway}")
        time.sleep(2)


class AirTrafficControlTower(ABC):
    @abstractmethod
    def request_take_off(self, airplane: Airplane):
        raise NotImplementedError()

    @abstractmethod
    def request_lane(self, airplane: Airplane):
        raise NotImplementedError()


class AirportControlTower(AirTrafficControlTower):
    _runway: List[int]

    def __init__(self):
        self._runway = [1, 2, 3]

    def request_take_off(self, airplane: Airplane):
        if self._runway:
            runway = self._runway.pop(0)
            airplane.take_off(runway)
            self._runway.append(runway)
            return

        time.sleep(2)
        self.request_take_off(airplane)

    def request_lane(self, airplane: Airplane):
        if self._runway:
            runway = self._runway.pop(0)
            airplane.land(runway)
            self._runway.append(runway)
            return

        time.sleep(2)
        self.request_lane(airplane)


if __name__ == "__main__":
    control_tower = AirportControlTower()

    airplane1 = CommercialAirplane("AP0001", control_tower)
    airplane2 = CommercialAirplane("AP0002", control_tower)
    airplane3 = CommercialAirplane("AP0003", control_tower)
    airplane4 = CommercialAirplane("AP0004", control_tower)
    airplane5 = CommercialAirplane("AP0005", control_tower)

    t1 = threading.Thread(target=airplane1.request_take_off)
    t2 = threading.Thread(target=airplane2.request_take_off)
    t3 = threading.Thread(target=airplane3.request_lane)
    t4 = threading.Thread(target=airplane4.request_lane)
    t5 = threading.Thread(target=airplane5.request_take_off)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
