

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from keras.models import Sequential
from keras.layers.core import Dense
import joblib
import seaborn as sns
import matplotlib.pyplot as plt

#Chargement des données
donnees = pd.read_excel("Rice_Cammeo_Osmancik.csv")

#Séparation des caractéristiques (X) et les étiquettes (y)
X = donnees.drop('Class', axis=1)
y = donnees['Class']

#la normalisation
Norm = MinMaxScaler()
X_Norm = Norm.fit_transform(X)

#sauvegarde de la normalisation
joblib.dump(Norm,'Normalisation.pkl')

#Encodage des étiquettes pour les transformer en valeurs numériques
Encode = LabelEncoder()
y_Encode = Encode.fit_transform(y)

def creer_modele(nb_couches, nb_neurones, activation):
    model = Sequential()
    
    model.add(Dense(nb_neurones[0], input_dim=X_Norm.shape[1], activation=activation))
    
    # Ajout des couches cachées supplémentaires
    for i in range(1, nb_couches):
        model.add(Dense(nb_neurones[i], activation=activation))
    
    # Couche de sortie avec 'softmax' pour la classification multiclass
    model.add(Dense(len(Encode.classes_), activation='softmax'))
    
    # Compilation du modèle
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    return model

scenarios = [
    {"nb_couches": 2, "nb_neurones": [14,7], "activation": 'relu'},
    {"nb_couches": 3, "nb_neurones": [1, 64, 32], "activation": 'relu'},
    {"nb_couches": 2, "nb_neurones": [64, 32], "activation": 'tanh'},
    {"nb_couches": 3, "nb_neurones": [128, 64, 32], "activation": 'tanh'},
    {"nb_couches": 2, "nb_neurones": [64, 32], "activation": 'sigmoid'},
    {"nb_couches": 3, "nb_neurones": [128, 64, 32], "activation": 'sigmoid'},
]

resultats = []

for scenario in scenarios:
    print(f"Test du modèle avec {scenario['nb_couches']} couches, neurones {scenario['nb_neurones']}, activation {scenario['activation']}")
    
    # Création et entraînement du modèle
    model = creer_modele(scenario['nb_couches'], scenario['nb_neurones'], scenario['activation'])
    entrainement_model = model.fit(X_Norm, y_Encode, epochs=50, batch_size=32, validation_split=0.2, verbose=0)
    
    # Extraction des précisions d'entraînement et de validation
    Precision_d_entraînement = entrainement_model.history['accuracy'][-1] * 100
    Precision_de_validation = entrainement_model.history['val_accuracy'][-1] * 100
    
    # Stockage des résultats
    resultats.append({
        "nb_couches": scenario['nb_couches'],
        "nb_neurones": scenario['nb_neurones'],
        "activation": scenario['activation'],
        "Precision_d_entraînement": Precision_d_entraînement,
        "Precision_de_validation": Precision_de_validation
    })
    
    print(f"Précision d'entraînement : {Precision_d_entraînement:.2f}%")
    print(f"Précision de validation : {Precision_de_validation:.2f}%\n")
    
# Création d'une matrice de résultats avec pandas
df_resultats = pd.DataFrame(resultats)

# Création de la matrice des résultats
matrice_precisions = pd.pivot_table(df_resultats, 
                                    values=['Precision_d_entraînement', 'Precision_de_validation'], 
                                    index=['nb_couches', 'activation'])

# Utilisation de seaborn pour afficher la matrice des résultats
sns.heatmap(matrice_precisions, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Précision (%)'})

# Ajout d'un titre et des labels
plt.title('Matrice de Précision d\'Entraînement et de Validation par Scénario')
plt.ylabel('Couches & Activation')
plt.xlabel('Type de Précision')

# Affichage du graphique
plt.tight_layout()
plt.show()
