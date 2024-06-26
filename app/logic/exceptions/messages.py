from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class ChatWithThatTitleAlreadyExistsException(LogicException):
    title: str

    @property
    def message(self):
        return f"Chat with title '{self.title}' already exists"


@dataclass(frozen=True, eq=False)
class ChatNotFoundException(LogicException):
    chat_oid: str

    @property
    def message(self):
        return f"Chat with {self.chat_oid=} not found"
