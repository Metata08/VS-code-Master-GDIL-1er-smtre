from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)

# Charger le modèle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    print("la fontion home  est executee")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extraire les caractéristiques depuis le formulaire
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Faire la prédiction
    prediction = model.predict(final_features)
    
    # Convertir la prédiction en nom de classe
    if prediction[0] == 0:
        output = "Cammeo"
    elif prediction[0] == 1:
        output = "Osmancik"
   # Adapte ceci si tu veux retourner un nom de variété
    
    return render_template('index.html', prediction_text=f'La variété prédite est : {output}')

if __name__ == "__main__":
    app.run(debug=True)
