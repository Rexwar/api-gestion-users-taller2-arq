import grpc
from user_service_pb2 import RegisterRequest, UpdatePasswordRequest
from user_service_pb2_grpc import UserServiceStub

def run():
    try:
        # Crear canal y cliente gRPC
        channel = grpc.insecure_channel('localhost:5053')  # Asegúrate de que el puerto sea correcto
        stub = UserServiceStub(channel)

        # Probar el registro de usuario
        register_request = RegisterRequest(name="Juan", surname="Pérez", email="juan@example.com", password="123456")
        response = stub.Register(register_request)
        print(f"Registro: {response.message}")

        # Probar la actualización de contraseña
        update_password_request = UpdatePasswordRequest(email="juan@example.com", current_password="123456", new_password="newpassword123")
        response = stub.UpdatePassword(update_password_request)
        print(f"Actualizar Contraseña: {response.message}")

    except grpc.RpcError as e:
        print(f"Error gRPC: {e}")
        print(f"Details: {e.details()}")
        print(f"Status code: {e.code()}")
        print(f"Debug string: {e.debug_error_string()}")

if __name__ == "__main__":
    run()
