from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class LogicException(Exception):
    @property
    def message(self):
        f"Logic error occured"
