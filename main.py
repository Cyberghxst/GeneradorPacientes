from generador_pacientes import *

# Ejecutar script
if __name__ == "__main__":
    print("🚀 GENERADOR DE BASE DE DATOS DE PACIENTES MEXICANOS")
    print("="*70)
    
    # Generar base de datos con 50 pacientes
    pacientes = generar_base_datos_json(250, "pacientes_mexicanos.json")
    
    # Consultar la base de datos
    consultar_base_datos("pacientes_mexicanos.json")
    
    # Ejemplos de búsqueda
    print("\n" + "="*70)
    print("  EJEMPLOS DE BÚSQUEDA")
    print("="*70)
    
    # Buscar alérgicos a penicilina
    buscar_por_alergia("Penicilina", "pacientes_mexicanos.json")
    
    # Filtrar mujeres entre 30 y 50 años
    filtrar_pacientes(sexo="F", edad_min=30, edad_max=50, archivo="pacientes_mexicanos.json")
