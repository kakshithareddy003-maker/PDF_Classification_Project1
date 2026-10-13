
import streamlit as st
from classifier import classify_pdf

st.set_page_config(
    page_title="PDF Classification System",
    page_icon="📄",
    layout="centered"
)

st.title("📄 PDF Classification System")

st.write(
    "Upload a PDF to identify whether it is an Invoice, Bill, or Receipt."
)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Classify PDF"):
        with st.spinner("Analyzing PDF..."):
            try:
                result = classify_pdf(uploaded_file)

                st.subheader("Classification Result")

                st.write(
                    f"**Document Type:** {result['document_type']}"
                )

                confidence = result["confidence"]

                if confidence > 0:
                    st.write(
                        f"**Model Confidence:** {confidence}%"
                    )
                    st.progress(confidence / 100)

            except Exception as error:
                st.error(f"Could not process the PDF: {error}")
