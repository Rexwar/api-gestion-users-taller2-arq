import pika

def callback(ch, method, properties, body):
    print(f"Recibido: {body.decode()}")

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Asegúrate de que la cola existe
    channel.queue_declare(queue='user_events')

    # Escuchar los mensajes en la cola
    channel.basic_consume(queue='user_events', on_message_callback=callback, auto_ack=True)

    print('Esperando eventos. Presiona CTRL+C para salir.')
    channel.start_consuming()

if __name__ == "__main__":
    consume()
