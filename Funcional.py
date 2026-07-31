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
