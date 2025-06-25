import os
import shutil

# 💡 Essa função classifica os arquivos por tipo (extensão)
def classificar_arquivo(nome_arquivo):
    extensoes_imagens = ['.png', '.jpg', '.jpeg', '.gif']
    extensoes_planilhas = ['.xls', '.xlsx', '.csv']
    extensoes_pdfs = ['.pdf']

    _, extensao = os.path.splitext(nome_arquivo)

    if extensao in extensoes_imagens:
        return 'Imagens'
    elif extensao in extensoes_planilhas:
        return 'Planilhas'
    elif extensao in extensoes_pdfs:
        return 'PDFs'
    elif extensao:  # se tiver alguma extensão que não foi mapeada
        return 'Outros'
    else:
        return None  # arquivos sem extensão (às vezes acontece rs)

# 🌈 Caminho de onde vem a bagunça
pasta_origem = '/home/meuuser/Downloads'

# 🗂️ Caminho de onde vai ficar tudo lindamente organizado
pasta_destino_base = '/home/meuuser/Documentos'

# ⚙️ Verifica se a pasta de origem existe
if not os.path.exists(pasta_origem):
    print("A pasta de origem não existe! 😢")
else:
    # ✨ Loop que organiza tudo bonitinho
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        if os.path.isfile(caminho_arquivo):
            categoria = classificar_arquivo(arquivo)

            if categoria:
                # 💖 Cria a pasta de destino com base na categoria
                pasta_destino = os.path.join(pasta_destino_base, categoria)

                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                # 🚚 Move o arquivo da bagunça pra casa nova
                destino = os.path.join(pasta_destino, arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f"Movido: {arquivo} -> {categoria}")

    print("✨ Organização concluída! Agora sua pasta Documentos tá um brinco. ✨")
