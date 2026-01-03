import streamlit as st
import cv2
import numpy as np
from ai_engine.detector import detect_objects
from ai_engine.visualization import draw_boxes

st.title("Object Detection using YOLO")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if st.button("Detect Objects"):
    if uploaded_file is None:
        st.warning("Please upload an image.")
        st.stop()

    image_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    results = detect_objects(image)
    output_image = draw_boxes(image, results)
    st.success("Objects detected successfully!")
    st.image(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB),caption="Detected Objects")





