from abc import ABC, abstractmethod
from dataclasses import dataclass
from aiokafka.producer import AIOKafkaProducer
from aiokafka.consumer import AIOKafkaConsumer



@dataclass
class BaseMessageBroker(ABC):
    consumer: AIOKafkaConsumer

    @abstractmethod
    async def send_message(self, topic: str, value: bytes):
        ...
    
    @abstractmethod
    async def consume(self, topic: str):
        ...
