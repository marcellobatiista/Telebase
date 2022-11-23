<p align="center">
<img src="imagens/Telebasetranslogo.png" width=300 height=300 />
</p>

---


# Telebase

Telebase é um projeto de código aberto que visa 
a criação de um sistema de gerenciamento de dados json para o Telegram.

Através de um mais bots do Telegram em um canal privado, que ajudam no CRUD dos dados. 

O intuito foi de facilitar no armazenamento e regaste de dados, como por exemplo,
uma lista de presença, uma lista de tarefas, uma lista de compras, etc 
sem a necessidade de um banco de dados.

## Instalação
```bash
pip install telebase
```

## Como usar

### 1. Criando um bot

Para criar um bot, você deve falar com o @BotFather no Telegram, e seguir as instruções.

### 2. Criando um canal

### 3. Adicionando os bots no canal

### 4. Criando a aplicação

```python

from telebase import Telebase

# Crie um objeto Telebase
db = TeleBase()

# Adicione o bot no objeto Telebase
db.adicionar_bot('<TOKEN: Union[str, list]>')

# Chame a mensagem de boas vindas no canal
db.criar_database()  # /start
```
No Telegram, você deve receber uma mensagem de boas vindas, com o ID do canal e a base de dados.

```json
TeleBase iniciado

{
  "ID": -1001488349617,
  "base": 1095,
  "tabelas": {}
}
____
```

Após isso, você já pode começar a usar o Telebase.

## Crie tabelas

```python
from telebase import Telebase

db = TeleBase(int('<CHAT_ID>'), int('<DATABASE_ID>'))
db.adicionar_bot('<TOKEN: Union[str, list]>')

# Inicie os bots
db.iniciar_bot()
# Insira as tabelas
db.criar_tabela('usuarios')
```
No Telegram você deve receber uma mensagem de confirmação.

```json
{
  "tabela": "usuarios",
  "dados": [
        {}
   ]
}
```

## Inserindo dados

```python

from telebase import Telebase

db = TeleBase(int('<CHAT_ID>'), int('<DATABASE_ID>'))
db.adicionar_bot('<TOKEN: Union[str, list]>')
db.iniciar_bot()

# Insira os dados
db.add('<TABELA>', '<CHAVE>', '<VALOR>')
```


# Métodos disponíveis

```python
db.criar_tabela('<TABELA>')  # Cria uma tabela
db.get_tabela('<TABELA>')  # Retorna uma tabela
db.drop_tabela('<TABELA>')  # Deleta a tabela
db.add('<TABELA>', '<CHAVE>', '<VALOR>')  # Insere dados
db.get('<TABELA>', '<CHAVE>')  # Retorna os dados
db.get_all('<TABELA>')  # Retorna todos os dados
db.get_all_keys('<TABELA>')  # Retorna todas as chaves
db.get_all_values('<TABELA>')  # Retorna todos os valores
db.update('<TABELA>', '<CHAVE>', '<VALOR>')  # Atualiza os dados
db.delete('<TABELA>', '<CHAVE>')  # Deleta os dados
db.drop_database()  # Deleta a base de dados
```

## Contribuindo

Contribuições são sempre bem-vindas!

## Autor

[**@marcellobatiista**](https://github.com/marcellobatiista)
