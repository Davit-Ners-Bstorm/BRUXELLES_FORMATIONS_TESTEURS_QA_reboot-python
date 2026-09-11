# EventFlow — Exercices Python

Tu travailles directement dans les fichiers `.py` fournis. Les données sont déjà
écrites : tu ne les modifies pas, tu ajoutes seulement le code demandé.

Documentation autorisée. Tu peux tester ton code en lançant le fichier :

```bash
python3 exo1_reboot.py
```

Les résultats attendus sont donnés pour que tu puisses vérifier toi-même si ton
code fait ce qu'il faut.

---

## EXO 1 — `exo1_reboot.py`

Une application possède une liste de 16 utilisateurs (`id`, `name`, `age`,
`active`, `role`).

### Partie A — les bases

**Q1.** Afficher le nom de chaque utilisateur, un par ligne.

```
Alice
Bob
Charlie
...
```

**Q2.** Afficher uniquement les utilisateurs actifs (`active == True`).

**Q3.** Compter les utilisateurs actifs et afficher la phrase :

```
11 utilisateurs actifs
```

**Q4.** Afficher uniquement les utilisateurs majeurs (18 ans ou plus).

**Q5.** Afficher les utilisateurs qui sont à la fois actifs **et** majeurs.
Il doit y en avoir 8.

### Partie B — les fonctions

**Q6.** `is_adult(user)` — reçoit un utilisateur, retourne `True` s'il a au
moins 18 ans, sinon `False`.

**Q7.** `get_active_users(users)` — retourne une nouvelle liste contenant
uniquement les utilisateurs actifs.

**Q8.** `get_active_adults(users)` — retourne une nouvelle liste contenant
uniquement les utilisateurs actifs **et** majeurs.

**Q9.** `find_user_by_id(users, user_id)` — retourne l'utilisateur qui a cet
`id`, ou `None` s'il n'existe pas.

```
find_user_by_id(users, 3)    ->  l'utilisateur Charlie
find_user_by_id(users, 999)  ->  None
```

### Partie C — le challenge

**Q10.** `get_statistics(users)` — retourne un dictionnaire de la forme :

```python
{
    "total": ...,
    "active": ...,
    "inactive": ...,
    "adults": ...,
    "minors": ...,
}
```

---

## EXO 2 — `exo2_can_create_event.py`

Règle métier d'EventFlow : un événement peut être créé **uniquement si** :

- le titre contient entre 3 et 100 caractères (bornes incluses) ;
- la capacité est strictement supérieure à 0 ;
- l'organisateur est actif.

**Avant d'écrire le code**, note sur papier les cas que tu testerais pour être
sûr que la règle est correcte. Pense au titre, à la capacité, à l'organisateur.

Ensuite, complète :

```python
def can_create_event(title, capacity, organizer):
    ...
```

Comportement attendu :

```
can_create_event("Concert Metal", 200, active_user)     ->  True
can_create_event("AB", 200, active_user)                ->  False
can_create_event("Concert Metal", 0, active_user)       ->  False
can_create_event("Concert Metal", 200, inactive_user)   ->  False
```

---

## EXO 3 — `exo3_donnees_pourries.py`

Les données reçues ne sont pas toujours propres. Ton code ne doit **jamais
planter** sur une valeur invalide : il l'ignore.

### Mission 1

À partir de la liste `ages` (des chaînes de caractères), calculer l'âge moyen
en ne gardant que les valeurs réellement numériques.

### Mission 2

Écrire `parse_ages(ages)` qui retourne la liste des âges valides convertis en
nombres :

```
[25, 17, 32, 41, 19, 60, 28, 45]
```

### Mission 3

À partir de la liste `users`, écrire `get_valid_adults(users)` qui retourne les
**noms** des utilisateurs majeurs.

La fonction ne doit pas planter si l'âge est manquant, vide ou non numérique.

```
['Alice', 'Charlie', 'Fatima', 'Hana', 'Julia']
```

---

## EXO 4 — `exo4_reponse_api.py`

La variable `response` imite une réponse renvoyée par une API : un `status` et
une clé `data` contenant une liste d'événements.

**Q1.** Afficher le `status`.

**Q2.** Afficher tous les titres d'événements.

**Q3.** Afficher uniquement les événements actifs.

**Q4.** Compter les événements actifs (il y en a 8).

**Q5.** Trouver l'événement ayant la plus grande capacité.

**Q6.** `find_event(response, event_id)` — retourne l'événement correspondant à
cet `id`, ou `None` s'il n'existe pas.

**Q7.** Vérifier « à la main » que la réponse est correcte : afficher `PASS` si
le `status` vaut 200, sinon `FAIL`.

```python
if response["status"] == 200:
    print("PASS")
else:
    print("FAIL")
```
