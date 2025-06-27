from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras import Input

# Load pre-trained model (no top = exclude classifier)
base_model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

# Freeze all layers (Transfer Learning)
for layer in base_model.layers:
    layer.trainable = False

# Add your classifier
x = base_model.output
output = Dense(3, activation='softmax')(x)  # e.g., 3 car types
model = Model(inputs=base_model.input, outputs=output)

# Later, for Fine-Tuning: unfreeze last few layers
for layer in base_model.layers[-10:]:
    layer.trainable = True
