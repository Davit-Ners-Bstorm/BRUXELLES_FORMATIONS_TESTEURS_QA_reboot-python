"""
Exercice 4 — Vous avez reçu une réponse API
Les consignes sont dans enonce.md (section EXO 4).

`response` imite ce qu'une API comme EventFlow pourrait renvoyer.
Aucun appel réseau ici : c'est un simple dictionnaire Python.
"""

response = {
    "status": 200,
    "data": [
        {"id": 1,  "title": "Metal Night",           "capacity": 300,  "active": True},
        {"id": 2,  "title": "Python Conference",      "capacity": 150,  "active": False},
        {"id": 3,  "title": "Rock Festival",          "capacity": 500,  "active": True},
        {"id": 4,  "title": "Techno Warehouse",       "capacity": 800,  "active": True},
        {"id": 5,  "title": "Jazz & Blues Evening",   "capacity": 120,  "active": True},
        {"id": 6,  "title": "Indie Showcase",         "capacity": 90,   "active": False},
        {"id": 7,  "title": "Hip-Hop Block Party",    "capacity": 650,  "active": True},
        {"id": 8,  "title": "Classical Gala",         "capacity": 400,  "active": False},
        {"id": 9,  "title": "Electro Sunset",         "capacity": 1000, "active": True},
        {"id": 10, "title": "Folk Acoustic Session",  "capacity": 60,   "active": True},
        {"id": 11, "title": "Reggae Beach Party",     "capacity": 750,  "active": True},
        {"id": 12, "title": "Drum & Bass Marathon",   "capacity": 900,  "active": False},
    ],
}


# Q1 — Afficher le status.


# Q2 — Afficher tous les titres.


# Q3 — Afficher uniquement les événements actifs.


# Q4 — Compter les événements actifs.


# Q5 — Trouver l'événement ayant la plus grande capacité.


# Q6
def find_event(response, event_id):
    pass


# Q7 — Vérification manuelle : afficher PASS si le status vaut 200, sinon FAIL.
