from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

p = data.data
t = data.target

print(p)
print(t)
print(len(t))

import keras

model = keras.Sequential()
model.add(keras.layers.Dense(units=64, activation='relu'))
model.add(keras.layers.Dense(units=1, activation='sigmoid'))

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.BinaryCrossentropy(),
    metrics=[
        keras.metrics.MeanSquaredError(),
        keras.metrics.AUC(),
    ],
)

history = model.fit(p, t, epochs=100, batch_size=32)

loss_and_metrics = model.evaluate(p, t, batch_size=32)
print(loss_and_metrics)

classes = model.predict(p, batch_size=32)
print(classes)

import matplotlib.pyplot as plt

plt.figure()

plt.plot(history.history['mean_squared_error'], label='Train MSE')
plt.plot(history.history['auc'], label='Accuracy')
plt.title('Model Mean Squared Error')
plt.ylabel('MSE')
plt.xlabel('Epochs')
plt.legend()
plt.grid()

plt.show()