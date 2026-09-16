"""
============================================================================
 LABORATOIRE PEDAGOGIQUE XSS (Cross-Site Scripting) - REFLECTED XSS
============================================================================

But : montrer concretement ce qui se passe quand la valeur d'un parametre
GET ("q") est inseree dans une page HTML :
  - SANS echappement (version VULNERABLE)
  - AVEC echappement (version SECURISEE)

IMPORTANT (securite / usage) :
  - Cette application est VOLONTAIREMENT vulnerable dans sa page "vulnerable".
  - Elle doit UNIQUEMENT tourner en local (127.0.0.1), jamais exposee sur
    un reseau public ou sur Internet.
  - Aucune vraie donnee utilisateur n'est stockee ou traitee.
  - Les payloads utilises dans "Try it yourself" ne font qu'afficher une
    alerte JavaScript locale (aucune attaque reelle, aucune cible externe).
============================================================================
"""

from flask import Flask, request, render_template
from markupsafe import escape  # fonction d'echappement HTML (utilisee par Jinja2 en interne)

app = Flask(__name__)


# Extraits de code (statiques, pour la section "How to fix?") montrant la
# difference entre une insertion directe et une insertion apres echappement.
VULN_CODE = (
    "# Insertion DIRECTE de la donnee utilisateur -> DANGEREUX\n"
    "q = request.args.get('q', '')\n"
    "html = f\"<p>Resultats pour : {q}</p>\"\n"
    "return html"
)

SECURE_CODE = (
    "from markupsafe import escape\n\n"
    "# Insertion APRES echappement HTML -> SUR\n"
    "q = request.args.get('q', '')\n"
    "html = f\"<p>Resultats pour : {escape(q)}</p>\"\n"
    "return html"
)


def build_snippets(q: str):
    """
    Construit, a partir de la valeur brute 'q' fournie par l'utilisateur,
    les deux fragments HTML qui seraient generes cote serveur :

    1) vulnerable_snippet : q est concatene TEL QUEL dans le HTML.
       => si q contient du HTML/JS, le navigateur va l'interpreter.

    2) secure_snippet : q est d'abord passe dans escape(), qui remplace
       les caracteres dangereux par leurs entites HTML :
           <  ->  &lt;
           >  ->  &gt;
           "  ->  &quot;
           '  ->  &#39;
           &  ->  &amp;
       => le navigateur affiche alors le texte tel quel, sans l'executer.
    """
    vulnerable_snippet = f'<p>Resultats pour : {q}</p>'
    secure_snippet = f'<p>Resultats pour : {escape(q)}</p>'
    return vulnerable_snippet, secure_snippet


@app.route("/")
def index():
    """Page d'accueil : presentation du labo et liens vers /search et /lab."""
    return render_template("index.html")


@app.route("/search")
def search():
    """
    Route principale du labo.

    On lit le parametre GET "q" (celui tape dans le champ de recherche ou
    passe directement dans l'URL, ex: /search?q=<script>alert(1)</script>).

    On affiche ensuite, cote a cote :
      - le rendu VULNERABLE (q insere sans echappement -> danger)
      - le rendu SECURISE   (q insere apres echappement -> sans danger)

    request.args.get("q", "") : recupere la valeur du parametre GET "q"
    dans l'URL ; si absent, on utilise une chaine vide par defaut.
    """
    q = request.args.get("q", "")

    vulnerable_snippet, secure_snippet = build_snippets(q)

    return render_template(
        "search.html",
        q=q,
        has_query=q != "",
        vulnerable_snippet=vulnerable_snippet,
        secure_snippet=secure_snippet,
        vuln_code=VULN_CODE,
        secure_code=SECURE_CODE,
    )


@app.route("/lab")
def lab():
    """Page explicative : schema du flux de donnees + schema d'attaque."""
    return render_template("lab.html")


if __name__ == "__main__":
    # host="127.0.0.1" => le serveur n'ecoute QUE sur la machine locale.
    # Ne jamais mettre host="0.0.0.0" pour ce labo (cela l'exposerait
    # sur le reseau local, avec une page volontairement vulnerable).
    # use_reloader=False : le rechargeur automatique de Flask plante dans
    # cet environnement (Git Bash / Windows) ; on garde le mode debug
    # (pages d'erreur detaillees) sans le redemarrage automatique.
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
