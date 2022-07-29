def celsiusAFahrenheit(celsius):
    f = celsius * 1.8 + 32
    return round(f)

def fahrenheitACelsius(fahrenheit):
    c = (fahrenheit - 32) / 1.8
    return round(c)

print(celsiusAFahrenheit(32))
print(fahrenheitACelsius(50))