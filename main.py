# Sistema de gestión educativa
# Tres clases relacionadas: Profesor, Estudiante y Materia.


class Profesor:
    def __init__(self, nombre, apellido, dni, especialidad, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.especialidad = especialidad
        self.antiguedad = antiguedad      # años de experiencia

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def cumplir_anio(self):
        self.antiguedad += 1
        return self.antiguedad

    def mostrar_info(self):
        print(f"Profesor: {self.nombre_completo()} | DNI: {self.dni} | "
              f"Especialidad: {self.especialidad} | Antigüedad: {self.antiguedad} años")


class Estudiante:
    def __init__(self, nombre, apellido, legajo, edad, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.edad = edad
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre} {self.apellido} | Legajo: {self.legajo} | "
              f"Edad: {self.edad} | Carrera: {self.carrera} | "
              f"Promedio: {self.promedio():.2f}")


class Materia:
    def __init__(self, nombre, codigo, creditos, profesor, cupo):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.profesor = profesor          # objeto Profesor
        self.cupo = cupo
        self.estudiantes = []             # lista de objetos Estudiante

    def inscribir_estudiante(self, estudiante):
        if len(self.estudiantes) >= self.cupo:
            print(f"  No hay cupo en {self.nombre}.")
            return False
        self.estudiantes.append(estudiante)
        print(f"  {estudiante.nombre} inscripto en {self.nombre}.")
        return True

    def cantidad_inscriptos(self):
        return len(self.estudiantes)

    def mostrar_info(self):
        prof = self.profesor.nombre_completo() if self.profesor else "Sin asignar"
        print(f"Materia: {self.nombre} ({self.codigo}) | Créditos: {self.creditos} | "
              f"Profesor: {prof} | Inscriptos: {self.cantidad_inscriptos()}/{self.cupo}")


def pedir_numero(mensaje):
    """Pide un número y reintenta si la entrada no es válida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  Valor inválido, ingresá un número.")


def main():
    profesores = []   # estructura 1: lista de Profesores
    estudiantes = []  # estructura 2: lista de Estudiantes
    materias = []     # estructura 3: lista de Materias

    print("=== CARGA DE PROFESORES ===")
    cant = int(pedir_numero("¿Cuántos profesores querés cargar? "))
    for i in range(cant):
        print(f"\nProfesor {i + 1}:")
        nombre = input("  Nombre: ")
        apellido = input("  Apellido: ")
        dni = input("  DNI: ")
        especialidad = input("  Especialidad: ")
        antiguedad = int(pedir_numero("  Antigüedad (años): "))
        profesores.append(Profesor(nombre, apellido, dni, especialidad, antiguedad))

    print("\n=== CARGA DE ESTUDIANTES ===")
    cant = int(pedir_numero("¿Cuántos estudiantes querés cargar? "))
    for i in range(cant):
        print(f"\nEstudiante {i + 1}:")
        nombre = input("  Nombre: ")
        apellido = input("  Apellido: ")
        legajo = input("  Legajo: ")
        edad = int(pedir_numero("  Edad: "))
        carrera = input("  Carrera: ")
        est = Estudiante(nombre, apellido, legajo, edad, carrera)
        cant_notas = int(pedir_numero("  ¿Cuántas notas cargar? "))
        for n in range(cant_notas):
            est.agregar_nota(pedir_numero(f"    Nota {n + 1}: "))
        estudiantes.append(est)

    print("\n=== CARGA DE MATERIAS ===")
    cant = int(pedir_numero("¿Cuántas materias querés cargar? "))
    for i in range(cant):
        print(f"\nMateria {i + 1}:")
        nombre = input("  Nombre: ")
        codigo = input("  Código: ")
        creditos = int(pedir_numero("  Créditos: "))
        cupo = int(pedir_numero("  Cupo: "))

        prof = None
        if profesores:
            print("  Profesores disponibles:")
            for idx, p in enumerate(profesores):
                print(f"    {idx} - {p.nombre_completo()}")
            sel = int(pedir_numero("  Elegí el profesor (número): "))
            if 0 <= sel < len(profesores):
                prof = profesores[sel]

        materia = Materia(nombre, codigo, creditos, prof, cupo)

        if estudiantes:
            print("  Estudiantes disponibles:")
            for idx, e in enumerate(estudiantes):
                print(f"    {idx} - {e.nombre} {e.apellido}")
            inscribir = input("  ¿Inscribir estudiantes? (s/n): ")
            if inscribir.lower() == "s":
                ids = input("  Números separados por coma (ej: 0,1): ")
                for x in ids.split(","):
                    x = x.strip()
                    if x.isdigit() and 0 <= int(x) < len(estudiantes):
                        materia.inscribir_estudiante(estudiantes[int(x)])

        materias.append(materia)

    print("\n========== RESUMEN ==========")
    print("\n-- Profesores --")
    for p in profesores:
        p.mostrar_info()
    print("\n-- Estudiantes --")
    for e in estudiantes:
        e.mostrar_info()
    print("\n-- Materias --")
    for m in materias:
        m.mostrar_info()


if __name__ == "__main__":
    main()
