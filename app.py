from flask import Flask

app = Flask("Olá")

@app.route('/')
def ola():
    return "Salve!"
