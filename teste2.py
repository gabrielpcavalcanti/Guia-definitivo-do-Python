import os
import openpyxl

spreadsheet_path = "C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Photos\\G11101\\name.xlsx"  
folder_path = "C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Photos\\G11101\\photos"  
profundidades = []
lista_id = []

os.chdir(folder_path)

print("Diretorios da pasta:")
print(os.listdir())

wb = openpyxl.load_workbook(spreadsheet_path)

ws = wb['Sheet1']

rows = list(ws.rows)

for a,b in rows:
    lista_id.append(a.value)
    profundidades.append(b.value)

profundidades.pop(0)
lista_id.pop(0)

#print(profundidades)
#print(lista_id)

dict_id_prof = {}

for i,j in zip(lista_id, profundidades):
    dict_id_prof[j] = i


for q in profundidades:

    if f"{q}m.jpeg" in os.listdir():
        continue
    else:
        dict_id_prof.pop(q)

print(dict_id_prof)


for n, m in dict_id_prof.items():

    os.rename(f"{n}m.jpeg", f"{m}.jpeg")

    

print("Diretorios da pasta após o rename:")
print(os.listdir())
