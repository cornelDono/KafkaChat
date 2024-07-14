from datetime import datetime
from uuid import uuid4
import pytest

from domain.entities.messages import Chat, Message
from domain.events.messages import NewMessageRecievedEvent
from domain.exceptions.messages import EmptyTextException, TitleTooLongException
from domain.values.messages import Text, Title


def test_create_message_success():
    text = Text('hello world')
    message = Message(text=text, chat_oid=str(uuid4()))

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_long_text_success():
    text = Text('hello world' * 400)
    message = Message(text=text, chat_oid=str(uuid4()))

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_empty_failed():
    with pytest.raises(EmptyTextException):
        text = Text('')
        message = Message(text=text, chat_oid=str(uuid4()))


def test_create_chat_success():
    title = Title('Plain chat')
    chat = Chat(title)

    assert chat.title == title
    assert not chat.messages


def test_create_chat_title_too_long_failed():
    with pytest.raises(TitleTooLongException):
        title = Title('Plain chat' * 50)
        chat = Chat(title)


def test_chat_add_message_success():
    text = Text('hello world')
    message = Message(text=text, chat_oid=str(uuid4()))

    title = Title('Plain chat')
    chat = Chat(title)

    chat.add_message(message)
    assert message in chat.messages


def test_chat_pull_events_success():
    text = Text('hello world')
    message = Message(text=text, chat_oid=str(uuid4()))

    title = Title('Plain chat')
    chat = Chat(title)

    chat.add_message(message)
    pulled_events = chat.pull_events()

    assert not chat._events, chat._events
    assert len(pulled_events) == 1, pulled_events

    new_event = pulled_events[0]

    assert isinstance(new_event, NewMessageRecievedEvent), new_event
    assert new_event.message_oid == message.oid
    assert new_event.message_text == message.text.as_generic_type()
