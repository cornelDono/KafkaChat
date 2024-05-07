from abc import ABC
from copy import copy
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from domain.events.base import BaseEvent


@dataclass(kw_only=True)
class BaseEntity(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
    )
    created_at: datetime = field(
        default_factory=datetime.now,
    )
    _events: list[BaseEvent] = field(default_factory=list)

    def register_event(self, event: BaseEvent) -> None:
        self._events.append(event)

    def pull_events(self) -> list[BaseEvent]:
        registered_events = copy(self._events)
        self._events.clear()

        return registered_events

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid
