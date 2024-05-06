from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class ApplciationException(Exception):
    @property 
    def message(self):
        return 'Application Error occurred'
