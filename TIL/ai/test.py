import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# 저장해 둔 모델을 불러와서 활용
loaded_model = tf.keras.models.load_model('mnist_model.h5')
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
sample_image = test_images[2]
plt.show()

# 로드된 모델로 예측
predictions = loaded_model.predict(np.expand_dims(sample_image, axis=0))
predicted_label = np.argmax(predictions)
print(f'Predicted label from loaded model: {predicted_label}')
