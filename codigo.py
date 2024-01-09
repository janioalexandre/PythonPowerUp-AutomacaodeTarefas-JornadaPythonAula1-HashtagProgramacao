# Passo a passo do projeto

# Passo 1: Entrar no Sistema da Empresa

# Passo 2: Fazer login

# Passo 3: Importar a base de dados de produtos

# Passo 4: Cadastrar 1 Produto

# Passo 5: Repetir o cadastro para todos os produtos

import pyautogui
import time
import pandas 

# Comandos 
# pyautogui.click     -> Clicar com o mouse
# pyautogui.write     -> Escrever um texto
# pyautogui.press     -> aperta 1 tecla
# pyautogui.hotkey    -> atalho (combinação de tavlas)

pyautogui.PAUSE = 1 

# Abrir o chrome 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Esperar o site carregar 
time.sleep(2)

# Passo 2: Fazer login

pyautogui.click(x=388, y=408)
pyautogui.write("janioalexandre@gmail.com")


pyautogui.press("tab")
pyautogui.write("DeuséFiel")
pyautogui.press("enter")

time.sleep(1)

# Passo 3: Importar a base de dados de produtos 
# pip install pandas numpy openpyxl

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 Produto
# Passo 5: Repetir o cadastro para todos os produtos

for linha in tabela.index:
    
    pyautogui.click(x=389, y=292)

    codigo  = tabela.loc[linha, "codigo"]

    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    
    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
       
    pyautogui.scroll(1000)