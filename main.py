from user_funcions import *
from text_to_speech import *

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

# id_user = 123
# arq_name = 'meu_audio.wav'
#
# if register_audio(id_user, arq_name):
#     print(f'O áudio {arq_name} foi inserido com sucesso para o usuário {id_user}.')
# else:
#     print('Ocorreu um erro ao inserir o áudio.')

##------------------------------------------------------------------------
##teste de text to speech

## vozes disponiveis
## link: https://learn.microsoft.com/pt-br/azure/cognitive-services/speech-service/language-support?tabs=tts#custom-neural-voice
## pt-BR-AntonioNeural (Masculino)
## pt-BR-BrendaNeural (Feminino)
## pt-BR-DonatoNeural (Masculino)
## pt-BR-ElzaNeural (Feminino)
## pt-BR-FabioNeural (Masculino)
## pt-BR-FranciscaNeural (Feminino)
## pt-BR-GiovannaNeural (Feminino)
## pt-BR-HumbertoNeural (Masculino)
## pt-BR-JulioNeural (Masculino)
## pt-BR-LeilaNeural (Feminino)
## pt-BR-LeticiaNeural (Feminino)
## pt-BR-ManuelaNeural (Feminino)
## pt-BR-NicolauNeural (Masculino)
## pt-BR-ValerioNeural (Masculino)
## pt-BR-YaraNeural (Feminino)

voice_name = "pt-BR-BrendaNeural"
user = 123
text = "Esse é um teste de código 01"

text_to_speech(user, text, voice_name)



