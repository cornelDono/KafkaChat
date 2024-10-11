from abc import abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable, List

from domain.events.base import BaseEvent
from logic.commands.base import CR, CT, BaseCommand, CommandHandler
from logic.events.base import ER, ET, EventHandler
from logic.exceptions.mediator import CommandHandlersNotRegisteredException, EventHandlersNotRegisteredException
from logic.queries.base import QR, QT, BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class QueryMediator:
    queries_map: dict[QT, BaseQueryHandler] = field(
        default_factory=dict,
        kw_only=True,
    )
    
    @abstractmethod
    def register_query(self, query: QT, query_handler: BaseQueryHandler[QT, QR]) -> QR:
        ...

    @abstractmethod
    async def handle_query(self, query: BaseQuery) -> QR:
        ...
