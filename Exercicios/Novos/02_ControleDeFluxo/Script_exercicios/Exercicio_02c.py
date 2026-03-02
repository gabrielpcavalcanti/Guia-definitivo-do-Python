"""
c) Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são

• Ter pelo menos 65 anos, 

• Ou ter trabalhado pelo menos 30 anos, 

• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

age_employee: int = int(input("Digite a idade do trabalhador: "))
time_service: int = int(input("Digite o tempo de serviço: "))

if age_employee >= 65:
    print("Ele(a) pode ser aposentar.")

elif time_service >= 30:
    print("Ele(a) pode ser aposentar.")

elif age_employee >= 60 and time_service >= 25:
    print("Ele(a) pode ser aposentar.")

else:
    print("Não pode se aposentar.")
