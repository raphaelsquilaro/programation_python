import os

pasta = "arquivos"

# Pega o caminho absoluto da pasta onde o organizador.py está salvo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Une o caminho atual com o nome da pasta de arquivos
pasta = os.path.join(diretorio_atual, "arquivos")

# Verifica se a pasta existe antes de começar
if not os.path.exists(pasta):
    print(f"Erro: A pasta '{pasta}' não foi encontrada.")
else:
    lista_arquivos = os.listdir(pasta)
    contador = 1

    try:
        for arquivo in lista_arquivos:
            # Ignora pastas, foca apenas em arquivos
            if os.path.isfile(os.path.join(pasta, arquivo)):
                nome, extensao = os.path.splitext(arquivo)
                
                novo_nome = f"boleto_empresaA_arquivo{contador:03d}{extensao}"
                
                caminho_antigo = os.path.join(pasta, arquivo)
                caminho_novo = os.path.join(pasta, novo_nome)
                
                os.rename(caminho_antigo, caminho_novo)
                print(f"✓ {arquivo} -> {novo_nome}")
                contador += 1
                
        print("\nProcesso concluído com sucesso!")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")