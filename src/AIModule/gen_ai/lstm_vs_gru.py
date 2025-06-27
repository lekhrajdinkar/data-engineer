import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Dummy sequence data
X = np.random.randint(1, 1000, size=(1000, 10))  # 1000 samples, 10 tokens each
y = np.random.randint(0, 2, size=(1000,))        # Binary classification

# Pad sequences (if needed)
X_padded = pad_sequences(X, maxlen=10)

# ----------- LSTM Model ------------
model_lstm = Sequential([
    Embedding(input_dim=1000, output_dim=64),
    LSTM(32),
    Dense(1, activation='sigmoid')
])
model_lstm.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("\nTraining LSTM model...")
model_lstm.fit(X_padded, y, epochs=3, batch_size=32)

# ----------- GRU Model ------------
model_gru = Sequential([
    Embedding(input_dim=1000, output_dim=64),
    GRU(32),
    Dense(1, activation='sigmoid')
])
model_gru.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("\nTraining GRU model...")
model_gru.fit(X_padded, y, epochs=3, batch_size=32)


"""
🔍 Observations:
LSTM will take slightly longer to train due to extra gates.
GRU is faster, often with similar accuracy.
For large datasets or longer sequences, try both and compare performance.

PyTorch 
"""