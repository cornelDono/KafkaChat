from datetime import datetime
from typing import Iterable
from pydantic import BaseModel

from application.api.schemas import BaseqQueryResponseSchema
from domain.entities.messages import Chat, Message


class CreateChatRequestSchema(BaseModel):
    title: str


class CreateChatResponseSchema(BaseModel):
    oid: str
    title: str

    @classmethod
    def from_entity(cls, chat: Chat) -> 'CreateChatRequestSchema':
        return cls(oid=chat.oid, title=chat.title.as_generic_type())
    

class ChatDetailSchema(BaseModel):
    oid: str
    title: str
    created_at: datetime

    @classmethod
    def from_entity(cls, chat: Chat) -> 'ChatDetailSchema':
        return cls(
            oid=chat.oid,
            title=chat.title.as_generic_type(),
            created_at=chat.created_at,
        )


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
    chat_oid: str

    @classmethod
    def from_entity(cls, message: Message) -> 'MessageDetailSchema':
        return cls(
            oid=message.oid,
            text=message.text.as_generic_type(),
            created_at=message.created_at,
            chat_oid=message.chat_oid,
        )


class GetMessagesQueryResponseSchema(BaseqQueryResponseSchema):
    items: list[MessageDetailSchema]
