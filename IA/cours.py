# -*- coding: utf-8 -*-


import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
training_data =np.array([[0,0],[0,1],[1,0],[1,1]])
target_data =np.array([0,1,1,0])
model = Sequential()
model.add(Dense(4, input_dim=2, activation='softmax'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error',optimizer='adam',
metrics=['binary_accuracy'])
model.fit(training_data, target_data, epochs=1000)
scores = model.evaluate(training_data, target_data)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print (model.predict(training_data).round())
model.summary()
from tensorflow.keras.utils import plot_model
plot_model(model, to_file='/home/mg4/model.png')
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

