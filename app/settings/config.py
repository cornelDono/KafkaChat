from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongodb_connection_settings_uri: str = Field(alias='MONGO_DB_CONNECTION_URI')
    mongo_db_chat_database: str = Field(default='chat', alias='MONGO_DB_CHAT_DATABASE')
    mongo_db_chat_collection: str = Field(default='chat', alias='MONGO_DB_CHAT_COLLECTION')
    mongo_db_messages_colletion: str = Field(default='messages', alias='MONGO_DB_MESSAGES_COLLECTION')
