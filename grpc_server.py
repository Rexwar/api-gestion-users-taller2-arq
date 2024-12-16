import grpc
from concurrent import futures
import user_service_pb2_grpc
from user_service_pb2 import RegisterResponse
from models import db, Usuario  # Importar el modelo y db desde Flask

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def Register(self, request, context):
        # Lógica de registro usando la base de datos de Flask
        print(f"Registrando usuario: {request.nombre} {request.primer_apellido}")
        
        # Verificar si el usuario ya existe por el RUT
        existing_user = db.session.query(Usuario).filter(Usuario.rut == request.rut).first()
        if existing_user:
            return RegisterResponse(message="User already exists", user_id=0)

        # Crear el usuario
        user = Usuario(
            nombre=request.nombre,
            primer_apellido=request.primer_apellido,
            segundo_apellido=request.segundo_apellido,
            rut=request.rut,
            correo=request.correo,
            carrera_id=request.carrera_id
        )
        db.session.add(user)
        db.session.commit()

        # Devuelve la respuesta con el ID del nuevo usuario
        return RegisterResponse(message="User registered successfully", user_id=user.id)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('localhost:50054')  # Asegúrate de que el puerto esté libre
    print("gRPC Server iniciado en el puerto 50054")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
