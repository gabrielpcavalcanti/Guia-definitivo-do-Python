import os

# Caminho da pasta onde estão os arquivos
pasta = r"C:\Users\Avell\Documents\GitHub\Guia-definitivo-do-Python\Exercicios\Novos\01_PrimeirosConceitos\Mais_exercicios"  # coloque o caminho aqui

for numero in range(1, 25):
    nome_antigo = f"Exercicio_{numero:02}.py"
    nome_novo = f"exercicio_{numero:02}.py"

    caminho_antigo = os.path.join(pasta, nome_antigo)
    caminho_novo = os.path.join(pasta, nome_novo)

    if os.path.exists(caminho_antigo):
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_antigo} → {nome_novo}")
    else:
        print(f"Arquivo não encontrado: {nome_antigo}")
