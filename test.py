base_string = "spectrum_256_id_{}.spc"
lista_strings = []

for i in range(15, 1225):
    nova_string = base_string.format(i)
    lista_strings.append(nova_string)

for i in range(1293, 1450):
    nova_string = base_string.format(i)
    lista_strings.append(nova_string)

for i in range(1551, 2395):
    nova_string = base_string.format(i)
    lista_strings.append(nova_string)


for i in os.listdir():

    caminho_do_arquivo = f"{os.getcwd()}\\{i}"

    if i in lista_strings:
        try:
            os.remove(caminho_do_arquivo)
            #print(f"O arquivo '{caminho_do_arquivo}' foi deletado com sucesso.")
        except FileNotFoundError:
            print(f"O arquivo '{caminho_do_arquivo}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao tentar deletar o arquivo: {e}")
    else:
        continue

