from datetime import datetime
import pytest

from domain.entities.messages import Chat, Message
from domain.exceptions.messages import EmptyTextException, TitleTooLongException
from domain.values.messages import Text, Title


def test_create_message_success():
    text = Text('hello world')
    message = Message(text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_long_text_success():
    text = Text('hello world' * 400)
    message = Message(text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_empty_failed():
    with pytest.raises(EmptyTextException):
        text = Text('')
        message = Message(text)


def test_create_chat_success():
    title = Title('Plain chat')
    chat = Chat(title)

    assert chat.title == title
    assert not chat.messages


def test_create_chat_title_too_long_failed():
    with pytest.raises(TitleTooLongException):
        title = Title('Plain chat' * 50)
        chat = Chat(title)


def test_chaat_add_message_success():
    text = Text('hello world')
    message = Message(text)

    title = Title('Plain chat')
    chat = Chat(title)

    chat.add_message(message)
    assert message in chat.messages

