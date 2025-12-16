# EchoGuard - Smart Audio Monitor

## Project Overview

EchoGuard is a smart room monitoring system that actively listens to ambient audio through a microphone, classifies specific emergency sounds in real-time, and displays alerts on a user-friendly web dashboard.

### Mission Statement
To build a smart room monitoring system that actively listens to ambient audio through a microphone, classifies specific emergency sounds in real-time, and displays alerts on a user-friendly web dashboard.

### Core Problem Solved
Provides an automated, always-on monitoring solution for critical audio events (like a smoke alarm or breaking glass) that might otherwise go unnoticed, enhancing safety and security.

### Key Differentiator
An end-to-end system that leverages the unique and challenging domain of Audio AI, directly fusing ECE concepts (signal processing) with advanced Machine Learning, data management, and an interactive UI.

## Technology Stack

- **Language**: Python 3.9+
- **AI/Audio Processing**: Librosa, Scikit-learn, TensorFlow/Keras, NumPy
- **Real-time Audio Capture**: PyAudio
- **Backend & Data**: Pandas, Flask
- **Frontend**: Streamlit

## System Architecture

1. **User Interface (Frontend - Streamlit)**: The user starts the system and views alerts.
2. **API Layer (Backend - Flask)**: The Frontend requests alert data from this layer.
3. **Core Logic (AI Engine - Python/Librosa/PyAudio)**: The Frontend triggers this engine to start listening.
4. **Data Management (Backend - Pandas)**: The AI Engine sends alert data to this layer for storage.
5. **Database (File System)**: The actual alert data is stored in a CSV file.

## Installation & Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the data preprocessor: `python preprocessor.py`
4. Train the model: `python trainer.py`
5. Start the API: `python api.py`
6. Start the dashboard: `streamlit run Dashboard.py`

## Usage

1. Open the Streamlit dashboard
2. Check "Start Monitoring" to begin audio classification
3. View alerts in the log table
4. Critical alerts (Smoke Alarm, Glass Break) are highlighted in red

## Team Roles

- **Lead Architect & Presenter**: Overall system design, AI model development, integration
- **Backend & API Engineer**: Data storage, Flask API development
- **UI/UX Specialist**: Dashboard design, documentation, presentation materials

## Features

- Real-time audio monitoring
- AI-powered sound classification
- Web-based dashboard
- Alert logging and display
- Critical alert highlighting

## Future Work

- Expand to more sound classes
- Improve model accuracy with real data
- Add notification systems (email, SMS)
- Mobile app integration
- Cloud deployment

