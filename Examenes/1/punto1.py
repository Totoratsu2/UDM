def main():
    notas = []
    nota = 0

    while nota != -1:
        nota = float(input("Ingresar la nota: ").strip())

        if nota < 0 or nota > 5:
            print("La nota debe de estar en el rango 0 a 5")
            continue

        notas.append(nota)

    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
        print("Nota definitiva:", round(promedio, 2))
    else:
        print("No hay suficientes datos")


if __name__ == '__main__':
    main()
