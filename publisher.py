import pika
import json 
import os 

class RabbiMQPublisher:
    def __init__(self) -> None:
        self.__host = os.getenv("RABBITMQ_HOST")
        self.__port = os.getenv("RABBITMQ_PORT")
        self.__user_name = os.getenv("RABBITMQ_USERNAME")
        self.__password = os.getenv("RABBITMQ_PASSWOWRD")
        self.__exchange = os.getenv("RABBITMQ_EXCHANGE")
        self.__routing_key = os.getenv("RABBITMQ_ROUTING_KEY")
        self.__channel = self.create_channel()
        
    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__user_name,
                password=self.__password
            )
        )
        
        channel = pika.BlockingConnection(connection_parameters).channel()
        
        return channel
    
rabbit_mq_publisher = RabbiMQPublisher()