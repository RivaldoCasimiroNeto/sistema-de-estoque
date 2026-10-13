import sqlite3
from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent
caminho_schema = pasta_projeto / "schema.sql"
caminho_banco = pasta_projeto / "sistema_estoque.db"

def conectar():
    return sqlite3.connect(caminho_banco)

def inicializar_banco(conexao):
    schema = caminho_schema.read_text(encoding="utf-8")
    conexao.executescript(schema)
    conexao.commit()

if __name__ == "__main__":
    conexao = conectar()
    cursor = conexao.cursor()
    inicializar_banco(conexao)

def cadastrar_produto(id, produto, qtd, valor_unidade):
    cursor.execute("INSERT INTO estoque (id, produto, qtd, valor_unidade) VALUES (?, ?, ?, ?)", (id, produto, qtd, valor_unidade))
    conexao.commit()
    print("Produtos cadastrados com sucesso.")

def ler():
    for linha in cursor.execute("SELECT * FROM estoque"):
        print(linha)

def atualizar_produto(qtd, valor_unidade, id):
    cursor.execute("UPDATE estoque SET qtd = ?, valor_unidade = ? WHERE id = ?", (qtd, valor_unidade, id))
    conexao.commit()
    print("Produto atualizado com sucesso.")

def deletar_produto(conexao, id):
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM estoque WHERE id =?", (id,))
        
        produto = cursor.fetchone()
        if produto is None: 
             print("Produto não encontrado.")
             return
        
        cursor.execute("DELETE FROM estoque WHERE id = ?", (id,))

        conexao.commit()
        print("Produto deletado com sucesso!")

conexao = conectar()
cadastrar_produto(1445, 'Vestido', 200, 18000)
ler()