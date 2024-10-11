from functools import lru_cache
from punq import Container, Scope

from motor.motor_asyncio import AsyncIOMotorClient

from infra.repositories.messages.base import BaseChatsRepository, BaseMessagesRepository
from infra.repositories.messages.mongo import MongoDBChatsRepository, MongoDBMessagesRepository
from logic.commands.messages import CreateChatCommand, CreateChatCommandHandler, CreateMessageCommand, CreateMessageCommandHandler
from logic.mediator.base import Mediator
from logic.mediator.event import EventMediator
from logic.queries.messages import GetChatDetailQuery, GetChatDetailQueryhandler, GetMessagesQuery, GetMessagesQueryHandler
from settings.config import Config


@lru_cache(1)
def init_container() -> Container:
    return _init_container()

def _init_container() -> Container:
    container = Container()
    container.register(Config, instance=Config(), scope=Scope.singleton)

    config: Config = container.resolve(Config)

    def create_mongo_db_client() -> AsyncIOMotorClient:
        return AsyncIOMotorClient(config.mongodb_connection_settings_uri, serverSelectionTimeoutMS=3000)

    container.register(AsyncIOMotorClient, factory=create_mongo_db_client, scope=Scope.singleton)
    client = container.resolve(AsyncIOMotorClient)

    def init_chats_mongo_db_repository() -> BaseChatsRepository:
        return MongoDBChatsRepository(
            mongo_db_client=client,
            mongo_db_name=config.mongo_db_chat_database,
            mongo_db_collection_name=config.mongo_db_chat_collection,
        )

    def init_messages_mongo_db_repository() -> BaseMessagesRepository:
        return MongoDBMessagesRepository(
            mongo_db_client=client,
            mongo_db_name=config.mongo_db_chat_database,
            mongo_db_collection_name=config.mongo_db_messages_colletion,
        )
    
    container.register(BaseChatsRepository, factory=init_chats_mongo_db_repository, scope=Scope.singleton)
    container.register(BaseMessagesRepository, factory=init_messages_mongo_db_repository, scope=Scope.singleton)

    #Commands handlers
    container.register(CreateChatCommandHandler)
    container.register(CreateMessageCommandHandler)

    #Query handlers
    container.register(GetChatDetailQueryhandler)
    container.register(GetMessagesQueryHandler)

    #Mediator
    def init_mediator() -> Mediator:
        mediator = Mediator()

        create_chat_handler = CreateChatCommandHandler(
            _mediator=mediator,
            chats_repository=container.resolve(BaseChatsRepository)
        )
        create_message_handler = CreateMessageCommandHandler(
            _mediator=mediator,
            message_repository=container.resolve(BaseMessagesRepository),
            chats_repository=container.resolve(BaseChatsRepository),
        )

        mediator.register_command(
            CreateChatCommand,
            [create_chat_handler],
        )
        mediator.register_command(
            CreateMessageCommand,
            [create_message_handler],
        )

        mediator.register_query(
            GetChatDetailQuery,
            container.resolve(GetChatDetailQueryhandler),
        )
        mediator.register_query(
            GetMessagesQuery,
            container.resolve(GetMessagesQueryHandler),
        )
        return mediator

    container.register(Mediator, factory=init_mediator)
    container.register(EventMediator, factory=init_mediator)

    return container
