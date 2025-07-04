# Passo a passo para rodar localmente

Este projeto fornece uma API REST utilizando Flask e MySQL. A maneira mais simples de executá-lo é por meio do Docker Compose, que já prepara todos os serviços necessários.

## Requisitos
- Docker
- Docker Compose

## Executando com Docker
1. Clone este repositório e acesse a pasta criada:
   ```bash
   git clone <url-do-repositorio>
   cd flask-rest-api
   ```
2. Construa as imagens e inicie os contêineres:
   ```bash
   docker compose up --build
   ```
3. A API ficará disponível em `http://localhost:5000/`.
   O phpMyAdmin poderá ser acessado em `http://localhost:8080/`.
   O MySQL escutará na porta `3308` do hospedeiro.

Para interromper, pressione `Ctrl+C` e execute `docker compose down`.

## Executando sem Docker (opcional)
1. Crie um ambiente virtual Python e ative-o:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente referentes ao banco de dados (MYSQL_USER, MYSQL_PASSWORD etc.) apontando para sua instalação local do MySQL.
4. Inicie a aplicação:
   ```bash
   python run.py
   ```
5. Acesse `http://localhost:5000/` para verificar se a API está ativa.

## Rodando as migrações

O controle de versões do banco é feito com o *Flask-Migrate*. Após instalar as
dependências e definir `FLASK_APP=app:create_app`, execute:

```bash
# primeira execução
flask --app app:create_app db init

# gerar um novo arquivo de migração
flask --app app:create_app db migrate -m "Mensagem"

# aplicar as migrações ao banco
flask --app app:create_app db upgrade
```
