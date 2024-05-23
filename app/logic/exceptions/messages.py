from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class ChatWithThatTitleAlreadyExistsExeption(LogicException):
    title: str

    @property
    def message(self):
        return f"Chat with title {self.title} already exists"
