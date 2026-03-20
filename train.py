# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.applications import MobileNetV2
# from tensorflow.keras import layers, models

# IMG_SIZE = 224
# BATCH_SIZE = 32

# train_gen = ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2
# )

# train_data = train_gen.flow_from_directory(
#     "dataset",   #  your dataset folder
#     target_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='training'
# )

# val_data = train_gen.flow_from_directory(
#     "dataset",
#     target_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='validation'
# )

# base_model = MobileNetV2(
#     input_shape=(224, 224, 3),
#     include_top=False,
#     weights='imagenet'
# )

# base_model.trainable = False

# model = models.Sequential([
#     base_model,
#     layers.GlobalAveragePooling2D(),
#     layers.Dense(128, activation='relu'),
#     layers.Dense(train_data.num_classes, activation='softmax')
# ])

# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# model.fit(train_data, validation_data=val_data, epochs=5)

# # SAVE MODEL
# model.save("model.keras")

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2

IMG_SIZE = 224
BATCH_SIZE = 32

# 🔹 Data generator
train_gen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train_data = train_gen.flow_from_directory(
    "./dataset",   # 👈 adjust if needed
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_data = train_gen.flow_from_directory(
    "./dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# 🔹 Base model
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights='imagenet'
)

base_model.trainable = False

#  Functional API (IMPORTANT FIX)
x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.3)(x)
output = tf.keras.layers.Dense(train_data.num_classes, activation='softmax')(x)

model = tf.keras.Model(inputs=base_model.input, outputs=output)

# 🔹 Compile
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 🔹 Train
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# 🔹 Save model (NEW FORMAT)
model.save("model.keras")

# print(" Model training complete and saved as model.keras")


# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.applications import MobileNetV2
# import numpy as np
# import json
# from sklearn.utils.class_weight import compute_class_weight

# IMG_SIZE = 224
# BATCH_SIZE = 32

# # 🔹 Data generator (strong augmentation)
# train_gen = ImageDataGenerator(
#     rescale=1./255,
#     validation_split=0.2,
#     rotation_range=40,
#     zoom_range=0.4,
#     horizontal_flip=True,
#     brightness_range=[0.7, 1.3]
# )

# # 🔹 Load dataset
# train_data = train_gen.flow_from_directory(
#     "./dataset",
#     target_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='training'
# )

# val_data = train_gen.flow_from_directory(
#     "./dataset",
#     target_size=(IMG_SIZE, IMG_SIZE),
#     batch_size=BATCH_SIZE,
#     class_mode='categorical',
#     subset='validation'
# )

# # 🔥 Save class mapping
# with open("classes.json", "w") as f:
#     json.dump(train_data.class_indices, f)

# print("Classes:", train_data.class_indices)

# # 🔥 Compute class weights (FIX IMBALANCE)
# class_weights = compute_class_weight(
#     class_weight='balanced',
#     classes=np.unique(train_data.classes),
#     y=train_data.classes
# )

# class_weights = dict(enumerate(class_weights))
# print("Class Weights:", class_weights)

# # 🔹 Base model
# base_model = MobileNetV2(
#     input_shape=(IMG_SIZE, IMG_SIZE, 3),
#     include_top=False,
#     weights='imagenet'
# )

# # 🔥 Fine-tuning
# base_model.trainable = True
# for layer in base_model.layers[:-30]:
#     layer.trainable = False

# # 🔹 Custom head
# x = base_model.output
# x = tf.keras.layers.GlobalAveragePooling2D()(x)
# x = tf.keras.layers.Dense(256, activation='relu')(x)
# x = tf.keras.layers.Dropout(0.5)(x)
# output = tf.keras.layers.Dense(train_data.num_classes, activation='softmax')(x)

# model = tf.keras.Model(inputs=base_model.input, outputs=output)

# # 🔹 Compile
# model.compile(
#     optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
#     loss='categorical_crossentropy',
#     metrics=['accuracy']
# )

# # 🔹 Train (with class weights)
# model.fit(
#     train_data,
#     validation_data=val_data,
#     epochs=25,
#     class_weight=class_weights
# )

# # 🔹 Save model
# model.save("model.keras")

# print("✅ Training complete")
# print("✅ model.keras saved")
# print("✅ classes.json saved")
