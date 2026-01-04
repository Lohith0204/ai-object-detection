import streamlit as st
from ultralytics import YOLO

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

def detect_objects(image):
    model = load_model()
    results = model(image)
    return results
