# desafio_B2W

Projeto realizado para o desafio técnico de back end da B2W.

## Setup do projeto

1. Clonar o repositório
2. Criar um virtualenv (Python 3.7.5)
3. Ativar o virtualenv
4. Instalar as dependências
5. Realizar as migrações
6. Criar um superuser
7. Iniciar o servidor


### Windows
```console
git clone hhttps://github.com/SamuelBacelar/desafio_B2W.git
cd desafio_B2W
python -m venv env
source env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
