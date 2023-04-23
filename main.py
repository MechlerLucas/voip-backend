from user_funcions import register_user
from user_funcions import verify_login

if register_user('meu_login', 'minha_senha', 'Meu Nome', '123456789'):
    print('Usuário cadastrado com sucesso!')
else:
    print('Erro ao cadastrar usuário.')

###############################################

if verify_login('meu_login', 'minha_senha'):
    print('Login bem-sucedido!')
else:
    print('Login falhou.')