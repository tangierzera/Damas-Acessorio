import sqlite3
import os

db_path = os.path.join('instance', 'loja.db')

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Tenta adicionar a coluna video_url
        cursor.execute("ALTER TABLE produto ADD COLUMN video_url TEXT")
        conn.commit()
        print("✅ Coluna 'video_url' adicionada com sucesso à tabela 'produto'!")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("ℹ️ A coluna 'video_url' já existe.")
        else:
            print(f"❌ Erro: {e}")
    finally:
        conn.close()
else:
    print("❌ Banco de dados 'instance/loja.db' não encontrado.")
