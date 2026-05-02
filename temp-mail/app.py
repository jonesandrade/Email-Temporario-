import os
import sqlite3
import random
import string
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Configuração do banco de dados (Caminho absoluto para o Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "inbox.db")

def init_db():
    """Cria a tabela se ela não existir."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS inbox (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            sender TEXT,
            subject TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

# Inicializa o banco de dados
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar")
def gerar():
    """Gera um endereço de e-mail aleatório."""
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{user}@temp.local"
    return jsonify({"email": email})

@app.route("/mensagens/<email>")
def mensagens(email):
    """Lista as mensagens recebidas para um e-mail específico."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT sender, subject, message FROM inbox WHERE email=? ORDER BY id DESC", (email,))
    rows = c.fetchall()
    conn.close()
    return jsonify([{"from": r[0], "subject": r[1], "message": r[2]} for r in rows])

@app.route("/enviar", methods=["POST"])
def enviar():
    """Rota que recebe os e-mails (aceita JSON e Form Data)."""
    # Verifica se os dados vieram como JSON ou Form (essencial para Webhooks)
    if request.is_json:
        dados = request.json
    else:
        dados = request.form
    
    # Mapeia diferentes nomes de campos (to/email, from/sender, etc)
    email = dados.get("email") or dados.get("to")
    sender = dados.get("sender") or dados.get("from")
    subject = dados.get("subject", "Sem Assunto")
    message = dados.get("message") or dados.get("plain") or dados.get("text")

    if email and message:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO inbox (email, sender, subject, message) VALUES (?, ?, ?, ?)",
                  (email, sender, subject, message))
        conn.commit()
        conn.close()
        return jsonify({"ok": True}), 200
    
    return jsonify({"error": "Dados incompletos"}), 400

if __name__ == "__main__":
    # O Render define a porta automaticamente na variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
