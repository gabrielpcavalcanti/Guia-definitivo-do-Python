tamanho_arquivo_mb = float(input("Digite o tamnho do arquivo em mb: "))
velocidade_link = float(input("Velocidade da internet em mbps: "))

tempo_minutos = (tamanho_arquivo_mb / velocidade_link) * 60

print("Tempo de download do arquivo em minutos: {:.3f}".format(tempo_minutos))
