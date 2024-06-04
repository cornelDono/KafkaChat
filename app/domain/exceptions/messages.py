from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Text Message is too long: {self.text[:255]}...'


@dataclass(frozen=True, eq=False)
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return f'Text is empty'