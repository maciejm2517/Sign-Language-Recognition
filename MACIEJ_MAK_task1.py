#import nessesary modules
import tensorflow as tf
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import pickle

#define constants
DATA_PATH='data'
CLASSES=os.listdir(DATA_PATH)
CLASSES.sort()
IMG_WIDTH=300
IMG_HEIGHT=300
RGB=3
NUM_CLASSES=len(CLASSES)
EPOCHS=8

#import data
data=tf.keras.utils.image_dataset_from_directory(DATA_PATH,
                                                 image_size=(IMG_WIDTH,IMG_HEIGHT))

#data augmentation to model
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal", 
                                                 input_shape=(IMG_HEIGHT, 
                                                              IMG_WIDTH,
                                                              3)),
    tf.keras.layers.experimental.preprocessing.RandomRotation(0.1),
    tf.keras.layers.experimental.preprocessing.RandomZoom(0.1),
])

#scaling data and making batches iterable
data=data.map(lambda x,y: (x/255,y))
data.as_numpy_iterator().next()

#divide data into training, validation and testing
train_size = int(len(data)*0.8)
val_size = int(len(data)*0.1)
test_size = int(len(data)*0.1)

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)

#creating model
model=tf.keras.Sequential([
    data_augmentation,
    tf.keras.layers.Conv2D(16, (3,3),1, activation='relu'),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(32, (3,3),1, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(NUM_CLASSES)    
])

#compiling model
model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=1e-4),
               loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True), 
               metrics=['accuracy']
               )

#import or training model
if os.path.isfile('model.h5'):
    model=tf.keras.models.load_model('model.h5')
    with open('trainHistoryDict', "rb") as file:
        hist = pickle.load(file)

else:
    history=model.fit(train, epochs=EPOCHS,validation_data=val)    
    model.save('model.h5')
    hist=history.history
    with open('trainHistoryDict', 'wb') as file:
        pickle.dump(hist, file)

#ploting accuracy and loss in epochs
acc = hist['accuracy']
val_acc = hist['val_accuracy']

loss = hist['loss']
val_loss = hist['val_loss']

epochs_range = range(EPOCHS)

plt.figure()
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='best')
plt.title('Training and Validation Accuracy')

plt.figure()
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='best')
plt.title('Training and Validation Loss')
plt.show()

#calculate metrics of model using testing data
accuracy=tf.keras.metrics.Accuracy()
precision=tf.keras.metrics.Precision()
recall=tf.keras.metrics.Recall()

for index,batch in enumerate(test.as_numpy_iterator()): 
    X, y = batch
    yhat = model.predict(X)
    accuracy.merge_state([accuracy])
    precision.merge_state([precision])
    recall.merge_state([recall])

    accuracy.update_state(y, np.argmax(yhat, axis=1))
    precision.update_state(y, np.argmax(yhat, axis=1))
    recall.update_state(y, np.argmax(yhat, axis=1))
accuracy_result=accuracy.result().numpy()
precision_result=precision.result().numpy()
recall_recult=recall.result().numpy()
F1Score = 2 * (precision_result * recall_recult) / (precision_result + recall_recult)
print('metrics')
print(f'accuracy: {accuracy_result}')
print(f'precision: {precision_result}')
print(f'recall: {recall_recult}')
print(f'F1Score : {F1Score}')

#ploting image with predicted and true labels
for _ in range(10):
    random_class=random.choice(CLASSES)
    random_path=os.path.join(DATA_PATH,random_class)
    random_image=random.choice(os.listdir(random_path))
    img=cv2.imread(os.path.join(random_path,random_image))
    print(img.shape)
    if img.shape!=(IMG_WIDTH,IMG_HEIGHT,RGB):
        img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT), interpolation = cv2.INTER_AREA)
    ans=model.predict(np.expand_dims(img/255,0))
    true_label=random_class
    pred_label=CLASSES[ans.argmax()]
    plt.figure()
    plt.title(f"True label: {true_label}, Pred label: {pred_label}")
    plt.imshow(img)
plt.show()