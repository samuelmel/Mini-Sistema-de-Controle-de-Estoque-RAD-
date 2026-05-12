from app.bancodedados import conectar


def inserir_produto(nome, quantidade, preco):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, quantidade, preco)
        VALUES (?, ?, ?)
    """, (nome, quantidade, preco))

    conexao.commit()
    conexao.close()


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, quantidade, preco
        FROM produtos
        ORDER BY id DESC
    """)

    produtos = cursor.fetchall()

    conexao.close()

    return produtos


def atualizar_produto(id_produto, nome, quantidade, preco):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE produtos
        SET nome = ?, quantidade = ?, preco = ?
        WHERE id = ?
    """, (nome, quantidade, preco, id_produto))

    conexao.commit()
    conexao.close()


def deletar_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM produtos
        WHERE id = ?
    """, (id_produto,))

    conexao.commit()
    conexao.close()