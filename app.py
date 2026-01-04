import streamlit as st
import numpy as np
from PIL import Image
from ai_engine.detector import detect_objects
from ai_engine.visualization import draw_boxes

st.set_page_config(page_title="YOLO Object Detection", layout="centered")
st.title("Object Detection using YOLOv8")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file and st.button("Detect Objects"):
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    with st.spinner("Detecting objects..."):
        results = detect_objects(image_np)
        output_image = draw_boxes(image_np, results)

    st.success("Objects detected successfully!")
    st.image(output_image, caption="Detected Objects", use_container_width=True)
