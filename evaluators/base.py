from abc import ABC, abstractmethod

class Evaluator(ABC):
    name: str

    @abstractmethod
    def __call__(self, sample: dict) -> float:
        pass
