## FinTrack_backend

Administrative system to manage schoolar finances

## Installation (dev)

1. Clone o repositório:

```sh
git clone git@github.com:lucyanocm/continnum_backend
```

2. Crie e execute o ambiente virtual python:

```sh
cd continnum_backend && python3 -m venv venv # irá criar uma pasta chamada venv na raiz do projeto, automaticamente ignorada pelo git

source venv/bin/activate # irá ativar o ambiente virtual

# para desativar, quando encerrar o desenvolvimento, execute:
deactivate # irá limpar as variáveis do ambiente virtual no seu sistema
```

3. Instale as dependências com pip:

```sh
python -m pip install Django djangorestframework

```

4. Entre na pasta do backend e execute o servidor:

```sh
cd backend_django
python manage.py runserver

# Se tudo ocorreu bem, no terminal deverá mostrar algo como:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 4.2.4, using settings 'backend_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

5. Teste fazendo uma requisição no endpoint http://127.0.0.1:8000/
