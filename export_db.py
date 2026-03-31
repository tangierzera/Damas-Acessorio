import sqlite3, json

conn = sqlite3.connect('instance/loja.db')
conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print('TABELAS:', tables)

cur.execute('SELECT * FROM categoria')
cats = [dict(r) for r in cur.fetchall()]
print('CATEGORIAS:', json.dumps(cats, ensure_ascii=False, indent=2))

cur.execute('SELECT * FROM subcategoria')
subs = [dict(r) for r in cur.fetchall()]
print('SUBCATEGORIAS:', json.dumps(subs, ensure_ascii=False, indent=2))

cur.execute('SELECT COUNT(*) as total FROM produto')
count = cur.fetchone()['total']
print('TOTAL PRODUTOS:', count)

cur.execute('SELECT * FROM produto')
prods = [dict(r) for r in cur.fetchall()]
print('PRODUTOS:', json.dumps(prods, ensure_ascii=False, indent=2))

conn.close()
