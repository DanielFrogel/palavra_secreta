import os
import requests
import random
import google.generativeai as genai

def ia_gemini():
    genai.configure(api_key="YOUR_API_KEY")

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]
    
    return genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    

def main(resposta_json):
    model = ia_gemini()

    valor_secreto = random.choice(resposta_json)

    palavra_secreto = valor_secreto['palavra']
    dica = valor_secreto['dica']
    dica = dica[0].upper() + dica[1:]
    
    os.system('cls')

    print('Encontre a Palavra\n')
    pergunta = f'A Palavra secreta têm: {len(palavra_secreto)} letras\nDica: {dica}\n'
    print(pergunta)
    
    chat = model.start_chat()
    
    resposta_ia = chat.send_message(f'responder somente com o nome da linguagem com {len(palavra_secreto)} letras Qual a linguagem de Programação? {pergunta}')
    
    print(f'A Palavra Secreta é: {resposta_ia.text}\n')
    
    print('Deseja executar novamente? Digite 1, qualquer outra tecla para sair')
    
    opcao = input('Opção: ')
    
    if opcao == '1':
        main(resposta_json)
    else:
        quit()             

if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'

    resposta = requests.get(url)

    if resposta.status_code == 200:    
        main(resposta.json())
    else:
        print(f'Problema ao fazer a fazer requisição: {resposta.status_code}')         