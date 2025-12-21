import os

# Caminho da pasta onde os arquivos serão criados
pasta_destino = r"C:\Users\Avell\Documents\GitHub\Guia-definitivo-do-Python\Exercicios\Novos\04_Funcoes"  # você pode mudar isso para qualquer caminho

# Cria a pasta, se não existir
os.makedirs(pasta_destino, exist_ok=True)

# Cria os 62 arquivos
for i in range(1, 100):
    nome_arquivo = f"Exercicio_{i:02}.py"  # nomes como Exercicio_01.txt, Exercicio_02.txt, ...
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    # Cria o arquivo vazio (ou com conteúdo, se quiser)
    with open(caminho_completo, "w") as f:
        f.write(f'""" \n\n"""')  # exemplo de conteúdo inicial

print("Arquivos criados com sucesso.")