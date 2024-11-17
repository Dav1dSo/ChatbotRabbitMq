from src.main.consumer import RabbiMQConsumer

if __name__ == "__main__":
    consumer = RabbiMQConsumer()
    consumer.start()
