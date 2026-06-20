# 📋 Generador de Base de Datos de Pacientes Mexicanos

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

Generador de datos ficticios pero realistas de pacientes mexicanos para bases de datos, pruebas de software, demostraciones y desarrollo de aplicaciones de salud.

## 📑 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso Rápido](#uso-rápido)
- [Estructura de Datos](#estructura-de-datos)
- [Funciones Disponibles](#funciones-disponibles)
- [Ejemplos de Código](#ejemplos-de-código)
- [Personalización](#personalización)
- [Validación de Datos](#validación-de-datos)
- [Contribución](#contribución)
- [Licencia](#licencia)

## ✨ Características

- 🇲🇽 **Datos Mexicanos Realistas**: Nombres, apellidos, direcciones, estados y códigos postales de México
- 🏥 **Datos de Salud Completos**: Edad, estatura, peso, IMC, alergias y medicamentos actuales
- 📊 **Múltiples Funciones**: Generación, consulta, búsqueda y filtrado de pacientes
- 🔍 **Búsqueda Avanzada**: Filtrado por alergias, sexo, rango de edad y más
- 📈 **Estadísticas Automáticas**: Resúmenes y análisis de los datos generados
- 🛡️ **Validación Integrada**: Datos consistentes y realistas
- 📁 **Formato JSON**: Fácil integración con cualquier aplicación o base de datos
- 🚀 **Escalable**: Genera desde 10 hasta miles de registros

## 📋 Requisitos

```bash
Python 3.7 o superior
Módulos:
- json (estándar)
- random (estándar)
- datetime (estándar)
- collections (estándar)
```

## 🔧 Instalación

### Opción 1: Clonar el repositorio
```bash
git clone https://github.com/Cyberghxst/GeneradorPacientes.git
cd GeneradorPacientes
```

### Opción 2: Descarga directa
1. Descarga el archivo `generador_pacientes.py`
2. Guárdalo en tu proyecto

### Opción 3: Usar el script directamente
```bash
wget https://raw.githubusercontent.com/Cyberghxst/GeneradorPacientes/refs/heads/main/generador_pacientes.py
```

## 🚀 Uso Rápido

### Generar base de datos básica
```python
from generador_pacientes import generar_base_datos_json

# Generar 50 pacientes
pacientes = generar_base_datos_json(50, "pacientes.json")
```

### Ejecutar desde línea de comandos
```bash
python generador_pacientes.py
```

### Ejemplo de salida
```
🚀 GENERADOR DE BASE DE DATOS DE PACIENTES MEXICANOS
======================================================================
✅ Base de datos generada exitosamente: pacientes_mexicanos.json
📊 Total de registros: 50

📈 Estadísticas generadas:
  Edad promedio: 42.3 años
  Estatura promedio: 164.8 cm
  Peso promedio: 72.5 kg
  Total de alergias registradas: 45
```

## 📊 Estructura de Datos

Cada paciente tiene la siguiente estructura JSON:

```json
{
  "id": 1,
  "nombre_completo": "María García Hernández",
  "nombre": "María",
  "apellido_paterno": "García",
  "apellido_materno": "Hernández",
  "sexo": "F",
  "fecha_nacimiento": "1985-06-15",
  "edad": 39,
  "estatura_cm": 162,
  "peso_kg": 68.5,
  "alergias_medicamentos": ["Penicilina", "Amoxicilina"],
  "medicamentos_actuales": ["Metformina", "Losartán"],
  "direccion": {
    "calle": "Calle 342",
    "colonia": "La Condesa",
    "ciudad": "Ciudad de México",
    "estado": "CDMX",
    "codigo_postal": "06100"
  },
  "telefono": "5512345678",
  "email": "maria.garcia@email.com",
  "contacto_emergencia": {
    "nombre": "Juan Martínez",
    "relacion": "Hermano",
    "telefono": "5598765432"
  },
  "fecha_registro": "2024-01-15 10:30:00"
}
```

### Campos Detallados

| Campo | Tipo | Descripción | Rango/Formato |
|-------|------|-------------|---------------|
| `id` | Integer | Identificador único | 1 - ∞ |
| `nombre_completo` | String | Nombre completo | 3-100 caracteres |
| `sexo` | String | Sexo | 'M' o 'F' |
| `edad` | Integer | Edad en años | 0 - 120 |
| `estatura_cm` | Integer | Estatura en cm | 50 - 250 |
| `peso_kg` | Float | Peso en kg | 2 - 300 |
| `alergias` | Array | Lista de alergias | 0-3 alergias |
| `medicamentos` | Array | Medicamentos actuales | 0-4 medicamentos |

## 🛠️ Funciones Disponibles

### 1. `generar_base_datos_json(cantidad, archivo)`
Genera una base de datos completa con datos ficticios.

**Parámetros:**
- `cantidad` (int): Número de pacientes a generar
- `archivo` (str): Nombre del archivo JSON de salida

**Retorna:** Lista de pacientes generados

**Ejemplo:**
```python
pacientes = generar_base_datos_json(100, "mi_base_datos.json")
```

### 2. `consultar_base_datos(archivo)`
Lee y muestra estadísticas de la base de datos.

**Parámetros:**
- `archivo` (str): Ruta del archivo JSON

**Retorna:** Lista de pacientes cargados

**Ejemplo:**
```python
pacientes = consultar_base_datos("pacientes.json")
```

### 3. `buscar_por_alergia(alergia, archivo)`
Busca pacientes con una alergia específica.

**Parámetros:**
- `alergia` (str): Alergia a buscar
- `archivo` (str): Ruta del archivo JSON

**Retorna:** Lista de pacientes con esa alergia

**Ejemplo:**
```python
alergicos_penicilina = buscar_por_alergia("Penicilina", "pacientes.json")
```

### 4. `filtrar_pacientes(sexo, edad_min, edad_max, archivo)`
Filtra pacientes por sexo y rango de edad.

**Parámetros:**
- `sexo` (str): 'M' o 'F' (opcional)
- `edad_min` (int): Edad mínima (opcional)
- `edad_max` (int): Edad máxima (opcional)
- `archivo` (str): Ruta del archivo JSON

**Retorna:** Lista de pacientes filtrados

**Ejemplo:**
```python
mujeres_30_50 = filtrar_pacientes(sexo="F", edad_min=30, edad_max=50)
```

## 💡 Ejemplos de Código

### Ejemplo 1: Generar y analizar datos
```python
from generador_pacientes import *

# Generar pacientes
pacientes = generar_base_datos_json(30, "clinica.json")

# Buscar pacientes con alergias
for paciente in pacientes:
    if paciente['alergias_medicamentos']:
        print(f"{paciente['nombre_completo']} - Alergias: {', '.join(paciente['alergias_medicamentos'])}")

# Filtrar pacientes con sobrepeso (IMC > 25)
for paciente in pacientes:
    altura_m = paciente['estatura_cm'] / 100
    imc = paciente['peso_kg'] / (altura_m ** 2)
    if imc > 25:
        print(f"⚠️ {paciente['nombre_completo']} - IMC: {imc:.1f}")
```

### Ejemplo 2: Exportar a CSV
```python
import csv
import json

# Leer JSON
with open('pacientes.json', 'r', encoding='utf-8') as f:
    pacientes = json.load(f)

# Exportar a CSV
with open('pacientes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Nombre', 'Sexo', 'Edad', 'Estatura', 'Peso', 'Alergias'])
    
    for p in pacientes:
        alergias = '; '.join(p['alergias_medicamentos']) if p['alergias_medicamentos'] else 'Ninguna'
        writer.writerow([
            p['id'], 
            p['nombre_completo'], 
            p['sexo'], 
            p['edad'],
            p['estatura_cm'],
            p['peso_kg'],
            alergias
        ])
```

### Ejemplo 3: Análisis estadístico
```python
import json
from collections import Counter

def analizar_pacientes(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        pacientes = json.load(f)
    
    # Análisis demográfico
    edades = [p['edad'] for p in pacientes]
    print(f"Edad promedio: {sum(edades)/len(edades):.1f} años")
    print(f"Edad mínima: {min(edades)} años")
    print(f"Edad máxima: {max(edades)} años")
    
    # Distribución por sexo
    sexos = Counter([p['sexo'] for p in pacientes])
    print(f"Hombres: {sexos['M']}, Mujeres: {sexos['F']}")
    
    # Alergias más comunes
    alergias = []
    for p in pacientes:
        alergias.extend(p['alergias_medicamentos'])
    
    alergias_comunes = Counter(alergias).most_common(5)
    print("Alergias más comunes:")
    for alergia, count in alergias_comunes:
        print(f"  - {alergia}: {count} pacientes")
    
    return pacientes

analizar_pacientes("pacientes.json")
```

## 🎨 Personalización

### Agregar más nombres mexicanos
```python
nombres_hombres_extra = ["Leonardo", "Emiliano", "Santiago", "Mateo"]
nombres_mujeres_extra = ["Valentina", "Regina", "Camila", "Sofía"]

# Agregar a las listas en el script
```

### Agregar más alergias
```python
alergias_extra = [
    "Albuterol",
    "Prednisona",
    "Insulina NPH",
    "Warfarina",
    "Heparina"
]
```

### Modificar rangos de estatura
```python
# Cambiar la media y desviación estándar
if sexo == "M":
    return round(random.gauss(172, 7))  # Hombres más altos
else:
    return round(random.gauss(160, 6))  # Mujeres más altas
```

## ✅ Validación de Datos

El script incluye validaciones automáticas:

- ✅ **Edad**: Calculada automáticamente desde fecha de nacimiento
- ✅ **Sexo**: Solo 'M' o 'F'
- ✅ **Teléfonos**: Formato de 10 dígitos
- ✅ **Códigos Postales**: Formato de 5 dígitos
- ✅ **Alergias**: Sin duplicados en la lista
- ✅ **Rangos**: Edad, estatura y peso dentro de rangos realistas

## 🔄 Integración con otras herramientas

### MongoDB
```python
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['clinica']
collection = db['pacientes']

with open('pacientes.json', 'r') as f:
    pacientes = json.load(f)

collection.insert_many(pacientes)
```

### SQLite
```python
import sqlite3
import json

conn = sqlite3.connect('pacientes.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY,
        nombre_completo TEXT,
        sexo TEXT,
        edad INTEGER,
        estatura_cm INTEGER,
        peso_kg REAL
    )
''')

# Insertar datos
with open('pacientes.json', 'r') as f:
    pacientes = json.load(f)

for p in pacientes:
    cursor.execute('''
        INSERT INTO pacientes VALUES (?, ?, ?, ?, ?, ?)
    ''', (p['id'], p['nombre_completo'], p['sexo'], 
          p['edad'], p['estatura_cm'], p['peso_kg']))

conn.commit()
conn.close()
```

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios
4. Haz commit: `git commit -m 'Agrega nueva funcionalidad'`
5. Push: `git push origin feature/nueva-funcionalidad`
6. Abre un Pull Request

### Áreas de mejora posibles:
- [ ] Agregar más estados y ciudades mexicanas
- [ ] Incluir enfermedades crónicas
- [ ] Agregar grupo sanguíneo
- [ ] Exportar a otros formatos (Excel, XML)
- [ ] Interfaz gráfica (GUI)
- [ ] API REST para generación on-demand

## 📝 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

**Hecho con ❤️ para la comunidad de desarrolladores en México**

⭐ Si te es útil, ¡no olvides darle una estrella!
