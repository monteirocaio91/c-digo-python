def verificar_idade(idade):
    if idade < 18:
        return "Criança"
    else:
        return "Adulto"

def main():
    cpf = input("Digite o CPF (apenas números): ")
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
        return
    
    try:
        idade = int(input("Digite a sua idade: "))
        categoria = verificar_idade(idade)
        print(f"Você é um(a) {categoria}.")
    except ValueError:
        print("Por favor, digite uma idade válida.")

if __name__ == "__main__":
    main()