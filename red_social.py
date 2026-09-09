"""
red_social.py
=============
Módulo que contiene la red social de referencia definida en el Taller 2 –
Búsqueda de conexiones en una red social.

Docente : Joaquín F. Sánchez
Asignatura: Inteligencia Artificial – Maestría en IA – Sergio Arboleda 2026
"""

# ─────────────────────────────────────────────────────────────────────────────
# Red social base (grafo no dirigido original con 11 usuarios - Puntos 1 al 8)
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

# ─────────────────────────────────────────────────────────────────────────────
# Red social modificada (Punto 10: 16 usuarios, 5 ficticios y 8 nuevas conexiones)
# ─────────────────────────────────────────────────────────────────────────────
red_social_modificada = {
    "Ana":     ["Bruno", "Carla", "Elena", "Luis"],
    "Bruno":   ["Ana",   "Diana", "Felipe"],
    "Carla":   ["Ana",   "Felipe", "Gabriel"],
    "Diana":   ["Bruno", "Helena"],
    "Elena":   ["Ana",   "Isabel", "Olga"],
    "Felipe":  ["Bruno", "Carla", "Helena"],
    "Gabriel": ["Carla", "Jorge"],
    "Helena":  ["Diana", "Felipe", "Karen"],
    "Isabel":  ["Elena", "Karen"],
    "Jorge":   ["Gabriel", "Karen"],
    "Karen":   ["Helena", "Isabel", "Jorge"],
    "Luis":    ["Ana", "Marta", "Néstor"],
    "Marta":   ["Luis", "Néstor", "Olga", "Pedro"],
    "Néstor":  ["Luis", "Marta", "Olga"],
    "Olga":    ["Elena", "Marta", "Néstor"],
    "Pedro":   ["Marta"],
}

