# Name: Ejercicio de conversión de temperaturas
# Purpose: Programa para convertir temperaturas entre Celsius, Fahrenheit y Kelvin aplicando PEP 8
# Author: Jose David Montesino Hoyos
# Created: 21/04/2024

def parar():
    """Función para parar el programa en cada una de las opciones."""
    input("Presione <ENTER> para continuar: ")


def capturar():
    """Función que permite capturar los números que serán objetos de la operación."""
    try:
        temperatura = float(input("Por favor digite la temperatura: "))
        return temperatura
    except Exception as ex:
        print(ex)
        return 0.0


def celsius_fahrenheit(c):
    # F = (9/5) + 32
    return (c * 9/5) + 32


def celsius_kelvin(c):
    # K = °C + 273.15
    return c + 273.15


def kelvin_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def kelvin_celsius(k):
    return k - 273.15


def fahrenheit_kelvin(f):
    return (f - 32) * 5/9 + 273.15


def fahrenheit_celsius(f):
    # C = (°F - 32) * 5/9
    return (f - 32) * 5/9


def main():
    try:
        continuar = True
        t = 0.0

        while continuar:
            opcion = input(
                "Seleccione una opción:\n"
                "1 --> Capturar Temperatura\n"
                "2 --> Celsius a Fahrenheit\n"
                "3 --> Celsius a Kelvin\n"
                "4 --> Kelvin a Fahrenheit\n"
                "5 --> Kelvin a Celsius\n"
                "6 --> Fahrenheit a Kelvin\n"
                "7 --> Fahrenheit a Celsius\n"
                "0 --> Salir\n"
            )

            if opcion == '1':
                t = capturar()
            elif opcion == '2':
                print(f"{t}°C = {celsius_fahrenheit(t)}°F")
                parar()
            elif opcion == '3':
                print(f"{t}°C = {celsius_kelvin(t)}°K")
                parar()
            elif opcion == '4':
                print(f"{t}°K = {kelvin_fahrenheit(t)}°F")
                parar()
            elif opcion == '5':
                print(f"{t}°K = {kelvin_celsius(t)}°C")
                parar()
            elif opcion == '6':
                print(f"{t}°F = {fahrenheit_kelvin(t)}°K")
                parar()
            elif opcion == '7':
                print(f"{t}°F = {fahrenheit_celsius(t)}°C")
                parar()
            elif opcion == '0':
                print("Bye")
                continuar = False
            else:
                print("Seleccione una opción válida")
                parar()

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()