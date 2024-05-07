from abc import ABC
from dataclasses import dataclass
from typing import Any, Generic, TypeVar


VT = TypeVar('VT', bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self.validate()

    @classmethod
    def validate(self):
        ...

    @classmethod
    def as_generic_type(self) -> VT:
        ...
