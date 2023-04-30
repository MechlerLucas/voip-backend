from user_funcions import register_user
from user_funcions import verify_login
from user_funcions import register_payment
from user_funcions import search_payment
from user_funcions import search_audios
from user_funcions import register_audio

##------------------------------------------------------------------------
##teste de registro de usuario

if register_user('meu_login', 'minha_senha', 'Meu Nome', '123456789'):
    print('Usuário cadastrado com sucesso!')
else:
    print('Erro ao cadastrar usuário.')

##------------------------------------------------------------------------
##teste de login

if verify_login('meu_login', 'minha_senha'):
    print('Login bem-sucedido!')
else:
    print('Login falhou.')

##------------------------------------------------------------------------
##teste de registro de pagamento

valor = 50.00
id_user = 123
id_audio = 456

if register_payment(valor, id_user, id_audio):
    print('Pagamento registrado com sucesso!')
else:
    print('Ocorreu um erro ao registrar o pagamento.')

##------------------------------------------------------------------------
##teste de pesquisa de pagamento

id_user = 123

lista_pagamentos = search_payment(id_user)

if lista_pagamentos:
    print(f'Foram encontrados {len(lista_pagamentos)} pagamentos para o usuário {id_user}:')
    for pagamento in lista_pagamentos:
        print(pagamento)
else:
    print(f'Nenhum pagamento encontrado para o usuário {id_user}.')

##------------------------------------------------------------------------
##teste de pesquisa de audios

id_user = 123

lista_audios = search_audios(id_user)

if lista_audios:
    print(f'Foram encontrados {len(lista_audios)} áudios para o usuário {id_user}:')
    for audio in lista_audios:
        print(audio)
else:
    print(f'Nenhum áudio encontrado para o usuário {id_user}.')

##------------------------------------------------------------------------
##teste de inserção de audios

id_user = 123
arq_name = 'meu_audio.wav'

if register_audio(id_user, arq_name):
    print(f'O áudio {arq_name} foi inserido com sucesso para o usuário {id_user}.')
else:
    print('Ocorreu um erro ao inserir o áudio.')
