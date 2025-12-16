import numpy as np
import os

# For demo purposes, generate dummy mel-spectrograms
# In real scenario, this would process actual audio files

def generate_dummy_spectrogram(shape=(128, 128)):
    # Random spectrogram-like data
    return np.random.rand(*shape)

# Create dummy data for each class
classes = ['alarm', 'glass', 'background']
num_samples_per_class = 50

for cls in classes:
    for i in range(num_samples_per_class):
        spec = generate_dummy_spectrogram()
        filename = f"{cls}_{i}.npy"
        filepath = os.path.join('processed_data', cls, filename)
        np.save(filepath, spec)

print("Dummy spectrograms generated.")