# Desafio Back-End da Fábrica de Software - 2025.1

## 📌 Do que se trata? 

Basicamente, a aplicação consiste em ter um 'Gerente', onde o mesmo possui acesso à dois Dashboards, um para registro de pessoas e outro onde há cadastro de endereços IP, sendo necessário associar um registro à um IP. 

---
## 🖥️ Como rodar o projeto 

Assumindo que o Python e PostgreSQL estão instalados no seu computador, vá para o diretório do projeto clonado através do terminal para criação de um ambiente virtual e ative-o em seguida.

```
cd .\wsBackend-Fabrica25.1\
py -m venv (nome da venv)
(nome da venv)\Scripts\activate
```
Tenha em mente que isto precisa aparecer no terminal toda vez que desejar instalar algo dentro da venv.

![image](https://github.com/user-attachments/assets/153c8ac5-b9e9-496e-be62-a29cf9c78482)

Depois que o ambiente virtual tiver sido instalado, vá até '../desafio/' onde 'requirements.txt' está localizado e instale as dependências em sua venv.
```
cd .\desafio\
pip install -r requirements.txt
```
Agora, vá até '..\desafio\desafio\settings.py' e conecte a aplicação à um banco de dados PostgreSQL de sua escolha (crie um caso não tiver).
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '----',
        'USER': '----', 
        'PASSWORD': '----',
        'HOST':'localhost',
        'PORT': '5432'
        }
}
```
Após isso, tudo o que falta é aplicar as migrações e criar um superuser.

```
python manage.py migrate
python manage.py createsuperuser
```

E então será possível rodar o projeto

```
python manage.py runserver
```
---

## 📦 Quer rodar o projeto em DOCKER?
Comece criando estes dois arquivos no mesmo diretório de 'requirements.txt'.

![image](https://github.com/user-attachments/assets/c5aaa1ae-08d4-4ff4-9f0b-3f83d0893507)

Em seguida, coloque os seguintes conteúdos nestes arquivos:

*Dockerfile*
```
FROM python:3.12.8

WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
*docker-compose.yml*
```
version: '3.9'

services:
  db:
    image: postgres:17
    environment:
      POSTGRES_DB: (nome da db)
      POSTGRES_USER: (nome do teu user)
      POSTGRES_PASSWORD: (senha)
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build: .
    container_name: django_container
    depends_on:
      - db
    ports:
      - "8000:8000"
    environment:
      - DB_NAME=(nome de sua db)
      - DB_USER=(seu user)
      - DB_PASSWORD=(sua senha)
      - DB_HOST=db
      - DB_PORT=5432
    volumes:
      - .:/app
    command: >
      sh -c "
      python manage.py migrate &&
      echo \"from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin') if not User.objects.filter(username='admin').exists() else print('superuser já existe')\" | python manage.py shell &&
      python manage.py runserver 0.0.0.0:8000" 
      
volumes:
  postgres_data:
```
Após isso, vá até 'settings.py' e mude o seguintes campos:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome da db',
        'USER': 'nome do teu user',      
        'PASSWORD': 'senha',
        'HOST':'db',
        'PORT': '5432'
        }
}
```
Com isso, estando no mesmo diretório dos arquivos, abra o terminal e realize este comando: ```docker-compose up --build``` para configurar o container.

Enfim, em um browser de sua escolha, insira o endereço ``` localhost:8000``` para enfim acessar o projeto.

---
## 📬 Endpoints da aplicação

| Método | Endpoint                            | Descrição                     |
| ------ | ----------------------------------- | ----------------------------- |
| GET    | `/`                                 | Página inicial                |
| POST   | `/registro/`                        | Registrar gerente             |
| POST   | `/login/`                           | Login Gerente                 |
| POST   | `/logout/`                          | Logout Gerente                |
| GET    | `/pessoaBoard/`                     | Listar Pessoas                |
| POST   | `/pessoaBoard/pCriar/`              | Criar  registro de pessoa     |
| PUT    | `/pessoaBoard/pAtualizar/<int:pk>`  | Atualizar registro de pessoa  |
| GET    | `/pessoaBoard/pVisualizar/<int:pk>` | Visualizar registro de pessoa |
| DELETE | `/pessoaBoard/pDeletar/<int:pk>`    | Excluir registro de pessoa    |
| GET    | `/ipBoard/`                         | Listar IPs                    |
| POST   | `/ipBoard/criarIP/`                 | Adicionar um novo IP          |
| PUT    | `/ipBoard/atualizarIP/<int:pk>/`    | Atualizar um IP               |
| GET    | `/ipBoard/visualizarIP/<int:pk>/`   | Visualizar um IP              |
| DELETE | `/ipBoard/deletarIP/<int:pk>/`      | Excluir um IP                 |

