from flask import Flask, request, render_template
import pickle
import numpy as np
import joblib 

app = Flask(__name__)

# Charger le modèle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

Norm = joblib.load('Normalisation.pkl')

@app.route('/')
def home():
    print("la fontion home  est executee")
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Extraire les caractéristiques depuis le formulaire
#     features = [float(x) for x in request.form.values()]
#     final_features = [np.array(features)]
    
#     # Faire la prédiction
#     prediction = model.predict(final_features)
    
#     # Convertir la prédiction en nom de classe
#     if prediction[0] == 0:
#         output = "Cammeo"
#     elif prediction[0] == 1:
#         output = "Osmancik"
#    # Adapte ceci si tu veux retourner un nom de variété
    
#     return render_template('index.html', prediction_text=f'La variété prédite est : {output}')

@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les valeurs du formulaire
    area = int(request.form['area'])
    perimeter = float(request.form['perimeter'])
    major_axis_length = float(request.form['major_axis_length'])
    minor_axis_length = float(request.form['minor_axis_length'])
    eccentricity = float(request.form['eccentricity'])
    convex_area = int(request.form['convex_area'])
    extent = float(request.form['extent'])

    features = np.array([[area, perimeter, major_axis_length, minor_axis_length, eccentricity, convex_area, extent]])

    # Normalisation
    features_norm = Norm.transform(features)

    # prédiction
    prediction = model.predict(features_norm)
    prediction_class = np.argmax(prediction, axis=1)[0]

    riz = ''
    if prediction_class==0:
        riz = 'Cammeo'
    elif prediction_class==1:
        riz = 'Osmancik'
            
        
        

    # Affichage du résultat
    return render_template('index.html', prediction_text=f'Classe prédite : {riz}')


if __name__ == "__main__":
    app.run(debug=True)
