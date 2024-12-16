from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Microservicio de Gestión de Usuarios funcionando"

if __name__ == "__main__":
    # Solo ejecutamos Flask aquí
    app.run(debug=True, port=5000)
