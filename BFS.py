"""
BFS.py  –  Punto 5: Implementación de BFS
==========================================
Implementa la función buscar_conexion_bfs(red, origen, destino) tal como
lo pide el Taller 2 del Docente Joaquín F. Sánchez.

Retorna un diccionario con:
  encontrado       → bool
  ruta             → lista de usuarios desde origen hasta destino
  grados_separacion→ len(ruta) - 1
  orden_expansion  → lista de usuarios en el orden en que fueron extraídos
  nodos_expandidos → cantidad de nodos extraídos de la frontera
  nodos_generados  → cantidad de nodos insertados en la frontera
  frontera_maxima  → tamaño máximo que alcanzó la frontera (Cola FIFO)

Docente : Joaquín F. Sánchez
Asignatura: Inteligencia Artificial – Maestría en IA – Sergio Arboleda 2026
"""

from collections import deque


# ─────────────────────────────────────────────────────────────────────────────
# Función auxiliar: reconstruir la ruta siguiendo los punteros de padre
# ─────────────────────────────────────────────────────────────────────────────
def reconstruir_ruta(padres: dict, destino: str) -> list:
    """
    Recorre el diccionario de padres hacia atrás desde 'destino'
    hasta la raíz (cuyo padre es None) y devuelve la ruta en orden
    correcto (de origen a destino).

    Parámetros
    ----------
    padres  : dict  → {nodo: nodo_padre}  construido durante la búsqueda
    destino : str   → nombre del usuario objetivo

    Retorna
    -------
    list → secuencia de usuarios desde el origen hasta el destino
    """
    ruta = []
    actual = destino

    while actual is not None:          # sube por la cadena de padres
        ruta.append(actual)
        actual = padres[actual]

    ruta.reverse()                     # la cadena estaba al revés
    return ruta


# ─────────────────────────────────────────────────────────────────────────────
# Función principal: BFS sobre el grafo de la red social
# ─────────────────────────────────────────────────────────────────────────────
def buscar_conexion_bfs(red: dict, origen: str, destino: str) -> dict:
    """
    Busca la conexión más corta (en saltos) entre 'origen' y 'destino'
    usando Breadth-First Search (BFS) con Cola FIFO.

    Estrategia
    ----------
    1. Encolar el origen y marcarlo como visitado.
    2. Mientras la frontera no esté vacía:
       a. Extraer el nodo del frente (popleft → FIFO).
       b. Registrarlo en orden_expansion.
       c. Si es el destino → reconstruir y retornar la ruta.
       d. Para cada vecino no visitado:
          - Marcar como visitado (al encolarlo, prueba temprana).
          - Asignar el padre.
          - Encolar al final de la frontera.
          - Actualizar métricas.
    3. Si la frontera se vacía sin encontrar el destino → no hay ruta.

    Parámetros
    ----------
    red     : dict → grafo como lista de adyacencia {usuario: [vecinos]}
    origen  : str  → usuario de partida
    destino : str  → usuario objetivo

    Retorna
    -------
    dict con las métricas definidas en el enunciado del Taller 2
    """
    # ── Validación de entrada ─────────────────────────────────────────────
    if origen not in red or destino not in red:
        return {
            "encontrado": False,
            "mensaje": "El usuario no existe en la red."
        }

    # Caso trivial: origen == destino
    if origen == destino:
        return {
            "encontrado": True,
            "ruta": [origen],
            "grados_separacion": 0,
            "orden_expansion": [origen],
            "nodos_expandidos": 1,
            "nodos_generados": 1,
            "frontera_maxima": 1,
        }

    # ── Inicialización de estructuras ─────────────────────────────────────
    frontera        = deque([origen])   # Cola FIFO
    visitados       = {origen}          # Conjunto de nodos ya encolados
    padres          = {origen: None}    # Punteros para reconstruir la ruta
    orden_expansion = []                # Orden en que se extraen los nodos
    nodos_generados = 1                 # El origen ya fue generado
    frontera_maxima = 1                 # Tamaño máximo de la frontera

    # ── Bucle principal BFS ───────────────────────────────────────────────
    while frontera:

        # 1. Extraer el nodo del frente (FIFO)
        actual = frontera.popleft()
        orden_expansion.append(actual)

        # 2. Prueba de meta al expandir (válida en BFS sobre grafos no ponderados)
        if actual == destino:
            ruta = reconstruir_ruta(padres, destino)
            return {
                "encontrado":        True,
                "ruta":              ruta,
                "grados_separacion": len(ruta) - 1,
                "orden_expansion":   orden_expansion,
                "nodos_expandidos":  len(orden_expansion),
                "nodos_generados":   nodos_generados,
                "frontera_maxima":   frontera_maxima,
            }

        # 3. Expandir vecinos en el orden definido en el diccionario
        for vecino in red[actual]:
            if vecino not in visitados:          # control de visitados
                visitados.add(vecino)            # marcar al encolar
                padres[vecino] = actual          # registrar padre
                frontera.append(vecino)          # insertar al final de la cola
                nodos_generados += 1

                # Actualizar el tamaño máximo de la frontera
                if len(frontera) > frontera_maxima:
                    frontera_maxima = len(frontera)

    # ── Sin camino ───────────────────────────────────────────────────────
    return {
        "encontrado":        False,
        "ruta":              [],
        "grados_separacion": None,
        "orden_expansion":   orden_expansion,
        "nodos_expandidos":  len(orden_expansion),
        "nodos_generados":   nodos_generados,
        "frontera_maxima":   frontera_maxima,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Bloque de prueba rápida (se ejecuta solo si se llama directamente este archivo)
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from red_social import red_social

    pruebas = [
        ("Ana",    "Karen"),
        ("Bruno",  "Jorge"),
        ("Diana",  "Isabel"),
        ("Gabriel","Elena"),
        ("Felipe", "Karen"),
        ("Helena", "Ana"),
    ]

    print("=" * 65)
    print("  PUNTO 5 – BFS: Búsqueda de conexiones en la red social")
    print("=" * 65)

    for origen, destino in pruebas:
        resultado = buscar_conexion_bfs(red_social, origen, destino)
        print(f"\n>> {origen}  ->  {destino}")
        if resultado["encontrado"]:
            print(f"  Ruta             : {' -> '.join(resultado['ruta'])}")
            print(f"  Grados sep.      : {resultado['grados_separacion']}")
            print(f"  Orden expansion  : {resultado['orden_expansion']}")
            print(f"  Nodos expandidos : {resultado['nodos_expandidos']}")
            print(f"  Nodos generados  : {resultado['nodos_generados']}")
            print(f"  Frontera maxima  : {resultado['frontera_maxima']}")
        else:
            print(f"  [!] No se encontro conexion.")
    print("\n" + "=" * 65)
