import pyaudio
import numpy as np
import librosa
from tensorflow.keras.models import load_model
from data_manager import log_alert
import time

# Load the trained model
model = load_model('audio_model.h5')

# Audio parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 22050
RECORD_SECONDS = 2

# Classes
classes = ['alarm', 'glass', 'background']

def preprocess_audio(audio_data):
    # Convert to float
    audio_float = audio_data.astype(np.float32) / 32768.0
    # Compute mel-spectrogram
    mel_spec = librosa.feature.melspectrogram(y=audio_float, sr=RATE, n_mels=128, fmax=8000)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    # Resize to 128x128
    mel_spec_resized = np.resize(mel_spec_db, (128, 128))
    return mel_spec_resized.reshape(1, 128, 128, 1)

def classify_audio(audio_data):
    processed = preprocess_audio(audio_data)
    predictions = model.predict(processed, verbose=0)
    max_prob = np.max(predictions)
    predicted_class = classes[np.argmax(predictions)]
    return predicted_class, max_prob

def main():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening...")

    try:
        while True:
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            # Convert to numpy array
            audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

            # Classify
            alert_type, confidence = classify_audio(audio_data)

            if alert_type in ['alarm', 'glass'] and confidence > 0.9:
                alert_msg = f"{alert_type.capitalize()} Detected"
                log_alert(alert_msg, confidence)
                print(f"Alert: {alert_msg} with confidence {confidence}")

            time.sleep(0.1)  # Small delay

    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()