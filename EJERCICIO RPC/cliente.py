import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:5048/")
    primer_numero = 9
    segundo_numero = 5

    try:
        resultado_suma = proxy.suma(primer_numero, segundo_numero)
        print(f"El resultado de la suma es: {resultado_suma}")

        resultado_resta = proxy.resta(primer_numero, segundo_numero)
        print(f"El resultado de la resta es: {resultado_resta}")

        resultado_multiplicacion = proxy.multiplicacion(primer_numero, segundo_numero)
        print(f"El resultado de la multiplicación es: {resultado_multiplicacion}")

        resultado_division = proxy.division(primer_numero, segundo_numero)
        print(f"El resultado de la división es: {resultado_division}")

        resultado_potencia = proxy.potencia(primer_numero, segundo_numero)
        print(f"El resultado de la potencia es: {resultado_potencia}")

    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor.")

if __name__ == "__main__":
    main()
