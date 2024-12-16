import pika
import grpc
from concurrent import futures
import user_service_pb2_grpc
from user_service_pb2 import RegisterResponse, UpdatePasswordResponse

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def __init__(self):
        # Configuración RabbitMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='user_events')

    def publish_event(self, event):
        # Publicar el evento en RabbitMQ
        self.channel.basic_publish(exchange='', routing_key='user_events', body=event)
        print(f"Evento publicado en RabbitMQ: {event}")

    def Register(self, request, context):
        # Lógica de registro
        print(f"Registrando usuario: {request.name} {request.surname}")
        self.publish_event(f"Usuario {request.name} {request.surname} registrado.")
        return RegisterResponse(message="Usuario registrado exitosamente")

    def UpdatePassword(self, request, context):
        # Lógica de actualización de contraseña
        print(f"Actualizando contraseña para: {request.email}")
        self.publish_event(f"Contraseña actualizada para: {request.email}")
        return UpdatePasswordResponse(message="Contraseña actualizada correctamente")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('127.0.0.1:50053')  # Asegúrate de que el puerto sea correcto
    print("gRPC Server iniciado en el puerto 50053")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
