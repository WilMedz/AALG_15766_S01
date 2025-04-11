def main():
    print("Ingrese los votos uno por uno (1-4 para candidatos, presione 0 para terminar):")

    candidato_1 = 0
    candidato_2 = 0
    candidato_3 = 0
    candidato_4 = 0
    total = 0

    while True:
        voto = input("Voto: ")

        try:
            voto = int(voto)
        except ValueError:
            print("El número ingresado no es válido")
            continue

        if voto == 0:
            break
        elif voto == 1:
            candidato_1 += 1
            total += 1
        elif voto == 2:
            candidato_2 += 1
            total += 1
        elif voto == 3:
            candidato_3 += 1
            total += 1
        elif voto == 4:
            candidato_4 += 1
            total += 1
        else:
            print("El número ingresado no es válido. Ingrese un número del 1 al 4")

    print("\n**** Resultados ****")
    print(f"La cantidad total de votos es: {total}")

    if total > 0:
        print(f"Candidato 1 obtuvo: {candidato_1} votos ({(candidato_1/total)*100:.2f}%)")
        print(f"Candidato 2 obtuvo: {candidato_2} votos ({(candidato_2/total)*100:.2f}%)")
        print(f"Candidato 3 obtuvo: {candidato_3} votos ({(candidato_3/total)*100:.2f}%)")
        print(f"Candidato 4 obtuvo: {candidato_4} votos ({(candidato_4/total)*100:.2f}%)")
    else:
        print("Los votos no han sido registrados")


if __name__ == "__main__":
    main()
