from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class EventHandlersNotRegisteredException(LogicException):
    event_type: str

    @property
    def message(self):
        f"Not handlers for event: {self.event_type}"



@dataclass(frozen=True, eq=False)
class CommandHandlersNotRegisteredException(LogicException):
    command_type: str

    @property
    def message(self):
        f"Not handlers for command: {self.command_type}"