from abc import ABC
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass(kw_only=True)
class BaseEvent(ABC):
    event_id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.now())
