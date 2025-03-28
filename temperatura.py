def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def main():
    print("Conversor de Temperaturas")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")
    
    escolha = int(input("Escolha uma opção (1-6): "))
    temperatura = float(input("Digite a temperatura: "))
    
    if escolha == 1:
        print(f"{temperatura}°C é igual a {celsius_para_fahrenheit(temperatura)}°F")
    elif escolha == 2:
        print(f"{temperatura}°F é igual a {fahrenheit_para_celsius(temperatura)}°C")
    elif escolha == 3:
        print(f"{temperatura}°C é igual a {celsius_para_kelvin(temperatura)}K")
    elif escolha == 4:
        print(f"{temperatura}K é igual a {kelvin_para_celsius(temperatura)}°C")
    elif escolha == 5:
        print(f"{temperatura}°F é igual a {fahrenheit_para_kelvin(temperatura)}K")
    elif escolha == 6:
        print(f"{temperatura}K é igual a {kelvin_para_fahrenheit(temperatura)}°F")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
