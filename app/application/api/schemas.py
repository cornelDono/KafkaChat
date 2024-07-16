from typing import Generic, Iterable, TypeVar
from pydantic import BaseModel


class ErrorSchema(BaseModel):
    error: str


IT = TypeVar('IT')


class BaseqQueryResponseSchema(BaseModel, Generic[IT]):
    count: int
    offset: int
    limit: int
    items: IT
