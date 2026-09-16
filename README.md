# Labo pedagogique XSS (Reflected XSS) — Flask

Petite application Flask **volontairement vulnérable**, à usage strictement
local, pour comprendre ce qui se passe quand un paramètre GET `q` est
inséré dans une page HTML sans échappement, puis avec échappement.

⚠️ **A lancer uniquement en local (127.0.0.1).** Ne jamais exposer ce
projet sur un réseau public ou sur Internet.

## Structure du projet

```
C:\TP\XSS\
├── app.py                 # Application Flask (routes, logique)
├── requirements.txt        # Dépendances Python
├── README.md
├── static\
│   └── style.css           # Styles (aucun JS externe nécessaire)
└── templates\
    ├── base.html            # Layout commun (bandeau, nav)
    ├── index.html           # Page d'accueil
    ├── search.html          # /search : formulaire + comparaison + explications
    └── lab.html             # /lab : schémas du flux et de l'attaque
```

## Installation

Prérequis : Python 3.9+ installé.

```powershell
cd C:\TP\XSS
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Lancement

```powershell
python app.py
```

Puis ouvrez votre navigateur sur :

```
http://127.0.0.1:5000/
```

## Pages disponibles

- `/` — accueil, présentation du labo
- `/search?q=...` — formulaire de recherche + comparaison
  **VULNERABLE** vs **SECURE**, section "Try it yourself",
  "What happened?" et "How to fix?"
- `/lab` — schéma visuel du flux `User input → q parameter → Server →
  HTML response → Browser`, et un schéma "Attack flow"

## Exemples à essayer sur `/search`

| Type                | Valeur de `q`                          |
|---------------------|------------------------------------------|
| Texte normal        | `Bonjour tout le monde`                  |
| HTML interprétable  | `<b>Texte en gras</b>`                   |
| JS interprétable    | `<script>alert('XSS Lab local')</script>` |

Comparez le rendu et le "code source HTML généré" affichés dans les deux
panneaux (vulnérable / sécurisé).

## Principe technique (résumé)

- **Version vulnérable** : `f"<p>Resultats pour : {q}</p>"` — la valeur
  brute de `q` est concaténée dans le HTML. Si `q` contient des balises,
  le navigateur les interprète.
- **Version sécurisée** : `f"<p>Resultats pour : {escape(q)}</p>"` —
  `escape()` (de `markupsafe`, la lib utilisée par Jinja2/Flask) remplace
  `< > " ' &` par leurs entités HTML avant l'insertion. Le navigateur
  affiche alors ces entités comme du texte, sans les exécuter.

## Portée pédagogique

- Aucun compte utilisateur, aucune base de données, aucune donnée réelle.
- Aucun payload ne cible un site externe : tous les exemples se contentent
  d'un `alert()` local, exécuté uniquement dans votre propre navigateur sur
  votre propre machine.
- Objectif unique : illustrer visuellement le principe du Reflected XSS et
  de l'échappement HTML côté serveur.
