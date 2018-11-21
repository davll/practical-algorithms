from abc import abstractmethod, ABCMeta
from typing import TypeVar, Any

class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        return False
    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        return False
    @abstractmethod
    def __le__(self, other: Any) -> bool:
        return False
    @abstractmethod
    def __ge__(self, other: Any) -> bool:
        return False
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        return False
    @abstractmethod
    def __ne__(self, other: Any) -> bool:
        return False
