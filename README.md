# 🤖 **Finanças Colaborativas: Bot de Telegram Open Source**

Este projeto é uma solução de código aberto para gerenciar finanças pessoais ou de um grupo de forma colaborativa, utilizando um bot do Telegram para registrar despesas e um dashboard web para visualização dos dados. O objetivo é fornecer uma ferramenta simples, transparente e totalmente customizável para quem quer ter controle total sobre seus dados.

## 🚀 **Características**

  - **Registro de Despesas via Telegram:** Envie mensagens simples ao bot para registrar gastos (ex: "compra mercado 150").
  - **Dados Privados:** Cada usuário possui seus dados vinculados ao seu ID do Telegram.
  - **Dashboard Web:** Visualize suas finanças com gráficos e tabelas detalhadas.
  - **Controle Total:** Por ser open source, você pode modificar o bot, a lógica de dados e o dashboard como preferir.

## 🛠️ **Tecnologias Utilizadas**

  - **Linguagem:** Python 3.x
  - **Bot:** `python-telegram-bot`
  - **Servidor Web:** `Flask`
  - **Banco de Dados:** `SQLite3` (integrado ao Python, sem necessidade de instalação externa)
  - **Gráficos:** `Matplotlib` e `Plotly`

## ⚙️ **Pré-requisitos**

Antes de começar, certifique-se de que você tem:

  * **Python 3.x** instalado.
  * **pip**, o gerenciador de pacotes do Python.
  * Um **Token de Acesso do BotFather** para seu bot do Telegram.

## 🚀 **Instalação e Uso**

Siga estes passos para ter o bot e o dashboard rodando na sua máquina.

### Passo 1: Clone o Repositório

Abra o terminal e execute o comando abaixo para baixar o projeto:

```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Crie e Ative um Ambiente Virtual

É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.

```sh
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

### Passo 3: Instale as Dependências

Instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```sh
pip install -r requirements.txt
```

### Passo 4: Configure o Bot

1.  Crie um arquivo chamado `.env` na raiz do projeto.

2.  Adicione seu token de acesso do Telegram neste arquivo, no seguinte formato:

    ```ini
    TELEGRAM_TOKEN=SEU_TOKEN_DO_BOT_AQUI
    ```

### Passo 5: Inicie o Bot e o Dashboard

O projeto está pronto para rodar\! Execute o arquivo principal para iniciar a aplicação:

```sh
python3 app.py
```

O bot será ativado e o servidor web do dashboard estará disponível em `http://127.0.0.1:5000`.

## 🤖 **Como Usar o Bot**

  - Envie mensagens ao bot para registrar despesas. O formato da mensagem deve ser: `[descrição] [valor]`.
  - **Exemplo:** `compra de mercado 150.50`

O bot irá processar a mensagem, extrair a descrição (`compra de mercado`), o valor (`150.50`) e associar a despesa ao seu ID de usuário.

## 📊 **Dashboard**

Acesse o endereço `http://127.0.0.1:5000` no seu navegador para ver o dashboard. Ele exibirá:

  - Um gráfico de pizza com a distribuição das suas despesas por categoria.
  - Uma tabela com o histórico de gastos mais recentes.
  - Filtros para visualizar seus próprios dados ou os dados de outros colaboradores, se houver.

## 🤝 **Como Contribuir**

Contribuições são sempre bem-vindas\! Se você tem ideias para melhorar o projeto, encontrou um bug ou quer adicionar novas funcionalidades, siga estes passos:

1.  Faça um **fork** deste repositório.
2.  Crie um **branch** para sua feature (`git checkout -b minha-nova-feature`).
3.  Faça suas alterações e **commit**-as (`git commit -m 'feat: adicionei nova funcionalidade'`).
4.  Envie o branch para o seu fork (`git push origin minha-nova-feature`).
5.  Abra um **Pull Request** no repositório original.
