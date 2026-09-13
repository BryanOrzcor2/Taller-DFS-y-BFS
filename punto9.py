"""
punto9.py  -  Punto 9: Usuarios sin conexión (Componente desconectado)
=====================================================================
Agrega un componente separado con Laura y Mateo y busca conexión
entre Ana y Laura con BFS y DFS.

Docente   : Joaquín F. Sánchez
Asignatura: Inteligencia Artificial - Maestría en IA - Sergio Arboleda 2026
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from red_social import red_social
from BFS import buscar_conexion_bfs
from DFS import buscar_conexion_dfs

# ── 1. Agregar el componente desconectado tal como pide el PDF ───────────────
red_social_p9 = {k: list(v) for k, v in red_social.items()}
red_social_p9["Laura"] = ["Mateo"]
red_social_p9["Mateo"] = ["Laura"]

def ejecutar_punto_9():
    print("\n" + "=" * 80)
    print("  PUNTO 9 - Usuarios sin conexion: Componente desconectado (Laura y Mateo)")
    print("=" * 80)
    print("  Componente 1: Red original (11 usuarios: Ana, Bruno, ..., Karen)")
    print("  Componente 2: Nuevo componente aislado (Laura <-> Mateo)")
    print("  Consulta    : Ana -> Laura")
    print("-" * 80)

    # ── 2. Ejecutar exactamente las dos llamadas solicitadas ─────────────────
    res_bfs = buscar_conexion_bfs(red_social_p9, "Ana", "Laura")
    res_dfs = buscar_conexion_dfs(red_social_p9, "Ana", "Laura", limite_profundidad=10)

    for alg_nombre, r in [("BFS", res_bfs), ("DFS", res_dfs)]:
        print(f"\n  [{alg_nombre}]")
        print(f"    Encontrado        : {r['encontrado']}")
        print(f"    Ruta              : {r['ruta']}")
        print(f"    Grados separacion : {r['grados_separacion']}")
        print(f"    Orden expansion   : {r['orden_expansion']}")
        print(f"    Nodos expandidos  : {r['nodos_expandidos']}")
        print(f"    Nodos generados   : {r['nodos_generados']}")
        print(f"    Frontera maxima   : {r['frontera_maxima']}")

        # Mensaje amigable al usuario que debe presentar el programa
        if not r["encontrado"]:
            print(f"    >> Mensaje del programa: 'No se encontro conexion entre Ana y Laura'")

    # ── 3. Respuestas al analisis solicitado en el PDF ───────────────────────
    print("\n" + "=" * 80)
    print("  ANALISIS TEORICO (Respuestas requeridas por el enunciado)")
    print("=" * 80)
    print("""
  1. Como se determina que no existe conexion?
     El bucle 'while frontera:' termina de manera natural porque la estructura
     de la frontera (cola en BFS o pila en DFS) queda completamente VACIA
     sin haber extraido nunca al nodo objetivo ('Laura').

  2. Que sucede con la frontera?
     Al inicio contiene [Ana]. A medida que avanza, va acumulando vecinos.
     Pero como todos los nodos alcanzables eventualmente entran a 'visitados',
     llega un momento donde ya no hay ningun vecino nuevo que agregar.
     La frontera se va vaciando con cada pop()/popleft() hasta que len(frontera) == 0.

  3. Cuantos usuarios se visitan?
     Se visitan exactamente 11 usuarios (todos los nodos pertenecientes a la
     componente conexa de Ana). Ningun usuario de la componente de Laura
     es jamas visitado ni generado.

  4. Que mensaje debe presentar el programa?
     Debe retornar: 'No se encontro conexion entre Ana y Laura'
     (o dict con encontrado=False y ruta=[]).
    """)
    print("=" * 80 + "\n")

if __name__ == "__main__":
    ejecutar_punto_9()
