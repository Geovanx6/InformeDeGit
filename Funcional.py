from functools import reduce

estudiantes = [
    ("Ana", 95),
    ("Luis", 62),
    ("Carlos", 80),
    ("María", 48),
    ("Elena", 90),
]

def Aprobado(estudiante):
    nombre, nota = estudiante
    return nota >= 70

def Nota(estudiante):
    _, nota = estudiante
    return nota

def Nombre(estudiante):
    nombre, _ = estudiante
    return nombre

aprobados = tuple(filter(Aprobado, estudiantes))
nombres = tuple(map(Nombre, aprobados))
print("Estudiantes aprobados:")
print(nombres)

notas = tuple(map(lambda x: x[1], estudiantes))
promedio = reduce(lambda acumulado, nota: acumulado + nota,notas,0) / len(notas)
estados = tuple(map(lambda x: "Aprobado" if x[1] >= 70 else "Reprobado", estudiantes))
resultado = tuple(zip(map(Nombre, estudiantes), estados))

print("\nResultados:")
print(resultado)
print("\nPromedio:")
print(promedio)
print("\nListado completo")
list(map(lambda x: print(f"{x[0]:10} -> {x[1]}"),resultado))