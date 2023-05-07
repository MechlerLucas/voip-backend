import sqlite3
import datetime

def register_user(login, senha, usuario, telefone):
    try:
        # Conecte-se ao banco de dados
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()

        # Insira o novo usuário na tabela usuarios
        cursor.execute("INSERT INTO user (login, password, user_name, phone) VALUES (?, ?, ?, ?)",
                       (login, senha, usuario, telefone))

        # Salve as mudanças e feche a conexão com o banco de dados
        conn.commit()
        conn.close()
        return True

    except Exception as e:
        ##Imprima a mensagem de erro e retorne False
        print(e)
        return False

def verify_login(login, senha):
    try:
        # Conecte-se ao banco de dados
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()

        # Verifique se o login e senha existem no banco de dados
        cursor.execute("SELECT * FROM user WHERE login = ? AND password = ?", (login, senha))
        # Obtenha o primeiro registro retornado pela consulta
        registro = cursor.fetchone()

        # Feche a conexão com o banco de dados
        conn.close()

        # Retorne True se as credenciais são válidas, ou False se não são válidas
        return registro is not None

    except Exception as e:
        ##Imprima a mensagem de erro e retorne False
        print(e)
        return False

def register_payment(valor, id_user, id_audio):
    try:
        # Conectar-se ao banco de dados
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()

        # Inserir um novo registro na tabela de pagamentos
        cursor.execute("INSERT INTO payment (value, id_user, id_audio) VALUES (?, ?, ?)",(valor, id_user, id_audio))

        # Salvar as mudanças no banco de dados e fechar a conexão
        conn.commit()
        conn.close()

        # Retornar True para indicar que o registro foi inserido com sucesso
        return True

    except Exception as e:
        # Imprimir a mensagem de erro e retornar False
        print(e)
        return False

def search_payment(id_user):
    try:
        # Conectar-se ao banco de dados
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()

        # Pesquisar por todos os pagamentos relacionados a este usuário
        cursor.execute("SELECT * FROM payment WHERE id_user = ?", (id_user,))

        # Extrair os resultados da pesquisa e criar uma lista
        resultados = cursor.fetchall()
        lista_pagamentos = []
        for pagamento in resultados:
            id_pagamento, valor, id_user, id_audio = pagamento
            lista_pagamentos.append({'id_pagamento': id_pagamento, 'valor': valor, 'id_user': id_user, 'id_audio': id_audio})

        # Fechar a conexão com o banco de dados
        conn.close()

        # Retornar a lista de pagamentos encontrados
        return lista_pagamentos

    except Exception as e:
        # Imprimir a mensagem de erro e retornar uma lista vazia
        print(e)
        return []

def search_audios(id_user):
    try:
        # Conectar-se ao banco de dados
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()

        # Pesquisar por todos os áudios relacionados a este usuário
        cursor.execute("SELECT * FROM audio WHERE id_user = ?", (id_user,))

        # Extrair os resultados da pesquisa e criar uma lista
        resultados = cursor.fetchall()
        lista_audios = []
        for audio in resultados:
            id_audio, arq_name, id_user, creation_date = audio
            lista_audios.append({'id_audio': id_audio, 'arq_name': arq_name, 'id_user': id_user, 'creation_date': creation_date})

        # Fechar a conexão com o banco de dados
        conn.close()

        # Retornar a lista de áudios encontrados
        return lista_audios

    except Exception as e:
        # Imprimir a mensagem de erro e retornar uma lista vazia
        print(e)
        return []

def register_audio(id_user, arq_name):
    try:
        # Conectar-se ao banco de dados
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()

        # Inserir um novo registro na tabela de áudios
        cursor.execute("INSERT INTO audio (arq_name, id_user, creation_date) VALUES (?, ?, ?)",
                                (arq_name, id_user, datetime.datetime.now()))

        id_audio = cursor.lastrowid  # retorna o id do último registro inserido
        conn.commit()
        conn.close()

        return id_audio
    except Exception as e:
        # Imprimir a mensagem de erro e retornar False para indicar que ocorreu um erro
        print(e)
        return False

def insert_text_audio(text, id_audio):
    try:
        # Estabelece conexão com o banco de dados
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()
        # Insere os valores na tabela text_audio
        cursor.execute("INSERT INTO text_audio (text, id_audio) VALUES (?, ?)", (text, id_audio))
        id_text = cursor.lastrowid  # retorna o id do último registro inserido
        conn.commit()
        conn.close()
        return id_text
    except Exception as e:
        # Imprimir a mensagem de erro e retornar False para indicar que ocorreu um erro
        print(e)
        return False

def insert_audio_preset(id_audio, config):
    try:
        conn = sqlite3.connect('db/banco.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO audio_preset (id_text, config) VALUES (?, ?)', (id_audio, config))
        conn.commit()
        conn.close()
        print('Dados inseridos com sucesso na tabela audio_preset')
        return True
    except Exception as e:
        print(e)
        return False

######################################################################

def insert_all(user, arq_name, text, config):

    # register audio and get its id_audio
    id_audio = register_audio(user,arq_name)

    # register text_audio and get its id_text
    id_text = insert_text_audio(text, id_audio)

    # register audio_preset
    insert_audio_preset(id_text, config)
