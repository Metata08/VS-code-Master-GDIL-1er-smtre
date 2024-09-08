from flask import Flask, request, render_template
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib

# Chargement
model = load_model('model_rice.pkl')
Norm = joblib.load('Normalisation.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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
