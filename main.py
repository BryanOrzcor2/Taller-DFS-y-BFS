"""
main.py  -  Punto 7: Pruebas de funcionamiento
================================================
Ejecuta BFS y DFS para las 6 consultas definidas en el Taller 2 y
presenta los resultados en la tabla comparativa del Punto 8.

Docente   : Joaquin F. Sanchez
Asignatura: Inteligencia Artificial - Maestria en IA - Sergio Arboleda 2026
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from red_social import red_social
from BFS import buscar_conexion_bfs
from DFS import buscar_conexion_dfs

# ─────────────────────────────────────────────────────────────────────────────
# Punto 7: Las 6 consultas definidas en el enunciado
# ─────────────────────────────────────────────────────────────────────────────
pruebas = [
    (1, "Ana",     "Karen"),
    (2, "Bruno",   "Jorge"),
    (3, "Diana",   "Isabel"),
    (4, "Gabriel", "Elena"),
    (5, "Felipe",  "Karen"),
    (6, "Helena",  "Ana"),
]

# ─────────────────────────────────────────────────────────────────────────────
# Tabla comparativa BFS vs DFS (Puntos 7 y 8)
# ─────────────────────────────────────────────────────────────────────────────
print()
print("=" * 82)
print("  PUNTO 7 - Pruebas de funcionamiento: BFS vs DFS")
print("=" * 82)
print(f"  {'P':>2}  {'Alg':<5}  {'Ruta':<43}  {'G':>2}  {'Exp':>4}  {'Gen':>4}  {'FMax':>5}")
print("-" * 82)

for num, origen, destino in pruebas:
    for alg_nombre, fn in [("BFS", buscar_conexion_bfs),
                            ("DFS", buscar_conexion_dfs)]:
        r = fn(red_social, origen, destino)

        if r["encontrado"]:
            ruta_str = " -> ".join(r["ruta"])
            g   = r["grados_separacion"]
            exp = r["nodos_expandidos"]
            gen = r["nodos_generados"]
            fmx = r["frontera_maxima"]
        else:
            ruta_str = "[sin conexion]"
            g = exp = gen = fmx = "-"

        print(f"  {num:>2}  {alg_nombre:<5}  {ruta_str:<43}  {str(g):>2}  "
              f"{str(exp):>4}  {str(gen):>4}  {str(fmx):>5}")

    # Linea separadora entre cada par de pruebas
    print(f"  {'-'*78}")

print("=" * 82)

# ─────────────────────────────────────────────────────────────────────────────
# Detalle expandido de cada prueba (para llenar la tabla del Punto 7 del PDF)
# ─────────────────────────────────────────────────────────────────────────────
print()
print("=" * 82)
print("  DETALLE COMPLETO POR PRUEBA (orden de expansion)")
print("=" * 82)

for num, origen, destino in pruebas:
    print(f"\n  Prueba {num}: {origen} -> {destino}")
    print(f"  {'-'*60}")

    for alg_nombre, fn in [("BFS", buscar_conexion_bfs),
                            ("DFS", buscar_conexion_dfs)]:
        r = fn(red_social, origen, destino)
        print(f"\n  [{alg_nombre}]")
        if r["encontrado"]:
            print(f"    Ruta             : {' -> '.join(r['ruta'])}")
            print(f"    Grados sep.      : {r['grados_separacion']}")
            print(f"    Orden expansion  : {r['orden_expansion']}")
            print(f"    Nodos expandidos : {r['nodos_expandidos']}")
            print(f"    Nodos generados  : {r['nodos_generados']}")
            print(f"    Frontera maxima  : {r['frontera_maxima']}")
        else:
            print(f"    [!] No se encontro conexion entre {origen} y {destino}.")

print("\n" + "=" * 82)
