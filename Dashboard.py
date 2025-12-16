import streamlit as st
import pandas as pd
import requests
import time
import subprocess
import os

# Page Config - gotta look aesthetic
st.set_page_config(
    page_title="EchoGuard",
    page_icon="👂",
    layout="wide"
)

# Title
st.title("EchoGuard - Smart Audio Monitor 🔊")

# Sidebar for controls
st.sidebar.header("Control Panel")
monitoring = st.sidebar.checkbox("Start Monitoring", value=False)

# Status Indicator
if monitoring:
    st.success("Status: 🟢 Monitoring Active")
    # Start the audio engine if not already running
    if 'process' not in st.session_state or st.session_state.process.poll() is not None:
        st.session_state.process = subprocess.Popen([
            "C:/Users/Sai_Sudarshan_S/OneDrive/Documents/GitHub/EchoGuard/.venv/Scripts/python.exe",
            "audio_engine.py"
        ])
else:
    st.warning("Status: 🔴 Inactive")
    # Stop the process if running
    if 'process' in st.session_state and st.session_state.process.poll() is None:
        st.session_state.process.terminate()
        st.session_state.process.wait()

st.divider()

# Auto-refresh loop placeholder (Streamlit reruns script on interaction)
st.subheader("🚨 Alert Log")

# Fetch data from our Flask API
try:
    # Attempt to connect to the Builder's API
    response = requests.get("http://127.0.0.1:5000/get-alerts")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        if not df.empty:
            # STYLE: Highlight 'Smoke Alarm' or 'Glass Break' in RED
            # We use a lambda function to apply styles row by row
            def highlight_critical(row):
                critical_events = ['Smoke Alarm Detected', 'Glass Break Detected']
                if row['Alert Type'] in critical_events:
                    return ['background-color: #ffcccc; color: #990000'] * len(row)
                else:
                    return [''] * len(row)

            st.dataframe(
                df.style.apply(highlight_critical, axis=1), 
                width='stretch'
            )
        else:
            st.info("No alerts detected yet. The room is safe. 🛡️")
    else:
        st.error("API Error: Could not fetch data.")
except Exception as e:
    st.error(f"⚠️ Connection Error: Is 'api.py' running? \n\nLog: {e}")

# Auto-refresh every 5 seconds if monitoring
if monitoring:
    time.sleep(5)
    st.rerun()

# Footer
st.markdown("---")
st.caption("EchoGuard System v1.0 | Built by Sai")