lista = ["Larissa", "Maiara", "Nathalia", "Gabriel", "Pedro", "Mateus"]
def select_short(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return print("Contém na lista")
        else:
            return print("Não contém")

valor = input("Digite o nome procurado: ")
select_short(lista, valor)
indice = lista.index(valor)
print(f"o nome digitado esta no indice: {indice}")