import sqlite3
import datetime
from flask import Flask, request, jsonify, send_from_directory
from user_funcions import *
from text_to_speech import *

app = Flask(__name__)

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

    result = register_payment(valor, id_user, id_audio)
    return jsonify({'success': result})

@app.route('/api/search_payment', methods=['GET'])
def api_search_payment():
    id_user = request.args.get('id_user')

    result = search_payment(id_user)
    return jsonify({'payments': result})

@app.route('/api/search_audios', methods=['GET'])
def api_search_audios():
    id_user = request.args.get('id_user')

    result = search_audios(id_user)
    return jsonify({'audios': result})

@app.route('/api/text_to_speech', methods=['POST'])
def api_text_to_speech():
    data = request.get_json()
    user = data['user']
    text = data['text']
    voice_name = data['voice_name']

    filename = text_to_speech(user, text, voice_name)
    return jsonify({'success': True, 'filename': filename})

@app.route('/api/get_audio', methods=['GET'])
def api_get_audio():
    filename = request.args.get('filename')

    return send_from_directory("audio", filename)

if __name__ == '__main__':
    app.run()