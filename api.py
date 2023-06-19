from flask import Flask, request, jsonify, send_from_directory
from user_funcions import *
from text_to_speech import *
import asyncio
import json

from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
loop = asyncio.get_event_loop()

@app.route('/api/register_user', methods=['POST'])
def api_register_user():
    data = request.get_json()
    login = data['login']
    senha = data['senha']
    usuario = data['usuario']
    telefone = data['telefone']
    

    result = register_user(login, senha, usuario, telefone)
    return jsonify({'success': result})

@app.route('/api/verify_login', methods=['POST'])
def api_verify_login():
    data = request.get_json()
    login = data['login']
    senha = data['senha']

    result = verify_login(login, senha)
    return jsonify({'success': result})

@app.route('/api/register_payment', methods=['POST'])
def api_register_payment():
    data = request.get_json()
    valor = data['valor']
    id_user = data['id_user']
    id_audio = data['id_audio']
    id_type = data['id_type']

    result = register_payment(valor, id_user, id_audio, id_type)
    return jsonify({'success': result})

@app.route('/api/search_payment', methods=['GET'])
def api_search_payment():
    id_user = request.args.get('id_user')
    result = search_payment(id_user)
    return result

@app.route('/api/search_audios', methods=['GET'])
def api_search_audios():
    id_user = request.args.get('id_user')

    result = search_audios(id_user)
    return result

@app.route('/api/text_to_speech', methods=['POST'])
def api_text_to_speech():
    data = request.get_json()
    user = data['user']
    text = data['text']
    voice_speed = data['voice_speed']
    voice_name = data['voice_name']
    pitch = data['pitch']

    result = text_to_speech(user, text, voice_name, voice_speed,pitch)
    return jsonify({'success': True, 'result': result})

@app.route('/api/load_voice_names', methods=['GET'])
def api_load_voice_names():
    voice_names = loop.run_until_complete(load_voices())
    return app.response_class(
        response=json.dumps(voice_names),
        status=200,
        mimetype='application/json'
    )

@app.route('/api/get_audio', methods=['GET'])
def api_get_audio():
    filename = request.args.get('filename')

    return send_from_directory("audio", filename)



# def init_db():
#     conn = sqlite3.connect('db/banco.db')  # Conecta ao banco de dados SQLite (cria um novo se não existir)
#     cursor = conn.cursor()

#     # Abra o arquivo "banco.sql" e execute os comandos SQL para criar as tabelas e definir a estrutura do banco de dados
#     with open('db/banco.sql', 'r') as f:
#         sql_script = f.read()
#         cursor.executescript(sql_script)
        
#     cursor.execute('INSERT INTO type_payment (id_type, name) VALUES (?, ?)', (1, "Pix"))
#     cursor.execute('INSERT INTO type_payment (id_type, name) VALUES (?, ?)', (2, "Boleto"))
#     cursor.execute('INSERT INTO type_payment (id_type, name) VALUES (?, ?)', (3, "Cartão de Crédito"))
#     cursor.execute('INSERT INTO type_payment (id_type, name) VALUES (?, ?)', (4, "Paypal"))

#     conn.commit()  # Confirma as alterações no banco de dados
#     conn.close()  # Fecha a conexão com o banco de dados
    
    
if __name__ == '__main__':
    # init_db()
    app.run()
    