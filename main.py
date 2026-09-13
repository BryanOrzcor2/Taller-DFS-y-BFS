"""
main.py  -  Taller 2: Ejecución Consolidada (Puntos 7, 9 y 10)
============================================================
Ejecuta de forma secuencial y limpia:
  - Punto 7 & 8: Las 6 pruebas comparativas BFS vs DFS en la red base.
  - Punto 9: Prueba de usuarios sin conexión (Laura y Mateo).
  - Punto 10: Pruebas sobre la red modificada (16 usuarios, 5 nuevos y 8 conexiones).

Docente   : Joaquín F. Sánchez
Asignatura: Inteligencia Artificial - Maestría en IA - Sergio Arboleda 2026
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from red_social import red_social, red_social_modificada
from BFS import buscar_conexion_bfs
from DFS import buscar_conexion_dfs


def ejecutar_punto_7():
    print("\n" + "=" * 82)
    print("  PUNTO 7 & 8 - Pruebas de funcionamiento: BFS vs DFS (Red Base 11 nodos)")
    print("=" * 82)
    print(f"  {'P':>2}  {'Alg':<5}  {'Ruta':<43}  {'G':>2}  {'Exp':>4}  {'Gen':>4}  {'FMax':>5}")
    print("-" * 82)

    pruebas = [
        (1, "Ana",     "Karen"),
        (2, "Bruno",   "Jorge"),
        (3, "Diana",   "Isabel"),
        (4, "Gabriel", "Elena"),
        (5, "Felipe",  "Karen"),
        (6, "Helena",  "Ana"),
    ]

    for num, origen, destino in pruebas:
        for alg_nombre, fn in [("BFS", buscar_conexion_bfs), ("DFS", buscar_conexion_dfs)]:
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
        print(f"  {'-'*78}")
    print("=" * 82)


def ejecutar_punto_8():
    print("\n" + "=" * 82)
    print("  PUNTO 8 - Conclusiones del Analisis Comparativo BFS vs DFS")
    print("=" * 82)
    print("""
  1. Misma ruta? No siempre (solo en P1 y P5 por coincidencia favorable).
  2. Menor grados sep.? BFS siempre garantiza la ruta con menor o igual saltos.
  3. Menos expansiones? DFS expandio menos en promedio (6.16 vs 9.33), pero con
     alta variabilidad segun la rama elegida.
  4. Frontera mas grande? DFS alcanzo FMax de hasta 6 nodos (vs 4 de BFS).
  5. Orden de vecinos? En DFS es critico (la cima de la pila define la rama);
     en BFS solo define desempates en el mismo nivel.
  6. Sin conjunto visitados? Bucle infinito en DFS y desbordamiento RAM en BFS
     por ciclos triviales de longitud 2 (grafo no dirigido).
  7. Por que BFS garantiza la ruta mas corta? Monotonicidad de la cola FIFO:
     extrae nodos en orden no decreciente de profundidad (g(n)).
  8. DFS puede hallar primero una ruta mas larga? Si (ej. P3: 10 vs 3 grados).
  9. Limite de profundidad? Si limite < d*, pierde completitud; si limite >> d*,
     permite ramas innecesariamente largas.
  10. Algoritmo recomendado? BFS indiscutiblemente, ya que los grados de
      separacion se definen como la distancia geodesica minima (d_G(u, v)).
    """)
    print("=" * 82)


def ejecutar_punto_9():
    print("\n" + "=" * 82)
    print("  PUNTO 9 - Usuarios sin conexion (Componente desconectado)")
    print("=" * 82)
    # Crear copia de la red y agregar componente aislado según pide el PDF
    red_desconectada = {k: list(v) for k, v in red_social.items()}
    red_desconectada["Laura"] = ["Mateo"]
    red_desconectada["Mateo"] = ["Laura"]

    print("  Buscando conexion: Ana -> Laura...")
    res_bfs = buscar_conexion_bfs(red_desconectada, "Ana", "Laura")
    res_dfs = buscar_conexion_dfs(red_desconectada, "Ana", "Laura", limite_profundidad=10)

    for alg_nombre, r in [("BFS", res_bfs), ("DFS", res_dfs)]:
        print(f"\n  [{alg_nombre}]")
        print(f"    Encontrado       : {r['encontrado']}")
        print(f"    Ruta             : {r['ruta']}")
        print(f"    Nodos expandidos : {r['nodos_expandidos']} (todos los nodos de la componente)")
        print(f"    Nodos generados  : {r['nodos_generados']}")
        print(f"    Frontera maxima  : {r['frontera_maxima']}")
        print(f"    Estado frontera  : Vacia (termina normalmente sin solucion)")
    print("\n" + "=" * 82)


def ejecutar_punto_10():
    print("\n" + "=" * 82)
    print("  PUNTO 10 - Red Social Modificada (16 usuarios, 5 ficticios y 8 aristas)")
    print("=" * 82)
    print(f"  {'#':<3} {'Alg':<5} {'Ruta':<46} {'G':>3} {'Exp':>5} {'Gen':>5} {'FMax':>5}")
    print("-" * 82)

    pruebas_p10 = [
        (1, "Ana",   "Pedro"),   # Hacia el nodo periférico de grado 1
        (2, "Pedro", "Karen"),   # Cruce de extremo a extremo
        (3, "Luis",  "Elena"),   # Prueba de rutas alternativas
    ]

    for num, origen, destino in pruebas_p10:
        res_bfs = buscar_conexion_bfs(red_social_modificada, origen, destino)
        res_dfs = buscar_conexion_dfs(red_social_modificada, origen, destino, limite_profundidad=15)

        for alg_nombre, r in [("BFS", res_bfs), ("DFS", res_dfs)]:
            if r["encontrado"]:
                ruta_str = " -> ".join(r["ruta"]).replace("Néstor", "Nestor")
                g   = r["grados_separacion"]
                exp = r["nodos_expandidos"]
                gen = r["nodos_generados"]
                fmx = r["frontera_maxima"]
            else:
                ruta_str = "[sin conexion]"
                g = exp = gen = fmx = "-"

            print(f"  {num:<3} {alg_nombre:<5} {ruta_str:<46} {str(g):>3} {str(exp):>5} {str(gen):>5} {str(fmx):>5}")
        print(f"  {'-'*78}")
    print("=" * 82)


if __name__ == "__main__":
    ejecutar_punto_7()
    ejecutar_punto_8()
    ejecutar_punto_9()
    ejecutar_punto_10()


