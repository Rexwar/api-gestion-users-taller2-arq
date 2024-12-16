from flask import Flask
import multiprocessing
import grpc_server

app = Flask(__name__)

@app.route("/")
def home():
    return "Microservicio de Gestión de Usuarios funcionando"

def run_grpc_server():
    grpc_server.serve()

if __name__ == "__main__":
    # Ejecutar Flask y gRPC en procesos separados
    grpc_process = multiprocessing.Process(target=run_grpc_server)
    grpc_process.start()
    
    # Iniciar Flask
    app.run(debug=True, port=5000)

    # Finalizar el proceso gRPC al cerrar Flask
    grpc_process.join()
