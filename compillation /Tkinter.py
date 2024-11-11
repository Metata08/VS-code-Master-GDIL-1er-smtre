import tkinter as tk
import ply.lex as lex
import ply.yacc as yacc

# Exemple d'analyse lexicale (simplifiée)
tokens = ('NOMBRE', 'PLUS', 'MOINS')

t_PLUS = r'\+'
t_MOINS = r'-'
t_ignore = ' \t'

def t_NOMBRE(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    result_label.config(text=f"Erreur lexicale : {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Fonction pour analyser le texte d'entrée
def analyser():
    entree = text_input.get("1.0", "end-1c")
    lexer.input(entree)
    tokens_result = [token for token in lexer]
    result_label.config(text=f"Tokens : {tokens_result}")

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Analyseur Lexical")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

analyse_button = tk.Button(root, text="Analyser", command=analyser)
analyse_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
