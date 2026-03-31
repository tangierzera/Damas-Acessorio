import sqlite3
import os

def migrate():
    db_path = os.path.join(os.path.dirname(__file__), 'instance', 'loja.db')
    
    if not os.path.exists(db_path):
        print(f"Banco de dados não encontrado em {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        
        # Adicionar coluna ativo
        try:
            c.execute("ALTER TABLE produto ADD COLUMN ativo BOOLEAN DEFAULT 1;")
            print("Coluna 'ativo' adicionada com sucesso.")
        except sqlite3.OperationalError as e:
            if "duplicate column name" in str(e).lower():
                print("Coluna 'ativo' já existe.")
            else:
                print(f"Erro ao adicionar coluna: {e}")
                
        conn.commit()
    except Exception as e:
        print(f"Erro geral: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    migrate()
