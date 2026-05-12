import sqlite3
import os

DB_PATH = os.path.join("database", "estoque.db")

def conectar():
    return sqlite3.connect(DB_PATH)


def criar_tabela():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


    conexao = conectar()
    cursor = conexao.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    
    conexao.commit()
    conexao.close() 