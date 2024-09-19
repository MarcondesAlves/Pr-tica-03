from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='db',
                            database='clinica_db',
                            user='clinica_user',
                            password='clinica_pass')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM agendamentos;')
    agendamentos = cur.fetchall()
    cur.close()
    conn.close()

    response = "<h1>Agendamentos da Clínica</h1><ul>"
    for agendamento in agendamentos:
        response += f"<li>ID: {agendamento[0]}, Paciente: {agendamento[1]}, Data: {agendamento[2]}</li>"
    response += "</ul>"
    
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
