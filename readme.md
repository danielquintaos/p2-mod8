
## Requisitos

- Python 3.x
- Acesso à API da OpenAI


## Instalação

Para configurar o ambiente do projeto, siga os seguintes passos:

1. Clone o repositório:
   ```bash
   git clone https://github.com/danielquintaos/mod8-pon5
   ```

2. Substitua 'your_api_key' pela sua chave API da OpenAI no script do chatbot.


3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script Python para iniciar a interface do chatbot:

```
python app.py
```

Isso abrirá a interface do chatbot em um navegador, onde os usuários podem interagir digitando perguntas.


## Estrutura do Projeto

- `app.py`: Arquivo principal do chatbot.
- `tts.py`: Integra a funcionalidade TTS ao projeto.
- `requirements.txt`: Lista de dependências do Python.
- `data/safety_rules.txt`: Arquivo com o texto das normas de segurança.
- `speech.mp3`: A demonstração