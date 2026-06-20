import json
import random
from datetime import datetime, timedelta

def generar_base_datos_json(cantidad=50, archivo="base_datos_pacientes.json"):
    """
    Genera una base de datos JSON con datos de pacientes mexicanos
    
    Args:
        cantidad: Número de registros a generar
        archivo: Nombre del archivo de salida
    """
    
    # Nombres y apellidos mexicanos comunes
    nombres_hombres = [
        "José", "Luis", "Carlos", "Juan", "Miguel", "Francisco", "Jesús", 
        "Antonio", "Alejandro", "Manuel", "Roberto", "Fernando", "Eduardo",
        "Daniel", "Jorge", "Ricardo", "Alberto", "Raúl", "Gerardo", "Héctor",
        "Arturo", "Sergio", "Omar", "Andrés", "David", "Rafael", "Mario",
        "Adrián", "Ángel", "Salvador", "Ignacio", "Rubén", "César", "Hugo"
    ]
    
    nombres_mujeres = [
        "María", "Guadalupe", "Juana", "Ana", "Rosa", "Carmen", "Martha",
        "Verónica", "Elizabeth", "Patricia", "Sandra", "Silvia", "Laura",
        "Angélica", "Gabriela", "Alejandra", "Teresa", "Alicia", "Leticia",
        "Norma", "Elena", "Monica", "Diana", "Rocio", "Cristina", "Isabel",
        "Claudia", "Andrea", "Paula", "Fernanda", "Karina", "Marisol", "Lorena"
    ]
    
    apellidos = [
        "García", "Martínez", "López", "González", "Pérez", "Rodríguez",
        "Sánchez", "Ramírez", "Flores", "Hernández", "Gómez", "Díaz",
        "Reyes", "Cruz", "Morales", "Vázquez", "Medina", "Torres", "Rivera",
        "Acosta", "Castillo", "Ortiz", "Mendoza", "Ramos", "Jiménez", "Ruiz",
        "Rojas", "Salazar", "Núñez", "Chávez", "Molina", "Castro", "Silva",
        "Velázquez", "Guzmán", "Méndez", "Bautista", "Romero", "Mejía", "Vega"
    ]
    
    # Alergias a medicamentos comunes
    alergias_comunes = [
        "Penicilina",
        "Amoxicilina",
        "Aspirina",
        "Ibuprofeno",
        "Paracetamol",
        "Naproxeno",
        "Cefalosporinas",
        "Sulfamidas",
        "Tetracielina",
        "Eritromicina",
        "Clindamicina",
        "Metronidazol",
        "Diclofenaco",
        "Codeína",
        "Morfina",
        "Anestésicos locales",
        "Anestésicos generales",
        "Insulina",
        "Vacunas (componentes)",
        "Contrastes yodados",
        "Lidocaína",
        "Corticoides",
        "Antihipertensivos",
        "Estatinas",
        "Omega 3",
        "Productos naturales"
    ]
    
    medicamentos_mexicanos = [
        "Paracetamol", "Ibuprofeno", "Aspirina", "Diclofenaco", "Omeprazol",
        "Metformina", "Losartán", "Atorvastatina", "Simvastatina", "Amoxicilina",
        "Azitromicina", "Ceftriaxona", "Levofloxacino", "Claritromicina",
        "Acetaminofén", "Naproxeno", "Tramadol", "Ketorolaco", "Morfina",
        "Lorazepam", "Alprazolam", "Diazepam", "Sertralina", "Fluoxetina",
        "Carbamazepina", "Gabapentina", "Levotiroxina", "Enalapril", "Captopril",
        "Nifedipino", "Amlodipino", "Furosemida", "Espironolactona", "Atropina",
        "Adrenalina", "Dexametasona", "Prednisona", "Metilprednisolona",
        "Cianocobalamina", "Ácido fólico", "Hierro", "Calcio", "Vitamina D"
    ]
    
    def generar_fecha_nacimiento():
        """Genera fecha de nacimiento aleatoria entre 1950 y 2006"""
        anio = random.randint(1950, 2006)
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        return f"{anio}-{mes:02d}-{dia:02d}"
    
    def calcular_edad(fecha_nac):
        """Calcula edad a partir de fecha de nacimiento"""
        nac = datetime.strptime(fecha_nac, "%Y-%m-%d")
        hoy = datetime.now()
        edad = hoy.year - nac.year - ((hoy.month, hoy.day) < (nac.month, nac.day))
        return edad
    
    def generar_estatura(sexo):
        """Genera estatura según sexo (distribución normal aproximada)"""
        if sexo == "M":
            return round(random.gauss(170, 8))  # Media 170cm, desviación 8
        else:
            return round(random.gauss(158, 7))  # Media 158cm, desviación 7
    
    def generar_peso(sexo, estatura):
        """Genera peso realista según sexo y estatura"""
        if sexo == "M":
            # IMC entre 18.5 y 30 para hombres
            imc = random.uniform(20, 28)
        else:
            # IMC entre 18.5 y 30 para mujeres
            imc = random.uniform(19, 27)
        
        altura_m = estatura / 100
        peso = imc * (altura_m ** 2)
        return round(peso, 1)
    
    def generar_alergias():
        """Genera lista de alergias (0-3 alergias por persona)"""
        num_alergias = random.choices([0, 1, 2, 3], weights=[40, 35, 15, 10])[0]
        
        if num_alergias == 0:
            return []
        
        # Seleccionar alergias aleatorias sin repetir
        alergias_seleccionadas = random.sample(alergias_comunes, num_alergias)
        return alergias_seleccionadas
    
    def generar_medicamentos():
        """Genera medicamentos que toma actualmente"""
        num_meds = random.choices([0, 1, 2, 3, 4], weights=[30, 30, 20, 15, 5])[0]
        if num_meds == 0:
            return []
        return random.sample(medicamentos_mexicanos, num_meds)
    
    def generar_direccion():
        """Genera dirección en México"""
        estados = [
            "CDMX", "Edo. México", "Jalisco", "Nuevo León", "Puebla",
            "Guanajuato", "Chihuahua", "Querétaro", "Yucatán", "Veracruz",
            "Sonora", "Coahuila", "Michoacán", "Guerrero", "Oaxaca", "Chiapas"
        ]
        
        colonias = [
            "Centro", "La Condesa", "Polanco", "Santa Fe", "Del Valle",
            "Coyoacán", "San Ángel", "Zona Roma", "Juárez", "Cuauhtémoc"
        ]
        
        return {
            "calle": f"Calle {random.randint(1, 1000)}",
            "colonia": random.choice(colonias),
            "ciudad": "Ciudad de México" if random.random() < 0.4 else random.choice(["Guadalajara", "Monterrey", "Puebla", "Querétaro", "Cancún"]),
            "estado": random.choice(estados),
            "codigo_postal": f"{random.randint(10000, 99999)}"
        }
    
    def generar_contacto_emergencia():
        """Genera contacto de emergencia"""
        relaciones = ["Padre", "Madre", "Hermano", "Hermana", "Esposo", "Esposa", "Hijo", "Hija", "Familiar"]
        return {
            "nombre": f"{random.choice(nombres_hombres + nombres_mujeres)} {random.choice(apellidos)}",
            "relacion": random.choice(relaciones),
            "telefono": f"55{random.randint(1000, 9999)}{random.randint(1000, 9999)}" if random.random() < 0.5 else f"{random.randint(10, 99)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
        }
    
    # Generar base de datos
    pacientes = []
    
    for i in range(cantidad):
        # Determinar sexo
        sexo = random.choice(["M", "F"])
        
        # Seleccionar nombre según sexo
        if sexo == "M":
            nombre = random.choice(nombres_hombres)
        else:
            nombre = random.choice(nombres_mujeres)
        
        apellido1 = random.choice(apellidos)
        apellido2 = random.choice(apellidos)
        
        # Generar fecha de nacimiento
        fecha_nac = generar_fecha_nacimiento()
        edad = calcular_edad(fecha_nac)
        
        # Generar estatura y peso
        estatura = generar_estatura(sexo)
        peso = generar_peso(sexo, estatura)
        
        # Generar alergias
        alergias = generar_alergias()
        
        # Crear registro del paciente
        paciente = {
            "id": i + 1,
            "nombre_completo": f"{nombre} {apellido1} {apellido2}",
            "nombre": nombre,
            "apellido_paterno": apellido1,
            "apellido_materno": apellido2,
            "sexo": sexo,
            "fecha_nacimiento": fecha_nac,
            "edad": edad,
            "estatura_cm": estatura,
            "peso_kg": peso,
            "alergias_medicamentos": alergias,
            "medicamentos_actuales": generar_medicamentos(),
            "direccion": generar_direccion(),
            "telefono": f"55{random.randint(1000, 9999)}{random.randint(1000, 9999)}",
            "email": f"{nombre.lower()}.{apellido1.lower()}@email.com",
            "contacto_emergencia": generar_contacto_emergencia(),
            "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        pacientes.append(paciente)
    
    # Guardar en archivo JSON
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(pacientes, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Base de datos generada exitosamente: {archivo}")
    print(f"📊 Total de registros: {len(pacientes)}")
    
    # Estadísticas básicas
    edades = [p["edad"] for p in pacientes]
    estaturas = [p["estatura_cm"] for p in pacientes]
    pesos = [p["peso_kg"] for p in pacientes]
    
    print("\n📈 Estadísticas generadas:")
    print(f"  Edad promedio: {sum(edades)/len(edades):.1f} años")
    print(f"  Estatura promedio: {sum(estaturas)/len(estaturas):.1f} cm")
    print(f"  Peso promedio: {sum(pesos)/len(pesos):.1f} kg")
    
    # Contar alergias
    total_alergias = sum(len(p["alergias_medicamentos"]) for p in pacientes)
    print(f"  Total de alergias registradas: {total_alergias}")
    
    return pacientes

# Función para leer y consultar la base de datos
def consultar_base_datos(archivo="base_datos_pacientes.json"):
    """Lee y muestra información de la base de datos"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            pacientes = json.load(f)
        
        print("\n" + "="*70)
        print("  CONSULTA DE BASE DE DATOS")
        print("="*70)
        print(f"Total de pacientes: {len(pacientes)}")
        
        # Mostrar los primeros 5 pacientes
        print("\n📋 PRIMEROS 5 PACIENTES:")
        print("-"*70)
        for paciente in pacientes[:5]:
            print(f"\nID: {paciente['id']}")
            print(f"Nombre: {paciente['nombre_completo']}")
            print(f"Sexo: {'Masculino' if paciente['sexo'] == 'M' else 'Femenino'}")
            print(f"Edad: {paciente['edad']} años")
            print(f"Estatura: {paciente['estatura_cm']} cm")
            print(f"Peso: {paciente['peso_kg']} kg")
            if paciente['alergias_medicamentos']:
                print(f"Alergias: {', '.join(paciente['alergias_medicamentos'])}")
            else:
                print("Alergias: Ninguna")
        
        # Estadísticas de alergias
        print("\n📊 ESTADÍSTICAS DE ALERGIAS:")
        print("-"*70)
        todas_alergias = []
        for p in pacientes:
            todas_alergias.extend(p['alergias_medicamentos'])
        
        from collections import Counter
        alergias_comunes = Counter(todas_alergias).most_common(10)
        print("Alergias más comunes:")
        for alergia, count in alergias_comunes:
            print(f"  {alergia}: {count} pacientes ({count/len(pacientes)*100:.1f}%)")
        
        return pacientes
        
    except FileNotFoundError:
        print("❌ Archivo no encontrado. Primero genera la base de datos.")
        return []
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return []

# Función para buscar por alergia
def buscar_por_alergia(alergia, archivo="base_datos_pacientes.json"):
    """Busca pacientes con una alergia específica"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            pacientes = json.load(f)
        
        resultados = [p for p in pacientes if alergia.lower() in [a.lower() for a in p['alergias_medicamentos']]]
        
        print(f"\n🔍 Pacientes alérgicos a: {alergia}")
        print("-"*70)
        print(f"Total encontrados: {len(resultados)}")
        
        for p in resultados:
            print(f"  {p['nombre_completo']} ({p['edad']} años, {'M' if p['sexo'] == 'M' else 'F'})")
        
        return resultados
        
    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
        return []

# Función para filtrar por sexo y rango de edad
def filtrar_pacientes(sexo=None, edad_min=None, edad_max=None, archivo="base_datos_pacientes.json"):
    """Filtra pacientes según criterios"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            pacientes = json.load(f)
        
        filtrados = pacientes
        
        if sexo:
            filtrados = [p for p in filtrados if p['sexo'] == sexo]
        
        if edad_min:
            filtrados = [p for p in filtrados if p['edad'] >= edad_min]
        
        if edad_max:
            filtrados = [p for p in filtrados if p['edad'] <= edad_max]
        
        print(f"\n📋 Resultados del filtro:")
        print("-"*70)
        print(f"Pacientes encontrados: {len(filtrados)}")
        
        for p in filtrados:
            print(f"  {p['nombre_completo']} - Edad: {p['edad']} - {'M' if p['sexo'] == 'M' else 'F'}")
        
        return filtrados
        
    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
        return []
