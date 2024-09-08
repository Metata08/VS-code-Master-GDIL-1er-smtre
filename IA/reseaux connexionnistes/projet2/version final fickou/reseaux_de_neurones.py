# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:21:13 2024

@author: FICKOU
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#Chargement des données
donnees = pd.read_excel("rice_data.csv")

#Séparation des caractéristiques (X) et les étiquettes (y)
X = donnees.drop('Class', axis=1)
y = donnees['Class']

#la normalisation
Norm = MinMaxScaler()
X_Norm = Norm.fit_transform(X)

#Encodage des étiquettes pour les transformer en valeurs numériques
Encode = LabelEncoder()
y_Encode = Encode.fit_transform(y)

#création du model de réseau de neurones
model = Sequential()

#Ajout de la première couche cachée avec 64 neurones et la fonction d'activation 'relu'
model.add(Dense(64, activation='relu'))
#Ajout de la deuxième couche cachée avec 32 neurones et la fonction d'activation 'relu'
model.add(Dense(32, activation='relu'))
#Ajout de la couche de sortie avec autant de neurones que de classes, activation 'softmax' pour la classification multicatégorielle
model.add(Dense(len(Encode.classes_), activation='softmax'))

#Compilation du modèle avec la fonction de perte, l'optimiseur, et la métrique d'évaluation
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#Entraînement du modèle avec les données normalisées, 50 époques, taille de batch de 32, et 20% des données pour la validation
entrainement_model = model.fit(X_Norm, y_Encode, epochs=50, batch_size=32, validation_split=0.2)

#Affichage du résumé du modèle pour visualiser la structure des couches et des paramètres
model.summary()

#Extraction de la précision finale sur l'entraînement et la validation
train_accuracy = entrainement_model.history['accuracy'][-1] * 100
val_accuracy = entrainement_model.history['val_accuracy'][-1] * 100

print(f"\nPrécision finale sur l'entraînement : {train_accuracy:.2f}%")
print(f"Précision finale sur la validation : {val_accuracy:.2f}%")

#Prédiction des classes pour les données normalisées
y_pred = model.predict(X_Norm)

#Conversion des prédictions en classes (indice de la classe ayant la plus grande probabilité)
y_pred_classes = np.argmax(y_pred, axis=1)

#Calcul et affichage de la matrice de confusion pour évaluer les performances du modèle
matrice = confusion_matrix(y_Encode, y_pred_classes)

#Affichage de la matrice de confusion
disp = ConfusionMatrixDisplay(confusion_matrix=matrice, display_labels=Encode.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.show()
