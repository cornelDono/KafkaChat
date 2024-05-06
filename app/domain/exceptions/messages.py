from dataclasses import dataclass

from domain.exceptions.base import ApplciationException


@dataclass(frozen=True, eq=False)
class TextTooLongException(ApplciationException):
    text: str

    @property
    def message(self):
        return f'Text Message is too long: {self.text[:255]}...'