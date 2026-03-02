"""a) Dada a String "Meu cachorro se chama Oreo", selecione so a palavra "cachorro", "Oreo" e inverta a String. Use apenas Slicing."""

string_question: str = "Meu cachorro se chama Oreo"

# Selecionado a palavra "cachorro"
print(string_question[4:12])

# Selecionado a palavra "Oreo"
print(string_question[-4:])

# Invertendo a String
print(string_question[::-1])
