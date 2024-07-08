from datetime import datetime
from typing import Iterable
from pydantic import BaseModel

from domain.entities.messages import Chat, Message


class CreateChatRequestSchema(BaseModel):
    title: str


class CreateChatResponseSchema(BaseModel):
    oid: str
    title: str

    @classmethod
    def from_entity(cls, chat: Chat) -> 'CreateChatRequestSchema':
        return cls(oid=chat.oid, title=chat.title.as_generic_type())


class CreateMessageRequestSchema(BaseModel):
    text: str


class CreateMessageResponseSchema(BaseModel):
    oid: str
    text: str

    @classmethod
    def from_entity(cls, message: Message) -> 'CreateMessageRequestSchema':
        return cls(oid=message.oid, text=message.text.as_generic_type())


class MessageDetailSchema(BaseModel):
    oid: str
    text: str
    created_at: datetime

    @classmethod
    def from_entity(cls, message: Message) -> 'CreateMessageRequestSchema':
        return cls(oid=message.oid, text=message.text.as_generic_type(), created_at=message.created_at)
    

class ChatDetailSchema(BaseModel):
    oid: str
    title: str
    created_at: datetime
    messages: Iterable[MessageDetailSchema]

    @classmethod
    def from_entity(cls, chat: Chat) -> 'ChatDetailSchema':
        return cls(
            oid=chat.oid,
            title=chat.title.as_generic_type(),
            messages=[MessageDetailSchema.from_entity(message) for message in chat.messages],
            created_at=chat.created_at,
        )