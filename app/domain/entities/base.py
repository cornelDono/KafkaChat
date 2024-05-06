from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass(kw_only=True)
class BaseEntity(ABC):
    oid: str = field(
        default_factory= lambda: str(uuid4()),
    )
    created_at: datetime = field(
        default_factory=datetime.now,
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseEntity') -> bool:
        return self.oid == __value.oid
