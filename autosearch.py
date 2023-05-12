from selenium import webdriver
import pandas as pd

navegador = webdriver.Chrome()
navegador.get("https://www.google.com")

#Leitura da tabela e pesquisa de itens da mesma no site de commodities
tabela = pd.read_excel("commodities.xlsx")
print(tabela)

for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    
    produto = produto.replace("ó","o").replace("ã", "a").replace("á", "a").replace("ç", "c").replace("ú","u").replace("é","e")
    
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    navegador.get(link)
    
    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preco = preco.replace(".", "").replace(",", ".")
    
    tabela.loc[linha, "Preço Atual"] = float(preco)
   
#gera uma tabela atualizada de acordo com preços 
tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
print(tabela)
tabela.to_excel("commodities_atualizado.xlsx", index=False)
navegador.quit()