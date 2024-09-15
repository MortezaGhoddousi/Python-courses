from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
print(data.data.shape)
print(data.target.shape)

x_train = data.data
y_train = data.target

import keras

model = keras.Sequential()
model.add(keras.layers.Dense(units=32, activation='relu'))
model.add(keras.layers.Dense(units=1, activation='sigmoid'))

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss=keras.losses.BinaryCrossentropy(),
    metrics=[
        keras.metrics.BinaryAccuracy(),
        keras.metrics.FalseNegatives(),
        keras.metrics.MeanSquaredError(),
        keras.metrics.AUC(),
    ],
)

history = model.fit(x_train, y_train, epochs=500, batch_size=32)

loss_and_metrics = model.evaluate(x_train, y_train, batch_size=32)
classes = model.predict(x_train, batch_size=32)

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

