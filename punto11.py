"""
punto11.py  -  Punto 11: Mejora del Sistema (Medición y Gráficas de Líneas)
===========================================================================
Mide con alta precisión (time.perf_counter_ns) los tiempos de ejecución de BFS y DFS,
genera gráficas en formato de líneas con marcadores para cada algoritmo y una
gráfica comparativa unificada final en líneas.

Docente   : Joaquín F. Sánchez
Asignatura: Inteligencia Artificial - Maestría en IA - Sergio Arboleda 2026
"""

import sys
import os
import time
import statistics
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from red_social import red_social
from BFS import buscar_conexion_bfs
from DFS import buscar_conexion_dfs

# Pares de prueba oficiales del Punto 7
PRUEBAS = [
    (1, "Ana",     "Karen"),
    (2, "Bruno",   "Jorge"),
    (3, "Diana",   "Isabel"),
    (4, "Gabriel", "Elena"),
    (5, "Felipe",  "Karen"),
    (6, "Helena",  "Ana"),
]

NUM_REPETICIONES = 1000

def benchmark_algoritmos():
    etiquetas = [f"P{num}\n({orig}→{dest})" for num, orig, dest in PRUEBAS]
    x_indices = list(range(len(PRUEBAS)))
    tiempos_bfs_us = []
    tiempos_dfs_us = []
    desv_bfs_us = []
    desv_dfs_us = []

    print("\n" + "=" * 86)
    print(f"  PUNTO 11 - Benchmark de Tiempo de Ejecución (Líneas / N = {NUM_REPETICIONES})")
    print("=" * 86)
    print(f"  {'Prueba':<20} | {'BFS Prom (µs)':<15} {'BFS Std':<10} | {'DFS Prom (µs)':<15} {'DFS Std':<10} | {'Diferencia':<10}")
    print("-" * 86)

    for num, orig, dest in PRUEBAS:
        # Calentamiento inicial
        buscar_conexion_bfs(red_social, orig, dest)
        buscar_conexion_dfs(red_social, orig, dest)

        # Muestreo BFS
        t_bfs = []
        for _ in range(NUM_REPETICIONES):
            inicio = time.perf_counter_ns()
            buscar_conexion_bfs(red_social, orig, dest)
            fin = time.perf_counter_ns()
            t_bfs.append((fin - inicio) / 1000.0)

        # Muestreo DFS
        t_dfs = []
        for _ in range(NUM_REPETICIONES):
            inicio = time.perf_counter_ns()
            buscar_conexion_dfs(red_social, orig, dest)
            fin = time.perf_counter_ns()
            t_dfs.append((fin - inicio) / 1000.0)

        prom_bfs = statistics.mean(t_bfs)
        std_bfs = statistics.stdev(t_bfs)
        prom_dfs = statistics.mean(t_dfs)
        std_dfs = statistics.stdev(t_dfs)

        tiempos_bfs_us.append(prom_bfs)
        desv_bfs_us.append(std_bfs)
        tiempos_dfs_us.append(prom_dfs)
        desv_dfs_us.append(std_dfs)

        dif_str = f"{prom_dfs / prom_bfs:.2f}x" if prom_bfs > 0 else "N/A"
        nombre_par = f"P{num}: {orig} -> {dest}"
        print(f"  {nombre_par:<20} | {prom_bfs:>13.2f} µs {std_bfs:>8.2f} | {prom_dfs:>13.2f} µs {std_dfs:>8.2f} | {dif_str:>10}")

    print("=" * 86)

    # Configuración de estilo global
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['axes.edgecolor'] = '#94a3b8'
    plt.rcParams['axes.linewidth'] = 0.9

    # ─────────────────────────────────────────────────────────────────────────
    # 1. Gráfica Individual de Línea - BFS
    # ─────────────────────────────────────────────────────────────────────────
    plt.figure(figsize=(8.5, 4.8))
    plt.plot(x_indices, tiempos_bfs_us, color='#2563eb', linewidth=2.8,
             marker='o', markersize=8, markerfacecolor='#1d4ed8', markeredgecolor='white', markeredgewidth=1.8,
             label='BFS (Cola FIFO)')
    plt.fill_between(x_indices, tiempos_bfs_us, color='#3b82f6', alpha=0.15)
    plt.title('Perfil Temporal - BFS (Breadth-First Search)', fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('Casos de Prueba (Pares de Usuarios)', fontsize=10, fontweight='bold')
    plt.ylabel('Tiempo Promedio (µs)', fontsize=10, fontweight='bold')
    plt.xticks(x_indices, etiquetas, fontsize=9)
    plt.ylim(0, max(tiempos_bfs_us) * 1.25)
    plt.grid(True, linestyle='--', alpha=0.5)

    for i, txt in enumerate(tiempos_bfs_us):
        plt.annotate(f'{txt:.2f} µs', (x_indices[i], tiempos_bfs_us[i]),
                     textcoords="offset points", xytext=(0, 9), ha='center',
                     fontsize=9, fontweight='bold', color='#1e3a8a')

    plt.tight_layout()
    ruta_bfs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiempo_bfs.png')
    plt.savefig(ruta_bfs, dpi=300)
    plt.close()
    print(f"  [+] Gráfica de línea BFS guardada en: {ruta_bfs}")

    # ─────────────────────────────────────────────────────────────────────────
    # 2. Gráfica Individual de Línea - DFS
    # ─────────────────────────────────────────────────────────────────────────
    plt.figure(figsize=(8.5, 4.8))
    plt.plot(x_indices, tiempos_dfs_us, color='#dc2626', linewidth=2.8,
             marker='s', markersize=8, markerfacecolor='#b91c1c', markeredgecolor='white', markeredgewidth=1.8,
             label='DFS (Pila LIFO)')
    plt.fill_between(x_indices, tiempos_dfs_us, color='#ef4444', alpha=0.15)
    plt.title('Perfil Temporal - DFS (Depth-First Search)', fontsize=12, fontweight='bold', pad=12)
    plt.xlabel('Casos de Prueba (Pares de Usuarios)', fontsize=10, fontweight='bold')
    plt.ylabel('Tiempo Promedio (µs)', fontsize=10, fontweight='bold')
    plt.xticks(x_indices, etiquetas, fontsize=9)
    plt.ylim(0, max(tiempos_dfs_us) * 1.25)
    plt.grid(True, linestyle='--', alpha=0.5)

    for i, txt in enumerate(tiempos_dfs_us):
        plt.annotate(f'{txt:.2f} µs', (x_indices[i], tiempos_dfs_us[i]),
                     textcoords="offset points", xytext=(0, 9), ha='center',
                     fontsize=9, fontweight='bold', color='#7f1d1d')

    plt.tight_layout()
    ruta_dfs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiempo_dfs.png')
    plt.savefig(ruta_dfs, dpi=300)
    plt.close()
    print(f"  [+] Gráfica de línea DFS guardada en: {ruta_dfs}")

    # ─────────────────────────────────────────────────────────────────────────
    # 3. Gráfica Comparativa Unificada de Líneas - BFS vs DFS
    # ─────────────────────────────────────────────────────────────────────────
    plt.figure(figsize=(10.5, 5.2))
    plt.plot(x_indices, tiempos_bfs_us, color='#2563eb', linewidth=2.6,
             marker='o', markersize=8, markerfacecolor='#1d4ed8', markeredgecolor='white', markeredgewidth=1.8,
             label='BFS (Cola FIFO - Monótono)')
    plt.plot(x_indices, tiempos_dfs_us, color='#dc2626', linewidth=2.6,
             marker='s', markersize=8, markerfacecolor='#b91c1c', markeredgecolor='white', markeredgewidth=1.8,
             label='DFS (Pila LIFO - Variable)')

    plt.title('Comparativa Simultánea de Tiempos de Ejecución: BFS vs. DFS', fontsize=13, fontweight='bold', pad=14)
    plt.xlabel('Casos de Prueba (Pares de Usuarios)', fontsize=10, fontweight='bold')
    plt.ylabel('Tiempo Promedio de CPU (µs)', fontsize=10, fontweight='bold')
    plt.xticks(x_indices, etiquetas, fontsize=9)
    y_max = max(max(tiempos_bfs_us), max(tiempos_dfs_us)) * 1.28
    plt.ylim(0, y_max)
    plt.grid(True, linestyle='--', alpha=0.55)
    plt.legend(loc='upper right', frameon=True, facecolor='#f8fafc', edgecolor='#cbd5e1', fontsize=10)

    # Etiquetas de datos para ambas líneas
    for i in range(len(x_indices)):
        # BFS arriba
        plt.annotate(f'{tiempos_bfs_us[i]:.2f}', (x_indices[i], tiempos_bfs_us[i]),
                     textcoords="offset points", xytext=(-14, 8), fontsize=8.5, fontweight='bold', color='#1d4ed8')
        # DFS abajo / arriba según cruce
        y_offset = -14 if tiempos_dfs_us[i] < tiempos_bfs_us[i] else 8
        plt.annotate(f'{tiempos_dfs_us[i]:.2f}', (x_indices[i], tiempos_dfs_us[i]),
                     textcoords="offset points", xytext=(12, y_offset), fontsize=8.5, fontweight='bold', color='#b91c1c')

    plt.tight_layout()
    ruta_comparativa = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'comparativa_tiempos_bfs_vs_dfs.png')
    plt.savefig(ruta_comparativa, dpi=300)
    plt.close()
    print(f"  [+] Gráfica comparativa de líneas guardada en: {ruta_comparativa}")
    print("=" * 86 + "\n")

if __name__ == "__main__":
    benchmark_algoritmos()
