
from abc import ABC, abstractmethod


class Student(ABC):

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def write_exams(self):
        pass

    def attend_class(self):
        print("Attending...")


class HighSchoolStudent(Student):

    def study(self):
        print("Studying...")

    def write_exams(self):
        print("Writing...")
