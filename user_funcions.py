import sqlite3

def register_user(login, senha, usuario, telefone):
    try:
        # Conecte-se ao banco de dados
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # Insira o novo usuário na tabela usuarios
        cursor.execute('''INSERT INTO user (login, password, user_name, phone) VALUES (?, ?, ?, ?)''',
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
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # Verifique se o login e senha existem no banco de dados
        cursor.execute('''SELECT * FROM user WHERE login = ? AND password = ?''', (login, senha))
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