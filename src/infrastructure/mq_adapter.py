import pika

class RabbitAdapter:
    def send(self, message: str):
        # Prueba cambiando 127.0.0.1 por 'localhost'
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters(
            host='localhost', 
            port=5672,
            credentials=credentials,
            heartbeat=600,
            blocked_connection_timeout=300
        )
        conn = pika.BlockingConnection(parameters)
        ch = conn.channel()
        ch.queue_declare(queue='examen_queue')
        ch.basic_publish(exchange='', routing_key='examen_queue', body=message)
        conn.close()