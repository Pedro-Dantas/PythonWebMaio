from flask import Flask, request

app = Flask("Olá")

@app.route('/')

def ola():
    user_agent = request.headers.get('User-Agent')
    print("User-Agent:", user_agent)
    return "Olá Mundo " + user_agent
