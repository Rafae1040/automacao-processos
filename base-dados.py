# Importar a base de vendas e usar o pandas
import pandas as pd

# A base de dados esta no repositorio

tabela = pd.read_excel(r"C:\Users\rafae\Downloads\vendas.xlsx")
print(tabela)


# Calcular os indicadores da empresa
# Faturamento e Quantidade de Produtos

faturamento = tabela["Valor Final"].sum()
print(faturamento)
quantidade = tabela["Quantidade"].sum()
print(quantidade)