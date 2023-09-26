import pyautogui as pyat
import pandas as pd
from time import sleep

pyat.PAUSE = 0.5
tabela = pd.read_csv('produtos.csv')

pyat.press('win')
pyat.write('chrome')
pyat.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

sleep(3)
pyat.write(link)
pyat.press('enter')

sleep(2)

# login
# print(pyat.position())
# Email: Point(x=867, y=327)
pyat.click(x=867, y=327)
pyat.write('example@gmail.com')
pyat.press('tab')
pyat.write('123mudar')
pyat.press('tab')
pyat.press('enter')


sleep(5)
# Preenchendo a tabela
# print(pyat.position())
# Point(x=903, y=230)

for linha in tabela.index:
    if linha == 0:
        continue
    # localizar item
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    observacao = tabela.loc[linha, "obs"]

    pyat.scroll(500000)
    pyat.click(x=903, y=230)
    pyat.write(str(codigo)) # converter para str garante que números sejam corretamente passados.
    pyat.press('tab')
    pyat.write(str(marca))
    pyat.press('tab')
    pyat.write(str(tipo))
    pyat.press('tab')
    pyat.write(str(categoria))
    pyat.press('tab')
    pyat.write(str(preco))
    pyat.press('tab')
    pyat.write(str(custo))
    pyat.press('tab')
    if not pd.isna(observacao): # se a variável não for vazia, preencha.
        pyat.write(str(observacao))
    pyat.press('tab')
    pyat.press('enter')
