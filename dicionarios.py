# > DICIONARIOS 

# Criando dicionarios 
dicionario ={}
dicionario = dict()
dicionario={'nome':'João', 'idade':30, 'altura':1.75}

print(dicionario)
print(dicionario['idade'])


# Adicionando elementos
dicionario['programador'] = true
print(dicionario)

dicionario['idade'] = 31
print(dicionario)

#Iterando sobre dicionários
for chave in dicionario:
    print(f'{chave}: {dicionario[chave]}')
    
# Testando a existência de uma chave

print('nome' in dicionario)  # True
print('peso' in dicionario)  # False