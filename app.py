from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "1234"

app = Flask("Olá")
app.config.from_object(__name__)

def conectar():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    print('abriu')
    g.bd = conectar()

@app.teardown_request
def teardown_request(f):
    print('fechou')
    g.bd.close()

@app.route('/')
def exibir_posts():
   #sql = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC"
    #resultado = g.bd.execute(sql)
    print('query')
    posts = [
        {"titulo":"Titulo 1", "texto":"Texto 1", "data_criacao":"21/05/2024"},
        {"titulo":"Titulo 2", "texto":"Texto 2", "data_criacao":"22/05/2024"},
        {"titulo":"Titulo 1", "texto":"Texto 1", "data_criacao":"23/05/2024"}
    ]

    return render_template("ola.html", post = posts) 