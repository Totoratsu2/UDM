def main():
    primos = []
    numero = int(input("Ingresar un numero: ").strip())

    for y in range(1, numero+1):
        flag = False

        for j in range(2, y):
            if y % j == 0:
                flag = True

        if not flag:
            primos.append(y)

    print("Hay", len(primos), "numeros primos en el rango 1,", numero)
    print(*primos)


if __name__ == '__main__':
    main()
