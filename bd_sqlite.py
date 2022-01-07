import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

#cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Lorenzo Emannuel", 29.9)')
#conexao.commit()

#cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#               {'nome':'Joao', 'peso':85}
#               )

#cursor.execute('INSERT INTO clientes (nome, peso) VALUES(?, ?)', ('Molly', 25))
#conexao.commit()

#cursor.execute('INSERT INTO clientes VALUES(:id, :nome, :peso)',
#               {'id': None, 'nome': 'Luigi', 'peso': 98.5}
#               )
#conexao.commit()

#cursor.execute(
#    'UPDATE clientes SET nome=:nome WHERE id=:id',
#    {'nome': 'Mario', 'id': 2}
#)
#conexao.commit()

#cursor.execute(
#    'UPDATE clientes SET nome=:nome, peso=:peso WHERE id=:id',
#    {'nome': 'Mario', 'peso': 95, 'id': 2}
#)
#conexao.commit()

#cursor.execute(
#    'DELETE FROM clientes WHERE id=:id',
#    {'id': 3}
#)
#conexao.commit()

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
    {'peso': 0})
for linha in cursor.fetchall():
    nome, peso = linha
    print(linha)

cursor.close()
conexao.close()