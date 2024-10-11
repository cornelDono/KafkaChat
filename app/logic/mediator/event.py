from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable, List

from domain.events.base import BaseEvent
from infra.message_brokers.base import BaseMessageBroker
from logic.events.base import ER, ET, EventHandler


@dataclass(frozen=True)
class EventMediator(ABC):
    events_map: dict[ET, List[EventHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    message_broker: BaseMessageBroker

    @abstractmethod
    def register_event(self, event: ET, event_handlers: Iterable[EventHandler[ET, ER]]) -> None:
        ...
    
    @abstractmethod
    async def publish(self, events: Iterable[BaseEvent]) -> Iterable[ER]:
        ...
