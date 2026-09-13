# 📘 Manual de Instrucciones y Ejecución — Taller 2: Búsqueda BFS y DFS

**Asignatura:** Inteligencia Artificial  
**Docente:** Joaquín F. Sánchez  
**Programa:** Maestría en Inteligencia Artificial (2026-01)  
**Institución:** Universidad Sergio Arboleda  

### 👥 Integrantes:
- **Santiago Rodríguez Palacio**
- **Juan José Segura Flórez**
- **Bryan Orozco Romero**

---

## 📋 1. Requisitos Previos

1. **Python:** Versión `3.8` o superior instalada.
2. **Bibliotecas Requeridas:**
   - La suite base (Puntos 1 al 10) utiliza únicamente la **librería estándar de Python** (no requiere instalar nada).
   - El módulo de benchmarking y graficación (Punto 11) requiere `matplotlib`.

Para instalar `matplotlib`:
```powershell
pip install matplotlib
```

---

## 🚀 2. Instrucciones de Ejecución

Abre una terminal (PowerShell, CMD o Bash) y ubícate en la carpeta del proyecto:
```powershell
cd "Introducion a Inteleginaci aritifical\Taller 2 Codigo\Taller-DFS-y-BFS"
```

---

### Opción A: Ejecución General Consolidada (Recomendada)
Para correr de forma secuencial y completa todos los puntos del taller (Puntos 7, 8, 9, 10 y 11):

```powershell
python main.py
```

**¿Qué hace este comando?**
1. **Puntos 7 & 8:** Ejecuta las 6 pruebas comparativas BFS vs. DFS en la red base de 11 nodos y proyecta la tabla resumen de métricas y conclusiones.
2. **Punto 9:** Ejecuta la prueba de usuarios sin conexión (`Ana` $\to$ `Laura`) demostrando el vaciado de la frontera ante componentes aisladas.
3. **Punto 10:** Ejecuta las pruebas sobre la red modificada de 16 usuarios (con 5 nodos ficticios y 8 aristas nuevas).
4. **Punto 11:** Ejecuta el benchmark de tiempos de CPU ($N=1\,000$ iteraciones) y genera automáticamente las 3 gráficas PNG en alta resolución.


---

### Opción B: Ejecución de la Mejora del Sistema (Punto 11)
Para ejecutar el benchmark estadístico de tiempos de CPU y generar automáticamente las gráficas de líneas:

```powershell
python punto11.py
```

**Salidas generadas:**
* Imprime en consola la tabla comparativa de tiempos en microsegundos ($\mu\text{s}$) tras $1\,000$ repeticiones por cada caso.
* Genera y guarda automáticamente en el directorio 3 archivos de imagen en alta resolución:
  1. `tiempo_bfs.png`: Curva de tiempo individual de BFS.
  2. `tiempo_dfs.png`: Curva de tiempo individual de DFS.
  3. `comparativa_tiempos_bfs_vs_dfs.png`: Gráfica comparativa simultánea con ambas curvas superpuestas.

---

### Opción C: Ejecución Modular Independiente (Por Punto del Taller)

Cada archivo contiene su propio bloque `if __name__ == "__main__":` y puede ejecutarse por separado según lo que se desee evaluar:

#### 1. Probar algoritmo BFS (Punto 5)
Ejecuta la búsqueda en anchura demostrativa:
```powershell
python BFS.py
```

#### 2. Probar algoritmo DFS (Punto 6)
Ejecuta la búsqueda en profundidad con pila LIFO:
```powershell
python DFS.py
```

#### 3. Probar usuarios sin conexión (Punto 9)
Evalúa el caso donde no existe ruta entre dos nodos (`Ana` y `Laura` en componentes desconectadas):
```powershell
python punto9.py
```

#### 4. Probar la red modificada de 16 nodos (Punto 10)
Muestra el detalle del orden de expansión y métricas con los 5 usuarios ficticios agregados:
```powershell
python punto10.py
```

---

## 💻 3. Uso Interactivo en Python (Como Módulo)

Puedes importar las funciones en tu propio script o consola interactiva de Python:

```python
from red_social import red_social, red_social_modificada
from BFS import buscar_conexion_bfs
from DFS import buscar_conexion_dfs

# 1. Búsqueda con BFS (Garantiza ruta más corta)
res_bfs = buscar_conexion_bfs(red_social, "Ana", "Karen")
print("Ruta BFS:", " -> ".join(res_bfs["ruta"]))
print("Grados de separación:", res_bfs["grados_separacion"])
print("Nodos expandidos:", res_bfs["nodos_expandidos"])

# 2. Búsqueda con DFS (Exploración profunda con límite)
res_dfs = buscar_conexion_dfs(red_social, "Ana", "Karen", limite_profundidad=10)
print("Ruta DFS:", " -> ".join(res_dfs["ruta"]))
print("Grados de separación:", res_dfs["grados_separacion"])
print("Frontera máxima:", res_dfs["frontera_maxima"])
```

---

## 📊 4. Interpretación de las Columnas de Salida

Al ejecutar los scripts, las tablas de consola presentan las siguientes métricas:

| Columna | Significado | Interpretación Técnica |
|---|---|---|
| **P / #** | Número de prueba | Identificador del caso evaluado. |
| **Alg** | Algoritmo | `BFS` (Cola FIFO) o `DFS` (Pila LIFO). |
| **Ruta** | Secuencia de nodos | Camino de usuarios encontrados desde origen hasta destino. |
| **G** | Grados de separación | Longitud del camino menos uno ($\text{len}(\text{ruta}) - 1$). Costo $g(n)$. |
| **Exp** | Nodos expandidos | Cantidad de nodos que salieron de la frontera para ser procesados. |
| **Gen** | Nodos generados | Cantidad de vecinos válidos descubiertos e insertados en la frontera. |
| **FMax** | Frontera máxima | Pico máximo de memoria de la cola o pila durante la búsqueda. |

---

## 📂 5. Mapa de Archivos del Repositorio

| Archivo | Punto del Taller | Descripción |
|---|:---:|---|
| `main.py` | Puntos 7, 8, 9, 10 | Script integrador que corre todas las pruebas principales. |
| `red_social.py` | Puntos 1, 2, 10 | Estructura de grafos (Red Base de 11 nodos y Red Modificada de 16 nodos). |
| `BFS.py` | Punto 5 | Implementación canónica de BFS con `collections.deque`. |
| `DFS.py` | Punto 6 | Implementación canónica de DFS con pila LIFO y exploración inversa. |
| `punto9.py` | Punto 9 | Prueba formal de usuarios en componentes aisladas. |
| `punto10.py` | Punto 10 | Pruebas y análisis de la red social extendida. |
| `punto11.py` | Punto 11 | Benchmark de tiempos de CPU ($N=1\,000$) y generador de gráficas. |
| `tiempo_bfs.png` | Punto 11 | Curva de tiempo individual de BFS generada por `punto11.py`. |
| `tiempo_dfs.png` | Punto 11 | Curva de tiempo individual de DFS generada por `punto11.py`. |
| `comparativa_tiempos_bfs_vs_dfs.png` | Punto 11 | Gráfica comparativa simultánea de tiempos. |

---

## 🔍 6. Verificación de Código

Para verificar que todos los archivos compilan sin errores de sintaxis:

```powershell
python -m py_compile BFS.py DFS.py red_social.py main.py punto9.py punto10.py punto11.py
```
*(Si no muestra ningún mensaje en consola, la compilación fue 100% exitosa).*
