# 🎓 Gestión Educativa

Programa en Python con **tres clases relacionadas** del ámbito educativo. Trabajo práctico de POO.

## Clases

| Clase | Atributos (5+) | Métodos (3+) |
|-------|----------------|--------------|
| `Profesor` | nombre, apellido, dni, especialidad, salario | `nombre_completo()`, `dar_aumento()`, `mostrar_info()` |
| `Estudiante` | nombre, apellido, legajo, edad, carrera, notas | `agregar_nota()`, `promedio()`, `mostrar_info()` |
| `Materia` | nombre, codigo, creditos, profesor, cupo, estudiantes | `inscribir_estudiante()`, `cantidad_inscriptos()`, `mostrar_info()` |

## Relación entre clases

Una `Materia` tiene **un** `Profesor` asignado y **una lista de** `Estudiante` inscriptos.

## Estructuras de datos en el `main`

Se crean tres listas con objetos cargados por el usuario vía `input()`:

- `profesores` → lista de `Profesor`
- `estudiantes` → lista de `Estudiante`
- `materias` → lista de `Materia`

## Cómo correr

```bash
python main.py
```

Solo requiere Python 3 (sin dependencias externas).
