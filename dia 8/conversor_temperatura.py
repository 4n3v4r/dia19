# conversor temperatura
def celsius_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

def farenheit_celsius(farenheit):
    celsius = (farenheit - 32) * 5/9
    return round(celsius, 2)

celsius = float(input("Digite o valor em Celsius: "))
print(f"O valor em Farenheit é: {celsius_farenheit(celsius)} °F")

farenheit = float(input("Digite o valor em Farenheit: "))
print(f"O valor em Celsius é: {farenheit_celsius(farenheit)} °C")
