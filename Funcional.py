from functools import reduce

def Aprobo(estudiante):
    nombre, nota = estudiante
    return nota >= 70


def Nota(estudiante):
    _, nota = estudiante
    return nota


def Nombre(estudiante):
    nombre, _ = estudiante
    return nombre

estudiantes = [
    ("Ana", 95),
    ("Luis", 62),
    ("Carlos", 80),
    ("María", 48),
    ("Elena", 90),
]

