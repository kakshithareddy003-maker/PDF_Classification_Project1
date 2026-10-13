import streamlit as st
from PIL import Image
import fitz
import pytesseract

st.set_page_config(page_title="PDF Classification")
st.title("PDF Classification Project - Invoice / Bill / Receipt")

st.write("Upload your document for classification")

uploaded = st.file_uploader("Choose file", type=["pdf","png","jpg","jpeg"])

if uploaded:
    text = ""
    if uploaded.name.endswith(".pdf"):
        doc = fitz.open(stream=uploaded.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    else:
        img = Image.open(uploaded)
        st.image(img, width=300)
        text = pytesseract.image_to_string(img)
    
    st.subheader("Extracted Text")
    st.text_area("Text", text, height=200)
    
    st.subheader("Prediction")
    upper = text.upper()
    if "INVOICE" in upper or "GSTIN" in upper:
        st.success("INVOICE")
    elif "ELECTRICITY" in upper or "BESCOM" in upper or "BILL NO" in upper:
        st.success("BILL")
    else:
        st.success("RECEIPT")
