opcionSeleccionar = int(input("seleciona una familia de la tabla periodica: "))

match opcionSeleccionar:
    case 1:
        print("Seleccionaste la familia de los metales alcalinos")
        print("Estos son los elementos de la familia de los metales alcalinos:")
        print("1. Litio (Li)")
        # break
    case 2:
        print("Seleccionaste la familia de los metales alcalinoterreos")
        print("Estos son los elementos de la familia de los metales alcalinoterreos:")
        print("1. Berilio (Be)")
        # break
    case 3:
        print("Seleccionaste la familia de los metales de transición")
        print("Estos son los elementos de la familia de los metales de transición:")
        print("1. Hierro (Fe)")
        # break
    case 4:
        print("Seleccionaste la familia de los metales del bloque p")
        print("Estos son los elementos de la familia de los metales del bloque p:")
        print("1. Galio (Ga)")
        # break
    case 5:
        print("Seleccionaste la familia de los metales del bloque d")
        print("Estos son los elementos de la familia de los metales del bloque d:")
        print("1. Manganeso (Mn)")
        # break
    case _:
        print("Opción no válida")
        # break