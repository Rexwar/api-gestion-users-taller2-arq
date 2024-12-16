import pika

def test_rabbitmq_connection():
    try:
        # Establecer conexión con RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        # Declarar una cola para pruebas
        channel.queue_declare(queue='test_queue')

        # Enviar un mensaje de prueba
        channel.basic_publish(exchange='', routing_key='test_queue', body='Hello RabbitMQ!')

        print("Mensaje enviado a RabbitMQ correctamente.")
        connection.close()
    except Exception as e:
        print(f"Error al conectarse a RabbitMQ: {e}")

if __name__ == "__main__":
    test_rabbitmq_connection()
