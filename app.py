import os
import sqlite3
from flask import Flask, render_template
import matplotlib.pyplot as plt

# Importações atualizadas para a nova versão da biblioteca
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# -- Configuração --
try:
    with open('.env') as f:
        env_vars = dict(line.strip().split('=', 1) for line in f)
    TELEGRAM_TOKEN = env_vars['TELEGRAM_TOKEN']
except FileNotFoundError:
    print("Erro: Arquivo .env não encontrado.")
    exit()

# -- Banco de Dados --
conn = sqlite3.connect('./db/financas.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS despesas (
               id INTEGER PRIMARY KEY,
               usuario_id TEXT,
               descricao TEXT,
               valor REAL,
               data TEXT)''')
conn.commit()

# -- Lógica do Bot --
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Eu sou seu bot de finanças. Para registrar uma despesa, digite: [descrição] [valor].')

async def registrar_despesa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        texto = update.message.text.split()
        valor = float(texto[-1])
        descricao = ' '.join(texto[:-1])
        usuario_id = str(update.message.from_user.id)
        data = update.message.date.strftime('%Y-%m-%d')
        
        c.execute("INSERT INTO despesas (usuario_id, descricao, valor, data) VALUES (?, ?, ?, ?)",
                  (usuario_id, descricao, valor, data))
        conn.commit()
        await update.message.reply_text(f'Despesa "{descricao}" de R$ {valor:.2f} registrada com sucesso!')
    except (ValueError, IndexError):
        await update.message.reply_text('Formato inválido. Use: [descrição] [valor].')

# -- Servidor Web (Dashboard) --
app = Flask(__name__)

@app.route('/')
def dashboard():
    c.execute("SELECT descricao, valor FROM despesas")
    dados = c.fetchall()
    
    # Criar um gráfico de pizza
    if dados:
        labels = [d[0] for d in dados]
        valores = [d[1] for d in dados]
        plt.figure(figsize=(8, 8))
        plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição de Despesas')
        plt.savefig('static/pie_chart.png')
    
    c.execute("SELECT * FROM despesas ORDER BY data DESC LIMIT 10")
    tabela_dados = c.fetchall()

    return render_template('index.html', tabela_dados=tabela_dados)

# -- Inicialização --
if __name__ == '__main__':
    # Inicializar a aplicação do bot
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Adicionar os handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), registrar_despesa))
    
    # Executar o bot
    application.run_polling()