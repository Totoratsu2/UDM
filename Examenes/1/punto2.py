from random import randint


def main():
    numero_r = randint(1, 20)
    numero = int(input("Ingrese un numero: ").strip())

    while numero != numero_r:
        if numero < numero_r:
            print("El numerado random es mayor")
        else:
            print("El numerado random es menor")

        numero = int(input("Ingrese un numero: ").strip())

    print("El numero ingresado es igual al numero random")


if __name__ == '__main__':
    main()
