from functools import lru_cache
from punq import Container, Scope

from motor.motor_asyncio import AsyncIOMotorClient

from infra.repositories.messages.base import BaseChatRepository
from infra.repositories.messages.memory import MemoryChatRepository
from infra.repositories.messages.mongo import MongoDBChatRepository
from logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
from logic.mediator import Mediator
from settings.config import Config


@lru_cache(1)
def init_container() -> Container:
    return _init_container()

def _init_container() -> Container:
    container = Container()

    container.register(CreateChatCommandHandler)
    container.register(Config, instance=Config(), scope=Scope.singleton)

    def init_mediator():
        mediator = Mediator()
        mediator.register_command(
            CreateChatCommand,
            [container.resolve(CreateChatCommandHandler)]
        )

        return mediator
    
    def init_chat_mongo_db_repository():
        config: Config = container.resolve(Config)
        client = AsyncIOMotorClient(config.mongodb_connection_settings_uri, serverSelectionTimeoutMS=3000)
        return MongoDBChatRepository(
            mongo_db_client=client,
            mongo_db_name=config.mongo_db_chat_database,
            mongo_db_collection_name=config.mongo_db_chat_collection,
        )
    
    container.register(BaseChatRepository, factory=init_chat_mongo_db_repository, scope=Scope.singleton)
    container.register(Mediator, factory=init_mediator)

    return container
