# ========================================
# Sistema simple de búsqueda de rutas
# usando búsqueda informada (A*)
# ========================================

import heapq
import math

# Definir las paradas del sistema
# Cada parada tiene: nombre, coordenadas (latitud, longitud)
paradas = {
    "A": (0, 0),
    "B": (1, 2),
    "C": (2, 4),
    "D": (4, 4),
    "E": (5, 1)
}

# Definir las conexiones entre paradas
# Cada conexión tiene un costo (minutos de viaje)
conexiones = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 7},
    "C": {"A": 10, "D": 3, "E": 12},
    "D": {"B": 7, "C": 3, "E": 4},
    "E": {"C": 12, "D": 4}
}

# Función heurística
# Calcula la distancia entre dos paradas
def heuristica(nodo_actual, nodo_objetivo):
    x1, y1 = paradas[nodo_actual]
    x2, y2 = paradas[nodo_objetivo]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Algoritmo de búsqueda A*
def busqueda_a_star(inicio, objetivo):
    # Cola prioridad (f = g + h, nodo, camino, costo_acumulado)
    frontera = []
    heapq.heappush(frontera, (0, inicio, [inicio], 0))

    visitados = set()

    while frontera:
        f, nodo, camino, g = heapq.heappop(frontera)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        # retornar el resultado
        if nodo == objetivo:
            return camino, g

        # Revisar vecinos
        for vecino, costo in conexiones[nodo].items():
            if vecino not in visitados:
                g_nuevo = g + costo
                h = heuristica(vecino, objetivo)
                f_nuevo = g_nuevo + h
                heapq.heappush(frontera, (f_nuevo, vecino, camino + [vecino], g_nuevo))

    return None, math.inf

# Ejemplo de uso del sistema
if __name__ == "__main__":
    inicio = "B"
    destino = "E"
    ruta, tiempo = busqueda_a_star(inicio, destino)

    if ruta:
        print("Ruta encontrada:", " -> ".join(ruta))
        print("Tiempo estimado:", tiempo, "minutos")
    else:
        print("No hay ruta posible entre", inicio, "y", destino)
