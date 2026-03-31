"""
seed.py - Popula o banco de dados com categorias e produtos iniciais.
Execute uma vez após o deploy: python seed.py
"""
from app import app, db, Categoria, Produto

CATEGORIAS = [
    {"id": 1, "nome": "Roupas"},
    {"id": 2, "nome": "Joias"},
    {"id": 3, "nome": "Chocolates"},
]

PRODUTOS = [
    {"nome": "Argola Clássica Zircônia", "categoria": "Joias", "preco": 65.0,
     "descricao": "Argolinha clássica com zircônias. Perfeita para o primeiro ou segundo furo.",
     "descricao_longa": "Zircônias de classe AAA\n- Fecho click de alta segurança",
     "imagens_url": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?ixlib=rb-4.0.3&w=800&q=80,https://images.unsplash.com/photo-1602751584552-8ba73aad10e1?ixlib=rb-4.0.3&w=800&q=80",
     "ativo": True},
    {"nome": "Bracelete Rígido Geométrico", "categoria": "Joias", "preco": 149.0,
     "descricao": "Peça de afirmação para os pulsos. Acabamento polido espelhado.",
     "descricao_longa": "Bracelete rígido com linhas geométricas fortes.\n- Material: Aço Inoxidável Antialérgico\n- Banhado a Ouro Amarelo 18k\n- Circunferência: 19cm",
     "imagens_url": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?ixlib=rb-4.0.3&w=800&q=80,https://images.unsplash.com/photo-1599643478524-fb66f70d00f8?ixlib=rb-4.0.3&w=800&q=80",
     "ativo": True},
    {"nome": "Vestido Midi Estampa Floral Exclusiva", "categoria": "Roupas", "preco": 129.9,
     "descricao": "Vestido midi em tecido leve estilo viscolinho. Acompanha cinto do mesmo tecido.",
     "descricao_longa": "O vestido perfeito para dias ensolarados.\n- Modelagem Veste do 38 ao 42\n- Composição: 100% Viscolinho Premium\n- Acompanha laço ajustável",
     "imagens_url": "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?ixlib=rb-4.0.3&w=800&q=80,https://images.unsplash.com/photo-1550639525-c97d455acf70?ixlib=rb-4.0.3&w=800&q=80",
     "link_mercadolivre": "https://mercadolivre.com.br", "ativo": True},
    {"nome": "Trench Coat Elegance Caramelo", "categoria": "Roupas", "preco": 289.0,
     "descricao": "Casaco sobretudo com faixa para amarração e botões perolados.",
     "descricao_longa": "Um item essencial no guarda-roupa de inverno, o Trench Coat Elegance oferece uma construção estruturada e chique.",
     "imagens_url": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?ixlib=rb-4.0.3&w=800&q=80",
     "link_mercadolivre": "https://mercadolivre.com.br", "ativo": True},
    {"nome": "Conjunto Alfaiataria Risca de Giz", "categoria": "Roupas", "preco": 320.0,
     "descricao": "Blazer alongado e calça reta com caimento perfeito, estampa clássica.",
     "descricao_longa": "O Conjunto Alfaiataria traz muito poder e autenticidade ao Office Look.\n- Ternos (Blazer + Calça)\n- Ombros estruturados",
     "imagens_url": "https://images.unsplash.com/photo-1584273143981-41c073dfe8f8?ixlib=rb-4.0.3&w=800&q=80",
     "ativo": True},
    {"nome": "Caixa Presente Trufas Sortidas", "categoria": "Chocolates", "preco": 54.9,
     "descricao": "Caixa com 12 trufas sortidas nos sabores tradicionais e frutados.",
     "descricao_longa": "O presente perfeito!\n- 3x Maracujá com recheio cremoso\n- 3x Brigadeiro Intenso\n- 3x Branco clássico\n- 3x Morango fresco",
     "imagens_url": "https://images.unsplash.com/photo-1549007994-cb92caebd54b?ixlib=rb-4.0.3&w=800&q=80",
     "link_mercadolivre": "https://mercadolivre.com.br", "ativo": True},
    {"nome": "Anel Solitário Classic", "categoria": "Joias", "preco": 129.9,
     "descricao": "O símbolo máximo da sofisticação.",
     "descricao_longa": "Peça essencial em qualquer coleção. Zircônia central com brilho de diamante.",
     "imagens_url": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=600",
     "ativo": True},
    {"nome": "Pulseira Elo Português", "categoria": "Joias", "preco": 198.0,
     "descricao": "Robusta e elegante para o dia a dia.",
     "descricao_longa": "Folheada a ouro, essa pulseira combina com diversos estilos, do casual ao formal.",
     "imagens_url": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?q=80&w=600",
     "ativo": True},
    {"nome": "Vestido Alfaiataria Noite", "categoria": "Roupas", "preco": 459.0,
     "descricao": "Corte impecável para noites inesquecíveis.",
     "descricao_longa": "Tecido estruturado que valoriza a silhueta com extremo conforto.",
     "imagens_url": "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?q=80&w=600",
     "ativo": True},
    {"nome": "Blusa Seda Soft", "categoria": "Roupas", "preco": 189.0,
     "descricao": "Toque suave e brilho discreto da seda.",
     "descricao_longa": "Item versátil para o closet feminino, transita bem do escritório ao jantar.",
     "imagens_url": "https://images.unsplash.com/photo-1582533561751-ef6f6ab93a2e?q=80&w=600",
     "ativo": True},
    {"nome": "Calça Flare Premium", "categoria": "Roupas", "preco": 229.0,
     "descricao": "Modelagem que alonga e sofistica.",
     "descricao_longa": "Jeans de alta gramatura com elastano que mantém a forma o dia todo.",
     "imagens_url": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=600",
     "ativo": True},
    {"nome": "Blazer Minimalist Blue", "categoria": "Roupas", "preco": 580.0,
     "descricao": "Estrutura moderna na cor da temporada.",
     "descricao_longa": "Forro acetinado e botões banhados, um investimento em estilo.",
     "imagens_url": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?q=80&w=600",
     "ativo": True},
    {"nome": "Cardigan Tricot Lux", "categoria": "Roupas", "preco": 195.0,
     "descricao": "O aconchego com fios de alta qualidade.",
     "descricao_longa": "Tramas trabalhadas que dão um ar artesanal e chique.",
     "imagens_url": "https://images.unsplash.com/photo-1516762689617-e1cffcef479d?q=80&w=600",
     "ativo": True},
    {"nome": "Macacão Longo Chic", "categoria": "Roupas", "preco": 349.0,
     "descricao": "Look completo e poderoso em peça única.",
     "descricao_longa": "Decote V e amarração na cintura para ajuste personalizado.",
     "imagens_url": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=600",
     "ativo": True},
    {"nome": "Body Renda Delicate", "categoria": "Roupas", "preco": 128.0,
     "descricao": "Sensualidade e delicadeza nos detalhes.",
     "descricao_longa": "Renda francesa aplicada e fecho invisível para maior conforto.",
     "imagens_url": "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?q=80&w=600",
     "ativo": True},
    {"nome": "Shorts Couro Eco", "categoria": "Roupas", "preco": 179.0,
     "descricao": "Atitude e modernidade para seu look.",
     "descricao_longa": "Material sintético de alta durabilidade com toque macio similar ao couro natural.",
     "imagens_url": "https://images.unsplash.com/photo-1591369822096-ffd140ec948f?q=80&w=600",
     "ativo": True},
    {"nome": "Cesta Presente Especial", "categoria": "Chocolates", "preco": 125.0,
     "descricao": "O presente perfeito para qualquer ocasião.",
     "descricao_longa": "Mix de tabletes, trufas e itens exclusivos da coleção sazonal.",
     "imagens_url": "https://images.unsplash.com/photo-1553452118-621e1f860f43?q=80&w=600",
     "ativo": True},
]

def seed():
    with app.app_context():
        db.create_all()

        # Verificar se já existem dados
        if Categoria.query.count() > 0:
            print("Banco já populado. Nenhuma ação necessária.")
            return

        # Criar categorias
        cat_map = {}
        for c in CATEGORIAS:
            cat = Categoria(nome=c["nome"])
            db.session.add(cat)
            db.session.flush()
            cat_map[c["nome"]] = cat.id

        db.session.commit()
        print(f"✅ {len(CATEGORIAS)} categorias criadas")

        # Criar produtos
        for p in PRODUTOS:
            cat_id = cat_map.get(p.get("categoria"), 1)
            prod = Produto(
                nome=p["nome"],
                categoria_id=cat_id,
                categoria=p.get("categoria", ""),
                descricao=p.get("descricao", ""),
                descricao_longa=p.get("descricao_longa", ""),
                preco=p.get("preco", 0),
                imagens_url=p.get("imagens_url", ""),
                link_mercadolivre=p.get("link_mercadolivre", ""),
                whatsapp="",
                ativo=p.get("ativo", True),
            )
            db.session.add(prod)

        db.session.commit()
        print(f"✅ {len(PRODUTOS)} produtos criados")
        print("🎉 Seed concluído com sucesso!")


if __name__ == "__main__":
    seed()
