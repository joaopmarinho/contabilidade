# 🤖 **Bot de Finanças Pessoais (Telegram + Google Sheets)**

Este projeto é uma solução de baixo código para gerenciar finanças pessoais de forma colaborativa, utilizando um bot do Telegram para registrar despesas, uma planilha do Google Sheets para armazenar os dados e um dashboard do Looker Studio para visualização.

A ideia é permitir que um grupo de pessoas (família, amigos, etc.) registre seus gastos de forma simples, enviando mensagens a um bot, e visualize um resumo financeiro em tempo real.

---

## 🚀 **Tecnologias Utilizadas**

* **Telegram:** Plataforma do chatbot.
* **Google Sheets:** Banco de dados simples para armazenar os registros.
* **Make (ex-Integromat):** Plataforma de automação que conecta o Telegram ao Google Sheets.
* **Google Looker Studio (ex-Data Studio):** Ferramenta de visualização para criar dashboards.
* **QuickChart.io (opcional):** Para gerar gráficos dinâmicos a partir dos dados.

---

## 🛠️ **Pré-requisitos**

Para replicar este projeto, você precisará de:

* Uma conta no **Telegram**.
* Uma conta do **Google** (para Google Sheets e Looker Studio).
* Uma conta gratuita no **Make**.

---

## 💡 **Como Configurar o Projeto (Passo a Passo)**

Siga estes passos para ter sua própria versão do bot funcionando.

### Passo 1: Crie o Bot no Telegram

1.  Abra o Telegram e procure por **@BotFather**.
2.  Envie o comando `/newbot`.
3.  Escolha um nome para o seu bot (ex: "Meu Financinhas").
4.  Escolha um username que termine em "bot" (ex: "meufinancas_bot").
5.  O BotFather irá gerar um **Token de Acesso**. Copie-o, pois você precisará dele para o próximo passo.

### Passo 2: Prepare a Planilha do Google Sheets

1.  Acesse o Google Sheets e **crie uma nova planilha**.
2.  Na primeira linha, crie as seguintes colunas:
    * `Data`
    * `Descricao`
    * `Valor`
    * `Usuario`
3.  Certifique-se de que a planilha esteja acessível para a sua conta do Make.

### Passo 3: Monte o Fluxo de Automação no Make

1.  Acesse sua conta no **Make** e crie um novo "Cenário".
2.  **Módulo 1 (Webhook do Telegram):**
    * Escolha o aplicativo **Telegram Bot**.
    * Selecione o módulo `Watch Updates`.
    * Conecte sua conta do Telegram usando o Token de Acesso do seu bot.
    * Configure para que o Make "escutar" as mensagens recebidas pelo bot.
3.  **Módulo 2 (Adicionar linha ao Google Sheets):**
    * Adicione o aplicativo **Google Sheets**.
    * Selecione o módulo `Add a Row`.
    * Conecte sua conta do Google e selecione a planilha que você criou.
    * Mapeie os dados da seguinte forma:
        * `Data`: Use a função de data do Make (`now`).
        * `Descricao`: Use o conteúdo da mensagem do Telegram (`Text`).
        * `Valor`: Extraia o número da mensagem (você pode precisar de uma expressão regular para isso).
        * `Usuario`: Use o nome do usuário que enviou a mensagem (`From: First Name`).
4.  **Ative seu cenário.** Agora, toda mensagem enviada ao bot será registrada na planilha.

### Passo 4: Crie o Dashboard no Looker Studio

1.  Acesse o **Looker Studio** e crie um novo "Relatório".
2.  Clique em **"Adicionar dados"** e escolha a opção `Google Sheets`.
3.  Selecione a planilha que você criou no passo 2.
4.  Use as ferramentas do Looker Studio para criar gráficos de pizza, barras, tabelas e indicadores que mostrem um resumo das finanças.
5.  **Compartilhe o dashboard** com quem você quiser, usando a opção de link para visualização.

---

## 🤝 **Como Contribuir**

Este projeto é um ponto de partida. Sinta-se à vontade para:

* Abrir **Issues** para relatar bugs ou sugerir novas funcionalidades.
* Enviar **Pull Requests** com melhorias de código ou novas ideias de automação.
* Compartilhar sua experiência e soluções para aprimorar a documentação.
