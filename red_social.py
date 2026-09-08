"""
red_social.py
=============
Módulo que contiene la red social de referencia definida en el Taller 2 –
Búsqueda de conexiones en una red social.

Docente : Joaquín F. Sánchez
Asignatura: Inteligencia Artificial – Maestría en IA – Sergio Arboleda 2026
"""

# ─────────────────────────────────────────────────────────────────────────────
# Red social base (grafo no dirigido con 11 usuarios)
# ─────────────────────────────────────────────────────────────────────────────
red_social = {
    "Ana":     ["Bruno", "Carla", "Elena"],
    "Bruno":   ["Ana",   "Diana", "Felipe"],
    "Carla":   ["Ana",   "Felipe", "Gabriel"],
    "Diana":   ["Bruno", "Helena"],
    "Elena":   ["Ana",   "Isabel"],
    "Felipe":  ["Bruno", "Carla", "Helena"],
    "Gabriel": ["Carla", "Jorge"],
    "Helena":  ["Diana", "Felipe", "Karen"],
    "Isabel":  ["Elena", "Karen"],
    "Jorge":   ["Gabriel", "Karen"],
    "Karen":   ["Helena", "Isabel", "Jorge"],
}
