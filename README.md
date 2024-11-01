# 🏥 Projeto de Cadastro de Pacientes e Monitoramento de Saneamento Básico - Backend

Este é o backend do sistema de **Cadastro de Pacientes e Monitoramento de Saneamento Básico** desenvolvido em **Django**.

## 🚀 Como Rodar o Projeto

### 1. Pré-requisitos

Certifique-se de ter:

- [Python 3.8+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [MySQL](https://www.mysql.com/) (ou outro banco de dados)

### 2. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/backend-saneamento.git
cd backend-saneamento
```

### 3. Criar e Ativar o Ambiente Virtual

```bash

python -m venv venv
source venv/bin/activate 
venv\Scripts\activate 
```

### 4. Instalar Dependências
```bash
pip install -r requirements.txt
```
### 5. Configurar o Banco de Dados

```bash
No settings.py, configure o banco de dados:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. Realizar Migrações

```bash

python manage.py migrate
```

### 7. Criar Superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 8. Iniciar o Servidor

```bash

python manage.py runserver

O projeto estará disponível em http://localhost:8000.
```
