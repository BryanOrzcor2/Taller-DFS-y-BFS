"""
punto10.py  -  Punto 10: Modificación de la red social
======================================================
Ejecuta BFS y DFS sobre la red social modificada que incorpora
5 usuarios ficticios y 8 nuevas conexiones cumpliendo:
  - Red no dirigida (bidireccional).
  - Sin auto-conexiones ni duplicados.
  - Al menos una ruta alternativa.
  - Un usuario con una sola conexión (Pedro -> grado 1).

Docente   : Joaquín F. Sánchez
Asignatura: Inteligencia Artificial - Maestría en IA - Sergio Arboleda 2026
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from red_social import red_social_modificada
from BFS import buscar_conexion_bfs
from DFS import buscar_conexion_dfs

# ── 3 Pares de prueba seleccionados ──────────────────────────────────────────
# Par 1: Ana -> Pedro   (Prueba alcanzar al nuevo usuario periférico de grado 1)
# Par 2: Pedro -> Karen (Prueba cruzar desde el nuevo extremo hasta el extremo opuesto)
# Par 3: Luis -> Elena  (Prueba el nuevo cluster y las rutas alternativas creadas)
PRUEBAS_P10 = [
    ("Ana",   "Pedro"),
    ("Pedro", "Karen"),
    ("Luis",  "Elena"),
]

def ejecutar_punto_10():
    print("\n" + "=" * 82)
    print("  PUNTO 10 - Pruebas sobre la Red Social Modificada (16 usuarios)")
    print("=" * 82)
    print(f" {'#':<3} {'Alg':<5} {'Ruta':<46} {'G':>3} {'Exp':>5} {'Gen':>5} {'FMax':>5}")
    print("-" * 82)

    resultados_detalle = []

    for i, (origen, destino) in enumerate(PRUEBAS_P10, 1):
        res_bfs = buscar_conexion_bfs(red_social_modificada, origen, destino)
        res_dfs = buscar_conexion_dfs(red_social_modificada, origen, destino, limite_profundidad=15)

        for alg_nombre, r in [("BFS", res_bfs), ("DFS", res_dfs)]:
            if r["encontrado"]:
                ruta_str = " -> ".join(r["ruta"])
                g   = r["grados_separacion"]
                exp = r["nodos_expandidos"]
                gen = r["nodos_generados"]
                fmx = r["frontera_maxima"]
            else:
                ruta_str = "[sin conexion]"
                g = exp = gen = fmx = "-"

            print(f" {i:<3} {alg_nombre:<5} {ruta_str:<46} {str(g):>3} {str(exp):>5} {str(gen):>5} {str(fmx):>5}")

        print("  " + "-" * 78)
        resultados_detalle.append((i, origen, destino, res_bfs, res_dfs))

    print("=" * 82)

    # Detalle con orden de expansión
    print("\n" + "=" * 82)
    print("  DETALLE COMPLETO (Orden de expansion)")
    print("=" * 82)
    for i, origen, destino, r_bfs, r_dfs in resultados_detalle:
        print(f"\n  Prueba {i}: {origen} -> {destino}")
        print(f"  {'-'*60}")
        for alg_nom, r in [("BFS", r_bfs), ("DFS", r_dfs)]:
            print(f"\n  [{alg_nom}]")
            if r["encontrado"]:
                print(f"    Ruta             : {' -> '.join(r['ruta'])}")
                print(f"    Grados sep.      : {r['grados_separacion']}")
                print(f"    Orden expansion  : {r['orden_expansion']}")
                print(f"    Nodos expandidos : {r['nodos_expandidos']}")
                print(f"    Nodos generados  : {r['nodos_generados']}")
                print(f"    Frontera maxima  : {r['frontera_maxima']}")
            else:
                print(f"    [!] Sin conexion.")
    print("\n" + "=" * 82)

if __name__ == "__main__":
    ejecutar_punto_10()
