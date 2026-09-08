"""
DFS.py  -  Punto 6: Implementacion de DFS
==========================================
Implementa la funcion buscar_conexion_dfs(red, origen, destino, limite_profundidad)
tal como lo pide el Taller 2 del Docente Joaquin F. Sanchez.

Retorna un diccionario con:
  encontrado        -> bool
  ruta              -> lista de usuarios desde origen hasta destino
  grados_separacion -> len(ruta) - 1
  orden_expansion   -> lista de usuarios en el orden en que fueron extraidos
  nodos_expandidos  -> cantidad de nodos extraidos de la frontera
  nodos_generados   -> cantidad de nodos insertados en la frontera (pila)
  frontera_maxima   -> tamano maximo que alcanzo la pila LIFO

Docente   : Joaquin F. Sanchez
Asignatura: Inteligencia Artificial - Maestria en IA - Sergio Arboleda 2026
"""

# ─────────────────────────────────────────────────────────────────────────────
# Funcion auxiliar compartida con BFS: reconstruir la ruta por punteros de padre
# ─────────────────────────────────────────────────────────────────────────────
def reconstruir_ruta(padres: dict, destino: str) -> list:
    """
    Sube por la cadena de padres desde 'destino' hasta la raiz
    (cuyo padre es None) y devuelve la ruta en orden correcto.

    Parametros
    ----------
    padres  : dict -> {nodo: nodo_padre}
    destino : str  -> nombre del usuario objetivo

    Retorna
    -------
    list -> secuencia de usuarios desde el origen hasta el destino
    """
    ruta = []
    actual = destino

    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]

    ruta.reverse()
    return ruta


# ─────────────────────────────────────────────────────────────────────────────
# Funcion principal: DFS sobre el grafo de la red social
# ─────────────────────────────────────────────────────────────────────────────
def buscar_conexion_dfs(
    red: dict,
    origen: str,
    destino: str,
    limite_profundidad: int = 10
) -> dict:
    """
    Busca una conexion entre 'origen' y 'destino' usando
    Depth-First Search (DFS) con Pila LIFO.

    Estrategia
    ----------
    1. Apilar el origen (profundidad 0).
    2. Mientras la pila no este vacia:
       a. Sacar el nodo de la CIMA (pop -> LIFO).
       b. Si ya fue visitado -> ignorar (continue).
       c. Marcarlo como visitado y registrarlo en orden_expansion.
       d. Si es el destino -> reconstruir y retornar la ruta.
       e. Si se supero el limite de profundidad -> cortar esa rama.
       f. Para cada vecino NO visitado (en orden del diccionario):
          - Registrar padre (solo la primera vez que se descubre).
          - Apilar el vecino con profundidad + 1.
          - Actualizar metricas.
    3. Si la pila se vacia sin encontrar el destino -> no hay ruta.

    Diferencia clave respecto a BFS
    --------------------------------
    - La estructura es una PILA (list con .pop()) en lugar de una Cola.
    - El nodo se marca visitado al EXTRAER (prueba tardia), no al apilar.
    - Esto permite que DFS siga la primera rama hasta el fondo antes
      de retroceder (backtracking).

    Parametros
    ----------
    red                : dict -> grafo como lista de adyacencia
    origen             : str  -> usuario de partida
    destino            : str  -> usuario objetivo
    limite_profundidad : int  -> profundidad maxima permitida (default 10)

    Retorna
    -------
    dict con las metricas definidas en el enunciado del Taller 2
    """
    # -- Validacion de entrada ------------------------------------------------
    if origen not in red or destino not in red:
        return {
            "encontrado": False,
            "mensaje": "El usuario no existe en la red."
        }

    # Caso trivial
    if origen == destino:
        return {
            "encontrado":        True,
            "ruta":              [origen],
            "grados_separacion": 0,
            "orden_expansion":   [origen],
            "nodos_expandidos":  1,
            "nodos_generados":   1,
            "frontera_maxima":   1,
        }

    # -- Inicializacion de estructuras ----------------------------------------
    # Cada elemento de la pila es una tupla (usuario, profundidad_actual)
    frontera        = [(origen, 0)]    # Pila LIFO
    visitados       = set()            # Se marca al EXTRAER (diferencia con BFS)
    padres          = {origen: None}   # Punteros para reconstruir la ruta
    orden_expansion = []               # Orden en que se extraen y procesan nodos
    nodos_generados = 1                # El origen ya fue generado
    frontera_maxima = 1                # Tamano maximo de la pila

    # -- Bucle principal DFS --------------------------------------------------
    while frontera:

        # 1. Extraer el nodo de la CIMA de la pila (LIFO)
        actual, profundidad = frontera.pop()

        # 2. Si ya fue visitado, descartar (puede ocurrir porque DFS apila
        #    vecinos sin marcarlos visitados, y el mismo nodo puede estar
        #    apilado multiples veces desde diferentes caminos)
        if actual in visitados:
            continue

        # 3. Marcar como visitado al extraer
        visitados.add(actual)
        orden_expansion.append(actual)

        # 4. Prueba de meta (tardia: al extraer de la pila)
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

        # 5. Respetar el limite de profundidad: cortar la rama si se supero
        if profundidad >= limite_profundidad:
            continue

        # 6. Generar e insertar vecinos en la pila LIFO
        #    Se insertan en orden INVERSO al del diccionario para que el
        #    primer vecino listado sea el primero en salir de la cima.
        for vecino in reversed(red[actual]):
            if vecino not in visitados:
                # Registrar padre solo la primera vez que se descubre
                if vecino not in padres:
                    padres[vecino] = actual
                frontera.append((vecino, profundidad + 1))
                nodos_generados += 1

                # Actualizar tamano maximo de la frontera
                if len(frontera) > frontera_maxima:
                    frontera_maxima = len(frontera)

    # -- Sin camino -----------------------------------------------------------
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
# Bloque de prueba rapida (Puntos 7 y 8 del taller)
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from red_social import red_social
    from BFS import buscar_conexion_bfs

    pruebas = [
        ("Ana",     "Karen"),
        ("Bruno",   "Jorge"),
        ("Diana",   "Isabel"),
        ("Gabriel", "Elena"),
        ("Felipe",  "Karen"),
        ("Helena",  "Ana"),
    ]

    # ── Punto 7: Tabla comparativa BFS vs DFS ────────────────────────────
    print("=" * 80)
    print("  PUNTO 7 - Pruebas de funcionamiento: BFS vs DFS")
    print("=" * 80)
    print(f"{'P':>2}  {'Alg':<5}  {'Ruta':<45}  {'G':>2}  {'Exp':>3}  {'Gen':>3}  {'FMax':>4}")
    print("-" * 80)

    for i, (origen, destino) in enumerate(pruebas, start=1):
        for alg_nombre, fn in [("BFS", buscar_conexion_bfs),
                                ("DFS", buscar_conexion_dfs)]:
            r = fn(red_social, origen, destino) if alg_nombre == "BFS" \
                else buscar_conexion_dfs(red_social, origen, destino)
            if r["encontrado"]:
                ruta_str = " -> ".join(r["ruta"])
                g   = r["grados_separacion"]
                exp = r["nodos_expandidos"]
                gen = r["nodos_generados"]
                fmx = r["frontera_maxima"]
            else:
                ruta_str = "[sin ruta]"
                g = exp = gen = fmx = "-"
            print(f"{i:>2}  {alg_nombre:<5}  {ruta_str:<45}  {str(g):>2}  "
                  f"{str(exp):>3}  {str(gen):>3}  {str(fmx):>4}")

    print("=" * 80)

    # ── Punto 8: Detalle completo de cada prueba con DFS ─────────────────
    print("\n" + "=" * 65)
    print("  PUNTO 6 - DFS: Detalle de orden de expansion")
    print("=" * 65)

    for origen, destino in pruebas:
        resultado = buscar_conexion_dfs(red_social, origen, destino)
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
