# Variable chargée 'df' à partir de l’URI : /home/mg4/Documents/codeblocks/VS code M1 1er smtre/reseaux connexionnistes/projet2/rice+cammeo+and+osmancik/Rice_Cammeo_Osmancik.csv
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv(r'Rice_Cammeo_Osmancik.csv')

from sklearn.preprocessing import  StandardScaler

# Sélection des colonnes numériques
cols_to_normalize =['Area Integer ', 'Perimeter Real', 'Major_Axis_Length Real',
       'Minor_Axis_Length Real', 'Eccentricity Real', 'Convex_Area Integer ',
       'Extent Real']

# Standardization (Z-score scaling)
scaler_standard = StandardScaler()
data_standard = df.copy()
data_standard[cols_to_normalize] = scaler_standard.fit_transform(df[cols_to_normalize])


# Distribution des classes
class_distribution = df['Class'].value_counts()
print(class_distribution)

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(df['Class'])

X = df.drop('Class', axis=1)
y = y_encoded

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()

# Ajoute la première couche cachée
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))

# Ajoute d'autres couches cachées si nécessaire
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))  # Ajoute du dropout pour éviter le surapprentissage

# Ajoute la couche de sortie
model.add(Dense(1, activation='sigmoid'))  # Utilise 'softmax' pour plus de deux classes

model.compile(loss='binary_crossentropy',  # Utilise 'categorical_crossentropy' pour plus de deux classes
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, 
                    epochs=50,  # Nombre d'époques d'entraînement
                    batch_size=32, 
                    validation_data=(X_test, y_test))

y_pred = (model.predict(X_test) > 0.5).astype("int32")  # Seuil pour binariser la sortie

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

import matplotlib.pyplot as plt

# Plot de la précision
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Plot de la perte
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

import seaborn as sns
from sklearn.metrics import confusion_matrix

# Prédictions sur les données de test
y_pred = (model.predict(X_test) > 0.5).astype("int32")

# Calcul de la matrice de confusion
conf_matrix = confusion_matrix(y_test, y_pred)

# Tracé de la matrice de confusion
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
    