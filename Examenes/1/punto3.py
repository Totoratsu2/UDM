def main():
    for _ in range(10):
        numero = int(input("Ingrese un numero: ").strip())
        factorial = 1

        for y in range(1, numero+1):
            factorial = factorial * y

        print("El facturial del numero", numero, "es", factorial)


if __name__ == '__main__':
    main()