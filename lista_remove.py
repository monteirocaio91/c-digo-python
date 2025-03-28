minha_lista = ['maçã', 'banana', 'laranja', 'uva']

# Exibindo a lista original
print("Lista original:", minha_lista)

# Removendo um item da lista
item_para_remover = 'banana'
if item_para_remover in minha_lista:
    minha_lista.remove(item_para_remover)
    print(f"{item_para_remover} foi removido da lista.")
else:
    print(f"{item_para_remover} não está na lista.")

# Exibindo a lista após a remoção
print("Lista após remoção:", minha_lista)
