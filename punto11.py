"""
punto11.py  -  Punto 11: Mejora del Sistema (Medición y Gráficas de Tiempo de Ejecución)
========================================================================================
Mide con alta precisión (time.perf_counter_ns) los tiempos de ejecución de BFS y DFS,
genera gráficas individuales para cada algoritmo y una gráfica unificada comparativa final.

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

NUM_REPETICIONES = 1000  # Repeticiones para significancia estadística

def benchmark_algoritmos():
    etiquetas = [f"P{num}\n({orig}→{dest})" for num, orig, dest in PRUEBAS]
    tiempos_bfs_us = []
    tiempos_dfs_us = []
    desv_bfs_us = []
    desv_dfs_us = []

    print("\n" + "=" * 86)
    print(f"  PUNTO 11 - Benchmark de Tiempo de Ejecución (N = {NUM_REPETICIONES} iteraciones por par)")
    print("=" * 86)
    print(f"  {'Prueba':<20} | {'BFS Prom (µs)':<15} {'BFS Std':<10} | {'DFS Prom (µs)':<15} {'DFS Std':<10} | {'Diferencia':<10}")
    print("-" * 86)

    for num, orig, dest in PRUEBAS:
        # Warmup inicial
        buscar_conexion_bfs(red_social, orig, dest)
        buscar_conexion_dfs(red_social, orig, dest)

        # Muestreo BFS
        t_bfs = []
        for _ in range(NUM_REPETICIONES):
            inicio = time.perf_counter_ns()
            buscar_conexion_bfs(red_social, orig, dest)
            fin = time.perf_counter_ns()
            t_bfs.append((fin - inicio) / 1000.0)  # microsegundos

        # Muestreo DFS
        t_dfs = []
        for _ in range(NUM_REPETICIONES):
            inicio = time.perf_counter_ns()
            buscar_conexion_dfs(red_social, orig, dest)
            fin = time.perf_counter_ns()
            t_dfs.append((fin - inicio) / 1000.0)  # microsegundos

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

    # ─────────────────────────────────────────────────────────────────────────
    # 1. Gráfica Individual BFS
    # ─────────────────────────────────────────────────────────────────────────
    plt.figure(figsize=(9, 5))
    barras_bfs = plt.bar(etiquetas, tiempos_bfs_us, color='#2563eb', edgecolor='#1d4ed8', width=0.55, alpha=0.9)
    plt.title('Tiempo de Ejecución - BFS (Breadth-First Search)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Casos de Prueba (Pares de Usuarios)', fontsize=11, fontweight='bold')
    plt.ylabel('Tiempo Promedio (Microsegundos - µs)', fontsize=11, fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Anotar valores en las barras
    for bar in barras_bfs:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + (max(tiempos_bfs_us)*0.02), f'{yval:.1f} µs',
                 ha='center', va='bottom', fontsize=9, fontweight='bold', color='#1e3a8a')

    plt.tight_layout()
    ruta_bfs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiempo_bfs.png')
    plt.savefig(ruta_bfs, dpi=300)
    plt.close()
    print(f"  [+] Gráfica individual BFS guardada en: {ruta_bfs}")

    # ─────────────────────────────────────────────────────────────────────────
    # 2. Gráfica Individual DFS
    # ─────────────────────────────────────────────────────────────────────────
    plt.figure(figsize=(9, 5))
    barras_dfs = plt.bar(etiquetas, tiempos_dfs_us, color='#dc2626', edgecolor='#b91c1c', width=0.55, alpha=0.9)
    plt.title('Tiempo de Ejecución - DFS (Depth-First Search)', fontsize=13, fontweight='bold', pad=15)
    plt.xlabel('Casos de Prueba (Pares de Usuarios)', fontsize=11, fontweight='bold')
    plt.ylabel('Tiempo Promedio (Microsegundos - µs)', fontsize=11, fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Anotar valores en las barras
    for bar in barras_dfs:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + (max(tiempos_dfs_us)*0.02), f'{yval:.1f} µs',
                 ha='center', va='bottom', fontsize=9, fontweight='bold', color='#7f1d1d')

    plt.tight_layout()
    ruta_dfs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tiempo_dfs.png')
    plt.savefig(ruta_dfs, dpi=300)
    plt.close()
    print(f"  [+] Gráfica individual DFS guardada en: {ruta_dfs}")

    # ─────────────────────────────────────────────────────────────────────────
    # 3. Gráfica Comparativa Unificada (BFS vs DFS)
    # ─────────────────────────────────────────────────────────────────────────
    x = range(len(etiquetas))
    ancho = 0.35

    plt.figure(figsize=(11, 6))
    rects1 = plt.bar([i - ancho/2 for i in x], tiempos_bfs_us, ancho, label='BFS (Cola FIFO)',
                     color='#2563eb', edgecolor='#1d4ed8', alpha=0.9)
    rects2 = plt.bar([i + ancho/2 for i in x], tiempos_dfs_us, ancho, label='DFS (Pila LIFO)',
                     color='#dc2626', edgecolor='#b91c1c', alpha=0.9)

    plt.title('Comparativa Simultánea de Tiempo de Ejecución: BFS vs DFS', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Casos de Prueba (Pares de Usuarios)', fontsize=11, fontweight='bold')
    plt.ylabel('Tiempo Promedio (Microsegundos - µs)', fontsize=11, fontweight='bold')
    plt.xticks(x, etiquetas)
    plt.legend(frameon=True, facecolor='#f8fafc', edgecolor='#cbd5e1', fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Etiquetas en barras
    for bar in rects1:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, f'{yval:.1f}',
                 ha='center', va='bottom', fontsize=8, color='#1e3a8a')
    for bar in rects2:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, f'{yval:.1f}',
                 ha='center', va='bottom', fontsize=8, color='#7f1d1d')

    plt.tight_layout()
    ruta_comparativa = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'comparativa_tiempos_bfs_vs_dfs.png')
    plt.savefig(ruta_comparativa, dpi=300)
    plt.close()
    print(f"  [+] Gráfica unificada final guardada en: {ruta_comparativa}")
    print("=" * 86 + "\n")

    return {
        "etiquetas": etiquetas,
        "tiempos_bfs": tiempos_bfs_us,
        "tiempos_dfs": tiempos_dfs_us
    }

if __name__ == "__main__":
    benchmark_algoritmos()
