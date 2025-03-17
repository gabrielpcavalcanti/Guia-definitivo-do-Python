# Comandos cmd e pip

Nesse aquivo estão presentes os principais comando do terminal do windows (cmd) que funcionam também no PowerShell, caso prefira e os comando do pip. 

## Comando do cmd e PowerShell


### 1 -  Navegar entre diretórios

 **Entrar em um diretório**

  ```bash
  cd nome_do_diretorio

  ```
**Voltar um diretório**

  ```bash
  cd ..
  ```

### 2 - Listar arquivos e pastas

Para listar arquivos e pastas no diretório atual

```bash
dir
```

### 3 - Criar um diretório (pasta)

```bash
mkdir nome_da_pasta
```

### 4 - Excluir arquivos e pastas

**Excluir um arquivo**

  ```bash
  del nome_do_arquivo
  ```

**Excluir uma pasta**

  ```bash
  rmdir /s /q nome_da_pasta
  ```
  (O parâmetro `/s` exclui a pasta e tudo dentro dela, e `/q` faz sem pedir confirmação).

### 5 - Copiar arquivos
```bash
copy <origem destino>
```

### 6 - Mover ou renomear arquivos

```bash
move <origem destino>
```

### 7 - Limpar a tela

Para limpar o terminal e começar de novo:

```bash
cls
```

### 8 - Fechar o terminal

Para fechar o prompt de comando:

```bash
exit
```

## Comandos do pip

### 1 - Verificar versão do pip

```bash
pip --version
```

### 2 - Instalar um pacote

```bash
pip install nome_do_pacote
```

### 3 - Instalar uma versão específica de um pacote

```bash
pip install nome_do_pacote==versao
```

### 4. Atualizar um pacote e o pip

```bash
pip install --upgrade nome_do_pacote
```

```bash
python.exe -m pip install --upgrade pip
```

### 5. Remover um pacote

```bash
pip uninstall nome_do_pacote
```

## 6. Listar pacotes instalados

```bash
pip list
```

```bash
pip freeze
```

## 7. Salvar dependências em um arquivo `requirements.txt`

```bash
pip freeze > requirements.txt
```
## 8. Instalar pacotes a partir de um arquivo `requirements.txt`

```bash
pip install -r requirements.txt
```