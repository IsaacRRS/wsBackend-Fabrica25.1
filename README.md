# Desafio Back-End da Fábrica de Software - 2025.1

### 📌 Do que se trata? 

Basicamente, a aplicação consiste em ter um 'Gerente', onde o mesmo possui acesso à dois Dashboards, um para registro de pessoas e outro onde há cadastro de endereços IP, sendo necessário associar um registro à um IP 

---
## 🖥️ Como rodar o projeto 

Assumindo que o Python e PostgreSQL estão instalados no seu computador, vá para o diretório do projeto. Abra o terminal do repositório para criação de um ambiente virtual e ative-o em seguida.

```
py -m venv (nome da venv)
/(nome da venv)/Scripts/activate
```
Depois que o ambiente virtual tiver sido instalado, vá até '../desafio/' onde 'requirements.txt' está localizado e instale as dependências em sua venv.
```
\..wsBackend-Fabrica25.1\desafio> 
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

