print("¡Hola! Bienvenido a MadLib")

print("Vamos a armar una historia, pero debes responder algunas preguntas...")
loop = 1

while loop > 10:
    r1 = str(input("Dinos... una profesion para el sujeto: "))

    print(r1, " Suena bien...")

    r2 = str(input("¿En que ciudad o lugar?: "))

    r3 = str(input("Indica a su pariente mas querido: "))

    print("Su ", r3 , "No me lo esperaba...")

    r4 = str(input("Cuentame que hacia nuestro protagonista: "))

    r5 = str(input("¿Cual es el artista favorito del protagonista?: "))
    print()
    print()

    print("Genial! la historia queda asi...")

    print()
    print()

    print("Habia una vez un ", r1 ," que solia caminar por las calles de " ,r2 , " buscando a su " ,r3 , " mientras " ,r4 , " y cantaba una cancion de " ,r5 , )

    loop = loop + 1.