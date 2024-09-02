import tracemalloc

# Simulación de memoria estática: variables globales
# Las variables globales se almacenan en la memoria estática
STATIC_VAR = "Soy una variable estática"

class DynamicMemory:
    def __init__(self, size):
        # Simulación de memoria dinámica: objetos en el heap
        # La memoria dinámica se asigna en el heap
        self.data = [0] * size

def show_memory_snapshot():
    # Muestra un snapshot de la memoria actualmente usada
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    
    print("\nTop 10 lugares con más uso de memoria:")
    for stat in top_stats[:10]:
        print(stat)

def main():
    tracemalloc.start()

    print("Inicio del programa")
    print(f"Variable estática: {STATIC_VAR}")

    show_memory_snapshot()

    # Simulación de uso de memoria dinámica
    print("\nAsignando memoria dinámica...")
    dynamic_var1 = DynamicMemory(100000)
    show_memory_snapshot()

    print("\nAsignando más memoria dinámica...")
    dynamic_var2 = DynamicMemory(200000)
    show_memory_snapshot()

    # Liberar memoria dinámica (automáticamente gestionado por Python)
    print("\nLiberando memoria dinámica...")
    del dynamic_var1
    del dynamic_var2
    tracemalloc.stop()

    print("\nFin del programa")

if __name__ == "__main__":
    main()
