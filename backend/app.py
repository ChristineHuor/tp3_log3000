from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__, template_folder='../templates', static_folder='../static')

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple contenant exactement un opérateur.

    Paramètres:
        expr (str): Expression à calculer, par exemple "3+4".

    Retour:
        float: Résultat du calcul.

    Exceptions:
        ValueError: Si l'expression est vide, que sont format est invalide ou contient des opérandes non numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application Flask.

    GET:
        Affiche la calculatrice avec un champ de résultat vide.

    POST:
        Récupère l'expression du formulaire, calcule le résultat et l'affiche.
        En cas d'erreur (expression invalide ou division par zéro), 
        affiche un message d'erreur.

    Retour:
        Page HTML 'index.html' avec le résultat du calcul ou un message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)