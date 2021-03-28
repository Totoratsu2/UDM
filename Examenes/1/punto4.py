def main():
    multiplos = []
    contador = 3

    while len(multiplos) <= 100:
        if contador % 3 == 0:
            multiplos.append(contador)

        contador += 1

    print("Primeros 100 multiplos de 3:", *multiplos)


if __name__ == '__main__':
    main()
