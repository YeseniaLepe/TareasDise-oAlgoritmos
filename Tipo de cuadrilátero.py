lado_1 = float(input("Ingrese lado 1: "))
lado_2 = float(input("Ingrese lado 2: "))
lado_3 = float(input("Ingrese lado 3: "))
lado_4 = float(input("Ingrese lado 4: "))

if lado_1 > 0 and lado_2 > 0 and lado_3 > 0 and lado_4 > 0:
    lados = [lado_1, lado_2, lado_3, lado_4]

    def reconocer (lados):
        if len(set(lados)) == 1:
            return "Cuadrado"
        elif len(set(lados)) == 2:
            return "Rectangulo"
        else:
            return "Otro Cuadrilatero"

    tipo = reconocer (lados)

    print(f"La figura es: {tipo}")
else:
    print("No es un cuadrilatero valido")

