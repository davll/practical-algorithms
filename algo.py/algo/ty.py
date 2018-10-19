from typing import Any, TypeVar
from abc import ABCMeta, abstractmethod

#T = TypeVar('T', bound='Comparable')

class Comparable(metaclass = ABCMeta):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass
    def __gt__(self, other: Any) -> bool:
        return (not self < other) and self != other
    def __le__(self, other: Any) -> bool:
        return self < other or self == other
    def __ge__(self, other: Any) -> bool:
        return (not self < other)
