from abc import ABC, abstractmethod
from typing import List


class Job:
    def __init__(self, title):
        self.title = title


class Observer(ABC):
    @abstractmethod
    def receive_notify(self, job: Job):
        raise NotImplementedError()


class Developer(Observer):
    def receive_notify(self, job: Job):
        print(f"Many thanks, I've received job: {job.title}")


class ITJobsCompany:
    _jobs: List[Job]
    _observers: List[Developer]

    def __init__(self):
        self._jobs = []
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, job: Job):
        for observer in self._observers:
            observer.receive_notify(job)

    def add_new_job(self, job: Job):
        self._jobs.append(job)
        self.notify_observers(job)


if __name__ == "__main__":
    it_company = ITJobsCompany()
    developer = Developer()

    # Add developer as an observer
    it_company.add_observer(developer)

    # Notify developer about new jobs
    it_company.add_new_job(Job("Senior Go backend engineer"))
    it_company.add_new_job(Job("Junior React developer"))

    # Remove developer, they won't receive further notifications
    it_company.remove_observer(developer)

    it_company.add_new_job(Job("Some boring IT job"))
