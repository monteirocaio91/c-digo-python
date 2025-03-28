lista = [4, 28, 10, 5, 18, 25, 13]
def select_short(lista, valor):
    for elemento in lista:
        if elemento == valor:
            return print("Contém na lista")
        else:
            return print("Não contém")
        
valor = int(input("Digite o valor procurado: "))
select_short(lista, valor)