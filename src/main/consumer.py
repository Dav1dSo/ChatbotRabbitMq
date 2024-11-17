import pika
import json 
import os 
from dotenv import load_dotenv

load_dotenv()

def rabbitmq_callback(ch, method, propeties, body):
    print(body)


class RabbiMQConsumer:
    def __init__(self) -> None:

        self.__host = os.getenv("RABBITMQ_HOST")
        self.__port = os.getenv("RABBITMQ_PORT")
        self.__user_name = os.getenv("RABBITMQ_USERNAME")
        self.__password = os.getenv("RABBITMQ_PASSWOWRD")
        self.__queue = os.getenv("RABBITMQ_QUEUE")
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
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )
        
        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=rabbitmq_callback
        )
        
        return channel
    
    def start(self):
        print("Consumindo!")
        self.__channel.start_consuming()